# Question 336

You create an Azure Machine Learning workspace named workspace1. The workspace contains a Python SDK v2 notebook that uses MLflow to collect model training metrics and artifacts from your local computer.

You must reuse the notebook to run on Azure Machine Learning compute instance in workspace1.

You need to continue to log metrics and artifacts from your data science code.

What should you do?

- A.Instantiate the job class.
- B.Instantiate the MLCIient class.
- C.Log in to workspace1.
- D.Configure the tracking URL.

<details>
  <summary>Show Suggested Answer</summary>

<strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>AnsiDP100</strong> <code>(Fri 21 Feb 2025 02:53)</code> - <em>Upvotes: 1</em></p><p>D is the right answer.</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Tue 07 Jan 2025 04:02)</code> - <em>Upvotes: 1</em></p><p>C. Log in to workspace1.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 09 Dec 2024 13:37)</code> - <em>Upvotes: 2</em></p><p>Tracking URL is mandatory, choose D</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Wed 27 Nov 2024 04:54)</code> - <em>Upvotes: 2</em></p><p>To connect MLflow to an Azure Machine Learning workspace, you need the tracking URI for the workspace. Each workspace has its own tracking URI and it has the protocol azureml://.
Link: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow-configure-tracking?view=azureml-api-2&amp;tabs=python%2Cmlflow</p></blockquote>
<blockquote><p><strong>a6cb3b0</strong> <code>(Fri 27 Sep 2024 23:19)</code> - <em>Upvotes: 1</em></p><p>You should log in to workspace 1</p></blockquote>
<blockquote><p><strong>Mikku123</strong> <code>(Tue 06 Feb 2024 22:10)</code> - <em>Upvotes: 3</em></p><p>C is the answer !</p></blockquote>

</details>

---

[<< Previous Question](question_335.md) | [Home](../index.md) | [Next Question >>](question_337.md)
