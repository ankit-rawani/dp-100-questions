# Question 361

You manage an Azure Machine Learning workspace.

You experiment with an MLflow model that trains interactively by using a notebook in the workspace.

You need to log dictionary type artifacts of the experiments in Azure Machine Learning by using MLflow.

Which syntax should you use?

* A.mlflow.log_input(my_dict)
* B.mlflow.log_metric("my_metric", my_dict)
* C.mlflow.log_metrics(my_dict)
* D.mlflow.log_text("my_metric", my_dict)

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>avinyc</strong> <code>(Wed 08 Jan 2025 02:26)</code> - <em>Upvotes: 3</em></p><p>Ref - https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_input

import mlflow

metrics = {&quot;mse&quot;: 2500.00, &quot;rmse&quot;: 50.00}

# Log a batch of metrics
with mlflow.start_run():
    mlflow.log_metrics(metrics)

# Log a batch of metrics in async fashion.
with mlflow.start_run():
    mlflow.log_metrics(metrics, synchronous=False)</p></blockquote>
<blockquote><p><strong>jl420</strong> <code>(Fri 08 Nov 2024 18:58)</code> - <em>Upvotes: 2</em></p><p>Answer is C - 
mlflow.log_metrics(my_dict)

Explanation:
In MLflow, when you want to log dictionary-type artifacts that contain multiple metrics, you should use the mlflow.log_metrics() method. This method allows you to log multiple key-value pairs (i.e., a dictionary) as metrics.</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Wed 23 Oct 2024 13:17)</code> - <em>Upvotes: 1</em></p><p>log_artifact maybe?</p></blockquote>
<blockquote><p><strong>AzureGeek79</strong> <code>(Sat 12 Oct 2024 02:58)</code> - <em>Upvotes: 2</em></p><p>the correct answer is log_params which is not included in the available options</p></blockquote>

</details>

---

[<< Previous Question](question_360.md) | [Home](/index.md) | [Next Question >>](question_362.md)
