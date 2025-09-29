# Question 389

You train a model and register it in your Azure Machine Learning workspace. You are ready to deploy the model as a real-time web service.

You deploy the model to an Azure Kubernetes Service (AKS) inference cluster, but the deployment fails because an error occurs when the service runs the entry script that is associated with the model deployment.

You need to debug the error by iteratively modifying the code and reloading the service, without requiring a re-deployment of the service for each code update.

What should you do?

- A.Modify the AKS service deployment configuration to enable application insights and re-deploy to AKS.
- B.Create an Azure Container Instances (ACI) web service deployment configuration and deploy the model on ACI.
- C.Add a breakpoint to the first line of the entry script and redeploy the service to AKS.
- D.Create a local web service deployment configuration and deploy the model to a local Docker container.
- E.Register a new version of the model and update the entry script to load the new version of the model from its registered path.

<details>
  <summary>Show Suggested Answer</summary>

<strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Bizmaercq</strong> <code>(Fri 05 Feb 2021 22:41)</code> - <em>Upvotes: 50</em></p><p>The right answer is D.

Deployment and runtime errors can be easier to diagnose by deploying the service as a container in a local Docker instance, like this:
from azureml.core.webservice import LocalWebservice

deployment_config = LocalWebservice.deploy_configuration(port=8890)
service = Model.deploy(ws, &#x27;test-svc&#x27;, [model], inference_config, deployment_config)

You can then troubleshoot runtime issues by making changes to the scoring file that is referenced in the inference configuration, and reloading the service without redeploying it (something you can only do with a local service):

service.reload()
print(service.run(input_data = json_data))</p></blockquote>

<blockquote><p><strong>Shariq</strong> <code>(Sun 17 Nov 2024 07:38)</code> - <em>Upvotes: 1</em></p><p>will this violates the requirement &quot;without requiring a re-deployment of the service for each code update&quot;</p></blockquote>
<blockquote><p><strong>111ssy</strong> <code>(Sun 28 Feb 2021 18:08)</code> - <em>Upvotes: 19</em></p><p>D: If you encounter problems deploying a model to ACI or AKS, try deploying it as a local web service. Using a local web service makes it easier to troubleshoot problems. The Docker image containing the model is downloaded and started on your local system.

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-troubleshoot-deployment</p></blockquote>

<blockquote><p><strong>sl_mslconsulting</strong> <code>(Fri 29 Nov 2024 20:08)</code> - <em>Upvotes: 1</em></p><p>you need to test and debug locally before deploying to prod. Check this link: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-debug-managed-online-endpoints-visual-studio-code?view=azureml-api-2&amp;tabs=cli</p></blockquote>
<blockquote><p><strong>Mal42</strong> <code>(Thu 22 Feb 2024 14:47)</code> - <em>Upvotes: 2</em></p><p>On exam Aug 18 2023</p></blockquote>
<blockquote><p><strong>Mal42</strong> <code>(Thu 22 Feb 2024 14:47)</code> - <em>Upvotes: 2</em></p><p>On exam Aug 18 2023</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 27 Jan 2024 02:51)</code> - <em>Upvotes: 1</em></p><p>D. D. Create a local web service deployment configuration and deploy the model to a local Docker container.

This option provides a flexible and quick environment for debugging and testing. Using a local Docker container, you can quickly change the code in your entry script and immediately see the effect of your changes without going through the entire deployment process on Azure Kubernetes Service (AKS) or Azure Container Instances (ACI). Once you&#x27;ve debugged your entry script locally, you can then deploy it to AKS.</p></blockquote>

<blockquote><p><strong>phdykd</strong> <code>(Tue 22 Aug 2023 21:39)</code> - <em>Upvotes: 1</em></p><p>C. Add a breakpoint to the first line of the entry script and redeploy the service to AKS.
Adding a breakpoint to the first line of the entry script and redeploying the service to AKS will allow you to iteratively modify and test the code without requiring a re-deployment of the service for each code update. This will enable you to identify and fix the error in the entry script, without having to repeatedly deploy the service, saving time and resources. You can use tools like Visual Studio Code or PyCharm to attach a debugger to the running service, set a breakpoint on the first line of the entry script, and then use the debugger to step through the code and identify the error. Once you have identified and fixed the error, you can update the code, remove the breakpoint, and redeploy the service to AKS.</p></blockquote>
<blockquote><p><strong>PremPatrick</strong> <code>(Thu 18 May 2023 22:16)</code> - <em>Upvotes: 1</em></p><p>The right answer is D.</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Wed 12 Oct 2022 01:42)</code> - <em>Upvotes: 2</em></p><p>If you encounter problems deploying a model to ACI or AKS, try deploying it as a local web service.</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 15:19)</code> - <em>Upvotes: 4</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>ZeeshanNawaz</strong> <code>(Wed 11 Aug 2021 00:00)</code> - <em>Upvotes: 3</em></p><p>Correct answer should be D</p></blockquote>
<blockquote><p><strong>hachascloud</strong> <code>(Sat 31 Jul 2021 16:26)</code> - <em>Upvotes: 3</em></p><p>D, agreed. ACI is for production of low resource models. 1GB size and 48 GB ram or less</p></blockquote>

</details>

---

[<< Previous Question](question_388.md) | [Home](../index.md) | [Next Question >>](question_390.md)
