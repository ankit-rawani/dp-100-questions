# Question 338

HOTSPOT

-

You manage an Azure Machine Learning workspace named workspace1 by using the Python SDK v2. You create a General Purpose v2 Azure storage account named mlstorage1. The storage account includes a publicly accessible container named mlcontainer1.

The container stores 10 blobs with files in the CSV format.

You must develop Python SDK v2 code to create a data asset referencing all blobs in the container named mlcontainer1.

You need to complete the Python SDK v2 code.

How should you complete the code? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q338_q_image512.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q338_ans_0_image513.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>A_PL300</strong> <code>(Mon 18 Sep 2023 21:21)</code> - <em>Upvotes: 5</em></p><p>On 4-Sept-2023 exam</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Mon 11 Nov 2024 21:39)</code> - <em>Upvotes: 3</em></p><p>Microsoft has deprecated the Windows Azure Storage Blob driver (WASB) in favor of the Azure Blob Filesystem driver (ABFS). ABFS has numerous benefits over WASB. Use ABFS for both Blob Storage and Data Lake for newer workloads.</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Wed 23 Aug 2023 14:28)</code> - <em>Upvotes: 4</em></p><p>sample_dataset = Data(
    path=&quot;wasbs://[email protected]/&quot;,
    type=AssetTypes.URI_FOLDER,
    description=&quot;sample_dataset&quot;,
    name=&quot;sample_dataset&quot;,
    version=&#x27;1.0&#x27;
)
Answers: wasbs &amp; URI_FOLDER
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-data-assets?view=azureml-api-2&amp;tabs=cli

By the way, abfss is used as the scheme identifier for the Hadoop Filesystem driver that is compatible with Azure Data Lake Storage Gen2.

SaM</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Mon 27 May 2024 18:26)</code> - <em>Upvotes: 1</em></p><p>Azure Data Lake Storage Gen2  is not Azure Blob Storage currently in V2. The answer provided is correct. https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Mon 27 May 2024 18:28)</code> - <em>Upvotes: 2</em></p><p>oops I meant your original answer is correct -&gt; wasbs</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 05 Jan 2024 15:37)</code> - <em>Upvotes: 2</em></p><p>Excuse me, abfss is the correct answer, the question clearly mentions that we have a gen2 storage

SaM</p></blockquote>
<blockquote><p><strong>orionduo</strong> <code>(Fri 01 Sep 2023 08:21)</code> - <em>Upvotes: 1</em></p><p>Agree with you 
A path on Azure Storage
(Blob) wasbs://&lt;containername&gt;@&lt;accountname&gt;.blob.core.windows.net/&lt;path_to_data&gt;/
(ADLS gen2) abfss://&lt;file_system&gt;@&lt;account_name&gt;.dfs.core.windows.net/&lt;path&gt;
(ADLS gen1) adl://&lt;accountname&gt;.azuredatalakestore.net/&lt;path_to_data&gt;/
Therefore, the first selection should be wasbs</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Wed 05 Jul 2023 19:47)</code> - <em>Upvotes: 1</em></p><p>&quot;abfss://&lt;file_system&gt;@&lt;account_name&gt;.dfs.core.windows.net/myimages/year=2023/week=1/**/*.jpeg&quot;
# Define the Data asset object
my_data = Data(
    path=mltable_folder,
    type=AssetTypes.MLTABLE,
    description=&quot;My images. Version includes data through to 2023-Jan-15.&quot;,
    name=&quot;myimages&quot;,
    version=&quot;20230115&quot;, # update version to the date</p></blockquote>

</details>

---

[<< Previous Question](question_337.md) | [Home](/index.md) | [Next Question >>](question_339.md)
