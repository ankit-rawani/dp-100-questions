# Question 490

You have an Azure Machine Learning workspace named workspace1.

You must add a datastore that connects an Azure Blob storage container to workspace1. You must be able to configure a privilege level.

You need to configure authentication.

Which authentication method should you use?

* A.Service principal
* B.Account key
* C.SAS token
* D.Managed identity

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Fefnut</strong> <code>(Fri 15 Nov 2024 15:26)</code> - <em>Upvotes: 2</em></p><p>Managed identity can be done see https://learn.microsoft.com/en-us/azure/machine-learning/how-to-datastore?view=azureml-api-2&amp;tabs=cli-identity-based-access%2Csdk-adls-identity-access%2Csdk-azfiles-accountkey%2Csdk-adlsgen1-identity-access%2Csdk-onelake-identity-access</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Tue 04 Jun 2024 20:28)</code> - <em>Upvotes: 3</em></p><p>The latest UI in the Machine Learning Studio only have two options in Authentication type when creating a datastore : Account Key or SAS Token. This is consistent with what you can specify in the constructor: https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.entities.azureblobdatastore?view=azure-python</p></blockquote>
<blockquote><p><strong>Piddi</strong> <code>(Sat 08 Apr 2023 02:36)</code> - <em>Upvotes: 1</em></p><p>You can have either Account Key or SAS while defining datastore. I guess SAS is the answer.</p></blockquote>
<blockquote><p><strong>esimsek</strong> <code>(Mon 27 Mar 2023 19:29)</code> - <em>Upvotes: 3</em></p><p>In exam on 2023-03-27</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 24 Feb 2023 17:25)</code> - <em>Upvotes: 1</em></p><p>A. the most secure and recommended method is to use a Service principal.
A Service principal is an Azure Active Directory (Azure AD) object that you can use to authenticate and authorize access to Azure resources. By using a Service principal, you can provide granular access to specific resources, without exposing the account key or SAS token. It also provides a centralized location to manage access to resources.
While using a Managed identity is a valid option for authenticating when running code within a workspace or compute instance, it&#x27;s not applicable for configuring authentication for datastores. A Managed identity provides an identity for a resource that can be used to authenticate to Azure services without requiring the use of credentials such as account keys or SAS tokens.</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Sat 25 Feb 2023 01:58)</code> - <em>Upvotes: 1</em></p><p>Service principle is less secure than managed identity. You can impersonate a service principle but you cannot impersonate a managed identity.</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Sat 25 Feb 2023 02:01)</code> - <em>Upvotes: 1</em></p><p>Automatically generated service principle is more secure than user created service principle, as for one identity you can have multiple user created service principles pointing to it, but you only have one automatically generated service principle per identity that cannot be modified.</p></blockquote>
<blockquote><p><strong>ahson0124</strong> <code>(Wed 15 Feb 2023 13:55)</code> - <em>Upvotes: 2</em></p><p>In exam on 2023-02-15</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Mon 09 Jan 2023 19:48)</code> - <em>Upvotes: 4</em></p><p>Managed Identity works for privilege control.</p></blockquote>
<blockquote><p><strong>giusecozza</strong> <code>(Fri 09 Sep 2022 14:30)</code> - <em>Upvotes: 2</em></p><p>on exam 09/09/2022</p></blockquote>
<blockquote><p><strong>giusecozza</strong> <code>(Thu 08 Sep 2022 10:30)</code> - <em>Upvotes: 4</em></p><p>service principal, SAS an auth are credential-based methods, which require the user to have Reader access on the whole workspace. I guess Managed identity is the answer we are looking for, since it enables a more fine-grained access control

https://docs.microsoft.com/en-us/azure/machine-learning/concept-data?tabs=uri-file-example%2Ccli-data-create-example#datastore</p></blockquote>

</details>

---

[<< Previous Question](question_489.md) | [Home](/index.md) | [Next Question >>](question_491.md)
