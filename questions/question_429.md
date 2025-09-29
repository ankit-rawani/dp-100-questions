# Question 429

You manage an Azure Machine Learning workspace.

You build a custom model you must log with MLflow. The custom model includes the following:

•	The model is not natively supported by MLflow.

•	The model cannot be serialized in Pickle format.

•	The model source code is complex.

•	The Python library for the model must be packaged with the model.

You need to create a custom model flavor to enable logging with MLflow.

What should you use?

* A.model loader
* B.artifacts
* C.model wrapper
* D.custom signatures

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 10:22)</code> - <em>Upvotes: 1</em></p><p>A is correct</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Sun 26 May 2024 04:17)</code> - <em>Upvotes: 1</em></p><p>A. model loader
reference:
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-mlflow-models?view=azureml-api-2&amp;tabs=loader#logging-custom-models</p></blockquote>
<blockquote><p><strong>BR_CS</strong> <code>(Thu 17 Aug 2023 13:55)</code> - <em>Upvotes: 3</em></p><p>See comments by phdykd and damaldon. A is correct.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 27 Jul 2023 18:53)</code> - <em>Upvotes: 1</em></p><p>A. https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-mlflow-models?view=azureml-api-2&amp;tabs=loader</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 07 Jul 2023 18:34)</code> - <em>Upvotes: 2</em></p><p>Ans. A
Sometimes your model logic is complex and there are several source files that your model loads on inference time. This would be the case when you have a Python library for your model for instance. In this scenario, you want to package the library all along with your model so it can move as a single piece.

Use this method when:

    Your model can&#x27;t be serialized in Pickle format or there is a better format available for that.
    Your model artifacts can be stored in a folder where all the requiered artifacts are placed.
    Your model source code is complex and it requires multiple Python files. Potentially, there is a library that supports your model.
    You want to customize the way the model is loaded and how the predict function works.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-log-mlflow-models?view=azureml-api-2&amp;tabs=loader</p></blockquote>

</details>

---

[<< Previous Question](question_428.md) | [Home](/index.md) | [Next Question >>](question_430.md)
