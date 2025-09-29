# Question 393

You use the designer to create a training pipeline for a classification model. The pipeline uses a dataset that includes the features and labels required for model training.

You create a real-time inference pipeline from the training pipeline. You observe that the schema for the generated web service input is based on the dataset and includes the label column that the model predicts. Client applications that use the service must not be required to submit this value.

You need to modify the inference pipeline to meet the requirement.

What should you do?

* A.Add a Select Columns in Dataset module to the inference pipeline after the dataset and use it to select all columns other than the label.
* B.Delete the dataset from the training pipeline and recreate the real-time inference pipeline.
* C.Delete the Web Service Input module from the inference pipeline.
* D.Replace the dataset in the inference pipeline with an Enter Data Manually module that includes data for the feature columns but not the label column.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>synapse</strong> <code>(Fri 13 Sep 2024 03:10)</code> - <em>Upvotes: 5</em></p><p>Given answer A is correct</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Thu 25 Jul 2024 12:57)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>

</details>

---

[<< Previous Question](question_392.md) | [Home](/index.md) | [Next Question >>](question_394.md)
