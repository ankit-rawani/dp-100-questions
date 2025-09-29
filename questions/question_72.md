# Question 72

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are a data scientist using Azure Machine Learning Studio.

You need to normalize values to produce an output column into bins to predict a target column.

Solution: Apply a Quantiles normalization with a QuantileIndex normalization.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>kty</strong> <code>(Wed 17 Mar 2021 18:24)</code> - <em>Upvotes: 29</em></p><p>I think Answer is &#x27;A&#x27;

If you select the Quantiles binning mode, use the Quantile normalization option to determine how values are normalized prior to sorting into quantiles. Note that normalizing values transforms the values, but does not affect the final number of bins. For an example, see Effects of Different Normalization Methods.

The following normalization types are supported:

Percent: Values are normalized within the range [0,100]

PQuantile: Values are normalized within the range [0,1]

QuantileIndex: Values are normalized within the range [1,number of bins]</p></blockquote>
<blockquote><p><strong>l2azure</strong> <code>(Fri 09 Apr 2021 11:38)</code> - <em>Upvotes: 13</em></p><p>Answer is correct, only the binning mode &#x27;Entropy MDL&#x27; takes into account the target column.
See documentation:
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins</p></blockquote>
<blockquote><p><strong>lcgcastro96</strong> <code>(Tue 13 Jun 2023 12:40)</code> - <em>Upvotes: 1</em></p><p>&quot;You need to normalize values to produce an output column into bins to predict a target column.&quot; =/= we need to take into consideration the target column when binning</p></blockquote>
<blockquote><p><strong>azurelearner666</strong> <code>(Sun 10 Apr 2022 15:13)</code> - <em>Upvotes: 3</em></p><p>Wrong, it is A. and the proper way to normalize the values is with Quantile normalization
&quot;If you select the Quantiles binning mode, use the Quantile normalization option to determine how values are normalized prior to sorting into quantiles. Note that normalizing values transforms the values, but does not affect the final number of bins&quot;
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins#bkmk_Effects</p></blockquote>
<blockquote><p><strong>ashvinn</strong> <code>(Thu 01 Aug 2024 11:49)</code> - <em>Upvotes: 1</em></p><p>A is to go</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Tue 12 Dec 2023 13:41)</code> - <em>Upvotes: 2</em></p><p>The Quantiles normalization module in Azure ML Studio normalizes values based on quantiles into a specified number of bins. The QuantileIndex normalization module further converts those binned quantiles into indices values.

Together these two normalization modules can take an input column and transform it into quantile indices, binning the original values.

This quantile binning allows the feature to then be used for targets prediction, meeting that part of the stated goal as well.</p></blockquote>
<blockquote><p><strong>Ahmed_Gehad</strong> <code>(Sun 23 Jul 2023 11:46)</code> - <em>Upvotes: 2</em></p><p>The answer is B. No.

Quantiles normalization is a technique that is used to normalize values by dividing the range of values into equal-sized intervals, or quantiles. QuantileIndex normalization is a technique that is used to normalize values by assigning each value to a quantile based on its rank.

In this case, the goal is to normalize values to produce an output column into bins to predict a target column. However, the solution of applying a Quantiles normalization with a QuantileIndex normalization will not achieve this goal. Instead, you should use a normalization technique that is specifically designed for binning, such as Equal Width Binning or Equal Frequency Binning.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 18 Mar 2023 19:19)</code> - <em>Upvotes: 2</em></p><p>B. No.
Quantiles normalization is a normalization technique that transforms the values in a dataset to have a specified distribution, usually a normal distribution. It is not used to produce an output column into bins.

Quantile Index normalization is a technique that transforms a dataset so that its values lie between 0 and 1, using the minimum and maximum values in the dataset. It is also not used to produce an output column into bins.

To produce an output column into bins, one could use the Discretize module in Azure Machine Learning Studio.</p></blockquote>
<blockquote><p><strong>DingDongSingSong</strong> <code>(Thu 31 Mar 2022 22:03)</code> - <em>Upvotes: 4</em></p><p>The question is poorly worded:
You need to normalize values to produce an output column into bins to predict a target column.

Why would you bin an output (target) column when you&#x27;re projecting a target column? That just doesn&#x27;t make sense.</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Wed 01 Dec 2021 18:22)</code> - <em>Upvotes: 2</em></p><p>I go with A</p></blockquote>
<blockquote><p><strong>v06ayxop1</strong> <code>(Thu 14 Oct 2021 08:45)</code> - <em>Upvotes: 3</em></p><p>Entropy MDL is not yet available in new Azure ML but only in Azure ML classic.
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/group-data-into-bins#how-to-configure-group-data-into-bins</p></blockquote>
<blockquote><p><strong>jitsblitz</strong> <code>(Wed 15 Sep 2021 08:56)</code> - <em>Upvotes: 8</em></p><p>&quot;You need to normalize values to produce an output column into bins to predict a target column.&quot;
Only Quantiles binning normalizes. You are not asked to use target column for binning. Dont get confused with just the mention of target column. All feature selection is to predict target column only. Entropy MDL uses Target column to determine number of bins.</p></blockquote>
<blockquote><p><strong>Askme101</strong> <code>(Sat 26 Dec 2020 14:07)</code> - <em>Upvotes: 1</em></p><p>Yes answer is correct as &#x27;a&#x27; as this requires a target column</p></blockquote>

</details>

---

[<< Previous Question](question_71.md) | [Home](/index.md) | [Next Question >>](question_73.md)
