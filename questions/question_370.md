# Question 370

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Machine Learning workspace.

You plan to tune model hyperparameters by using a sweep job.

You need to find a sampling method that supports early termination of low-performance jobs and continuous hyperparameters.

Solution: Use the Sobol sampling method over the hyperparameter space.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>b805b03</strong> <code>(Mon 07 Jul 2025 12:50)</code> - <em>Upvotes: 1</em></p><p>I would say &quot;yes&quot;:

Sobol is a type of random sampling supported by sweep job types.
Random sampling supports discrete and continuous hyperparameters. It supports early termination of low-performance jobs

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2</p></blockquote>

</details>

---

[<< Previous Question](question_369.md) | [Home](/index.md) | [Next Question >>](question_371.md)
