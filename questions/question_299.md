# Question 299

HOTSPOT

-

You use Azure Machine Learning to implement hyperparameter tuning with a Bandit early termination policy.

The policy uses a slack_factor set to 0.1. an evaluation interval set to 1, and an evaluation delay set to 5.

You need to evaluate the outcome of the early termination policy.

What should you evaluate? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q299_q_image418.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q299_ans_0_image419.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>3a0b61c</strong> <code>(Thu 19 Sep 2024 00:04)</code> - <em>Upvotes: 2</em></p><p>correct
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2#bandit-policy</p></blockquote>
<blockquote><p><strong>rahuljain788</strong> <code>(Sat 23 Sep 2023 22:24)</code> - <em>Upvotes: 2</em></p><p>https://azure.github.io/azureml-sdk-for-r/reference/bandit_policy.html</p></blockquote>
<blockquote><p><strong>rahuljain788</strong> <code>(Sat 23 Sep 2023 22:24)</code> - <em>Upvotes: 4</em></p><p># In this example, the early termination policy is applied at every interval
# when metrics are reported, starting at evaluation interval 5. Any run whose
# best metric is less than (1 / (1 + 0.1)) or 91\% of the best performing run will
# be terminated
if (FALSE) {
early_termination_policy = bandit_policy(slack_factor = 0.1,
                                         evaluation_interval = 1L,
                                         delay_evaluation = 5L)
}</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Fri 01 Dec 2023 19:25)</code> - <em>Upvotes: 2</em></p><p>evaluation delay set to 5 not evaluation interval</p></blockquote>

</details>

---

[<< Previous Question](question_298.md) | [Home](/index.md) | [Next Question >>](question_300.md)
