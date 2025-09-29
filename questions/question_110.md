# Question 110

DRAG DROP

-

You need to implement source control for scripts in an Azure Machine Learning workspace. You use a terminal window in the Azure Machine Learning Notebook tab.

You must authenticate your Git account with SSH.

You need to generate a new SSH key.

Which four actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

![Question Image](images/q110_q_image381.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q110_ans_0_image382.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Kanwal001</strong> <code>(Wed 28 Feb 2024 20:34)</code> - <em>Upvotes: 7</em></p><p>On exam 28 Aug 2023</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Sun 21 Jan 2024 10:29)</code> - <em>Upvotes: 5</em></p><p>Answer is correct: 

Here is a breakdown of each step:

1. The ssh-keygen command will generate a new SSH key pair. The key pair will consist of a public key and a private key. The public key will be used to authenticate your Git account with SSH, and the private key will be used to access your Git repositories.

2. When you run the ssh-keygen command, you will be prompted to enter a file in which to save the key pair. You can press Enter to accept the default location, which is /home/azureuser/.ssh.

3. The default location for SSH keys is /home/azureuser/.ssh. You should verify that this is the correct location before you press Enter.

4. You will be prompted to type a secure passphrase. The passphrase will be used to protect your private key. You should choose a strong passphrase that you will not forget.</p></blockquote>
<blockquote><p><strong>TA_</strong> <code>(Wed 25 Sep 2024 10:23)</code> - <em>Upvotes: 1</em></p><p>On exam 15-03-2024</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Mon 12 Aug 2024 13:35)</code> - <em>Upvotes: 1</em></p><p>On exam 12-02-2024.</p></blockquote>
<blockquote><p><strong>Jin_22</strong> <code>(Fri 22 Sep 2023 12:10)</code> - <em>Upvotes: 1</em></p><p>The answer seems correct.</p></blockquote>

</details>

---

[<< Previous Question](question_109.md) | [Home](/index.md) | [Next Question >>](question_111.md)
