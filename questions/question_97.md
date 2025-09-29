# Question 97

HOTSPOT -

You have an Azure Machine Learning workspace named workspace1 that is accessible from a public endpoint. The workspace contains an Azure Blob storage datastore named store1 that represents a blob container in an Azure storage account named account1. You configure workspace1 and account1 to be accessible by using private endpoints in the same virtual network.

You must be able to access the contents of store1 by using the Azure Machine Learning SDK for Python. You must be able to preview the contents of store1 by using Azure Machine Learning studio.

You need to configure store1.

What should you do? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q97_q_0012600001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q97_ans_0_image601.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>roo123</strong> <code>(Fri 16 Feb 2024 04:46)</code> - <em>Upvotes: 6</em></p><p>The answer should be
1. Update authentication
2.Set store1 as the default datastore</p></blockquote>
<blockquote><p><strong>MelMac</strong> <code>(Tue 21 Jan 2025 06:59)</code> - <em>Upvotes: 1</em></p><p>To access the contents of store1 using the Azure ML Python SDK, the correct action is to update authentication for store1. This ensures that the datastore is properly authenticated and accessible within the Azure Machine Learning workspace.
To allow the preview of the contents of store1 using Azure ML studio, you need to set store1 as the default datastore. This ensures that the datastore is readily accessible and can be used for various operations within the Azure ML studio.</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Fri 11 Oct 2024 09:30)</code> - <em>Upvotes: 1</em></p><p>1. set store1 as the default datastore
2. update the authentication</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Wed 13 Dec 2023 10:16)</code> - <em>Upvotes: 2</em></p><p>You should just update the authentication for store 1 for both cases.

The key reason this meets both requirements is that the original problem stated that workspace1 and its linked storage account are configured with private endpoints for access within the virtual network.</p></blockquote>
<blockquote><p><strong>kel_dp_100</strong> <code>(Wed 15 Nov 2023 16:45)</code> - <em>Upvotes: 4</em></p><p>second should be Set store1 as the default datastore:</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Wed 18 May 2022 13:22)</code> - <em>Upvotes: 2</em></p><p>If you are in the same vnet, and the key or SAS never changed, why would you want to regenerate the key???</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Tue 14 Feb 2023 22:07)</code> - <em>Upvotes: 3</em></p><p>The workspace was accessible from a public endpoint, and you reconfigure it for it to be accessible by using private endpoints, and you will need to regenerate the key.</p></blockquote>
<blockquote><p><strong>azurelearner666</strong> <code>(Sun 10 Apr 2022 17:45)</code> - <em>Upvotes: 3</em></p><p>seems correct</p></blockquote>
<blockquote><p><strong>[Removed]</strong> <code>(Sun 20 Feb 2022 19:14)</code> - <em>Upvotes: 4</em></p><p>On 20Feb2022</p></blockquote>

</details>

---

[<< Previous Question](question_96.md) | [Home](/index.md) | [Next Question >>](question_98.md)
