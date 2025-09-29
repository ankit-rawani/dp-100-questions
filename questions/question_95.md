# Question 95

You create a new Azure subscription. No resources are provisioned in the subscription.

You need to create an Azure Machine Learning workspace.

What are three possible ways to achieve this goal? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

* A.Run Python code that uses the Azure ML SDK library and calls the Workspace.create method with name, subscription_id, and resource_group parameters.
* B.Navigate to Azure Machine Learning studio and create a workspace.
* C.Use the Azure Command Line Interface (CLI) with the Azure Machine Learning extension to call the az group create function with --name and --location parameters, and then the az ml workspace create function, specifying ג€"w and ג€"g parameters for the workspace name and resource group.
* D.Navigate to Azure Machine Learning studio and create a workspace.
* E.Run Python code that uses the Azure ML SDK library and calls the Workspace.get method with name, subscription_id, and resource_group parameters.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>ABC</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 14:57)</code> - <em>Upvotes: 39</em></p><p>On exam 2021/7/10
My answers: ABC

Correct options:
A . Run Python code that uses the Azure ML SDK library and calls the Workspace.create method with name, subscription_id, resource_group, and location parameters.
B . Use an Azure Resource Management template that includes a Microsoft.MachineLearningServices/ workspaces resource and its dependencies.
C . Use the Azure Command Line Interface (CLI) with the Azure Machine Learning extension to call the az group create function with –name and –location parameters, and then the az ml workspace create function, specifying Cw and Cg parameters for the workspace name and resource group.
D . Navigate to Azure Machine Learning studio and create a workspace.
E . Run Python code that uses the Azure ML SDK library and calls the Workspace.get method with name, subscription_id, and resource_group parameters.</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Fri 14 Apr 2023 08:37)</code> - <em>Upvotes: 7</em></p><p>My Answer:BCD
A is wrong at 2022/10
The  subscription_id and resource_group is not needed.
D is correct. You can go to http://ml.azure.com to create a new workspace!

python code:
ws_basic = Workspace(
    name=basic_workspace_name,
    location=&quot;eastus&quot;,
    display_name=&quot;Basic workspace-example&quot;,
    description=&quot;This example shows how to create a basic workspace&quot;,
    hbi_workspace=False,
    tags=dict(purpose=&quot;demo&quot;),
)
ml_client.workspaces.begin_create(ws_basic)</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 12 Jan 2024 17:44)</code> - <em>Upvotes: 1</em></p><p>if there are no resources provisioned in the subscription, you cannot directly use Python code that calls Workspace.create method with the resource_group parameter. The resource_group parameter requires an existing resource group to be specified. So we can&#x27;t use the &quot;A&quot; option. 

My Answer:BCD</p></blockquote>
<blockquote><p><strong>allanm</strong> <code>(Mon 15 Nov 2021 19:47)</code> - <em>Upvotes: 14</em></p><p>I&#x27;m confused - Why is B and D the same answer option?</p></blockquote>
<blockquote><p><strong>andre999</strong> <code>(Mon 20 Dec 2021 19:48)</code> - <em>Upvotes: 11</em></p><p>The D option should be : Navigate to the Azure portal and create a workspace.</p></blockquote>
<blockquote><p><strong>ppchar</strong> <code>(Thu 23 Dec 2021 15:33)</code> - <em>Upvotes: 2</em></p><p>then answer is: CD</p></blockquote>
<blockquote><p><strong>allanm</strong> <code>(Mon 15 Nov 2021 19:49)</code> - <em>Upvotes: 8</em></p><p>Also noticed A &amp; E are the same answers as well. What&#x27;s going on?</p></blockquote>
<blockquote><p><strong>Norasit</strong> <code>(Mon 31 Jul 2023 14:18)</code> - <em>Upvotes: 1</em></p><p>Try to look at Workspace.____
A. Workspace.create
E. Workspace.get</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Fri 07 Jul 2023 19:04)</code> - <em>Upvotes: 1</em></p><p>B or D are Azure Machine Learning Service</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Thu 13 Jun 2024 07:32)</code> - <em>Upvotes: 1</em></p><p>Option A uses the SDK to programmatically create the workspace
Option B leverages the visual interface to create the workspace
Option C uses CLI commands to automatically create both resource group and workspace</p></blockquote>
<blockquote><p><strong>Nadine_nm</strong> <code>(Sat 24 Feb 2024 23:19)</code> - <em>Upvotes: 1</em></p><p>Answers should be ABD : 
https://learn.microsoft.com/en-us/azure/machine-learning/concept-workspace?view=azureml-api-2
Workspace management task |	Portal 	| Studio | Python SDK 	|Azure CLI 	| VS Code
Create a workspace 	            |      ✓ 	|   ✓       |          ✓ 	        |   ✓ 	        |  ✓</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 26 Dec 2023 15:04)</code> - <em>Upvotes: 1</em></p><p>BCD.
az group create --name &lt;resource-group-name&gt; --location &lt;location&gt;

