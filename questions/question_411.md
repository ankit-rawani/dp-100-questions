# Question 411

You train and publish a machine learning model.

You need to run a pipeline that retrains the model based on a trigger from an external system.

What should you configure?

* A.Azure Data Catalog
* B.Azure Batch
* C.Azure Logic App

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Vince_1</strong> <code>(Sat 31 Aug 2024 08:59)</code> - <em>Upvotes: 1</em></p><p>Correct</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Mon 05 Feb 2024 11:58)</code> - <em>Upvotes: 1</em></p><p>The answer is correct. Here is a reference: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-trigger-published-pipeline?view=azureml-api-1&amp;viewFallbackFrom=azureml-api-2</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Sun 04 Jun 2023 11:40)</code> - <em>Upvotes: 2</em></p><p>To run a pipeline that retrains a machine learning model based on a trigger from an external system, you can use Azure Logic App. Azure Logic App is an event-driven platform that can be used to trigger applications, processes, or CI/CD workflows based on Azure Machine Learning events[1]. You can set up a Logic App to be triggered by a Machine Learning event, such as a pipeline run, and then perform an action based on that trigger[1].

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-event-grid?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>esimsek</strong> <code>(Mon 27 Mar 2023 19:50)</code> - <em>Upvotes: 2</em></p><p>On exam 2023-03-27</p></blockquote>

</details>

---

[<< Previous Question](question_410.md) | [Home](/index.md) | [Next Question >>](question_412.md)
