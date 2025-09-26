import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

def create_question_bank(url, output_file='question_bank.md', image_dir='images', is_first_run=True, question_start_index=1):
    """
    Scrapes questions and answers from a single URL, downloads images locally,
    and appends them to a markdown file.

    Args:
        url (str): The URL of the exam questions page to scrape.
        output_file (str): The name of the file to save the markdown content.
        image_dir (str): The directory to save the downloaded images.
        is_first_run (bool): Determines if the file should be overwritten or appended to.
        question_start_index (int): The number to start counting questions from.
        
    Returns:
        int: The number of questions successfully scraped from the URL.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        if not os.path.exists(image_dir) and is_first_run:
            os.makedirs(image_dir)
            print(f"Created directory: {image_dir}")
        
        print(f"Fetching content from {url}...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        question_containers = soup.find_all('div', class_='question-body')

        if not question_containers:
            print(f"No questions found at {url}. The structure may have changed.")
            return 0

        # Determine file mode: 'w' for write on first run, 'a' for append on subsequent runs
        mode = 'w' if is_first_run else 'a'
        
        with open(output_file, mode, encoding='utf-8') as f:
            if is_first_run:
                f.write("# Question Bank\n\n")

            for i, container in enumerate(question_containers, question_start_index):
                f.write(f"## Question {i}\n\n")

                # --- Extract and process question text and images ---
                question_p = container.find('p', class_='card-text')
                if question_p:
                    for content in question_p.contents:
                        if content.name == 'img':
                            img_src = content.get('src', '')
                            if img_src:
                                full_img_url = urljoin(url, img_src)
                                img_filename = os.path.basename(full_img_url.split('?')[0])
                                unique_img_filename = f"q{i}_{img_filename}"
                                local_img_path = os.path.join(image_dir, unique_img_filename)
                                
                                try:
                                    img_response = requests.get(full_img_url, headers=headers)
                                    img_response.raise_for_status()
                                    with open(local_img_path, 'wb') as img_f:
                                        img_f.write(img_response.content)
                                    f.write(f"![Question Image]({local_img_path})\n\n")
                                except requests.exceptions.RequestException as img_e:
                                    print(f"❌ Failed to download image {full_img_url}: {img_e}")
                                    f.write(f"![Image failed to download]({full_img_url})\n\n")
                        else:
                            text = str(content).replace('<br/>', '\n').replace('<br>', '\n')
                            clean_text = BeautifulSoup(text, 'html.parser').get_text()
                            if clean_text.strip():
                                f.write(f"{clean_text.strip()}\n\n")
                
                # --- Extract and process answer text and images ---
                answer_div = container.find('div', class_='question-answer')
                answer_content = ""
                if answer_div:
                    correct_answer_span = answer_div.find('span', class_='correct-answer')
                    if correct_answer_span:
                        for content in correct_answer_span.contents:
                            if content.name == 'img':
                                img_src = content.get('src', '')
                                if img_src:
                                    full_img_url = urljoin(url, img_src)
                                    img_filename = os.path.basename(full_img_url.split('?')[0])
                                    unique_img_filename = f"q{i}_ans_{img_filename}"
                                    local_img_path = os.path.join(image_dir, unique_img_filename)
                                    
                                    try:
                                        img_response = requests.get(full_img_url, headers=headers)
                                        img_response.raise_for_status()
                                        with open(local_img_path, 'wb') as img_f:
                                            img_f.write(img_response.content)
                                        answer_content += f"![Suggested Answer Image]({local_img_path})\n"
                                    except requests.exceptions.RequestException as img_e:
                                        print(f"❌ Failed to download image {full_img_url}: {img_e}")
                                        answer_content += f"![Image failed to download]({full_img_url})\n"
                            else:
                                text = str(content)
                                clean_text = BeautifulSoup(text, 'html.parser').get_text()
                                if clean_text.strip():
                                    answer_content += f"{clean_text.strip()}\n"
                
                f.write("<details>\n")
                f.write("  <summary>Show Suggested Answer</summary>\n\n")
                if answer_content:
                    f.write(f"  {answer_content.strip()}\n\n")
                else:
                    f.write("  Answer not found.\n\n")
                f.write("</details>\n\n")
                f.write("---\n\n")

        print(f"✅ Successfully scraped {len(question_containers)} questions from {url}.")
        return len(question_containers)

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching the URL: {e}")
        return 0
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return 0

if __name__ == '__main__':
    output_filename = 'question_bank.md'
    image_directory = 'images'
    
    try:
        with open('./saved-links.txt', 'r', encoding='utf-8') as links:
            urls = links.read().splitlines()
    except FileNotFoundError:
        print("❌ Error: 'saved-links.txt' not found. Please create this file and add URLs to it.")
        urls = []

    question_counter = 1
    if urls:
        for i, target_url in enumerate(urls):
            print(f"\n--- Processing URL {i+1}/{len(urls)}: {target_url} ---")
            num_scraped = create_question_bank(
                target_url,
                output_file=output_filename,
                image_dir=image_directory,
                is_first_run=(i == 0),
                question_start_index=question_counter
            )
            if num_scraped > 0:
                question_counter += num_scraped
        
        print(f"\n✅ All done. Total questions saved to '{output_filename}': {question_counter - 1}")

