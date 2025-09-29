# Question 245

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You create a model to forecast weather conditions based on historical data.

You need to create a pipeline that runs a processing script to load data from a datastore and pass the processed data to a machine learning model training script.

Solution: Run the following code:

![Question Image](../images/q245_q_0025400001.png)

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

<p>train_step is missing.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.pipelinedata?view=azure-ml-py</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Peeking</strong> <code>(Fri 13 Sep 2024 02:33)</code> - <em>Upvotes: 1</em></p><p>There is no training step where the PipelineData (output of process_step) will be used as input.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 01 Dec 2023 14:25)</code> - <em>Upvotes: 2</em></p><p>Missing training step</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Thu 07 Sep 2023 11:42)</code> - <em>Upvotes: 1</em></p><p>prepped_data = OutputFileDatasetConfig(&quot;prepped_data&quot;)
then add prepped_data  to the arguments parameter</p></blockquote>

</details>

---

[<< Previous Question](question_244.md) | [Home](/index.md) | [Next Question >>](question_246.md)
