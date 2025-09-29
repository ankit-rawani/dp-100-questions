# Question 269

HOTSPOT -

You are running a training experiment on remote compute in Azure Machine Learning.

The experiment is configured to use a conda environment that includes the mlflow and azureml-contrib-run packages.

You must use MLflow as the logging package for tracking metrics generated in the experiment.

You need to complete the script for the experiment.

How should you complete the code? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q269_q_0029100001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q269_ans_0_0029200001.png" alt="Answer Image"><br>
<p>Box 1: import mlflow -</p>
<p>Import the mlflow and Workspace classes to access MLflow&#x27;s tracking URI and configure your workspace.</p>
<p>Box 2: mlflow.start_run()</p>
<p>Set the MLflow experiment name with set_experiment() and start your training run with start_run().</p>
<p>Box 3: mlflow.log_metric(&#x27; ..&#x27;)</p>
<p>Use log_metric() to activate the MLflow logging API and begin logging your training run metrics.</p>
<p>Box 4: mlflow.end_run()</p>
<p>Close the run:</p>
<p>run.endRun()</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>dev2dev</strong> <code>(Tue 20 Sep 2022 11:31)</code> - <em>Upvotes: 15</em></p><p>Correct
https://www.mlflow.org/docs/latest/python_api/mlflow.html</p></blockquote>
<blockquote><p><strong>Anty85</strong> <code>(Thu 22 Sep 2022 09:31)</code> - <em>Upvotes: 6</em></p><p>Yup. https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Sun 08 Sep 2024 11:25)</code> - <em>Upvotes: 1</em></p><p>Exactly this question was on exam 07/March/2023</p></blockquote>
<blockquote><p><strong>ABHINAVY27</strong> <code>(Sun 12 Nov 2023 23:08)</code> - <em>Upvotes: 1</em></p><p>You don&#x27;t see end_run in the docs coz they use &#x27;while mlflow.start_run&#x27; to avoid using it @ TheYazan</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Wed 06 Sep 2023 07:27)</code> - <em>Upvotes: 1</em></p><p>I don&#x27;t see any use of end_run in the docs</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Wed 06 Sep 2023 07:29)</code> - <em>Upvotes: 1</em></p><p>and what are the libraries to log metrics?</p></blockquote>
<blockquote><p><strong>AI247</strong> <code>(Sun 07 May 2023 21:10)</code> - <em>Upvotes: 2</em></p><p>on exam 5 Nov 2021</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Thu 20 Apr 2023 09:51)</code> - <em>Upvotes: 3</em></p><p>on 19Oct2021</p></blockquote>

</details>

---

[<< Previous Question](question_268.md) | [Home](/index.md) | [Next Question >>](question_270.md)
