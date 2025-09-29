# Question 78

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are analyzing a numerical dataset which contains missing values in several columns.

You must clean the missing values using an appropriate operation without affecting the dimensionality of the feature set.

You need to analyze a full dataset to include all values.

Solution: Remove the entire column that contains the missing data point.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>
<p>Use the Multiple Imputation by Chained Equations (MICE) method.</p>
<p>Reference:</p>
<p>https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3074241/</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/clean-missing-data</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>pg13</strong> <code>(Fri 17 Jun 2022 14:15)</code> - <em>Upvotes: 5</em></p><p>correct answer is no</p></blockquote>
<blockquote><p><strong>pranav33</strong> <code>(Sat 22 Jun 2024 14:54)</code> - <em>Upvotes: 1</em></p><p>No is correct</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Tue 20 Dec 2022 09:54)</code> - <em>Upvotes: 3</em></p><p>If you remove columns, dimensions will be affected, hence answer given is correct, which is no.</p></blockquote>
<blockquote><p><strong>Shanggavee</strong> <code>(Wed 19 Oct 2022 03:20)</code> - <em>Upvotes: 2</em></p><p>the answer is no</p></blockquote>
<blockquote><p><strong>Shashi_mv</strong> <code>(Sun 02 Oct 2022 22:55)</code> - <em>Upvotes: 1</em></p><p>the answer is Ýes. we cannot remove the entire column for a single missing data point.</p></blockquote>
<blockquote><p><strong>nick234987</strong> <code>(Thu 13 Oct 2022 10:50)</code> - <em>Upvotes: 4</em></p><p>So it is No</p></blockquote>

</details>

---

[<< Previous Question](question_77.md) | [Home](/index.md) | [Next Question >>](question_79.md)
