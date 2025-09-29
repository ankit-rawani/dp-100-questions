# Question 313

You create a training pipeline by using the Azure Machine Learning designer.

You need to load data into a machine learning pipeline by using the Import Data component.

Which two data sources could you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- A.Azure SQL Database
- B.Registered dataset
- C.URL via HTTP
- D.Azure Blob storage container through a registered datastore
- E.Azure Data Lake Storage Gen2

<details>
  <summary>Show Suggested Answer</summary>

<strong>CD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>609c591</strong> <code>(Thu 23 Jan 2025 16:35)</code> - <em>Upvotes: 1</em></p><p>You can use the following two data sources to load data into a machine learning pipeline using the Import Data component in Azure Machine Learning designer:

B. Registered dataset
Registered Dataset: A dataset that has been registered in your Azure Machine Learning workspace can be easily imported into your pipeline. This ensures that your data is well-organized and easily accessible for your machine learning experiments.

D. Azure Blob storage container through a registered datastore
Azure Blob Storage: By registering an Azure Blob storage container as a datastore in your Azure Machine Learning workspace, you can directly import data from it into your pipeline. This is especially useful for large datasets that are stored in Blob storage.

These options allow you to efficiently load and manage your data for machine learning pipelines.</p></blockquote>

<blockquote><p><strong>PI_Team</strong> <code>(Fri 23 Feb 2024 10:29)</code> - <em>Upvotes: 2</em></p><p>The Import Data component supports reading data from the following sources: URL via HTTP, Azure Blob Container, Azure File Share, Azure Data Lake, Azure Data Lake Gen2, Azure SQL Database, and Azure PostgreSQL1. Therefore, the correct answers to your question are A. Azure SQL Database, C. URL via HTTP, D. Azure Blob storage container through a registered datastore, and E. Azure Data Lake Storage Gen2

Reference: https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/machine-learning/component-reference/import-data.md</p></blockquote>

<blockquote><p><strong>hiyoww</strong> <code>(Thu 10 Oct 2024 08:24)</code> - <em>Upvotes: 2</em></p><p>if ACDE can be answers, then question not asking well</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Sun 14 Jan 2024 20:00)</code> - <em>Upvotes: 1</em></p><p>Correct</p></blockquote>
<blockquote><p><strong>fqc</strong> <code>(Mon 20 Nov 2023 12:05)</code> - <em>Upvotes: 4</em></p><p>The Import Data component support read data from following sources:

URL via HTTP
Azure cloud storages through Datastores)
Azure Blob Container
Azure File Share
Azure Data Lake
Azure Data Lake Gen2
Azure SQL Database
Azure PostgreSQL</p></blockquote>

<blockquote><p><strong>Tommo565</strong> <code>(Sat 23 Sep 2023 14:50)</code> - <em>Upvotes: 1</em></p><p>Correct according to the link</p></blockquote>
<blockquote><p><strong>oakmm</strong> <code>(Fri 22 Sep 2023 21:38)</code> - <em>Upvotes: 3</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/import-data</p></blockquote>

</details>

---

[<< Previous Question](question_312.md) | [Home](../index.md) | [Next Question >>](question_314.md)
