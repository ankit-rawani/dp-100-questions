# Question 258

You plan to use the Hyperdrive feature of Azure Machine Learning to determine the optimal hyperparameter values when training a model.

You must use Hyperdrive to try combinations of the following hyperparameter values. You must not apply an early termination policy.

✑ learning_rate: any value between 0.001 and 0.1

✑ batch_size: 16, 32, or 64

You need to configure the sampling method for the Hyperdrive experiment.

Which two sampling methods can you use? Each correct answer is a complete solution.

NOTE: Each correct selection is worth one point.

- A.No sampling
- B.Grid sampling
- C.Bayesian sampling
- D.Random sampling

<details>
  <summary>Show Suggested Answer</summary>

<strong>CD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Abhinav_nasaiitkgp</strong> <code>(Fri 23 Jul 2021 21:29)</code> - <em>Upvotes: 17</em></p><p>Answer is correct as Grid Sampling doesn&#x27;t support continuous hyperparameter configuration</p></blockquote>
<blockquote><p><strong>PremPatrick</strong> <code>(Mon 15 May 2023 01:06)</code> - <em>Upvotes: 5</em></p><p>Correct!</p></blockquote>
<blockquote><p><strong>f82411e</strong> <code>(Mon 09 Jun 2025 12:00)</code> - <em>Upvotes: 1</em></p><p>C. Bayesian sampling requiere una política de terminación anticipada, lo cual la hace incompatible en este caso de acuerdo a la pregunta</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Sun 05 Jan 2025 23:16)</code> - <em>Upvotes: 1</em></p><p>B. Grid sampling 
D. Random sampling
Grid Sampling does not support continuous value but we can define a finely spaced range for learning rates and use that as hyperparameter
learning_rate_values = np.linspace(0.001, 0.1, num=10).tolist()</p></blockquote>
<blockquote><p><strong>Mal42</strong> <code>(Thu 22 Feb 2024 08:04)</code> - <em>Upvotes: 3</em></p><p>On exam 18 Aug 2023</p></blockquote>
<blockquote><p><strong>Peeking</strong> <code>(Thu 14 Sep 2023 09:05)</code> - <em>Upvotes: 2</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-tune-hyperparameters-v1</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Mon 21 Aug 2023 16:47)</code> - <em>Upvotes: 3</em></p><p>BD. Both Grid sampling and Random sampling can be used for configuring the sampling method for the Hyperdrive experiment.

Grid sampling will allow you to define a search space with different combinations of hyperparameters, and it will train the model with every possible combination of hyperparameters. This approach works well when the search space is relatively small.

Random sampling will randomly sample hyperparameters from the defined search space. This method can cover a larger search space more efficiently than grid sampling, and it can be useful when there are a large number of hyperparameters to tune.

Bayesian sampling is not an option in this case, as it requires an early termination policy to be applied in order to determine which hyperparameters to explore next based on the results of previous runs. Since an early termination policy is not allowed in this scenario, Bayesian sampling is not a viable option</p></blockquote>

<blockquote><p><strong>deyoz</strong> <code>(Sat 03 Aug 2024 02:37)</code> - <em>Upvotes: 1</em></p><p>baysian sampling doesn&#x27;t have any policy parameter.</p></blockquote>
<blockquote><p><strong>striver</strong> <code>(Fri 02 Dec 2022 11:48)</code> - <em>Upvotes: 4</em></p><p>CD is correct</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 11 Oct 2022 02:21)</code> - <em>Upvotes: 2</em></p><p>The answer is correct. Grid sampling only supports discrete hyperparameters. 
Refer to this link in Microsoft documentation:
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters#grid-sampling</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Mon 12 Sep 2022 00:35)</code> - <em>Upvotes: 2</em></p><p>Bayesian and Default don&#x27;t permit early termination.  Random and Grid support early termination</p></blockquote>
<blockquote><p><strong>Arend78</strong> <code>(Thu 15 Jun 2023 13:30)</code> - <em>Upvotes: 1</em></p><p>My guess is that &quot;A. No sampling&quot; is incorrect, since that would mean trying the infite of continuous values between between 0.001 and 0.1 for the learning rate</p></blockquote>
<blockquote><p><strong>wasthi</strong> <code>(Wed 22 Jun 2022 17:36)</code> - <em>Upvotes: 3</em></p><p>Correct answers</p></blockquote>
<blockquote><p><strong>dataimage</strong> <code>(Wed 25 May 2022 03:30)</code> - <em>Upvotes: 3</em></p><p>In  my opinion, the answer is A C. we need to select the sampling which is not supporting early termination. Random and Grid both are supporting the early termination</p></blockquote>
<blockquote><p><strong>Roszu</strong> <code>(Fri 05 Aug 2022 19:17)</code> - <em>Upvotes: 1</em></p><p>You clearly misinterpreted it, you cannot use early termination and on Random Sampling you don&#x27;t have to use it.</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Apr 2022 09:51)</code> - <em>Upvotes: 2</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Sat 09 Apr 2022 21:27)</code> - <em>Upvotes: 1</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>Niz__</strong> <code>(Wed 23 Mar 2022 08:54)</code> - <em>Upvotes: 1</em></p><p>Bayesian Sampling - https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.hyperdrive.bayesianparametersampling?view=azure-ml-py#:~:text=Bayesian%20sampling%20does%20not%20support,leave%20off%20the%20early_termination_policy%20parameter.
Random Sampling - https://docs.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters#:~:text=Random%20sampling%20supports%20discrete%20and,termination%20of%20low%2Dperformance%20runs.
Grid Sampling - https://docs.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters#:~:text=Grid%20sampling,-Grid%20sampling%20supports&amp;text=Supports%20early%20termination%20of%20low%2Dperformance%20runs.,-Grid%20sampling%20does
Random and Grid Sampling supports early termination policy for low-performance runs in the documentations. A and C maybe?</p></blockquote>
<blockquote><p><strong>Niz__</strong> <code>(Wed 23 Mar 2022 09:05)</code> - <em>Upvotes: 3</em></p><p>C and D is correct.  You can set policy to NoTerminationPolicy</p></blockquote>
<blockquote><p><strong>RyanTsai</strong> <code>(Fri 18 Mar 2022 09:37)</code> - <em>Upvotes: 4</em></p><p>the answer is B, D</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Tue 25 Jan 2022 15:37)</code> - <em>Upvotes: 2</em></p><p>&quot;Random sampling supports discrete and continuous hyperparameters. It supports early termination of low-performance runs.&quot;</p></blockquote>

</details>

---

[<< Previous Question](question_257.md) | [Home](../index.md) | [Next Question >>](question_259.md)
