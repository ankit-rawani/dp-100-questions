# Question 128

HOTSPOT

-

You have an Azure Machine Learning workspace.

You need to use the Azure Machine Learning SDK for Python to create and register the Azure Data Lake Storage Generation 2 datastore for the workspace.

How should you complete the following code segment? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q128_q_image450.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q128_ans_0_image451.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>A_PL300</strong> <code>(Sun 08 Sep 2024 22:04)</code> - <em>Upvotes: 5</em></p><p>On Exam 9-4-23</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Thu 25 Jul 2024 11:46)</code> - <em>Upvotes: 2</em></p><p>Answer is correct. Here is the link to the Microsoft document for it: 
https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.datastore(class)?view=azure-ml-py#azureml-core-datastore-register-azure-data-lake-gen2

SaM</p></blockquote>
<blockquote><p><strong>Ahmed_Gehad</strong> <code>(Tue 23 Jul 2024 18:12)</code> - <em>Upvotes: 3</em></p><p>I think this question will be invalid in the new version of the exam. currently it&#x27;s azure.ai.ml &amp; we use abfs(s) now for data stores in an Azure Data Lake Storage Gen 2</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 12 Jul 2024 15:53)</code> - <em>Upvotes: 1</em></p><p>Cprrect.
static register_azure_data_lake_gen2(workspace, datastore_name, filesystem, account_name, tenant_id=None, client_id=None, client_secret=None, resource_url=None, authority_url=None, protocol=None, endpoint=None, overwrite=False, subscription_id=None, resource_group=None, grant_workspace_access=False)</p></blockquote>
<blockquote><p><strong>labriji</strong> <code>(Tue 23 Apr 2024 18:34)</code> - <em>Upvotes: 1</em></p><p>Given answer is correct 😄
snippet code : 
datastore = Datastore.```register_azure_data_lake_gen2```(workspace=ws,
                                                   datastore_name=&#x27;datastore_name&#x27;,
                                                   account_name=&#x27;account_name&#x27;,
                                                   ```filesystem```=&#x27;test&#x27;,
                                                   tenant_id=&#x27;tenant_id&#x27;,
                                                   client_id=&#x27;client_id&#x27;,
                                                   client_secret=&#x27;client_secret&#x27;)</p></blockquote>
<blockquote><p><strong>bibabrian</strong> <code>(Mon 15 Apr 2024 12:22)</code> - <em>Upvotes: 3</em></p><p>https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.datastore(class)?view=azure-ml-py#azureml-core-datastore-register-azure-data-lake-gen2</p></blockquote>

</details>

---

[<< Previous Question](question_127.md) | [Home](/index.md) | [Next Question >>](question_129.md)
