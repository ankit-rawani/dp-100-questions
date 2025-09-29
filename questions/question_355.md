# Question 355

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Machine Learning workspace.

You plan to tune model hyperparameters by using a sweep job.

You need to find a sampling method that supports early termination of low-performance jobs and continuous hyperparameters.

Solution: Use the grid sampling method over the hyperparameter space.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>D0ktor</strong> <code>(Tue 19 Nov 2024 22:44)</code> - <em>Upvotes: 1</em></p><p>No. Although Grid sampling supports early termination, does not  support continuous parameters</p></blockquote>
<blockquote><p><strong>VeraKo</strong> <code>(Tue 09 Jul 2024 13:42)</code> - <em>Upvotes: 1</em></p><p>The answer is No, because grid search supports early termination but does not support continuous hyperparameters. It supports only discrete ones

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>0ea0482</strong> <code>(Wed 19 Jun 2024 10:37)</code> - <em>Upvotes: 2</em></p><p>It should be yes. Random and Grid sampling methods support early termination.</p></blockquote>

</details>

---

[<< Previous Question](question_354.md) | [Home](/index.md) | [Next Question >>](question_356.md)
