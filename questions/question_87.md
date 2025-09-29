# Question 87

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are a data scientist using Azure Machine Learning Studio.

You need to normalize values to produce an output column into bins to predict a target column.

Solution: Apply a Quantiles binning mode with a PQuantile normalization.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>modschegiebsch</strong> <code>(Fri 03 Jul 2020 07:09)</code> - <em>Upvotes: 22</em></p><p>Answer is B, because Quantile binning is not supervised. The binning is independent of the target column. You cannot use the output to predict the target directly.</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Thu 25 Mar 2021 06:48)</code> - <em>Upvotes: 15</em></p><p>If you select the Quantiles binning mode, use the Quantile normalization option to determine how values are normalized prior to sorting into quantiles. Note that normalizing values transform the values, but does not affect the final number of bins

Entropy MDL: This method requires that you select the column you want to predict and the column or columns that you want to group into bins. It then makes a pass over the data and attempts to determine the number of bins that minimizes the entropy. In other words, it chooses a number of bins that allows the data column to best predict the target column

I think the answer is &#x27;A&#x27;</p></blockquote>

<blockquote><p><strong>dija123</strong> <code>(Sun 12 Dec 2021 17:52)</code> - <em>Upvotes: 2</em></p><p>Totally agree with you</p></blockquote>
<blockquote><p><strong>FactCheckr4</strong> <code>(Thu 15 Aug 2024 11:39)</code> - <em>Upvotes: 1</em></p><p>Why the Solution Doesn’t Meet the Goal:
Quantiles Binning vs. PQuantile Normalization: While quantiles binning directly addresses the goal of creating bins for normalization, PQuantile normalization is not designed specifically for binning data into discrete categories. PQuantile normalization is more about adjusting data distributions rather than creating discrete bins.
To achieve the goal of normalizing values into bins, you should use Quantiles Binning directly. PQuantile normalization does not achieve this goal effectively because its purpose is to normalize data distributions rather than to bin data into quantile-based categories.

Thus, the solution of applying a Quantiles binning mode with PQuantile normalization does not fully meet the goal of binning values for predicting a target column.</p></blockquote>

<blockquote><p><strong>NullVoider_0</strong> <code>(Wed 13 Dec 2023 06:21)</code> - <em>Upvotes: 1</em></p><p>Using Quantiles binning mode with PQuantile normalization in Azure Machine Learning Studio is an appropriate solution for normalizing values and transforming them into bins, which can aid in the prediction of a target column in a machine learning model. This method is effective for creating evenly distributed bins based on the data&#x27;s distribution, which can be beneficial for various predictive modeling tasks.</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 24 Nov 2023 11:48)</code> - <em>Upvotes: 3</em></p><p>I need to correct my previous comment:

The solution of using Quantiles binning mode with PQuantile normalization in Azure Machine Learning Studio is valid. Quantiles binning discretizes data based on percentile ranks, and the PQuantile normalization option within this mode normalizes values within a [0,1] range before sorting into quantiles. This is specific to preparing data for quantile binning and is not general data normalization. Therefore, this approach aligns with Azure Machine Learning Studio&#x27;s capabilities for data preparation in quantile binning, meeting the objective of the task.</p></blockquote>

<blockquote><p><strong>PI_Team</strong> <code>(Wed 12 Jul 2023 15:55)</code> - <em>Upvotes: 1</em></p><p>The correct answer to the question is (B) No.

The given solution of applying a Quantiles binning mode with a PQuantile normalization does not meet the goal of normalizing values to produce an output column into bins for predicting a target column.

While Quantiles binning and PQuantile normalization are useful techniques in their own right, they are not directly applicable for producing bins to predict a target column.

To achieve the goal of normalizing values into bins to predict a target column, you would need to use appropriate techniques such as binning based on specific ranges or intervals, or other normalization methods tailored for your specific data and problem.

SaM</p></blockquote>

<blockquote><p><strong>PI_Team</strong> <code>(Fri 24 Nov 2023 11:48)</code> - <em>Upvotes: 1</em></p><p>I need to correct my previous comment: 
The solution of using Quantiles binning mode with PQuantile normalization in Azure Machine Learning Studio is valid. Quantiles binning discretizes data based on percentile ranks, and the PQuantile normalization option within this mode normalizes values within a [0,1] range before sorting into quantiles. This is specific to preparing data for quantile binning and is not general data normalization. Therefore, this approach aligns with Azure Machine Learning Studio&#x27;s capabilities for data preparation in quantile binning, meeting the objective of the task.</p></blockquote>
<blockquote><p><strong>striver</strong> <code>(Sat 04 Jun 2022 18:44)</code> - <em>Upvotes: 1</em></p><p>Answer is A. Normalization makes the value fall in range [0, 1] and that&#x27;s what PQuantile does too.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Mon 16 May 2022 11:43)</code> - <em>Upvotes: 3</em></p><p>Yes, this is the answer, see the link https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/group-data-into-bins

&quot;Entropy MDL mode is defined in Studio (classic) and there&#x27;s no corresponding open source package which can be leveraged to support in Designer yet.&quot;
&quot;If you select the Quantiles binning mode, use the Quantile normalization option to determine how values are normalized before sorting into quantiles. &quot;</p></blockquote>

<blockquote><p><strong>TheCyanideLancer</strong> <code>(Sat 22 Jan 2022 07:11)</code> - <em>Upvotes: 2</em></p><p>as per question, I believe, if target column is mentioned then ans mdl if feature column is mentioned then ans is PQuantile</p></blockquote>
<blockquote><p><strong>Tushazz</strong> <code>(Tue 04 Jan 2022 12:31)</code> - <em>Upvotes: 1</em></p><p>Yes should be answer.</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Wed 05 May 2021 14:24)</code> - <em>Upvotes: 7</em></p><p>Entropy MDL is not available in designer. The answer applies only to studio(classic).</p></blockquote>
<blockquote><p><strong>Gonza967</strong> <code>(Tue 14 Jan 2020 19:43)</code> - <em>Upvotes: 2</em></p><p>Answer is B</p></blockquote>

</details>

---

[<< Previous Question](question_86.md) | [Home](../index.md) | [Next Question >>](question_88.md)
