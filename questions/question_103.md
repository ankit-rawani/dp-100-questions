# Question 103

You use an Azure Machine Learning workspace.

You have a trained model that must be deployed as a web service. Users must authenticate by using Azure Active Directory.

What should you do?

* A.Deploy the model to Azure Kubernetes Service (AKS). During deployment, set the token_auth_enabled parameter of the target configuration object to true
* B.Deploy the model to Azure Container Instances. During deployment, set the auth_enabled parameter of the target configuration object to true
* C.Deploy the model to Azure Container Instances. During deployment, set the token_auth_enabled parameter of the target configuration object to true
* D.Deploy the model to Azure Kubernetes Service (AKS). During deployment, set the auth.enabled parameter of the target configuration object to true

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>madrid99</strong> <code>(Thu 18 May 2023 11:32)</code> - <em>Upvotes: 8</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-authenticate-web-service
So there&#x27;s a token_auth_enabled parmeter</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 01 Dec 2024 03:10)</code> - <em>Upvotes: 4</em></p><p>Explanation:
Azure Kubernetes Service (AKS): AKS provides enterprise-grade security, governance, and increased scalability. It is ideal for production deployments.
token_auth_enabled parameter: This parameter, when set to true, enables token-based authentication using Azure Active Directory for the deployed web service.
The other options do not correctly combine the deployment target and configuration parameters for enabling Azure Active Directory authentication:

B and C (Azure Container Instances): While you can deploy models to Azure Container Instances (ACI), they do not support the token_auth_enabled parameter for Azure AD authentication.
D (auth.enabled parameter): This is not a recognized parameter for setting up Azure AD authentication in the deployment configuration.
Thus, the correct deployment strategy involves using AKS and setting token_auth_enabled to true during the deployment process</p></blockquote>
<blockquote><p><strong>daviskv74</strong> <code>(Mon 15 Apr 2024 17:06)</code> - <em>Upvotes: 1</em></p><p>GPT says D is correct</p></blockquote>
<blockquote><p><strong>Nadine_nm</strong> <code>(Sun 25 Feb 2024 14:33)</code> - <em>Upvotes: 3</em></p><p>the 2 parameters exists in the documentation, there is a slight difference in their definitions : 
token_auth_enabled = Whether or not to enable Token auth for this Webservice. If this is enabled, users can access this Webservice by fetching access token using their Azure Active Directory credentials

auth_enabled = Whether or not to enable key auth for this Webservice. Defaults to True.

since we are using Azure Active Directory, answer A is correct</p></blockquote>
<blockquote><p><strong>Mal42</strong> <code>(Tue 20 Feb 2024 16:05)</code> - <em>Upvotes: 3</em></p><p>On exam 18 Aug 2023</p></blockquote>
<blockquote><p><strong>Mikku123</strong> <code>(Fri 02 Feb 2024 03:27)</code> - <em>Upvotes: 2</em></p><p>Its identity based for AAD , not credential based SAS(token). so &quot;D&quot; is the correct answer!</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Sat 20 Jan 2024 14:21)</code> - <em>Upvotes: 1</em></p><p>On exam 20 July 2023.</p></blockquote>
<blockquote><p><strong>ajay0011</strong> <code>(Wed 04 Oct 2023 00:25)</code> - <em>Upvotes: 2</em></p><p>I think D is correct.
# Define workspace and model details
workspace = Workspace.from_config()
model = Model(workspace, &#x27;model_name&#x27;)
aks_service_name = &#x27;my-aks-service&#x27;
deployment_config = AksWebservice.deploy_configuration(
    cpu_cores=1,
    memory_gb=1,
    auth_enabled=True  # Enable Azure Active Directory authentication)
env = Environment.from_conda_specification(name=&#x27;env_name&#x27;, file_path=&#x27;./conda_dependencies.yml&#x27;)
auth = InteractiveLoginAuthentication()
aks_service = Model.deploy(
    workspace=workspace,
    name=aks_service_name,
    models=[model],
    inference_config=inference_config,
    deployment_config=deployment_config,
    environment=env,
    auth=auth,
    overwrite=True)</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Fri 14 Apr 2023 09:20)</code> - <em>Upvotes: 3</em></p><p>I can&#x27;t find token_auth_enabled parameter.
In ref i got parameter &quot;auth_mode&quot;.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-authenticate-online-endpoint

You can set the authentication type when you create an online endpoint. Set the auth_mode to key or aml_token depending on which one you want to use. The default value is key.</p></blockquote>
<blockquote><p><strong>silva_831</strong> <code>(Sun 30 Apr 2023 04:51)</code> - <em>Upvotes: 1</em></p><p>I didn&#x27;t find token_auth-enabled as well according to attached link.</p></blockquote>
<blockquote><p><strong>klowqw</strong> <code>(Thu 02 Mar 2023 20:38)</code> - <em>Upvotes: 3</em></p><p>correct</p></blockquote>
<blockquote><p><strong>manualrg</strong> <code>(Sun 23 Jul 2023 21:45)</code> - <em>Upvotes: 2</em></p><p>Correct is A: From (v1 SDK) https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-authenticate-web-service
# Create the config
aks_config = AksWebservice.deploy_configuration()

#  Enable token auth and disable (key) auth on the webservice
aks_config = AksWebservice.deploy_configuration(token_auth_enabled=True, auth_enabled=False)</p></blockquote>

</details>

---

[<< Previous Question](question_102.md) | [Home](/index.md) | [Next Question >>](question_104.md)
