# Question 430

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You train and register an Azure Machine Learning model.

You plan to deploy the model to an online endpoint.

You need to ensure that applications will be able to use the authentication method with a non-expiring artifact to access the model.

Solution: Create a managed online endpoint with the default authentication settings. Deploy the model to the online endpoint.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>phdykd</strong> <code>(Thu 27 Jul 2023 18:16)</code> - <em>Upvotes: 5</em></p><p>A) Yes. https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/machine-learning/how-to-authenticate-online-endpoint.md</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 10:15)</code> - <em>Upvotes: 2</em></p><p>The default authentication method when creating a managed online endpoint is a key, which does not expire unless explicitly regenerated. This satisfies the requirement of using a non-expiring artifact for authentication.

Thus, the solution of creating a managed online endpoint with the default authentication settings and deploying the model to the online endpoint meets the goal.</p></blockquote>
<blockquote><p><strong>zafnad</strong> <code>(Wed 12 Jun 2024 11:27)</code> - <em>Upvotes: 1</em></p><p>No, the solution does not meet the goal.
The default authentication settings for a managed online endpoint typically use Azure Active Directory (AAD) tokens, which do expire and are not non-expiring artifacts.

To ensure that applications can use an authentication method with a non-expiring artifact, you should use a key-based authentication method, such as API keys, which do not expire unless explicitly regenerated.</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Sun 03 Mar 2024 21:15)</code> - <em>Upvotes: 1</em></p><p>A- Yes, Key is default if not specified 
https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.entities.managedonlineendpoint?view=azure-python</p></blockquote>
<blockquote><p><strong>robdale</strong> <code>(Thu 02 Nov 2023 19:38)</code> - <em>Upvotes: 1</em></p><p>Should be YES. The default value is &#x27;key&#x27;.</p></blockquote>
<blockquote><p><strong>ferren</strong> <code>(Wed 23 Aug 2023 04:46)</code> - <em>Upvotes: 1</em></p><p>Chat pgt said it is No. But the link said it is YES</p></blockquote>
<blockquote><p><strong>Learnineveryday</strong> <code>(Wed 05 Jul 2023 18:12)</code> - <em>Upvotes: 3</em></p><p>The answer appears to be Yes as the default value is key. 
https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/machine-learning/how-to-authenticate-online-endpoint.md</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 07 Jul 2023 18:22)</code> - <em>Upvotes: 3</em></p><p>Agree.
When consuming an online endpoint from a client, you can use either a key or a token. Keys don&#x27;t expire, tokens do.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-authenticate-online-endpoint?view=azureml-api-2&amp;tabs=python</p></blockquote>

</details>

---

[<< Previous Question](question_429.md) | [Home](/index.md) | [Next Question >>](question_431.md)
