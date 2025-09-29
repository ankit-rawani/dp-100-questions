# Question 275

You create a binary classification model by using Azure Machine Learning Studio.

You must tune hyperparameters by performing a parameter sweep of the model. The parameter sweep must meet the following requirements:

✑ iterate all possible combinations of hyperparameters

✑ minimize computing resources required to perform the sweep

You need to perform a parameter sweep of the model.

Which parameter sweep mode should you use?

- A.Random sweep
- B.Sweep clustering
- C.Entire grid
- D.Random grid

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>pepmir</strong> <code>(Fri 25 Jun 2021 20:23)</code> - <em>Upvotes: 20</em></p><p>Random grid:
You can also reduce the size of the grid and run a random grid sweep. Research has shown that this method yields the same results, but is more efficient computationally.
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/tune-model-hyperparameters</p></blockquote>
<blockquote><p><strong>rr200</strong> <code>(Tue 03 Aug 2021 12:09)</code> - <em>Upvotes: 9</em></p><p>D is right.  
A is incorrect, as Random Sweep does not iterate all possible combination and randomly select parameters
B is incorrect, as it is only for clustering algos
C is incorrect, as Entire grid is resource intensive</p></blockquote>
<blockquote><p><strong>f82411e</strong> <code>(Mon 09 Jun 2025 12:22)</code> - <em>Upvotes: 1</em></p><p>C is Correct</p></blockquote>
<blockquote><p><strong>7bbe541</strong> <code>(Sat 03 May 2025 14:31)</code> - <em>Upvotes: 2</em></p><p>should be C &quot;iterate all possible combinations of hyperparameters&quot;</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 24 Jul 2024 15:02)</code> - <em>Upvotes: 5</em></p><p>The question&#x27;s requirements seem a bit contradictory as it asks to &quot;iterate all possible combinations of hyperparameters&quot; (which points to Entire Grid) but also to &quot;minimize computing resources required to perform the sweep&quot; (which points to Random Sweep/Grid).

If we prioritize iterating over all combinations, then Entire Grid would be chosen. However, if we prioritize minimizing computational resources, then Random Sweep/Grid would be more suitable. As the question initially asks for iterating over all combinations, I chose Entire Grid in my previous response, but I acknowledge that if resource usage is a primary concern, Random Sweep/Grid would be more appropriate.</p></blockquote>

<blockquote><p><strong>PI_Team</strong> <code>(Thu 08 Aug 2024 11:21)</code> - <em>Upvotes: 1</em></p><p>I agree with you. To meet the requirement of iterating all possible combinations of hyperparameters while minimizing computing resources, you should use the “Entire grid” parameter sweep mode in Azure Machine Learning Studio. This mode performs a grid search over the entire hyperparameter space, trying all possible combinations of hyperparameter values. While this can be computationally expensive, it ensures that all combinations are tried and can result in finding the best combination of hyperparameters for your model. To minimize computing resources, you can carefully choose the range and granularity of the hyperparameters to be swept, and use parallel processing to speed up the sweep</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 22 Feb 2024 00:51)</code> - <em>Upvotes: 1</em></p><p>C. To iterate all possible combinations of hyperparameters, you should use the &quot;Entire grid&quot; parameter sweep mode in Azure Machine Learning Studio. This mode will sweep over all possible combinations of the hyperparameters that you specify.

While the &quot;Random sweep&quot; and &quot;Random grid&quot; modes can also help you minimize computing resources by only evaluating a subset of possible combinations, they may not guarantee that you will evaluate all possible combinations of hyperparameters. On the other hand, the &quot;Sweep clustering&quot; mode is not a valid parameter sweep mode in Azure Machine Learning Studio.</p></blockquote>

<blockquote><p><strong>ning</strong> <code>(Tue 06 Jun 2023 11:40)</code> - <em>Upvotes: 4</em></p><p>I do not understand this question, there might be something messed up 
https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/tune-model-hyperparameters
Only two options are: entire grid and random sweep, also it is stated only entire grid can try all possible combinations of values, so in any sense it cannot be D</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Tue 06 Jun 2023 11:46)</code> - <em>Upvotes: 1</em></p><p>The question is asking for check all possible combinations, not asking for the best results ...</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 11 Apr 2023 02:56)</code> - <em>Upvotes: 1</em></p><p>This question is outdated. In the newer version of ML Studio there are only two options to specify the parameter sweeping mode: 1) Entire grid 2) Random sweep</p></blockquote>
<blockquote><p><strong>Ankicaa</strong> <code>(Sat 18 Mar 2023 14:17)</code> - <em>Upvotes: 1</em></p><p>This is confusing. In Azure ML Studio and in Documentation is clearly that only options are entire grid and random sweep. But does random sweep tries every possible combination?</p></blockquote>
<blockquote><p><strong>MohammadKhubeb</strong> <code>(Sun 05 Feb 2023 12:29)</code> - <em>Upvotes: 1</em></p><p>Entire Grid is NOT because it is used when we do not know the best parameters to choose. Here, the binary classification is provided. So we need to select either Random Grid or Random Sweep.</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Sun 15 Jan 2023 06:21)</code> - <em>Upvotes: 2</em></p><p>given ans looks to be correct. Just try opening Tune Model Hyperparameters in old machine learning studio classic. The module has THREE options of Entire Grid, Random Sweep and Random Grid</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Thu 08 Dec 2022 10:06)</code> - <em>Upvotes: 1</em></p><p>I vote for D</p></blockquote>
<blockquote><p><strong>mikosann</strong> <code>(Fri 21 Oct 2022 09:53)</code> - <em>Upvotes: 3</em></p><p>Correct answer is Entire Grid. The document clearly states that Entire Grid should be used to try every possible combinations.
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/tune-model-hyperparameters</p></blockquote>
<blockquote><p><strong>claudiapatricia777</strong> <code>(Tue 18 Oct 2022 12:30)</code> - <em>Upvotes: 1</em></p><p>The correct answer is A- Random Sweep, since in Azure Machine Learning Studio we only have 2 options - Random Sweep and Entire Grid: https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/tune-model-hyperparameters#bkmk_sweep</p></blockquote>
<blockquote><p><strong>prasad06</strong> <code>(Tue 20 Sep 2022 10:33)</code> - <em>Upvotes: 1</em></p><p>Is this still being asked ? Applies to: Machine Learning Studio (classic) only</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Mon 25 Jul 2022 06:28)</code> - <em>Upvotes: 2</em></p><p>If you still have some doubt, then please read
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/tune-model-hyperparameters:
&quot;You can also reduce the size of the grid and run a random grid sweep. Research has shown that this method yields the same results, but is more efficient computationally.&quot;
So, given answer is correct!</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Wed 01 Jun 2022 18:46)</code> - <em>Upvotes: 1</em></p><p>You can also reduce the size of the grid and run a random grid sweep. Research has shown that this method yields the same results, but is more efficient computationally.

for those who are confused Ans is correct refer to link provided in Ans there you will get the below line :
You can also reduce the size of the grid and run a random grid sweep. Research has shown that this method yields the same results, but is more efficient computationally.</p></blockquote>

</details>

---

[<< Previous Question](question_274.md) | [Home](../index.md) | [Next Question >>](question_276.md)
