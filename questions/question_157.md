# Question 157

HOTSPOT

-

You manage an Azure Machine Learning workspace named workspace1.

You must register an Azure Blob storage datastore in workspace1 by using an access key. You develop Python SDK v2 code to import all modules required to register the datastore.

You need to complete the Python SDK v2 code to define the datastore.

How should you complete the code? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](../images/q157_q_image558.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q157_ans_0_image559.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jl420</strong> <code>(Thu 07 Nov 2024 14:42)</code> - <em>Upvotes: 4</em></p><p>container_name; abfss, because wasb is deprecated</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Tue 05 Mar 2024 19:33)</code> - <em>Upvotes: 2</em></p><p>answer is correct 
https://github.com/Azure/azureml-examples/blob/main/sdk/python/resources/datastores/datastore.ipynb</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Mon 12 Feb 2024 15:20)</code> - <em>Upvotes: 4</em></p><p>wasb[s] has been deprecated. Reference: https://learn.microsoft.com/en-us/azure/databricks/connect/storage/azure-storage. abfs[s] seems to be recommended instead.</p></blockquote>

</details>

---

[<< Previous Question](question_156.md) | [Home](/index.md) | [Next Question >>](question_158.md)
