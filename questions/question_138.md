# Question 138

You manage an Azure Machine Learning workspace. The workspace includes an Azure Machine Learning Kubernetes compute target configured as an Azure Kubernetes Service (AKS) cluster named AKS1. AKS1 is configured to enable the targeting of different nodes to train workloads.

You must run a command job on AKS1 by using the Azure ML Python SDK v2. The command job must select different types of compute nodes. The compute node types must be specified by using a command parameter.

You need to configure the command parameter.

Which parameter should you use?

* A.environment
* B.compute
* C.limits
* D.instance_type

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Norasit</strong> <code>(Tue 26 Dec 2023 02:47)</code> - <em>Upvotes: 9</em></p><p>D. instance_type</p></blockquote>
<blockquote><p><strong>LadyCasilda</strong> <code>(Sun 18 Feb 2024 19:52)</code> - <em>Upvotes: 6</em></p><p>On exam 18 August 2023</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 01 Dec 2024 13:50)</code> - <em>Upvotes: 1</em></p><p>compute node type= instance type</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Fri 15 Nov 2024 19:04)</code> - <em>Upvotes: 1</em></p><p>AKS is the compute target you want to use.
instance_type is about the size of the VM you are using.
   command_node.set_resources(
       instance_count=1,
       instance_type=&quot;STANDARD_D2_v2&quot;,
       properties={&quot;key&quot;: &quot;new_val&quot;},
       shm_size=&quot;3g&quot;,
   )</p></blockquote>
<blockquote><p><strong>Plb2</strong> <code>(Sat 24 Aug 2024 14:55)</code> - <em>Upvotes: 1</em></p><p>With the parameter &#x27;instance_type&#x27; on the method command.set_resources the type of compute instance to run the job on can be configured. If not specified, the job will run on the default compute target.

https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.entities.command?view=azure-python#azure-ai-ml-entities-command-set-resources</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Wed 10 Jul 2024 09:52)</code> - <em>Upvotes: 1</em></p><p>B. compute: The &#x27;compute&#x27; parameter is used to specify the compute target on which the job will run. In the context of Azure ML and AKS, you can use this parameter to specify different node types in your AKS cluster. This is done by referencing the specific AKS compute targets that are configured for different node types.</p></blockquote>
<blockquote><p><strong>Ahmed_Gehad</strong> <code>(Mon 29 Jan 2024 08:47)</code> - <em>Upvotes: 6</em></p><p>The instance_type is optional, which is the type of VM used as supported by the compute target. The compute is required and is the name of the compute where the command job is executed.</p></blockquote>
<blockquote><p><strong>cloud6190</strong> <code>(Sat 27 Jan 2024 11:51)</code> - <em>Upvotes: 2</em></p><p>B. Compute is the right answer.</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 12 Jan 2024 18:37)</code> - <em>Upvotes: 4</em></p><p>Correct.
from azure.ai.ml import command

# define the command
command_job = command(
    command=&quot;python -c &quot;print(&#x27;Hello world!&#x27;)&quot;&quot;,
    environment=&quot;AzureML-lightgbm-3.2-ubuntu18.04-py37-cpu@latest&quot;,
    compute=&quot;&lt;Kubernetes-compute_target_name&gt;&quot;,
    instance_type=&quot;&lt;instance_type_name&gt;&quot;
)</p></blockquote>
<blockquote><p><strong>Batman160591</strong> <code>(Wed 20 Dec 2023 22:59)</code> - <em>Upvotes: 3</em></p><p>To configure the command parameter to select different types of compute nodes when running a command job on an Azure Machine Learning Kubernetes compute target (AKS) using the Azure ML Python SDK v2, you should use:

B. compute

The &quot;compute&quot; parameter allows you to specify the target compute resource for the command job. In this case, you want to target different types of compute nodes. By setting the &quot;compute&quot; parameter to the desired node type, you can instruct the command job to use the specific compute nodes for the job execution.</p></blockquote>

</details>

---

[<< Previous Question](question_137.md) | [Home](/index.md) | [Next Question >>](question_139.md)
