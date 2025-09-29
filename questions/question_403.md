# Question 403

DRAG DROP -

You train and register a model by using the Azure Machine Learning SDK on a local workstation. Python 3.6 and Visual Studio Code are installed on the workstation.

When you try to deploy the model into production as an Azure Kubernetes Service (AKS)-based web service, you experience an error in the scoring script that causes deployment to fail.

You need to debug the service on the local workstation before deploying the service to production.

Which four actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Select and Place:

![Question Image](images/q403_q_0040700001.jpg)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q403_ans_0_0040800001.jpg" alt="Answer Image"><br>
<p>Step 1: Install Docker on the workstation</p>
<p>Prerequisites include having a working Docker installation on your local system.</p>
<p>Build or download the dockerfile to the compute node.</p>
<p>Step 2: Create an AksWebservice deployment configuration and deploy the model to it</p>
<p>To deploy a model to Azure Kubernetes Service, create a deployment configuration that describes the compute resources needed.</p>
<p># If deploying to a cluster configured for dev/test, ensure that it was created with enough</p>
<p># cores and memory to handle this deployment configuration. Note that memory is also used by</p>
<p># things such as dependencies and AML components.</p>
<p>deployment_config = AksWebservice.deploy_configuration(cpu_cores = 1, memory_gb = 1) service = Model.deploy(ws, &quot;myservice&quot;, [model], inference_config, deployment_config, aks_target) service.wait_for_deployment(show_output = True) print(service.state) print(service.get_logs())</p>
<p>Step 3: Create a LocalWebservice deployment configuration for the service and deploy the model to it</p>
<p>To deploy locally, modify your code to use LocalWebservice.deploy_configuration() to create a deployment configuration. Then use Model.deploy() to deploy the service.</p>
<p>Step 4: Debug and modify the scoring script as necessary. Use the reload() method of the service after each modification.</p>
<p>During local testing, you may need to update the score.py file to add logging or attempt to resolve any problems that you&#x27;ve discovered. To reload changes to the score.py file, use reload(). For example, the following code reloads the script for the service, and then sends data to it.</p>
<p>Incorrect Answers:</p>
<p>✑ AciWebservice: The types of web services that can be deployed are LocalWebservice, which will deploy a model locally, and AciWebservice and</p>
<p>AksWebservice, which will deploy a model to Azure Container Instances (ACI) and Azure Kubernetes Service (AKS), respectively.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-azure-kubernetes-service https://docs.microsoft.com/en-us/azure/machine-learning/how-to-troubleshoot-deployment-local</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>JTWang</strong> <code>(Mon 24 Apr 2023 05:39)</code> - <em>Upvotes: 33</em></p><p>My answer:
1.Install Docker on the workstation
Create a LocalWebservice deployment configuration for the service and deploy the mode to it
3.Debug and modify the scroing script as necessary. use the reload() method of the service after earch modification.
4.Creae an AksWebservice deployment configuration for the service and deploy the model to it

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-managed-online-endpoints?tabs=python</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Tue 06 Aug 2024 02:11)</code> - <em>Upvotes: 3</em></p><p>I agree with this answer but i want to know if the following sequence is also correct:
1. Create localwebservice
2. debug and modify the scoring script
3. install docker
4. Create Akswebserice</p></blockquote>
<blockquote><p><strong>chevyli</strong> <code>(Wed 08 Mar 2023 04:01)</code> - <em>Upvotes: 8</em></p><p>Logically, &quot;Create AksWebService&quot; should be the last step.</p></blockquote>
<blockquote><p><strong>Johlec</strong> <code>(Fri 21 Apr 2023 14:46)</code> - <em>Upvotes: 2</em></p><p>agree with you, you redeploy to aks after finished to debug.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 23 Aug 2023 23:43)</code> - <em>Upvotes: 2</em></p><p>Install Docker on the workstation 
Create a LocalWebservice deployment configuration for the service and deploy the model to it (C)
Debug and modify the scoring script as necessary. Use the reload() method of the service after each modification 
Create an AksWebservice deployment configuration and deploy the model to it</p></blockquote>

</details>

---

[<< Previous Question](question_402.md) | [Home](/index.md) | [Next Question >>](question_404.md)
