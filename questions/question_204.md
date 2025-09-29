# Question 204

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are creating a new experiment in Azure Machine Learning Studio.

One class has a much smaller number of observations than the other classes in the training set.

You need to select an appropriate data sampling strategy to compensate for the class imbalance.

Solution: You use the Stratified split for the sampling mode.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>timosi</strong> <code>(Thu 31 Mar 2022 14:07)</code> - <em>Upvotes: 17</em></p><p>I would say the answer is correct. 
The question is not how to make the sample more balanced but how to deal with the unbalanced sample. And stratified approach helps to handle an unbalanced sample.</p></blockquote>
<blockquote><p><strong>beny</strong> <code>(Thu 18 Aug 2022 01:26)</code> - <em>Upvotes: 1</em></p><p>Agree as well</p></blockquote>
<blockquote><p><strong>treadst0ne</strong> <code>(Mon 20 Jun 2022 19:24)</code> - <em>Upvotes: 2</em></p><p>Totally agree.</p></blockquote>
<blockquote><p><strong>concernedCitizen</strong> <code>(Tue 13 Jul 2021 16:42)</code> - <em>Upvotes: 15</em></p><p>Apparently SMOTE is the only way in MSFT&#x27;s mind to fix undersampled datasets</p></blockquote>
<blockquote><p><strong>a_1234567_</strong> <code>(Mon 26 Jul 2021 11:24)</code> - <em>Upvotes: 8</em></p><p>It might seem so just based on a few undersampled questions :)
But no. Even the auto ML has some variety suggested:
https://docs.microsoft.com/en-us/azure/machine-learning/concept-manage-ml-pitfalls#handle-imbalanced-data</p></blockquote>
<blockquote><p><strong>umair_hanu</strong> <code>(Thu 11 Jul 2024 05:00)</code> - <em>Upvotes: 1</em></p><p>agreed with timosi</p></blockquote>
<blockquote><p><strong>mkk888</strong> <code>(Tue 25 Jun 2024 18:34)</code> - <em>Upvotes: 1</em></p><p>there are other techniques apart from oversampling that work just as well, in those situations too you should use stratified split to make sure your test set has samples from the rarer class. so technically if you are using such a model(hyperparameter) you can achieve your goal, i&#x27;d say it should be yes but it&#x27;s probably no cause microsoft has promoted SMOTE as the go to solution.</p></blockquote>
<blockquote><p><strong>krishna1818</strong> <code>(Wed 29 May 2024 10:19)</code> - <em>Upvotes: 1</em></p><p>Maybe SMOTE</p></blockquote>
<blockquote><p><strong>Sumit_DP100</strong> <code>(Thu 15 Jun 2023 18:39)</code> - <em>Upvotes: 7</em></p><p>Stratified Sampling does not guarantee balanced dataset. It just makes sure the proportion of classes are sampled in equal proportion. The imbalance issue will still be there so SMOTE is the right option.</p></blockquote>
<blockquote><p><strong>FU_User</strong> <code>(Fri 19 May 2023 09:35)</code> - <em>Upvotes: 5</em></p><p>I guess the keyword is &quot;compensate&quot;
If you have a stratified split you only guarantee that the labels are in the same proportion in test and train set (95/5 incoming data -&gt; 95/5 training set and 95/5 testing set)
This doesn&#x27;t compensate for anything it just doesn&#x27;t introduce a new problem on limited training data, for example not having a particular label in the training set at all in the worst case.

As SMOTE  generates new data points it &quot;compensates&quot;.</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Fri 23 Dec 2022 18:56)</code> - <em>Upvotes: 3</em></p><p>Given answer is correct</p></blockquote>

</details>

---

[<< Previous Question](question_203.md) | [Home](/index.md) | [Next Question >>](question_205.md)
