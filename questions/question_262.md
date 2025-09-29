# Question 262

You are training machine learning models in Azure Machine Learning. You use Hyperdrive to tune the hyperparameters.

In previous model training and tuning runs, many models showed similar performance.

You need to select an early termination policy that meets the following requirements:

✑ accounts for the performance of all previous runs when evaluating the current run avoids comparing the current run with only the best performing run to date

![Question Image](../images/q262_q_0028000002.png)

Which two early termination policies should you use? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

- A.Median stopping
- B.Bandit
- C.Default
- D.Truncation selection

<details>
  <summary>Show Suggested Answer</summary>

<strong>AD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>dushmantha</strong> <code>(Sat 27 Aug 2022 07:06)</code> - <em>Upvotes: 25</em></p><p>Condition 1: account for all previous runs
Condition 2: avoid comparing with only best performing run up to date

1. Condition 1: ok, Condition 2: ok (calculates running avg and its median at every step)
2. Condition 1: ok, Condition 2: no (slack transformed value is compared with previous best value)
3. Condition 1: no, Condition 2: no (no termination)
4. Condition 1: ok, Condition 2: ok (to get lowest performing runs need to account for all runs)</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 20 Jul 2024 05:26)</code> - <em>Upvotes: 1</em></p><p>A and D</p></blockquote>
<blockquote><p><strong>Peeking</strong> <code>(Thu 14 Mar 2024 10:29)</code> - <em>Upvotes: 2</em></p><p>Median stopping is an early termination policy based on running averages of primary metrics reported by the runs. This policy computes running averages across all training runs and stops runs whose primary metric value is worse than the median of the averages.

Truncation selection cancels a percentage of lowest performing runs at each evaluation interval. Runs are compared using the primary metric.</p></blockquote>

<blockquote><p><strong>phdykd</strong> <code>(Wed 21 Feb 2024 18:36)</code> - <em>Upvotes: 2</em></p><p>So, the recommended early termination policies in this case are A (Median Stopping) and B (Bandit) because they both account for the performance of all previous runs when evaluating the current run and do not rely only on the best performing run to date.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 21 Feb 2024 18:17)</code> - <em>Upvotes: 2</em></p><p>A. Median stopping B. Bandit</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sun 18 Jun 2023 01:46)</code> - <em>Upvotes: 2</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Sat 22 Apr 2023 10:51)</code> - <em>Upvotes: 1</em></p><p>on exam 04/22/2022</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sun 12 Mar 2023 01:40)</code> - <em>Upvotes: 3</em></p><p>AD see Dushmantha explain</p></blockquote>
<blockquote><p><strong>yuanxuan1</strong> <code>(Fri 10 Feb 2023 06:36)</code> - <em>Upvotes: 2</em></p><p>answer is AD</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Mon 19 Dec 2022 09:15)</code> - <em>Upvotes: 4</em></p><p>I agree with AD</p></blockquote>
<blockquote><p><strong>tunaktunak</strong> <code>(Sat 26 Nov 2022 12:20)</code> - <em>Upvotes: 2</em></p><p>On exam 26/11/2021</p></blockquote>
<blockquote><p><strong>VJPrakash</strong> <code>(Wed 10 Aug 2022 09:18)</code> - <em>Upvotes: 3</em></p><p>It should be B and D(Truncate instead of Default).

The default as per documentation means no termination policy.</p></blockquote>

<blockquote><p><strong>pancman</strong> <code>(Tue 11 Apr 2023 02:26)</code> - <em>Upvotes: 1</em></p><p>The correct answer should be A and D.</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Sun 07 Aug 2022 19:27)</code> - <em>Upvotes: 3</em></p><p>Given answers are correct.
- Truncation cancels a percentage of lowest performing runs at each evaluation interval;
- Bandit policy compares the value (Y + Y * slack_factor) to AUC value, and if smaller, cancels the run.

So &quot;Median stopping policy&quot; and &quot;Default&quot; are correct answers.

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters
https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.hyperdrive.banditpolicy?view=azure-ml-py#definition</p></blockquote>

<blockquote><p><strong>trickerk</strong> <code>(Sun 07 Aug 2022 19:29)</code> - <em>Upvotes: 1</em></p><p>&quot;accounts for the performance of all previous runs&quot;</p></blockquote>
<blockquote><p><strong>manualrg</strong> <code>(Sat 27 Jan 2024 22:49)</code> - <em>Upvotes: 1</em></p><p>To apply truncation policy , a percentile must be computed, so indeed it uses &quot;performance of all previous runs&quot; IMHO</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 11 Apr 2023 02:28)</code> - <em>Upvotes: 1</em></p><p>You&#x27;re wrong. The default policy is no early termination. Therefore it doesn&#x27;t satisfy the requirement in the question.
The correct answer is median and truncation. (A and D)</p></blockquote>
<blockquote><p><strong>slash_nyk</strong> <code>(Wed 03 Aug 2022 20:33)</code> - <em>Upvotes: 2</em></p><p>I take my words back. Median and Bandit look for best performing runs.. Truncation cancels at each interval</p></blockquote>
<blockquote><p><strong>slash_nyk</strong> <code>(Sat 16 Jul 2022 09:47)</code> - <em>Upvotes: 4</em></p><p>Median and Truncation are the correct answers</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Mon 25 Jul 2022 03:48)</code> - <em>Upvotes: 1</em></p><p>&quot;Truncation selection cancels a percentage of lowest performing runs at [each evaluation interval].&quot;</p></blockquote>
<blockquote><p><strong>guddusao</strong> <code>(Wed 13 Jul 2022 12:30)</code> - <em>Upvotes: 3</em></p><p>I don&#x27;t think default would be there. The right answer would be Median stopping policy and truncate selection policy both supports early termination policy.</p></blockquote>
<blockquote><p><strong>saurabh288</strong> <code>(Wed 20 Jul 2022 09:18)</code> - <em>Upvotes: 1</em></p><p>Truncation selection doesn&#x27;t stop the run.</p></blockquote>
<blockquote><p><strong>NickData90</strong> <code>(Mon 08 Aug 2022 07:01)</code> - <em>Upvotes: 4</em></p><p>How does a &quot;termination policy&quot; not stop a run? If I look at the docs it clearly says that it looks at all runs and cancels a percentage of this each interval: https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.hyperdrive.truncationselectionpolicy?view=azure-ml-py</p></blockquote>

</details>

---

[<< Previous Question](question_261.md) | [Home](/index.md) | [Next Question >>](question_263.md)
