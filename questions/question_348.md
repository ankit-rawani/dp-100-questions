# Question 348

You manage an Azure Machine Learning workspace.

You must log multiple metrics by using MLflow.

You need to maximize logging performance.

What are two possible ways to achieve this goal? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- A.MLflowClient.log_batch
- B.mlflow.log_metrics
- C.mlflow.log_metric
- D.mlflow.log_param

<details>
  <summary>Show Suggested Answer</summary>

<strong>AB</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>avinyc</strong> <code>(Tue 07 Jan 2025 04:22)</code> - <em>Upvotes: 2</em></p><p>The correct answers are:

A. MLflowClient.log_batch
B. mlflow.log_metrics</p></blockquote>

<blockquote><p><strong>Murzfam</strong> <code>(Tue 28 Jan 2025 10:08)</code> - <em>Upvotes: 1</em></p><p>But, there is no option for log_metrics but log_metric</p></blockquote>
<blockquote><p><strong>testgm</strong> <code>(Mon 02 Dec 2024 15:55)</code> - <em>Upvotes: 1</em></p><p>No log_metrics, just log_metric</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Sun 11 Feb 2024 21:11)</code> - <em>Upvotes: 2</em></p><p>Performance considerations: If you need to log multiple metrics (or multiple values for the same metric), avoid making calls to mlflow.log_metric in loops. Better performance can be achieved by logging a batch of metrics. Use the method mlflow.log_metrics which accepts a dictionary with all the metrics you want to log at once or use MLflowClient.log_batch which accepts multiple type of elements for logging. See Log curves or list of values for an example.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Mon 05 Feb 2024 02:43)</code> - <em>Upvotes: 1</em></p><p>If you need to log multiple metrics (or multiple values for the same metric), avoid making calls to mlflow.log_metric in loops. Better performance can be achieved by logging a batch of metrics. Use the method mlflow.log_metrics which accepts a dictionary with all the metrics you want to log at once or use MLflowClient.log_batch which accepts multiple type of elements for logging. See Log curves or list of values for an example.

answer A,B</p></blockquote>

<blockquote><p><strong>Tin_Tin</strong> <code>(Sat 20 Jan 2024 08:25)</code> - <em>Upvotes: 1</em></p><p>A &amp; B are correct</p></blockquote>
<blockquote><p><strong>Ran2025</strong> <code>(Sun 22 Oct 2023 05:38)</code> - <em>Upvotes: 1</em></p><p>A &amp; B
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics?view=azureml-api-2&amp;tabs=interactive</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Thu 24 Aug 2023 13:55)</code> - <em>Upvotes: 4</em></p><p>Correct answer! :) 
Performance considerations: If you need to log multiple metrics (or multiple values for the same metric) avoid making calls to mlflow.log_metric in loops. Better performance can be achieved by logging batch of metrics. Use the method mlflow.log_metrics which accepts a dictionary with all the metrics you want to log at once or use MLflowClient.log_batch which accepts multiple type of elements for logging.

See here: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics?view=azureml-api-2&amp;tabs=interactive

SaM</p></blockquote>

<blockquote><p><strong>BR_CS</strong> <code>(Thu 17 Aug 2023 11:43)</code> - <em>Upvotes: 1</em></p><p>there is no &quot;log_metrics&quot; but &quot;log_metric&quot;</p></blockquote>
<blockquote><p><strong>Tin_Tin</strong> <code>(Sat 20 Jan 2024 08:25)</code> - <em>Upvotes: 1</em></p><p>Use mlflow.log_metrics() to log multiple metrics at once.</p></blockquote>
<blockquote><p><strong>SGES</strong> <code>(Wed 16 Aug 2023 11:06)</code> - <em>Upvotes: 1</em></p><p>AB is correct
Performance considerations: If you need to log multiple metrics (or multiple values for the same metric) avoid making calls to mlflow.log_metric in loops. Better performance can be achieved by logging batch of metrics. Use the method mlflow.log_metrics which accepts a dictionary with all the metrics you want to log at once or use MLflowClient.log_batch which accepts multiple type of elements for logging. See Logging curves or list of values for an example.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics?view=azureml-api-2&amp;tabs=interactive</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 08 Aug 2023 01:04)</code> - <em>Upvotes: 1</em></p><p>A,C is right</p></blockquote>
<blockquote><p><strong>abcd9999</strong> <code>(Wed 02 Aug 2023 06:06)</code> - <em>Upvotes: 2</em></p><p>There is no method called mlflow.log_metrics.  It&#x27;s mlflow.log_metric</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 26 Jul 2023 19:04)</code> - <em>Upvotes: 3</em></p><p>A. MLflowClient.log_batch
B. mlflow.log_metrics</p></blockquote>

</details>

---

[<< Previous Question](question_347.md) | [Home](../index.md) | [Next Question >>](question_349.md)
