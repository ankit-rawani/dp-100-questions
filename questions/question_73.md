# Question 73

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are creating a new experiment in Azure Machine Learning Studio.

One class has a much smaller number of observations than the other classes in the training set.

You need to select an appropriate data sampling strategy to compensate for the class imbalance.

Solution: You use the Scale and Reduce sampling mode.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

<p>Instead use the Synthetic Minority Oversampling Technique (SMOTE) sampling mode.</p>
<p>Note: SMOTE is used to increase the number of underepresented cases in a dataset used for machine learning. SMOTE is a better way of increasing the number of rare cases than simply duplicating existing cases.</p>
<p>Incorrect Answers:</p>
<p>Common data tasks for the Scale and Reduce sampling mode include clipping, binning, and normalizing numerical values.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/smote https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/data-transformation-scale-and-reduce</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>azurelearner666</strong> <code>(Mon 10 Oct 2022 15:29)</code> - <em>Upvotes: 7</em></p><p>Response is correct, B.
The &quot;Scale and Reduce sampling mode&quot; will not be able to compensate for the class imbalance, so B (no) is the right Answer.

The proper response should be SMOTE.
More info on https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/smote</p></blockquote>

<blockquote><p><strong>Tehseen</strong> <code>(Fri 24 Dec 2021 12:51)</code> - <em>Upvotes: 6</em></p><p>Correct af</p></blockquote>
<blockquote><p><strong>windy610</strong> <code>(Sat 15 Jun 2024 09:14)</code> - <em>Upvotes: 1</em></p><p>should use SMOTE</p></blockquote>
<blockquote><p><strong>nick234987</strong> <code>(Wed 13 Apr 2022 10:01)</code> - <em>Upvotes: 2</em></p><p>The correct answer is B</p></blockquote>

</details>

---

[<< Previous Question](question_72.md) | [Home](../index.md) | [Next Question >>](question_74.md)
