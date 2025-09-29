# Question 236

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You plan to use a Python script to run an Azure Machine Learning experiment. The script creates a reference to the experiment run context, loads data from a file, identifies the set of unique values for the label column, and completes the experiment run:

![Question Image](../images/q236_q_0023500001.png)

The experiment must record the unique labels in the data as metrics for the run that can be reviewed later.

You must add code to the script to record the unique label values as run metrics at the point indicated by the comment.

Solution: Replace the comment with the following code:

run.log_table('Label Values', label_vals)

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

<p>Instead use the run_log function to log the contents in label_vals: for label_val in label_vals: run.log(&#x27;Label Values&#x27;, label_val)</p>
<p>Reference:</p>
<p>https://www.element61.be/en/resource/azure-machine-learning-services-complete-toolbox-ai</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>JTWang</strong> <code>(Sat 19 Oct 2024 06:34)</code> - <em>Upvotes: 7</em></p><p>label_vals is numpy.ndarray
==&gt;run.log_list(&#x27;Label Values&#x27;, label_vals) 
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

<blockquote><p><strong>ranjsi01</strong> <code>(Thu 18 Jul 2024 09:31)</code> - <em>Upvotes: 5</em></p><p>B is correct. run.log_table is used to Log a dictionary object to the run with the given name using azureml.core.Run.log_table</p></blockquote>

</details>

---

[<< Previous Question](question_235.md) | [Home](../index.md) | [Next Question >>](question_237.md)
