# Question 306

You are developing a machine learning model by using Azure Machine Learning. You are using multiple text files in tabular format for model data.

You have the following requirements:

•	You must use AutoMLjobs to train the model.

•	You must use data from specified columns.

•	The data concept must support lazy evaluation.

You need to load data into a Pandas dataframe.

Which data concept should you use?

* A.Data asset
* B.URI
* C.Datastore
* D.MLTable

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ZoeJ</strong> <code>(Wed 26 Apr 2023 08:31)</code> - <em>Upvotes: 13</em></p><p>https://learn.microsoft.com/en-us/python/api/mltable/mltable.mltable.mltable?source=recommendations&amp;view=azure-ml-py
A MLTable defines a series of lazily-evaluated, immutable operations to load data from the data source.</p></blockquote>
<blockquote><p><strong>AnsiDP100</strong> <code>(Fri 21 Feb 2025 02:17)</code> - <em>Upvotes: 1</em></p><p>D is the right answer.</p></blockquote>
<blockquote><p><strong>AzureGeek79</strong> <code>(Wed 09 Oct 2024 03:09)</code> - <em>Upvotes: 2</em></p><p>Selected Answer: D</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 08 Jun 2024 08:08)</code> - <em>Upvotes: 2</em></p><p>lazy evaluation==&gt;MLtable</p></blockquote>
<blockquote><p><strong>Gpblax</strong> <code>(Fri 08 Dec 2023 17:44)</code> - <em>Upvotes: 3</em></p><p>A. MLTable
In order to provide training data to AutoML in SDK v2 you need to upload it into the cloud through an MLTable.
Requirements for loading data into an MLTable:
•	Data must be in tabular form.
•	The value to predict, target column, must be in the data.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-train?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>Fercho5813</strong> <code>(Wed 25 Oct 2023 00:41)</code> - <em>Upvotes: 2</em></p><p>Answer should be C</p></blockquote>
<blockquote><p><strong>bobML</strong> <code>(Sun 10 Sep 2023 17:06)</code> - <em>Upvotes: 2</em></p><p>C
To load data into a Pandas dataframe for use with AutoMLjobs in Azure Machine Learning, you should use the Datastore concept.

C. Datastore

A Datastore in Azure Machine Learning is a way to store, access, and manage data securely. It allows you to connect to various data storage options, including Azure Blob Storage, Azure SQL Database, and more. Datastores are commonly used for accessing and managing datasets in Azure Machine Learning.

You can use the Datastore to load your tabular text files into a Pandas dataframe, and it supports lazy evaluation, meaning data is loaded only when needed, which is useful for working with large datasets efficiently.

Options A, B, and D are not the primary mechanisms for loading data into a Pandas dataframe within the context of Azure Machine Learning.</p></blockquote>
<blockquote><p><strong>sap_dg</strong> <code>(Mon 27 Mar 2023 17:34)</code> - <em>Upvotes: 4</em></p><p>Answer should be C. Datastore</p></blockquote>

</details>

---

[<< Previous Question](question_305.md) | [Home](/index.md) | [Next Question >>](question_307.md)