ws_basic = ml_client.workspaces.begin_create(ws_basic).result()
print(ws_basic)</p></blockquote>
<blockquote><p><strong>krishna1818</strong> <code>(Wed 29 Nov 2023 10:31)</code> - <em>Upvotes: 1</em></p><p>C is a definite option, and B also seems right</p></blockquote>
<blockquote><p><strong>Dilesha</strong> <code>(Sat 19 Aug 2023 00:38)</code> - <em>Upvotes: 6</em></p><p>On Exam 17 Feb 2023</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Sun 20 Aug 2023 23:37)</code> - <em>Upvotes: 3</em></p><p>Thanks Dilesha. If by any chance you come back again, do you remember the differences between option B and D?</p></blockquote>
<blockquote><p><strong>hammamse</strong> <code>(Mon 02 Oct 2023 21:25)</code> - <em>Upvotes: 2</em></p><p>The D option should be : Navigate to the Azure portal and create a workspace.
And it&#x27;s not correct.
Correct answers are :A B C</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 05 Aug 2023 00:50)</code> - <em>Upvotes: 3</em></p><p>A. Run Python code that uses the Azure ML SDK library and calls the Workspace.create method with name, subscription_id, and resource_group parameters.
B. Navigate to Azure Machine Learning studio and create a workspace.
C. Use the Azure Command Line Interface (CLI) with the Azure Machine Learning extension to call the az group create function with --name and --location parameters, and then the az ml workspace create function, specifying &quot;w&quot; and &quot;g&quot; parameters for the workspace name and resource group. Option D. Navigate to Azure Machine Learning studio and create a workspace. is a correct answer, but it is a duplicate of option B. So, the correct answers are A, B, and C</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Fri 04 Aug 2023 01:00)</code> - <em>Upvotes: 1</em></p><p>I think, but not 100% sure that the code for creation of a workspcace is workspaces.begin_create and not Workspaces.create as described in option A. 
example: ml_client.workspaces.begin_create(ws)
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=python</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Fri 04 Aug 2023 01:06)</code> - <em>Upvotes: 3</em></p><p>Sorry my bad. Workspace.create is correct.

   from azureml.core import Workspace
   ws = Workspace.create(name=&#x27;myworkspace&#x27;,
               subscription_id=&#x27;&lt;azure-subscription-id&gt;&#x27;,
               resource_group=&#x27;myresourcegroup&#x27;,
               create_resource_group=True,
               location=&#x27;eastus2&#x27;
               )

https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace.workspace?view=azure-ml-py#azureml-core-workspace-workspace-create</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Fri 04 Aug 2023 01:08)</code> - <em>Upvotes: 1</em></p><p>It seems that ABCD are all correct.</p></blockquote>
<blockquote><p><strong>MansoorDataScientist</strong> <code>(Wed 02 Aug 2023 14:29)</code> - <em>Upvotes: 1</em></p><p>A cannot consider before creating a workspace, yes we can create through different methods of CICD but it&#x27;s not considered here</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Fri 14 Apr 2023 08:28)</code> - <em>Upvotes: 2</em></p><p>If D is create workspace by Azure Machine Learning Studio, it is true!

https://ml.azure.com/
You can go to https://ml.azure.com/  to create  a new workspace.</p></blockquote>
<blockquote><p><strong>gursimran_s</strong> <code>(Wed 30 Nov 2022 16:10)</code> - <em>Upvotes: 2</em></p><p>Why not ACD?</p></blockquote>
<blockquote><p><strong>zb99</strong> <code>(Sun 20 Nov 2022 18:21)</code> - <em>Upvotes: 2</em></p><p>A is wrong:  Cannot create a workspace this way because resource group does not yet exist.</p></blockquote>
<blockquote><p><strong>casiopa</strong> <code>(Thu 08 Jun 2023 10:17)</code> - <em>Upvotes: 1</em></p><p>You can create a Workspace this way, but you need to include this argument: create_resource_group=True.
This is why option A is wrong, there is no previous resource group and it isn&#x27;t created automatically on the Worspace.create method.</p></blockquote>
<blockquote><p><strong>dsaz</strong> <code>(Fri 09 Jun 2023 23:58)</code> - <em>Upvotes: 3</em></p><p>`create_resource_group=True` by default according to the docs (https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.workspace.workspace?view=azure-ml-py#azureml-core-workspace-workspace-create). So A so be a valid option too</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Thu 17 Nov 2022 14:35)</code> - <em>Upvotes: 1</em></p><p>With the correct options, ABC no doubt!</p></blockquote>
<blockquote><p><strong>DingDongSingSong</strong> <code>(Sat 01 Oct 2022 04:46)</code> - <em>Upvotes: 3</em></p><p>Option D is a repeat</p></blockquote>
<blockquote><p><strong>Thornehead</strong> <code>(Tue 27 Sep 2022 23:26)</code> - <em>Upvotes: 4</em></p><p>Use Azure portal 
Python SDK or Azure CLI
Use Resource Manager template

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=python</p></blockquote>
<blockquote><p><strong>Thornehead</strong> <code>(Tue 27 Sep 2022 23:24)</code> - <em>Upvotes: 1</em></p><p>Use Azure portal or Python SDK
Use Azure CLI
Use Resource Manager template

This is from the 

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-manage-workspace?tabs=python</p></blockquote>

</details>

---

[<< Previous Question](question_94.md) | [Home](/index.md) | [Next Question >>](question_96.md)
