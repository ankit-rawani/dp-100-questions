# Question 480

You create a binary classification model. The model is registered in an Azure Machine Learning workspace. You use the Azure Machine Learning Fairness SDK to assess the model fairness.

You develop a training script for the model on a local machine.

You need to load the model fairness metrics into Azure Machine Learning studio.

What should you do?

- A.Implement the download_dashboard_by_upload_id function
- B.Implement the create_group_metric_set function
- C.Implement the upload_dashboard_dictionary function
- D.Upload the training script

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>GHill1982</strong> <code>(Wed 17 Jul 2024 05:14)</code> - <em>Upvotes: 1</em></p><p>To load the model fairness metrics into Azure Machine Learning studio, you should do option C: Implement the upload_dashboard_dictionary function. This function takes a dictionary of fairness insights and uploads it to Azure Machine Learning, where you can see the fairness assessment dashboard. You can also use this function to upload fairness insights for multiple models or mitigated models.</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Fri 08 Sep 2023 11:33)</code> - <em>Upvotes: 4</em></p><p>Exactly this question was on exam 07/March/2023</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 25 Apr 2023 06:38)</code> - <em>Upvotes: 2</em></p><p>Correct.
Sample Code:
from azureml.contrib.fairness import upload_dashboard_dictionary, download_dashboard_by_upload_id
https://learn.microsoft.com/zh-tw/azure/machine-learning/how-to-machine-learning-fairness-aml</p></blockquote>
<blockquote><p><strong>NeitherLand</strong> <code>(Thu 20 Apr 2023 07:10)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>

</details>

---

[<< Previous Question](question_479.md) | [Home](../index.md) | [Next Question >>](question_481.md)
