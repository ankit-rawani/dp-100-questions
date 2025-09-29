# Question 18

You are planning to host practical training to acquaint learners with data visualization creation using Python. Learner devices are able to connect to the internet.

Learner devices are currently NOT configured for Python development. Also, learners are unable to install software on their devices as they lack administrator permissions. Furthermore, they are unable to access Azure subscriptions.

It is imperative that learners are able to execute Python-based data visualization code.

Which of the following actions should you take?

- A.You should consider configuring the use of Azure Container Instance.
- B.You should consider configuring the use of Azure BatchAI.
- C.You should consider configuring the use of Azure Notebooks.
- D.You should consider configuring the use of Azure Kubernetes Service.

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>pancman</strong> <code>(Wed 13 Apr 2022 18:36)</code> - <em>Upvotes: 10</em></p><p>The answer is correct. Azure Notebooks are accessible by any device that can connect to the internet. The other options require installation of additional software, which is not permitted in this scenario.</p></blockquote>
<blockquote><p><strong>Learner_Thunder2</strong> <code>(Wed 12 Jan 2022 17:58)</code> - <em>Upvotes: 5</em></p><p>Azure Notebooks is correct</p></blockquote>
<blockquote><p><strong>sar77</strong> <code>(Sat 12 Jul 2025 00:21)</code> - <em>Upvotes: 1</em></p><p>Azure Notebooks is correct</p></blockquote>
<blockquote><p><strong>raidenstrike1945</strong> <code>(Wed 11 Dec 2024 03:34)</code> - <em>Upvotes: 1</em></p><p>Why C? there&#x27;s no Internet, no Azure Subscription. How ppl can use Azure Notebook without these two?</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Thu 26 Sep 2024 10:10)</code> - <em>Upvotes: 1</em></p><p>Learner devices NOT configured for Python development --&gt; Azure Notebooks. Choose C.

Quote &#x27;Since you don&#x27;t share compute instances, other users who run your notebook will do so on their own compute instance.&#x27;

at https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2#share-a-notebook</p></blockquote>

<blockquote><p><strong>evangelist</strong> <code>(Thu 26 Sep 2024 10:10)</code> - <em>Upvotes: 2</em></p><p>The correct answer is C. You should consider configuring the use of Azure Notebooks.

Explanation:
Azure Notebooks is a free service that provides Jupyter notebooks that are hosted in the cloud. The service allows users to write and execute Python (among other languages) code in their browsers without the need for any configuration or installation of software on the local machine. This makes it an ideal solution for scenarios where learners do not have administrator permissions to install software and cannot access Azure subscriptions directly. Azure Notebooks support data visualization libraries in Python, such as Matplotlib, Seaborn, or Plotly, making it suitable for the practical training aimed at acquainting learners with data visualization creation.</p></blockquote>

<blockquote><p><strong>sl_mslconsulting</strong> <code>(Wed 05 Jun 2024 20:22)</code> - <em>Upvotes: 1</em></p><p>Seems Azure Notebooks is no longer available.</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Fri 17 May 2024 05:16)</code> - <em>Upvotes: 2</em></p><p>I understood C may be the best choice here, however, how could you use azure notebooks without subscription?
notebook prerequisites:
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Fri 07 Jul 2023 19:54)</code> - <em>Upvotes: 3</em></p><p>I dont understand why does it say they are unable to access Azure subscriptions but they can use some Azure services like Azure notebooks. Can someone please explain?</p></blockquote>
<blockquote><p><strong>daviduzo</strong> <code>(Tue 20 Jun 2023 17:14)</code> - <em>Upvotes: 1</em></p><p>Other options require you to install additional software which the no admin access disallows</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sat 12 Mar 2022 10:39)</code> - <em>Upvotes: 3</em></p><p>Answer is correct</p></blockquote>
<blockquote><p><strong>txu002</strong> <code>(Thu 03 Mar 2022 03:04)</code> - <em>Upvotes: 1</em></p><p>Configuring the use of Azure Kubernetes Service</p></blockquote>

</details>

---

[<< Previous Question](question_17.md) | [Home](../index.md) | [Next Question >>](question_19.md)
