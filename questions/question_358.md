# Question 358

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Machine Learning workspace.

You plan to tune model hyperparameters by using a sweep job.

You need to find a sampling method that supports early termination of low-performance jobs and continuous hyperparameters.

Solution: Use the Bayesian sampling method over the hyperparameter space.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>445f1bd</strong> <code>(Wed 02 Jul 2025 04:27)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.hyperdrive.bayesianparametersampling?view=azure-ml-py see this in the note section....Bayesian sampling does not support early termination policies. When using Bayesian parameter sampling, use NoTerminationPolicy, set early termination policy to None, or leave off the early_termination_policy parameter.</p></blockquote>
<blockquote><p><strong>sanctafrax</strong> <code>(Sat 01 Feb 2025 22:35)</code> - <em>Upvotes: 1</em></p><p>wasnt sure myself. Chatgpt explained it:
- Bayesian sampling support early termination of low-performing jobs
- Bayesian sampling can handle continuous hyperparameters.

Therefore, the answer is yes?</p></blockquote>

<blockquote><p><strong>gunn_m</strong> <code>(Sun 01 Dec 2024 00:18)</code> - <em>Upvotes: 1</em></p><p>You need to use Bandit for this</p></blockquote>

</details>

---

[<< Previous Question](question_357.md) | [Home](../index.md) | [Next Question >>](question_359.md)
