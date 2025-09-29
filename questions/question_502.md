# Question 502

You use an Azure Machine Learning workspace.

You must monitor cost at the endpoint and deployment level.

You have a trained model that must be deployed as an online endpoint. Users must authenticate by using Microsoft Entra ID.

What should you do?

* A.Deploy the model to Azure Kubernetes Service (AKS). During deployment, set the token_auth_mode parameter of the target configuration object to true.
* B.Deploy the model to Azure Kubernetes Service (AKS). During deployment, set the auth_mode parameter to configure the authentication type.
* C.Deploy the model to a managed online endpoint. During deployment, set the auth_mode parameter to configure the authentication type.
* D.Deploy the model to a managed online endpoint. During deployment, set the token_auth_mode parameter of the target configuration object to true.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>D0ktor</strong> <code>(Sun 17 Nov 2024 16:26)</code> - <em>Upvotes: 1</em></p><p>It should be D as one of the needs is authentication by Microsoft Entra ID, and that only works with token authentication</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Fri 29 Nov 2024 21:04)</code> - <em>Upvotes: 1</em></p><p>why not AKS? Because it is costly?</p></blockquote>
<blockquote><p><strong>kfgg</strong> <code>(Tue 22 Oct 2024 07:45)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/how-to-authenticate-online-endpoint?view=azureml-api-2&amp;tabs=azure-cli#create-an-endpoint</p></blockquote>
<blockquote><p><strong>f2a9aa5</strong> <code>(Fri 28 Jun 2024 14:46)</code> - <em>Upvotes: 3</em></p><p>C.

Attributes: Diagnostics and Monitoring and Cost 
Managed online endpoints (v2): 
- Local endpoint debugging possible with Docker and Visual Studio Code 
- Advanced metrics and logs analysis with chart/query to compare between deployments 
- Cost breakdown down to deployment level 
-Azure Monitor and Log Analytics powered (includes key metrics and log tables for endpoints and deployments) 

ACI or AKS(v1): No easy local debugging 

https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-online?view=azureml-api-2</p></blockquote>

</details>

---

[<< Previous Question](question_501.md) | [Home](/index.md) | [Next Question >>](question_503.md)
