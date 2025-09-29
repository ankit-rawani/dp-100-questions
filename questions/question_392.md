# Question 392

You retrain an existing model.

You need to register the new version of a model while keeping the current version of the model in the registry.

What should you do?

- A.Register a model with a different name from the existing model and a custom property named version with the value 2.
- B.Register the model with the same name as the existing model.
- C.Save the new model in the default datastore with the same name as the existing model. Do not register the new model.
- D.Delete the existing model and register the new one with the same name.

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

<p>Model version: A version of a registered model. When a new model is added to the Model Registry, it is added as Version 1. Each model registered to the same model name increments the version number.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/databricks/applications/mlflow/model-registry</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Abhinav_nasaiitkgp</strong> <code>(Fri 23 Jul 2021 21:00)</code> - <em>Upvotes: 11</em></p><p>Answer is correct.
Model version: A version of a registered model. When a new model is added to the Model Registry, it is added as Version 1. Each model registered to the same model name increments the version number.</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 15:20)</code> - <em>Upvotes: 7</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 14:10)</code> - <em>Upvotes: 1</em></p><p>registering a model with the same name as an existing model will automatically create a new version of that model. Each time you register a model with the same name, the version number increments by one.</p></blockquote>

</details>

---

[<< Previous Question](question_391.md) | [Home](../index.md) | [Next Question >>](question_393.md)
