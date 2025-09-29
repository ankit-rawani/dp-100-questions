# Question 170

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You manage an Azure Machine Learning workspace. The development environment for managing the workspace is configured to use Python SDK v2 in Azure Machine Learning Notebooks.

A Synapse Spark Compute is currently attached and uses system-assigned identity.

You need to use Python code to update the Synapse Spark Compute to use a user-assigned identity.

Solution: Configure the IdentityConfiguration class with the appropriate identity type.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>KeiNek</strong> <code>(Tue 11 Feb 2025 01:30)</code> - <em>Upvotes: 1</em></p><p>To use system-assigned identity, pass IdentityConfiguration, with type set to SystemAssigned, as the identity parameter of the SynapseSparkCompute class. This code snippet updates a Synapse Spark pool to use a system-assigned identity :
synapse_identity = IdentityConfiguration(type=&quot;SystemAssigned&quot;) 

Ref :
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-synapse-spark-pool?view=azureml-api-2&amp;tabs=sdk#update-the-synapse-spark-pool</p></blockquote>
<blockquote><p><strong>D0ktor</strong> <code>(Mon 18 Nov 2024 23:14)</code> - <em>Upvotes: 2</em></p><p>Seems correct to me</p></blockquote>

</details>

---

[<< Previous Question](question_169.md) | [Home](/index.md) | [Next Question >>](question_171.md)
