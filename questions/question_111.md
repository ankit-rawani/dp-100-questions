# Question 111

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You use Azure Machine Learning designer to load the following datasets into an experiment:

Dataset1 -

![Question Image](../images/q111_q_image383.png)

Dataset2 -

![Question Image](../images/q111_q_image384.png)

You need to create a dataset that has the same columns and header row as the input datasets and contains all rows from both input datasets.

Solution: Use the Apply Transformation module.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>MiteshKachhatiya</strong> <code>(Thu 20 Jun 2024 06:54)</code> - <em>Upvotes: 2</em></p><p>Answer is B</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Mon 25 Mar 2024 17:42)</code> - <em>Upvotes: 2</em></p><p>on exam 3/25/2024</p></blockquote>
<blockquote><p><strong>TA_</strong> <code>(Mon 25 Mar 2024 11:24)</code> - <em>Upvotes: 1</em></p><p>This set-up of questions on exam 15-03-2024</p></blockquote>
<blockquote><p><strong>Plb2</strong> <code>(Fri 23 Feb 2024 22:09)</code> - <em>Upvotes: 1</em></p><p>Assuming we&#x27;re speaking of the &#x27;Apply SQL Transformation&#x27; component here and reading the documentation I was thinking this could work:
&quot;Using the Apply SQL Transformation component, you can:
- Create tables for results and save the datasets in a portable database&quot; and &quot;The component can take up to three datasets as inputs&quot;.

However further down it&#x27;s stated that with SQLLite &quot;LEFT OUTER JOIN is implemented, but not RIGHT OUTER JOIN or FULL OUTER JOIN&quot;.

https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/apply-sql-transformation?view=azureml-api-2</p></blockquote>

<blockquote><p><strong>DaniloMagone</strong> <code>(Fri 03 May 2024 13:17)</code> - <em>Upvotes: 1</em></p><p>Why would you assume that if there is a component named Apply Transformation exactly? And this component does not fit the problem. The answer should be B.</p></blockquote>
<blockquote><p><strong>Plb2</strong> <code>(Fri 23 Feb 2024 22:11)</code> - <em>Upvotes: 1</em></p><p>Correcting the selected anwer; should be B (no)</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Thu 20 Jul 2023 13:24)</code> - <em>Upvotes: 4</em></p><p>On exam 20 July 2023.</p></blockquote>
<blockquote><p><strong>Dp_100_11</strong> <code>(Wed 24 May 2023 12:02)</code> - <em>Upvotes: 4</em></p><p>No, the solution provided using the Apply Transformation module does not meet the goal of creating a dataset that contains all rows from both input datasets with the same columns and header row.

The Apply Transformation module is used to apply custom transformations or operations on the dataset, but it does not perform the task of merging or combining two datasets into a single dataset with all rows and columns.</p></blockquote>

</details>

---

[<< Previous Question](question_110.md) | [Home](../index.md) | [Next Question >>](question_112.md)
