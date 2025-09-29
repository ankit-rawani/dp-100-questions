# Question 100

You use Azure Machine Learning to train a model based on a dataset named dataset1.

You define a dataset monitor and create a dataset named dataset2 that contains new data.

You need to compare dataset1 and dataset2 by using the Azure Machine Learning SDK for Python.

Which method of the DataDriftDetector class should you use?

- A.run
- B.get
- C.backfill
- D.update

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>84b1989</strong> <code>(Wed 15 Jan 2025 21:06)</code> - <em>Upvotes: 2</em></p><p>To compare dataset1 and dataset2 for data drift using the Azure Machine Learning SDK for Python, you should use the run method of the DataDriftDetector class. Here&#x27;s why:

Purpose of the run method:
The run method is used to execute the data drift detection process. It compares the baseline dataset (dataset1) with the target dataset (dataset2) and calculates metrics such as drift magnitude and feature-level drift.

Steps to use the run method:

Define a DataDriftDetector object, specifying the baseline dataset (dataset1) and the target dataset (dataset2).

Call the run method to perform the comparison and generate the data drift report.

Output:
The run method produces a detailed report that highlights any significant differences between the two datasets, helping you identify potential data drift.</p></blockquote>

<blockquote><p><strong>viineet</strong> <code>(Sat 07 Dec 2024 19:04)</code> - <em>Upvotes: 3</em></p><p>option A is correct, given answer is in correct as backfill use to generate report on datadrift in historical dataset over time</p></blockquote>
<blockquote><p><strong>labriji</strong> <code>(Tue 23 Apr 2024 12:10)</code> - <em>Upvotes: 4</em></p><p>given answer is correct, have a look at the code provided in the official doc: https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-monitor-datasets?view=azureml-api-1&amp;tabs=python#:~:text=SDK%20documentation.-,Create%20dataset%20monitor,-Create%20a%20dataset</p></blockquote>
<blockquote><p><strong>reddragondms</strong> <code>(Tue 26 Sep 2023 07:34)</code> - <em>Upvotes: 2</em></p><p>A DataDriftDetector object represents a data drift job definition that can be used to run three job run types:

an adhoc run for analyzing a specific day&#x27;s worth of data; see the run method.

a scheduled run in a pipeline; see the enable_schedule method.

a backfill run to see how data changes over time; see the backfill method.</p></blockquote>

<blockquote><p><strong>klowqw</strong> <code>(Sat 02 Sep 2023 19:38)</code> - <em>Upvotes: 3</em></p><p>correct</p></blockquote>

</details>

---

[<< Previous Question](question_99.md) | [Home](../index.md) | [Next Question >>](question_101.md)
