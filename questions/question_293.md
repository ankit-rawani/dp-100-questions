# Question 293

HOTSPOT

-

You use Azure Machine Learning to implement hyperparameter tuning.

Training runs must terminate when the primary metric is lowered by 25 percent or more compared to the best performing run.

You need to configure an early termination policy to terminate training jobs.

Which values should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q293_q_image410.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q293_ans_0_image411.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>oakmm</strong> <code>(Sat 23 Sep 2023 12:34)</code> - <em>Upvotes: 5</em></p><p>would Truncation Selection and Truncation_percentage be better answer?</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 08:24)</code> - <em>Upvotes: 2</em></p><p>Bandit Policy:
The Bandit policy is an early termination policy that stops poorly performing runs early based on the ratio of the performance of the run to the best performing run. This is suitable for the given requirement as it compares the primary metric of each run against the best run and terminates those that fall below a certain threshold.
slack_factor:
The slack_factor parameter defines the allowable slack (tolerance) as a ratio. A slack_factor of 0.75 means that runs which perform worse than 75% of the best run (i.e., lowered by 25% or more) will be terminated.</p></blockquote>
<blockquote><p><strong>Mal42</strong> <code>(Thu 22 Feb 2024 09:55)</code> - <em>Upvotes: 4</em></p><p>On exam 18 Aug 2023</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Fri 01 Dec 2023 18:40)</code> - <em>Upvotes: 3</em></p><p>Bandit policy is based on slack factor/slack amount and evaluation interval. Bandit policy ends a job when the primary metric isn&#x27;t within the specified slack factor/slack amount of the most successful job.</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Thu 21 Sep 2023 13:12)</code> - <em>Upvotes: 4</em></p><p>Correct: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters#bandit-policy</p></blockquote>

</details>

---

[<< Previous Question](question_292.md) | [Home](/index.md) | [Next Question >>](question_294.md)
