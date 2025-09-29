import requests
from bs4 import BeautifulSoup, NavigableString
import os
from urllib.parse import urljoin
import re
import html
import concurrent.futures

def download_image(img_url, question_num, image_dir, headers, unique_id=""):
    """
    Downloads an image, saves it locally with a unique name, and returns the relative path.
    """
    if not img_url:
        return None
    
    try:
        # Create a clean filename from the URL
        img_filename = os.path.basename(img_url.split('?')[0])
        # Sanitize filename
        img_filename = re.sub(r'[^a-zA-Z0-9._-]', '', img_filename)
        
        unique_img_filename = f"q{question_num}_{unique_id}_{img_filename}"
        local_img_path = os.path.join(image_dir, unique_img_filename)
        
        # Download the image
        img_response = requests.get(img_url, headers=headers, stream=True)
        img_response.raise_for_status()
        
        with open(local_img_path, 'wb') as img_f:
            for chunk in img_response.iter_content(chunk_size=8192):
                img_f.write(chunk)
        
        # Return the relative path for the markdown file
        relative_path = os.path.join(image_dir, unique_img_filename).replace('\\', '/')
        return relative_path
        
    except requests.exceptions.RequestException as img_e:
        print(f"❌ Failed to download image {img_url}: {img_e}")
        return None

def parse_and_generate_file(question_block_soup, base_url, question_num, total_questions, image_dir, output_dir, headers):
    """
    Parses a single question block (including comments) and generates a markdown file.
    """
    output_filepath = os.path.join(output_dir, f"question_{question_num}.md")

    # --- 1. Parse Question Header (as Markdown) ---
    header_container = question_block_soup.find('div', class_='discussion-header-container')
    question_body = header_container.find('div', class_='question-body')
    
    question_content_md = ""
    # Question Text and Images
    question_p = question_body.find('p', class_='card-text')
    if question_p:
        for content in question_p.contents:
            if content.name == 'img':
                img_src = content.get('src', '')
                full_img_url = urljoin(base_url, img_src)
                relative_path = download_image(full_img_url, question_num, image_dir, headers, "q")
                if relative_path:
                    question_content_md += f"![Question Image]({relative_path})\n\n"
            else:
                text = str(content).replace('<br/>', '\n').replace('<br>', '\n')
                clean_text = BeautifulSoup(text, 'html.parser').get_text(strip=True)
                if clean_text:
                    question_content_md += f"{clean_text}\n\n"
    
    # MCQ Choices
    choices_container = question_body.find('div', class_='question-choices-container')
    if choices_container:
        choices = choices_container.find_all('li', class_='multi-choice-item')
        for choice in choices:
            question_content_md += f"* {choice.get_text(strip=True)}\n"
        question_content_md += "\n"

    # --- 2. Parse Answer (as HTML) ---
    answer_html = ""
    answer_div = question_body.find('div', class_='question-answer')
    if answer_div:
        # Suggested Answer part
        correct_answer_span = answer_div.find('span', class_='correct-answer')
        if correct_answer_span:
            for i, content in enumerate(correct_answer_span.contents):
                if content.name == 'img':
                    full_img_url = urljoin(base_url, content.get('src', ''))
                    relative_path = download_image(full_img_url, question_num, image_dir, headers, f"ans_{i}")
                    if relative_path:
                        answer_html += f'<img src="{relative_path}" alt="Answer Image"><br>'
                elif isinstance(content, NavigableString) and content.strip():
                    answer_html += f"<strong>{html.escape(content.strip())}</strong><br>"
        
        # Answer Description part (references, etc.)
        answer_desc_span = answer_div.find('span', class_='answer-description')
        if answer_desc_span:
            desc_parts = []
            for i, content in enumerate(answer_desc_span.contents):
                if content.name == 'img':
                    full_img_url = urljoin(base_url, content.get('src', ''))
                    relative_path = download_image(full_img_url, question_num, image_dir, headers, f"ref_{i}")
                    if relative_path:
                        desc_parts.append(f'<img src="{relative_path}" alt="Reference Image"><br>')
                else:
                    text = str(content).replace('<br/>', '<br>').replace('<br>', '<br>')
                    clean_text = BeautifulSoup(text, 'html.parser').get_text(strip=True)
                    if clean_text:
                        desc_parts.append(f"<p>{html.escape(clean_text)}</p>")
            if desc_parts:
                answer_html += "\n" + "\n".join(desc_parts)

    if not answer_html:
        answer_html = "<p>Answer not found.</p>"

    # --- 3. Parse Comments (as HTML) ---
    comments_html = ""
    comments_section = question_block_soup.find('div', class_='discussion-page-comments-section')
    if comments_section:
        comments = comments_section.find_all('div', class_='comment-container')
        for comment in comments:
            username = comment.find('h5', class_='comment-username').get_text(strip=True)
            date = comment.find('span', class_='comment-date').get('title', '')
            content = comment.find('div', class_='comment-content').get_text(strip=True)
            upvotes = comment.find('span', class_='upvote-count').get_text(strip=True)
            
            comments_html += '<blockquote>'
            comments_html += f'<p><strong>{html.escape(username)}</strong> <code>({html.escape(date)})</code> - <em>Upvotes: {html.escape(upvotes)}</em></p>'
            comments_html += f'<p>{html.escape(content)}</p>'
            comments_html += '</blockquote>\n'
    
    if not comments_html:
        comments_html = "<p>No discussions yet.</p>"

    # --- 4. Write to Markdown File ---
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write(f"# Question {question_num}\n\n")
        f.write(question_content_md)

        f.write("<details>\n")
        f.write("  <summary>Show Suggested Answer</summary>\n\n")
        f.write(f"  {answer_html.strip()}\n\n")
        f.write("</details>\n\n")

        f.write("<details>\n")
        f.write("  <summary>Show Discussions</summary>\n\n")
        f.write(f"{comments_html.strip()}\n\n")
        f.write("</details>\n\n")

        # --- 5. Add Navigation ---
        f.write("---\n\n")
        nav_links = []
        if question_num > 1:
            nav_links.append(f"[<< Previous Question](question_{question_num - 1}.md)")
        
        nav_links.append(f"[Home](/index.md)") # Link back to the main index

        if question_num < total_questions:
            nav_links.append(f"[Next Question >>](question_{question_num + 1}.md)")
        f.write(" | ".join(nav_links) + "\n")

