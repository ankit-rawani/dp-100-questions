# Question 23

This question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the recommendation satisfies the requirements.

You are in the process of carrying out feature engineering on a dataset.

You want to add a feature to the dataset and fill the column value.

Recommendation: You must make use of the Group Categorical Values Azure Machine Learning Studio module.

Will the requirements be satisfied?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ppchar</strong> <code>(Sat 13 Nov 2021 14:11)</code> - <em>Upvotes: 18</em></p><p>The typical use for grouping categorical values is to merge multiple string values into a single new level.</p></blockquote>
<blockquote><p><strong>Xsesi</strong> <code>(Mon 29 Jul 2024 15:42)</code> - <em>Upvotes: 1</em></p><p>Group Categorical Values Module is used to group similar categorical values into a single category, which is useful for reducing the number of categories or combining similar categories instead of adding new features or filling column values with specific data.</p></blockquote>
<blockquote><p><strong>microscape</strong> <code>(Sat 08 Jun 2024 08:40)</code> - <em>Upvotes: 1</em></p><p>For Output mode, indicate whether you want to output just the new levels, or append the changes to see the original column, with the replacements side by side.

The default, ResultOnly, shows only the new values. The Inplace option replaces the existing column values with the new levels.
https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/group-categorical-values?redirectedfrom=MSDN</p></blockquote>

<blockquote><p><strong>Ben999</strong> <code>(Sat 04 Jan 2025 02:29)</code> - <em>Upvotes: 1</em></p><p>based on this link the answer is B. No. &#x27;Group Categorical Values&#x27; can be used to create new columns by combining multiple string values to a new value/column; however it cannot be used for columns of numeric type or columns designated as labels or FEATURES.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Wed 21 Feb 2024 12:45)</code> - <em>Upvotes: 3</em></p><p>The &quot;Group Categorical Values&quot; module in Azure Machine Learning Studio is designed to reduce the granularity of categorical data. It groups together categorical values that appear infrequently in the data, which can be beneficial for models that may not handle high-cardinality categorical data well. This module is useful for managing and simplifying categorical features but does not directly address the task of adding a new feature and filling its values.</p></blockquote>
<blockquote><p><strong>GHill1982</strong> <code>(Tue 23 Jan 2024 21:01)</code> - <em>Upvotes: 2</em></p><p>The answer is no, the recommendation is incorrect. The Group Categorical Values Azure Machine Learning Studio module is designed to group a set of categorical values of a categorical feature into a smaller number of groups. It is not suitable for adding a new feature to the dataset or filling the column value.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Thu 19 Oct 2023 08:04)</code> - <em>Upvotes: 3</em></p><p>The question is Out of date. Don&#x27;t need care about this question. https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/group-categorical-values?redirectedfrom=MSDN</p></blockquote>
<blockquote><p><strong>PradhanManva</strong> <code>(Sun 24 Sep 2023 18:23)</code> - <em>Upvotes: 1</em></p><p>This is the answer.</p></blockquote>
<blockquote><p><strong>PopeyeDS</strong> <code>(Sat 15 Jul 2023 04:01)</code> - <em>Upvotes: 1</em></p><p>Extract from website:

Let&#x27;s assume that you want to group cars in the Automobile price dataset by engine size, using the number of cylinders. Rather than lots of different engine sizes, you will create the new levels, &quot;big&quot;, &quot;small&quot;, and &quot;other&quot; as follows:

Big engines: six cylinders or larger
Small engines: two or four cylinders
Other: anything else

I think A is correct</p></blockquote>

<blockquote><p><strong>Ammy_b</strong> <code>(Fri 10 Feb 2023 09:35)</code> - <em>Upvotes: 2</em></p><p>Changing the string values into numerical by group categorial is also one of the feature engineering but too many columns might be added while processing, leading to an error.

A is Correct</p></blockquote>

<blockquote><p><strong>Edriv</strong> <code>(Sat 10 Dec 2022 17:47)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/group-categorical-values?redirectedfrom=MSDN</p></blockquote>

</details>

---

[<< Previous Question](question_22.md) | [Home](../index.md) | [Next Question >>](question_24.md)
