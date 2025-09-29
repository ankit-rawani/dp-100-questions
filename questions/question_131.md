# Question 131

You have an Azure Machine Learning workspace. You are connecting an Azure Data Lake Storage Gen2 account to the workspace as a data store.

You need to authorize access from the workspace to the Azure Data Lake Storage Gen2 account.

What should you use?

* A.Service principal
* B.SAS token
* C.Managed identity
* D.Account key

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>victorlie</strong> <code>(Sat 08 Mar 2025 14:45)</code> - <em>Upvotes: 1</em></p><p>Managed Identity is a feature of Azure Active Directory that allows Azure services to authenticate and access other Azure resources securely without needing to manage credentials</p></blockquote>
<blockquote><p><strong>Secure_Defense</strong> <code>(Tue 28 Jan 2025 19:59)</code> - <em>Upvotes: 1</em></p><p>Managed Identity, here&#x27;s the answer.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-identity-based-service-authentication?view=azureml-api-2&amp;tabs=cli</p></blockquote>
<blockquote><p><strong>cayenne06</strong> <code>(Fri 20 Dec 2024 10:31)</code> - <em>Upvotes: 1</em></p><p>Managed Identity:
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-identity-based-service-authentication?view=azureml-api-2&amp;tabs=cli</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Sat 23 Nov 2024 16:48)</code> - <em>Upvotes: 2</em></p><p>C. Managed identity</p></blockquote>
<blockquote><p><strong>sai384957324</strong> <code>(Wed 10 Apr 2024 19:38)</code> - <em>Upvotes: 1</em></p><p>The answer is Service Principle.</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Tue 23 Jan 2024 17:09)</code> - <em>Upvotes: 2</em></p><p>Managed Identity. If azure services talk to each other, managed identity is recommended (was also on the DP-203). Note that managed identity is a specific type of service principal. Reference: https://stackoverflow.com/questions/61322079/difference-between-service-principal-and-managed-identities-in-azure</p></blockquote>
<blockquote><p><strong>Kanwal001</strong> <code>(Mon 28 Aug 2023 19:37)</code> - <em>Upvotes: 4</em></p><p>On exam 28 Aug 2023</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Tue 25 Jul 2023 13:56)</code> - <em>Upvotes: 4</em></p><p>A. Service principal

Explanation:

A service principal is an identity that can be used by applications, services, or automation tools to access specific resources within Azure. By creating a service principal and granting it the necessary permissions, you can authorize the Azure Machine Learning workspace to access the Azure Data Lake Storage Gen2 account securely.

SaM</p></blockquote>
<blockquote><p><strong>heidousl</strong> <code>(Mon 15 May 2023 03:32)</code> - <em>Upvotes: 1</em></p><p>Answer is A</p></blockquote>
<blockquote><p><strong>ajay0011</strong> <code>(Sat 22 Apr 2023 04:14)</code> - <em>Upvotes: 1</em></p><p>Service Principle is correct.</p></blockquote>
<blockquote><p><strong>chaymat</strong> <code>(Sun 16 Apr 2023 13:04)</code> - <em>Upvotes: 2</em></p><p>I think we can use Service principle as well as Managed Identity</p></blockquote>
<blockquote><p><strong>avotofu</strong> <code>(Sat 15 Apr 2023 10:24)</code> - <em>Upvotes: 1</em></p><p>A. Service principle
Adding Azure Data Lake Gen. 2 as a datastore can only be authenticated via service principle.</p></blockquote>
<blockquote><p><strong>avotofu</strong> <code>(Sat 15 Apr 2023 10:43)</code> - <em>Upvotes: 3</em></p><p>Sorry, question is about &#x27;access&#x27; to datastore. Still answer should be A. service principle.
https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-access-data?view=azureml-api-1</p></blockquote>

</details>

---

[<< Previous Question](question_130.md) | [Home](/index.md) | [Next Question >>](question_132.md)
