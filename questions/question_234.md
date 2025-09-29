# Question 234

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You plan to use a Python script to run an Azure Machine Learning experiment. The script creates a reference to the experiment run context, loads data from a file, identifies the set of unique values for the label column, and completes the experiment run:

![Question Image](images/q234_q_0023300001.png)

The experiment must record the unique labels in the data as metrics for the run that can be reviewed later.

You must add code to the script to record the unique label values as run metrics at the point indicated by the comment.

Solution: Replace the comment with the following code:

run.upload_file('outputs/labels.csv', './data.csv')

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ajay0011</strong> <code>(Tue 08 Oct 2024 00:08)</code> - <em>Upvotes: 3</em></p><p>should use run.log_list(&quot;Unique Label Values&quot;, label_vals) because labels can be more than one value.</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Thu 19 Oct 2023 06:33)</code> - <em>Upvotes: 3</em></p><p>label_vals is numpy.ndarray

Scalar
Example: run.log(&quot;accuracy&quot;, 0.95)

List
Example: run.log_list(&quot;accuracies&quot;, [0.6, 0.7, 0.87])

Row
Example: run.log_row(&quot;Y over X&quot;, x=1, y=0.4)

Table
Example: run.log_table(&quot;Y over X&quot;, {&quot;x&quot;:[1, 2, 3], &quot;y&quot;:[0.6, 0.7, 0.89]})

Image
Example: run.log_image(&quot;ROC&quot;, path)</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Tue 18 Jul 2023 09:26)</code> - <em>Upvotes: 3</em></p><p>no is correct. should use run.log</p></blockquote>
<blockquote><p><strong>ajay0011</strong> <code>(Tue 08 Oct 2024 00:09)</code> - <em>Upvotes: 1</em></p><p>If you use run.log() to log the unique label values, it will raise an exception because the run.log() method expects a key-value pair, where the key is a string and the value can be a number, string, or boolean. The unique method of a Pandas DataFrame returns an array of unique values, which is not a valid type for logging using the run.log() method.</p></blockquote>

</details>

---

[<< Previous Question](question_233.md) | [Home](/index.md) | [Next Question >>](question_235.md)
