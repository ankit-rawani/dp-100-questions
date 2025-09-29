# Question 113

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You use Azure Machine Learning designer to load the following datasets into an experiment:

Dataset1 -

![Question Image](images/q113_q_image383.png)

Dataset2 -

![Question Image](images/q113_q_image384.png)

You need to create a dataset that has the same columns and header row as the input datasets and contains all rows from both input datasets.

Solution: Use the Execute Python Script module.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Alex310andra</strong> <code>(Wed 22 Mar 2023 12:41)</code> - <em>Upvotes: 6</em></p><p>Why not?</p></blockquote>
<blockquote><p><strong>ajay0011</strong> <code>(Tue 04 Apr 2023 01:35)</code> - <em>Upvotes: 5</em></p><p>Yes, it is possible. with the script we can perform any operation</p></blockquote>
<blockquote><p><strong>chaymat</strong> <code>(Sat 15 Apr 2023 23:49)</code> - <em>Upvotes: 3</em></p><p>same here,  with Python script, we can perform any operation</p></blockquote>
<blockquote><p><strong>25f71e3</strong> <code>(Sat 24 Aug 2024 09:05)</code> - <em>Upvotes: 1</em></p><p>It is possible using the Execute Python Script module in Azure Machine Learning designer, but this approach is unnecessarily complex for this task. Use Add Rows instead. Poorly written question.</p></blockquote>
<blockquote><p><strong>bbe8966</strong> <code>(Sun 09 Jun 2024 09:36)</code> - <em>Upvotes: 1</em></p><p>No, The statement specifies that a dataset should be created with the same columns and contain all rows from both datasets. When performing a join, regardless of the type, we will not obtain a single dataframe with all the rows; this can only be achieved through concatenation.</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Mon 25 Mar 2024 17:43)</code> - <em>Upvotes: 1</em></p><p>on exam 3/25/2024</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Mon 12 Feb 2024 14:37)</code> - <em>Upvotes: 1</em></p><p>On exam 12-02-2024.</p></blockquote>
<blockquote><p><strong>Mikku123</strong> <code>(Wed 02 Aug 2023 03:54)</code> - <em>Upvotes: 4</em></p><p>B seems the correct answer as the question explicitly states that you are using Azure Machine Learning designer to load the datasets into an experiment, and the Execute Python Script module is not used for loading datasets directly.</p></blockquote>
<blockquote><p><strong>Ahmed_Gehad</strong> <code>(Sun 23 Jul 2023 16:19)</code> - <em>Upvotes: 1</em></p><p>The Execute Python Script module can be used to execute Python code in Azure Machine Learning Studio. However, it cannot be used to create a dataset that has the same columns and header row as the input datasets and contains all rows from both input datasets.</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Thu 20 Jul 2023 13:24)</code> - <em>Upvotes: 3</em></p><p>On exam 20 July 2023.</p></blockquote>
<blockquote><p><strong>SovanMistry</strong> <code>(Sat 01 Jul 2023 12:59)</code> - <em>Upvotes: 2</em></p><p>With Script it&#x27;s possible</p></blockquote>
<blockquote><p><strong>Dp_100_11</strong> <code>(Wed 24 May 2023 12:03)</code> - <em>Upvotes: 4</em></p><p>Within the Python script, you can read the input datasets, concatenate or merge the rows using pandas functions (e.g., pd.concat() or pd.merge()), and generate a new dataset that contains all rows from both inputs. By specifying the appropriate logic in the Python script, you can ensure that the resulting dataset has the same columns and header row as the input datasets.</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Sat 10 Jun 2023 12:24)</code> - <em>Upvotes: 2</em></p><p>No, You use Azure Machine Learning designer</p></blockquote>

</details>

---

[<< Previous Question](question_112.md) | [Home](/index.md) | [Next Question >>](question_114.md)
