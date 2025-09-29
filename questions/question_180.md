# Question 180

You manage an Azure Machine Learning Workspace named Workspase1 and an Azure Files share named Share1.

You plan to create an Azure Files datastore in Workspace1 to target Share1.

You need to configure permanent access to Share1 from the Azure Files datastore.

Which authorization method should you use?

* A.Secondary access key
* B.Anonymous access
* C.Account SAS key
* D.Service SAS key

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>f82411e</strong> <code>(Tue 03 Jun 2025 10:57)</code> - <em>Upvotes: 1</em></p><p>C. Account SAS key
Provides delegated access to the entire storage resource (such as Azure Files).
Can be configured with far expiration (or renewed periodically) for persistent access.
Supports Azure Machine Learning data stores.</p></blockquote>
<blockquote><p><strong>jl420</strong> <code>(Thu 07 Nov 2024 17:37)</code> - <em>Upvotes: 3</em></p><p>The correct answer is:
A. Secondary access key
Explanation:
To configure permanent access to an Azure Files share from an Azure Files datastore in an Azure Machine Learning workspace, you generally use the primary or secondary access key of the Azure Storage account that contains the file share. This provides long-term access without the need to renew credentials, as the access keys remain valid until they are manually regenerated.

Why the Other Options Don’t Meet the Goal:
B. Anonymous access: Azure Files does not support anonymous access. Access requires authentication through either account keys, SAS tokens, or identity-based methods.

C. Account SAS key: While an Account SAS key provides scoped access to storage resources, it is typically short-lived and must be regenerated periodically, making it unsuitable for permanent access.

D. Service SAS key: Similar to the Account SAS, a Service SAS key is also short-lived and used for temporary access to specific resources. It must be renewed, so it does not meet the requirement for permanent access.</p></blockquote>
<blockquote><p><strong>Arvindu89</strong> <code>(Sun 27 Oct 2024 04:48)</code> - <em>Upvotes: 2</em></p><p>Account SAS and Service SAS are both types of Shared Access Signatures in Azure, but they differ in terms of scope and control.

Account SAS:

Grants access to resources within a storage account, such as blobs, files, queues, or tables.

Offers broader permissions and can cover multiple services within the storage account.

Allows you to specify permissions, including read, write, delete, list, and more for the entire account.

Service SAS:

Grants access to specific resources within a single service, like a specific blob or file share.

Offers more fine-grained control compared to Account SAS.

Allows you to specify permissions and set constraints, like IP ranges, protocols, and expiration times, but only for the specified resource.</p></blockquote>
<blockquote><p><strong>kfgg</strong> <code>(Thu 24 Oct 2024 15:47)</code> - <em>Upvotes: 2</em></p><p>A user delegation SAS has a maximum expiry interval of 7 days, regardless of the SAS expiration policy.

I think answer should be A?

https://learn.microsoft.com/en-us/azure/storage/common/sas-expiration-policy?tabs=azure-portal#configure-a-sas-expiration-policy

https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Mon 14 Oct 2024 13:52)</code> - <em>Upvotes: 2</em></p><p>I never came across service sas key, only account sas key</p></blockquote>

</details>

---

[<< Previous Question](question_179.md) | [Home](/index.md) | [Next Question >>](question_181.md)
