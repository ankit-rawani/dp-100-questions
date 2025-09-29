# Question 427

You create an Azure Machine Learning workspace.

You must use the Python SDK v2 to implement an experiment from a Jupyter notebook in the workspace. The experiment must log string metrics.

You need to implement the method to log the string metrics.

Which method should you use?

* A.mlflow.log_artifact()
* B.mlflow.log.dict()
* C.mlflow.log_metric()
* D.mlflow.log_text()

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>445f1bd</strong> <code>(Mon 28 Jul 2025 02:29)</code> - <em>Upvotes: 1</em></p><p>mlflow.log_text(text: str, artifact_file: str, run_id: Optional[str] = None) → None[source]
Log text as an artifact.

Parameters
text – String containing text to log.

artifact_file – The run-relative artifact file path in posixpath format to which the text is saved (e.g. “dir/file.txt”).

run_id – If specified, log the artifact to the specified run. If not specified, log the artifact to the currently active run.

https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.log_metric</p></blockquote>
<blockquote><p><strong>Ben999</strong> <code>(Tue 07 Jan 2025 03:45)</code> - <em>Upvotes: 1</em></p><p>MLflow is primarily used to log numerical metrics. However, you can log string data as a parameter - mlflow.log_param(), or an artifact if string is too long or to safe as a file - mlfow.log_artifact</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Sun 01 Dec 2024 20:04)</code> - <em>Upvotes: 1</em></p><p>C is correct, becase D is to Log text in a text file and the question does not tals about text file.
Log text in a text file	mlflow.log_text(&quot;text string&quot;, &quot;notes.txt&quot;)	Text is persisted inside of the run in a text file with name notes.txt.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics?view=azureml-api-2&amp;tabs=interactive#logging-metrics</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 07 Jul 2023 18:39)</code> - <em>Upvotes: 2</em></p><p>Correct.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-view-metrics?view=azureml-api-2&amp;tabs=interactive#logging-metrics</p></blockquote>

</details>

---

[<< Previous Question](question_426.md) | [Home](/index.md) | [Next Question >>](question_428.md)
