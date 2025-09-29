# Question 152

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You use Azure Machine Learning designer to load the following datasets into an experiment:

Dataset1 -

![Question Image](../images/q152_q_image538.png)

Dataset2 -

![Question Image](../images/q152_q_image539.png)

You need to create a dataset that has the same columns and header row as the input datasets and contains all rows from both input datasets.

Solution: Use the Join Data module.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>f82411e</strong> <code>(Wed 28 May 2025 11:51)</code> - <em>Upvotes: 1</em></p><p>Debes usar el módulo Add Rows</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Fri 03 Jan 2025 03:43)</code> - <em>Upvotes: 1</em></p><p>&quot;Join Data&quot; is for SQL type joins, &quot;Add Rows&quot; will be suitable in this case. Hence the solution does not meet the guideline.</p></blockquote>
<blockquote><p><strong>jojashi</strong> <code>(Fri 29 Nov 2024 17:36)</code> - <em>Upvotes: 1</em></p><p>Correct. B
I checked on the Designer module description.. 
Module: Join Data
Description: Joins two datasets on selected key columns.

we don&#x27;t need to select key columns and there is no matching rows. We only need to append data. So, Add Row module is right</p></blockquote>

<blockquote><p><strong>kay1101</strong> <code>(Thu 21 Nov 2024 05:38)</code> - <em>Upvotes: 1</em></p><p>not sure about this one, thought it would be append more than join.</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Sat 16 Nov 2024 02:35)</code> - <em>Upvotes: 1</em></p><p>It won&#x27;t work using the Join Data even you use Full Outer Join
For each of the rows in either table that have no matching rows in the other, the result includes a row containing missing values.</p></blockquote>
<blockquote><p><strong>Plb2</strong> <code>(Sat 24 Aug 2024 16:42)</code> - <em>Upvotes: 1</em></p><p>Yes this should work, FULL OUTER JOIN is supported 
https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/join-data?view=azureml-api-2#how-to-configure-join-data</p></blockquote>
<blockquote><p><strong>Plb2</strong> <code>(Sat 24 Aug 2024 16:44)</code> - <em>Upvotes: 1</em></p><p>whereas on Apply SQL transformation (one of the other questions) FULL OUTER JOIN is not supported;
https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/apply-sql-transformation?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>zishankamal</strong> <code>(Thu 15 Aug 2024 02:38)</code> - <em>Upvotes: 1</em></p><p>We use the Join Data component to merge two datasets using a database-style join operation. 
Full Outer Join: A full outer join returns all rows from the left table (table1) and from the right table (table2).

https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/join-data?view=azureml-api-2

&quot;Add Rows&quot; or &quot;Execute Python Script&quot; are also possible ways to do this.</p></blockquote>

<blockquote><p><strong>edogawa</strong> <code>(Wed 10 Apr 2024 09:04)</code> - <em>Upvotes: 2</em></p><p>It is the &#x27;Add Rows&#x27; component which does it.</p></blockquote>
<blockquote><p><strong>umair_hanu</strong> <code>(Wed 10 Jan 2024 07:35)</code> - <em>Upvotes: 2</em></p><p>b is correct</p></blockquote>

</details>

---

[<< Previous Question](question_151.md) | [Home](../index.md) | [Next Question >>](question_153.md)
