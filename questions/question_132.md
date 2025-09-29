# Question 132

You manage an Azure Machine Learning workspace named workspace1.

You must develop Python SDK v2 code to attach an Azure Synapse Spark pool as a compute target in workspace1. The code must invoke the constructor of the SynapseSparkCompute class.

You need to invoke the constructor.

What should you use?

* A.Synapse workspace web URL and Spark pool name
* B.resource ID of the Synapse Spark pool and a user-defined name
* C.pool URL of the Synapse Spark pool and a system-assigned name
* D.Synapse workspace name and workspace web URL

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>damaldon</strong> <code>(Fri 12 Jan 2024 17:10)</code> - <em>Upvotes: 5</em></p><p>Correct. 
To attach a Synapse Compute using Python SDK, first create an instance of azure.ai.ml.MLClient class. This provides convenient functions for interaction with Azure Machine Learning services. The following code sample uses azure.identity.DefaultAzureCredential for connecting to a workspace in resource group of a specified Azure subscription. In the following code sample, define the SynapseSparkCompute with the parameters:

    name - user-defined name of the new attached Synapse Spark pool.
    resource_id - resource ID of the Synapse Spark pool created earlier in the Azure Synapse Analytics workspace.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 01 Dec 2024 13:31)</code> - <em>Upvotes: 1</em></p><p>given answer is correct</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Wed 25 Sep 2024 16:44)</code> - <em>Upvotes: 1</em></p><p>on exam 3/25/2024</p></blockquote>
<blockquote><p><strong>ymj_000</strong> <code>(Tue 07 May 2024 01:42)</code> - <em>Upvotes: 1</em></p><p>For reference: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-synapse-spark-pool?view=azureml-api-2&amp;tabs=sdk</p></blockquote>
<blockquote><p><strong>Mal42</strong> <code>(Wed 21 Feb 2024 08:22)</code> - <em>Upvotes: 3</em></p><p>On exam 18 Aug 2023</p></blockquote>
<blockquote><p><strong>Batman160591</strong> <code>(Wed 20 Dec 2023 21:51)</code> - <em>Upvotes: 1</em></p><p>Answer is B. 
To invoke the constructor of the SynapseSparkCompute class in Azure Machine Learning SDK v2, you need to provide the resource ID of the Synapse Spark pool and a user-defined name.</p></blockquote>

</details>

---

[<< Previous Question](question_131.md) | [Home](/index.md) | [Next Question >>](question_133.md)
