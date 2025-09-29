# Question 442

You create an Azure Machine Learning workspace.

You must use the Python SDK v2 to implement an experiment from a Jupyter notebook in the workspace. The experiment must log a list of numeral metrics.

You need to implement a method to log a list of numeral metrics.

Which method should you use?

- A.mlflow.log_metric()
- B.mlflow.log.batch()
- C.mlflow.log_image()
- D.mlflow.log_artifact()

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>hbase</strong> <code>(Tue 17 Oct 2023 15:58)</code> - <em>Upvotes: 6</em></p><p>B. log_batch</p></blockquote>
<blockquote><p><strong>ferdcoz</strong> <code>(Fri 24 Jan 2025 17:59)</code> - <em>Upvotes: 2</em></p><p>Performance considerations: If you need to log multiple metrics (or multiple values for the same metric), avoid making calls to mlflow.log_metric in loops. Better performance can be achieved by using asynchronous logging with mlflow.log_metric(&quot;metric1&quot;, 9.42, synchronous=False) or by logging a batch of metrics

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics?view=azureml-api-2&amp;tabs=interactive#logging-metrics</p></blockquote>

<blockquote><p><strong>jefimija</strong> <code>(Mon 04 Nov 2024 08:44)</code> - <em>Upvotes: 2</em></p><p>list of numeric metrics isn&#x27;t exactly a batch</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 18 May 2024 03:42)</code> - <em>Upvotes: 2</em></p><p>A is Correct!</p></blockquote>
<blockquote><p><strong>LMCloud1000</strong> <code>(Wed 10 Apr 2024 13:32)</code> - <em>Upvotes: 1</em></p><p>Answer is B to Log a list of metrics.   A would be for only logging 1 metric</p></blockquote>
<blockquote><p><strong>indomanish</strong> <code>(Thu 29 Feb 2024 10:08)</code> - <em>Upvotes: 1</em></p><p>correct .CHTGPT :To log a list of numeral metrics in your Azure Machine Learning experiment using the Python SDK v2, you should use the following method:

mlflow.log_metric(metric_name, metric_value): This method allows you to log a numerical value (such as accuracy, loss, or any other metric) to the run with the given name. The metric will be stored in the run record within the experiment.</p></blockquote>

<blockquote><p><strong>vv_bb</strong> <code>(Sat 25 Nov 2023 19:16)</code> - <em>Upvotes: 2</em></p><p>... log a list of numeric metrics ..
The answer is B
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics?view=azureml-api-2&amp;tabs=interactive#logging-metrics</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 07 Jul 2023 19:58)</code> - <em>Upvotes: 2</em></p><p>Correct.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics?view=azureml-api-2&amp;tabs=interactive#logging-metrics</p></blockquote>

</details>

---

[<< Previous Question](question_441.md) | [Home](../index.md) | [Next Question >>](question_443.md)
