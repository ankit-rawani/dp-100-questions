# Question 99

DRAG DROP -

You are using a Git repository to track work in an Azure Machine Learning workspace.

You need to authenticate a Git account by using SSH.

Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Select and Place:

![Question Image](images/q99_q_0013100001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q99_ans_0_0013200001.png" alt="Answer Image"><br>
<p>Authenticate your Git Account with SSH:</p>
<p>Step 1: Generating a public/private key pair</p>
<p>Generate a new SSH key -</p>
<p>1. Open the terminal window in the Azure Machine Learning Notebook Tab.</p>
<p>2. Paste the text below, substituting in your email address.</p>
<p>ssh-keygen -t rsa -b 4096 -C &quot;</p>
<p>[email protected]</p>
<p>&quot;</p>
<p>This creates a new ssh key, using the provided email as a label.</p>
<p>&gt; Generating public/private rsa key pair.</p>
<p>Step 2: Add the public key to the Git Account</p>
<p>In your terminal window, copy the contents of your public key file.</p>
<p>Step 3: Clone the Git repository by using an SSH repository URL</p>
<p>1. Copy the SSH Git clone URL from the Git repo.</p>
<p>2. Paste the url into the git clone command below, to use your SSH Git repo URL. This will look something like: git clone</p>
<p>[email protected]</p>
<p>:GitUser/azureml-example.git</p>
<p>Cloning into &#x27;azureml-example&#x27;.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/concept-train-model-git-integration</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>silva_831</strong> <code>(Sun 30 Apr 2023 02:29)</code> - <em>Upvotes: 7</em></p><p>The given answer is correct.</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Fri 08 Sep 2023 11:12)</code> - <em>Upvotes: 5</em></p><p>Exactly this question was on exam 07/March/2023</p></blockquote>
<blockquote><p><strong>daviduzo</strong> <code>(Fri 22 Dec 2023 16:53)</code> - <em>Upvotes: 1</em></p><p>roughly how many questions from this site appeared in your exam if I may ask?</p></blockquote>
<blockquote><p><strong>MiteshKachhatiya</strong> <code>(Tue 10 Jun 2025 09:26)</code> - <em>Upvotes: 1</em></p><p>On exam 8th June 2025</p></blockquote>
<blockquote><p><strong>thisiston</strong> <code>(Sun 03 Nov 2024 19:58)</code> - <em>Upvotes: 1</em></p><p>1. Generate a public/private key pair. This is the initial step in setting up SSH authentication. The key pair consists of a private key, which you keep secure on your machine, and a public key that you will share.
2. Add the public key to the Git account. Once the key pair is generated, the public key must be added to your Git account settings. This allows the Git server to recognize and authenticate your SSH requests.
3. Clone the Git repository by using an SSH repository URL. After your public key is accepted by the Git server, you can securely clone the repository using SSH, which will utilize your private key for authentication.</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Wed 25 Sep 2024 16:42)</code> - <em>Upvotes: 1</em></p><p>on exam 3/25/2024</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Mon 12 Aug 2024 13:34)</code> - <em>Upvotes: 1</em></p><p>On exam 12-02-2024.</p></blockquote>
<blockquote><p><strong>Awooga</strong> <code>(Tue 06 Aug 2024 14:16)</code> - <em>Upvotes: 1</em></p><p>On exam 2024-02-06</p></blockquote>
<blockquote><p><strong>Kanwal001</strong> <code>(Wed 28 Feb 2024 20:33)</code> - <em>Upvotes: 5</em></p><p>On exam 28 Aug 2023</p></blockquote>
<blockquote><p><strong>Mal42</strong> <code>(Tue 20 Feb 2024 14:24)</code> - <em>Upvotes: 2</em></p><p>On exam 18 Aug 2023</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Sat 20 Jan 2024 14:19)</code> - <em>Upvotes: 2</em></p><p>On exam 20 July 2023.</p></blockquote>
<blockquote><p><strong>ahson0124</strong> <code>(Tue 15 Aug 2023 12:41)</code> - <em>Upvotes: 2</em></p><p>In exam on 2023-02-15</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Sun 06 Aug 2023 14:42)</code> - <em>Upvotes: 4</em></p><p>answer looks good</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Fri 19 May 2023 15:03)</code> - <em>Upvotes: 3</em></p><p>Never share a private key :) Answer is correct.</p></blockquote>
<blockquote><p><strong>fvil</strong> <code>(Sun 07 May 2023 14:39)</code> - <em>Upvotes: 2</em></p><p>Appeared on exam 07/11/2022</p></blockquote>

</details>

---

[<< Previous Question](question_98.md) | [Home](/index.md) | [Next Question >>](question_100.md)