def fetch_and_parse(url, headers):
    """
    Fetches content from a single URL and returns a parsed BeautifulSoup object.
    Returns a dictionary {'soup': soup, 'url': url} or None on failure.
    """
    try:
        print(f"Fetching from {url}...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return {'soup': soup, 'url': url}
    except requests.exceptions.RequestException as e:
        print(f"❌ Could not process URL {url}: {e}")
        return None

def main():
    """Main function to orchestrate the scraping and file generation."""
    image_directory = 'images'
    output_directory = 'questions'
    urls_file = './saved-links.txt'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        with open(urls_file, 'r', encoding='utf-8') as links:
            urls = [line.strip() for line in links if line.strip()]
    except FileNotFoundError:
        print(f"❌ Error: '{urls_file}' not found. Please create this file and add URLs to it.")
        return

    # --- Phase 1: Scrape all question data from all URLs in parallel ---
    print("--- Starting Phase 1: Gathering all question data in parallel ---")
    all_question_data = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all URL fetch tasks to the executor
        future_to_url = {executor.submit(fetch_and_parse, url, headers): url for url in urls}
        
        for future in concurrent.futures.as_completed(future_to_url):
            result = future.result()
            if result:
                # If fetch was successful, parse out the question blocks
                soup = result['soup']
                url = result['url']
                question_blocks = soup.find_all('div', class_='discussion-header-container')
                for block in question_blocks:
                    parent_container = block.find_parent(class_='col-12')
                    if parent_container:
                         all_question_data.append({'soup': parent_container, 'url': url})

    total_questions = len(all_question_data)
    if total_questions == 0:
        print("\nNo questions found. Exiting.")
        return
        
    print(f"\nFound a total of {total_questions} questions across all URLs.")

    # --- Phase 2: Generate markdown files for each question ---
    print("\n--- Starting Phase 2: Generating Markdown files ---")
    os.makedirs(output_directory, exist_ok=True)
    os.makedirs(image_directory, exist_ok=True)

    for i, data in enumerate(all_question_data):
        question_num = i + 1
        print(f"Generating file for question {question_num}/{total_questions}...")
        parse_and_generate_file(
            data['soup'], data['url'], question_num, total_questions,
            image_directory, output_directory, headers
        )

    # --- Phase 3: Create an index file ---
    print("\n--- Starting Phase 3: Generating index file ---")
    index_path = os.path.join(output_directory, '..', 'index.md')
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Question Bank Index\n\n")
        f.write("A list of all scraped questions.\n\n")
        for i in range(total_questions):
            question_num = i + 1
            f.write(f"* [Question {question_num}](./{output_directory}/question_{question_num}.md)\n")
    
    print(f"✅ Index file created at '{index_path}'")
    print(f"\n✅ All done. {total_questions} question files created in the '{output_directory}' directory.")

if __name__ == '__main__':
    main()
