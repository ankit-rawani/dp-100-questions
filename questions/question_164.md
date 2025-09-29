# Question 164

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You manage an Azure Machine Learning workspace. The development environment for managing the workspace is configured to use Python SDK v2 in Azure Machine Learning Notebooks.

A Synapse Spark Compute is currently attached and uses system-assigned identity.

You need to use Python code to update the Synapse Spark Compute to use a user-assigned identity.

Solution: Initialize the DefaultAzureCredential class.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Sadhak</strong> <code>(Sun 17 Nov 2024 20:09)</code> - <em>Upvotes: 1</em></p><p>from azure.identity import DefaultAzureCredential
from azure.mgmt.synapse import SynapseManagementClient</p></blockquote>

</details>

---

[<< Previous Question](question_163.md) | [Home](../index.md) | [Next Question >>](question_165.md)
