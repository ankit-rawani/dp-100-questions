# Question 295

You are implementing hyperparameter tuning by using Bayesian sampling for a model training from a notebook. The notebook is in an Azure Machine Learning workspace that uses a compute cluster with 20 nodes.

The code implements Bandit termination policy with slack factor set to 0.2 and the HyperDriveConfig class instance with max_concurrent_runs set to 10.

You must increase effectiveness of the tuning process by improving sampling convergence.

You need to select which sampling convergence to use.

What should you select?

- A.Set the value of slack factor of early_termination_policy to 09.
- B.Set the value of max_concurrent_runs of HyperDriveConfig to 4.
- C.Set the value of slack factor of early_termination_policy to 0.1.
- D.Set the value of max_concurrent_runs of HyperDriveConfig to 20.

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>esimsek</strong> <code>(Wed 27 Sep 2023 08:15)</code> - <em>Upvotes: 6</em></p><p>The number of concurrent jobs has an impact on the effectiveness of the tuning process. A &quot;smaller number of concurrent jobs&quot; may lead to &quot;better sampling convergence&quot;, since the smaller degree of parallelism increases the number of jobs that benefit from previously completed jobs.</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Fri 01 Dec 2023 18:56)</code> - <em>Upvotes: 2</em></p><p>it&#x27;s true, because we use Bayesian sampling</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 08:28)</code> - <em>Upvotes: 1</em></p><p>B is correct: Bayesian optimization uses the results of previous runs to inform the selection of the next set of hyperparameters. Running too many concurrent runs can reduce the effectiveness of Bayesian optimization because the results of the previous runs are not immediately available to inform the next set of runs.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Mon 02 Sep 2024 20:02)</code> - <em>Upvotes: 1</em></p><p>does bayesian sampling has early termination policy? i understand, only random and grid sampling have?</p></blockquote>
<blockquote><p><strong>Mal42</strong> <code>(Thu 22 Feb 2024 09:59)</code> - <em>Upvotes: 4</em></p><p>On exam 18 Aug 2023</p></blockquote>
<blockquote><p><strong>oakmm</strong> <code>(Sat 23 Sep 2023 12:54)</code> - <em>Upvotes: 2</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters#bayesian-sampling</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Thu 21 Sep 2023 13:21)</code> - <em>Upvotes: 1</em></p><p>Answer is correct.</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Thu 21 Sep 2023 13:18)</code> - <em>Upvotes: 1</em></p><p>I *think* this is D</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Thu 21 Sep 2023 13:21)</code> - <em>Upvotes: 5</em></p><p>Please delete this comment.</p></blockquote>

</details>

---

[<< Previous Question](question_294.md) | [Home](../index.md) | [Next Question >>](question_296.md)
