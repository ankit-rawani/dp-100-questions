# Question 419

You create an MLflow model.

You must deploy the model to Azure Machine Learning for batch inference.

You need to create the batch deployment.

Which two components should you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

* A.Environment
* B.Model files
* C.Online endpoint
* D.Kubernetes online endpoint
* E.Compute target

<details>
  <summary>Show Suggested Answer</summary>

  <strong>BE</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Tommo565</strong> <code>(Thu 28 Mar 2024 05:33)</code> - <em>Upvotes: 6</em></p><p>Correct (I think)

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-mlflow-batch?tabs=cli

MLflow models don&#x27;t require you to indicate an environment or a scoring script when creating the deployments as it is created for you. However, you can specify them if you want to customize how the deployment does inference.</p></blockquote>
<blockquote><p><strong>Fercho5813</strong> <code>(Mon 28 Oct 2024 02:59)</code> - <em>Upvotes: 1</em></p><p>I think that is AE</p></blockquote>
<blockquote><p><strong>vv_bb</strong> <code>(Mon 25 Nov 2024 11:04)</code> - <em>Upvotes: 2</em></p><p>The MLflow model already describes the required environment, so there is no need to define it once again
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models?view=azureml-api-2&amp;tabs=azureml</p></blockquote>

</details>

---

[<< Previous Question](question_418.md) | [Home](/index.md) | [Next Question >>](question_420.md)
