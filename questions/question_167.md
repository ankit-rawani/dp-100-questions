# Question 167

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You manage an Azure Machine Learning workspace. The development environment for managing the workspace is configured to use Python SDK v2 in Azure Machine Learning Notebooks.

A Synapse Spark Compute is currently attached and uses system-assigned identity.

You need to use Python code to update the Synapse Spark Compute to use a user-assigned identity.

Solution: Create an instance of the MLClient class.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Sadhak</strong> <code>(Tue 05 Nov 2024 16:44)</code> - <em>Upvotes: 1</em></p><p>To update a Synapse Spark Compute to use a user-assigned identity in Python code, you need to access the Azure Synapse Analytics management client and configure the &quot;identity&quot; property of your Synapse Spark pool object with the desired user-assigned managed identity details, specifying the &quot;type&quot; as &quot;UserAssigned&quot; and providing the relevant &quot;principalId&quot; of the user-assigned identity. 
Key steps:
Import necessary libraries.
Code

   from azure.mgmt.synapse import SynapseManagementClient

   from azure.identity import DefaultAzureCredential</p></blockquote>

</details>

---

[<< Previous Question](question_166.md) | [Home](/index.md) | [Next Question >>](question_168.md)
