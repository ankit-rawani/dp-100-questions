# Question 337

You use Azure Machine Learning to train a model.

You must use Bayesian sampling to tune hyperparameters.

You need to select a learning_rate parameter distribution.

Which two distributions can you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- A.Uniform
- B.Choice
- C.QNormal
- D.Normal
- E.LogUniform

<details>
  <summary>Show Suggested Answer</summary>

<strong>AB</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>damaldon</strong> <code>(Fri 05 Jul 2024 19:21)</code> - <em>Upvotes: 6</em></p><p>Bayesian sampling only supports choice, uniform, and quniform distributions over the search space.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Tue 07 Jan 2025 04:06)</code> - <em>Upvotes: 1</em></p><p>Bayesian sampling only supports choice, uniform, and quniform</p></blockquote>

</details>

---

[<< Previous Question](question_336.md) | [Home](../index.md) | [Next Question >>](question_338.md)
