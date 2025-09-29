# Question 88

You are with a time series dataset in Azure Machine Learning Studio.

You need to split your dataset into training and testing subsets by using the Split Data module.

Which splitting mode should you use?

* A.Recommender Split
* B.Regular Expression Split
* C.Relative Expression Split
* D.Split Rows with the Randomized split parameter set to true

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jameswoo</strong> <code>(Sat 14 Nov 2020 19:21)</code> - <em>Upvotes: 58</em></p><p>i think it is C.   time-series data means you should split the data by date, otherwise you may have information leaking.</p></blockquote>
<blockquote><p><strong>human_ai</strong> <code>(Wed 02 Feb 2022 17:02)</code> - <em>Upvotes: 5</em></p><p>Nope, my bad... definitely C. Relative Expression split cause it is a time series dataset.</p></blockquote>
<blockquote><p><strong>human_ai</strong> <code>(Wed 02 Feb 2022 16:55)</code> - <em>Upvotes: 7</em></p><p>I think the Answer is correct. Since you just want to split into test and training Data. You are NOT trying to  SPLIT into CATEGORIES. or dates</p></blockquote>
<blockquote><p><strong>saegeb2000</strong> <code>(Fri 08 Jan 2021 06:48)</code> - <em>Upvotes: 29</em></p><p>This should be C: Relative Expression Split: Use this option whenever you want to apply a condition to a number column. The number can be a date/time field, a column that contains age or dollar amounts, or even a percentage. For example, you might want to divide your dataset based on the cost of the items, group people by age ranges, or separate data by a calendar date.
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/split-data</p></blockquote>
<blockquote><p><strong>84b1989</strong> <code>(Wed 15 Jan 2025 22:20)</code> - <em>Upvotes: 2</em></p><p>Explanation:
When working with a time series dataset in Azure Machine Learning Studio, the Split Rows mode with the Randomized split parameter set to true is the most appropriate choice for splitting the dataset into training and testing subsets. Here&#x27;s why:

Time Series Data Considerations:
Time series data has a temporal order, and splitting it randomly ensures that the training and testing subsets are representative of the entire dataset without breaking the time sequence. This helps in maintaining the integrity of the data for model evaluation.

Split Rows Mode:
The Split Rows mode allows you to specify a fraction of the dataset to be used for training and testing. For example, you can allocate 70% of the data for training and 30% for testing.

Randomized Split Parameter:
Setting the Randomized split parameter to true ensures that the data is shuffled before splitting, which is crucial for time series data to avoid bias and ensure that the model generalizes well.</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 15:32)</code> - <em>Upvotes: 2</em></p><p>WRONG. The Correct answer is: C
The correct method for splitting a time series dataset should consider the sequential nature of the data. The options available in the Split Data component in Azure ML are:
1. Split Rows: This mode is used to simply divide the data into two parts. This mode is generally used when the sequence of data is not a concern.
2. Regular Expression Split: This mode is for dividing the dataset based on a pattern in a text field such as analyzing sentiment.
3. Relative Expression Split: This mode applies to conditions on a number column, which could include date/time fields.
For time series data, where the sequence and continuity of data points are important, neither randomization (as in Split Rows with randomization) nor pattern-based splits (as in Regular Expression Split) are appropriate. Instead, the Relative Expression Split, which can handle conditions on date/time fields, is suited for time series data, allowing the dataset to be divided without disrupting the sequence.
Therefore, the correct answer should be C. Relative Expression Split.</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Thu 13 Jun 2024 05:53)</code> - <em>Upvotes: 3</em></p><p>When splitting a time series dataset in Azure Machine Learning Studio, you should use the &quot;Split Rows&quot; option with the &quot;Randomized split&quot; parameter set to false to ensure that the temporal order of the data is preserved. This approach is crucial for maintaining the integrity of time series data in training and testing subsets.</p></blockquote>
<blockquote><p><strong>dporwal04</strong> <code>(Wed 12 Jun 2024 09:20)</code> - <em>Upvotes: 1</em></p><p>use any tool like search, bard, chatgpt or any other tool but ans is C</p></blockquote>
<blockquote><p><strong>ymj_000</strong> <code>(Sat 04 May 2024 21:31)</code> - <em>Upvotes: 2</em></p><p>I think the answer is D because Randomized split is preferred option when you&#x27;re creating training and test datasets. See https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/split-data?view=azureml-api-2.
This is very sneaky by mentioning this is a time series data which makes me think the answer should be Relative Expression Split.</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 12 Jan 2024 17:01)</code> - <em>Upvotes: 2</em></p><p>For splitting a time series dataset in Azure Machine Learning Studio, the appropriate splitting mode to use is the &quot;Relative Expression Split&quot; (C).

The Relative Expression Split mode allows you to split the dataset based on conditions applied to a number column. This number column can be a date/time field, age, dollar amounts, percentages, or any other numerical value. It provides flexibility in defining the splitting criteria based on these numeric conditions.

In the context of a time series dataset, you can use the Relative Expression Split mode to split the dataset based on conditions related to the time component, such as dividing data by calendar date, time periods, or specific ranges of dates.</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Thu 10 Aug 2023 14:56)</code> - <em>Upvotes: 1</em></p><p>it clearly C!! you can check on https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/split-data</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Sun 06 Aug 2023 13:54)</code> - <em>Upvotes: 2</em></p><p>why the moderator does not bother to correct those answers?</p></blockquote>
<blockquote><p><strong>NachoPrendes</strong> <code>(Sun 30 Jul 2023 15:02)</code> - <em>Upvotes: 1</em></p><p>I think D is the correct one to choose random dates belonging to all years in two datasets</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Wed 14 Jun 2023 14:59)</code> - <em>Upvotes: 1</em></p><p>why not B?</p></blockquote>
<blockquote><p><strong>KIshor1212</strong> <code>(Thu 01 Jun 2023 18:10)</code> - <em>Upvotes: 1</em></p><p>Calendar year
A common scenario is to divide a dataset by years. The following expression selects all rows where the values in the column Year are greater than 2010.</p></blockquote>
<blockquote><p><strong>PremPatrick</strong> <code>(Thu 18 May 2023 06:20)</code> - <em>Upvotes: 2</em></p><p>C should be correct</p></blockquote>
<blockquote><p><strong>fvil</strong> <code>(Sun 07 May 2023 14:36)</code> - <em>Upvotes: 1</em></p><p>Question about Split Data module and differences between Regular Expression and Relative Expression appears on exam 07/11/2022</p></blockquote>
<blockquote><p><strong>azurelearner666</strong> <code>(Mon 10 Oct 2022 17:20)</code> - <em>Upvotes: 1</em></p><p>Selected Answer: C

Without any shadow of a doubt ;)

In machine learning, train/test split splits the data randomly, as there’s no dependence from one observation to the other. That’s not the case with time series data. Here, you’ll want to use values at the rear of the dataset for testing and everything else for training.
Example: Select first 10 years for training and 2 years for testing.

https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/split-data (check the Relative Expression Split section)</p></blockquote>
<blockquote><p><strong>sam844</strong> <code>(Mon 26 Sep 2022 05:54)</code> - <em>Upvotes: 1</em></p><p>C is the correct choice. It is time series data so it has to be split by date which is only Relative Expression</p></blockquote>

</details>

---

[<< Previous Question](question_87.md) | [Home](/index.md) | [Next Question >>](question_89.md)
