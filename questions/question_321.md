# Question 321

You create an Azure Machine Learning workspace. You are implementing hyperparameter tuning for a model training from a notebook.

You must configure a Bandit termination policy that provides the following outcome:

If the value of the primary metric of AUC is 0.8 at the point of evaluation intervals, any run with the primary metric value below 0.66 will be terminated.

You need to identify which Bandit termination policy configuration to use.

What should you identify?

* A.Set slack_amount to 0.2.
* B.Set slack_factor to 0.1.
* C.Set slack_factor to 0.2.
* D.Set slack_amount to 0.1.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>kay1101</strong> <code>(Sat 23 Nov 2024 12:05)</code> - <em>Upvotes: 1</em></p><p>quote from MS Doc:
For example, consider a Bandit policy applied at interval 10. Assume that the best performing job at interval 10 reported a primary metric is 0.8 with a goal to maximize the primary metric. If the policy specifies a slack_factor of 0.2, any training jobs whose best metric at interval 10 is less than 0.66 (0.8/(1+slack_factor)) will be terminated.

link:https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2#bandit-policy</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Sun 04 Aug 2024 03:06)</code> - <em>Upvotes: 1</em></p><p>its correct</p></blockquote>
<blockquote><p><strong>Tin_Tin</strong> <code>(Thu 18 Jul 2024 14:42)</code> - <em>Upvotes: 3</em></p><p>correct.
For example, consider a Bandit policy applied at interval 10. Assume that the best performing job at interval 10 reported a primary metric is 0.8 with a goal to maximize the primary metric. If the policy specifies a slack_factor of 0.2, any training jobs whose best metric at interval 10 is less than 0.66 (0.8/(1+slack_factor)) will be terminated.</p></blockquote>
<blockquote><p><strong>vprowerty</strong> <code>(Fri 19 Jul 2024 09:53)</code> - <em>Upvotes: 1</em></p><p>Hi Tin_Tin are you preparing the exam now? Do you think the questions on this website are accurated?</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Sun 03 Dec 2023 16:21)</code> - <em>Upvotes: 4</em></p><p>0.8/1+0.2 = 0.6(6)
Correct</p></blockquote>
<blockquote><p><strong>paperflying</strong> <code>(Fri 27 Oct 2023 17:37)</code> - <em>Upvotes: 1</em></p><p>correct.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2#bandit-policy</p></blockquote>

</details>

---

[<< Previous Question](question_320.md) | [Home](/index.md) | [Next Question >>](question_322.md)
