# Question 499

You have an Azure Machine Learning (ML) model deployed to an online endpoint.

You need to review container logs from the endpoint by using Azure ML Python SDK v2. The logs must include the console log from the inference server, with print/log statements from the model’s scoring script.

What should you do first?

- A.Connect by using SSH to the inference server.
- B.Create an instance of the MLCIient class.
- C.Connect by using Docker tools to the inference server.
- D.Create an instance of the OnlineDeploymentOperations class.

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>AnsiDP100</strong> <code>(Sat 08 Mar 2025 05:06)</code> - <em>Upvotes: 1</em></p><p>B is the correct</p></blockquote>
<blockquote><p><strong>ulg</strong> <code>(Sat 08 Feb 2025 10:42)</code> - <em>Upvotes: 1</em></p><p>The MLClient class is the primary entry point for SDK operations, allowing you to:
1. Connect to the Azure ML workspace.
2. Access deployment details, including logs.
3. Use methods like online_deployments.get_logs() to retrieve inference server logs, which include scoring script outputs.

SSH/Docker tools (A/C): Not required for SDK-based log retrieval.
OnlineDeploymentOperations (D): Accessed via ml_client.online_deployments, not instantiated directly.</p></blockquote>

<blockquote><p><strong>3a0b61c</strong> <code>(Tue 19 Mar 2024 15:59)</code> - <em>Upvotes: 2</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/how-to-troubleshoot-online-endpoints?view=azureml-api-2&amp;tabs=python#get-container-logs
https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.operations.onlinedeploymentoperations?view=azure-python
You should not instantiate this class directly. Instead, you should create an MLClient instance that instantiates it for you and attaches it as an attribute.</p></blockquote>
<blockquote><p><strong>bbe8966</strong> <code>(Sat 22 Jun 2024 10:28)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Tue 06 Feb 2024 15:53)</code> - <em>Upvotes: 2</em></p><p>you create a OnlineDeploymentOperation by referencing &#x27;ml_client.online_deployments&#x27;. OnlineDeploymentOperation has then the method &#x27;get_logs(...)&#x27;

References:
https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.mlclient?view=azure-python
https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.operations.onlinedeploymentoperations?view=azure-python#azure-ai-ml-operations-onlinedeploymentoperations-be</p></blockquote>

<blockquote><p><strong>hgjdsh</strong> <code>(Wed 24 Jan 2024 21:01)</code> - <em>Upvotes: 3</em></p><p>I think the answer should be B because you need an instance of ml_client class to call get_logs on online_deployment instance.</p></blockquote>
<blockquote><p><strong>GHill1982</strong> <code>(Wed 17 Jan 2024 20:24)</code> - <em>Upvotes: 2</em></p><p>To review the container logs from an online endpoint by using the Azure ML Python SDK v2, you need to do the following steps:
Create an instance of the OnlineDeploymentOperations class by passing the workspace object and the name of the online endpoint.
Call the get_logs method on the OnlineDeploymentOperations object by passing the name of the deployment. This method returns a dictionary with the logs for the deployment, including the console log from the inference server and the print/log statements from the model’s scoring script.</p></blockquote>
<blockquote><p><strong>sanctafrax</strong> <code>(Sun 02 Feb 2025 22:13)</code> - <em>Upvotes: 1</em></p><p>arent you stating a difference answer then? what should you do FIRST. 
You say pass the workspace object into the onlinedeploymentOperations class. Therefore you first create an instance of the MLClient class.</p></blockquote>
<blockquote><p><strong>ferren</strong> <code>(Tue 07 Nov 2023 23:14)</code> - <em>Upvotes: 1</em></p><p>chatgpt and bard say it should be D</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Mon 10 Jul 2023 21:22)</code> - <em>Upvotes: 4</em></p><p>Correct.
ml_client is the instance for MLCLient class, and online_deployment is the instance for either ManagedOnlineDeployment class or KubernetesOnlineDeployment class.
https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/machine-learning/how-to-troubleshoot-online-endpoints.md#get-container-logs</p></blockquote>

</details>

---

[<< Previous Question](question_498.md) | [Home](../index.md) | [Next Question >>](question_500.md)
