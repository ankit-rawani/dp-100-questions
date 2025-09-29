# Question 353

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Machine Learning workspace.

You plan to tune model hyperparameters by using a sweep job.

You need to find a sampling method that supports early termination of low-performance jobs and continuous hyperparameters.

Solution: Use the random sampling method over the hyperparameter space.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>astone42</strong> <code>(Mon 13 Jan 2025 12:45)</code> - <em>Upvotes: 1</em></p><p>&quot;Random sampling supports discrete and continuous hyperparameters. It supports early termination of low-performance jobs. Some users do an initial search with random sampling and then refine the search space to improve results.&quot;</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Sat 14 Dec 2024 17:19)</code> - <em>Upvotes: 2</em></p><p>Sorry. I did a mistake:
Random sampling supports discrete and continuous hyperparameters. It supports early termination of low-performance jobs. Some users do an initial search with random sampling and then refine the search space to improve results.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Sun 01 Dec 2024 00:17)</code> - <em>Upvotes: 1</em></p><p>You need to use Bandit for this</p></blockquote>
<blockquote><p><strong>D0ktor</strong> <code>(Tue 19 Nov 2024 22:43)</code> - <em>Upvotes: 2</em></p><p>Random sampling supports discrete and continuous hyperparameters. It supports early termination of low-performance jobs. Some users do an initial search with random sampling and then refine the search space to improve results.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Wed 23 Oct 2024 13:14)</code> - <em>Upvotes: 1</em></p><p>it should be median stopping or bandit</p></blockquote>

</details>

---

[<< Previous Question](question_352.md) | [Home](/index.md) | [Next Question >>](question_354.md)
