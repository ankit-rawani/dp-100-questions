# Question 196

HOTSPOT -

You are using Azure Machine Learning to train machine learning models. You need a compute target on which to remotely run the training script.

You run the following Python code:

![Question Image](images/q196_q_0016200001.png)

For each of the following statements, select Yes if the statement is true. Otherwise, select No.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q196_q_0016200002.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q196_ans_0_0016300001.png" alt="Answer Image"><br>
<p>Box 1: Yes -</p>
<p>The compute is created within your workspace region as a resource that can be shared with other users.</p>
<p>Box 2: Yes -</p>
<p>It is displayed as a compute cluster.</p>
<p>View compute targets -</p>
<p>1. To see all compute targets for your workspace, use the following steps:</p>
<p>2. Navigate to Azure Machine Learning studio.</p>
<p>3. Under Manage, select Compute.</p>
<p>4. Select tabs at the top to show each type of compute target.</p>
<img src="images/q196_ref_20_0016400001.jpg" alt="Reference Image"><br>
<p>Box 3: Yes -</p>
<p>min_nodes is not specified, so it defaults to 0.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.amlcompute.amlcomputeprovisioningconfiguration https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-attach-compute-studio</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>trickerk</strong> <code>(Fri 28 Jan 2022 12:48)</code> - <em>Upvotes: 11</em></p><p>Given answer is correct!</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 15:00)</code> - <em>Upvotes: 5</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Wed 24 Jul 2024 09:13)</code> - <em>Upvotes: 1</em></p><p>2 should be no. &#x27;AmlCompute&#x27; refers to compute clusters, not instances: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-attach-compute-cluster?view=azureml-api-2&amp;tabs=python

Instances require &#x27;ComputeInstance&#x27;, see https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-compute-instance?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Tue 13 Aug 2024 06:21)</code> - <em>Upvotes: 1</em></p><p>My mistake. The answer should be &#x27;yes&#x27;</p></blockquote>
<blockquote><p><strong>haby</strong> <code>(Fri 14 Jun 2024 23:18)</code> - <em>Upvotes: 1</em></p><p>2 should be No, this script is for training a ml model, that must be a computer instance, the first item in the pic shows. You can&#x27;t say it&#x27;s a cluster coz you assign it &#x27;the_cluster_name&#x27;.</p></blockquote>
<blockquote><p><strong>SunilB</strong> <code>(Tue 05 Sep 2023 23:46)</code> - <em>Upvotes: 3</em></p><p>Box 3 is correct - 0
The minimum number of nodes to use on the cluster. If not specified, defaults to 0.
https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.amlcompute(class)?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>danishanis</strong> <code>(Sat 26 Aug 2023 23:54)</code> - <em>Upvotes: 1</em></p><p>The correct answer is Yes, Yes and No
The minimum number of nodes for the compute target created in the above code will default to 1 if you do not specify the min_nodes parameter, not 0</p></blockquote>
<blockquote><p><strong>danishanis</strong> <code>(Sat 26 Aug 2023 23:57)</code> - <em>Upvotes: 1</em></p><p>Additional explanation: For box 3, it is 1 and not 0; This means that the compute target will always have at least one node running, even if no jobs are currently scheduled to run on it.

The max_nodes parameter, on the other hand, does default to 1 if not specified. This means that by default, the compute target will have a single node, and will not scale up to more nodes automatically.</p></blockquote>
<blockquote><p><strong>GaryEl</strong> <code>(Fri 10 Nov 2023 22:52)</code> - <em>Upvotes: 6</em></p><p>The default is zero

https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.amlcompute.amlcomputeprovisioningconfiguration?view=azure-ml-py#parameters</p></blockquote>
<blockquote><p><strong>Suman_512</strong> <code>(Sat 26 Aug 2023 07:32)</code> - <em>Upvotes: 1</em></p><p>For 2 it will be rather &quot;Compute Instance&quot; than &quot;Compute Cluster&quot; so - NO</p></blockquote>
<blockquote><p><strong>InversaRadice</strong> <code>(Mon 03 Jun 2024 08:19)</code> - <em>Upvotes: 1</em></p><p>&quot;We guess&quot; its a cluster by the varable name, I agree with YES and a not misleading question had to Exibit the Compute configuration ...</p></blockquote>
<blockquote><p><strong>racnaoamo</strong> <code>(Sat 19 Nov 2022 08:50)</code> - <em>Upvotes: 4</em></p><p>similar question on 18-5-22</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Apr 2022 09:44)</code> - <em>Upvotes: 3</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>mthombenindhl84</strong> <code>(Fri 11 Mar 2022 23:00)</code> - <em>Upvotes: 3</em></p><p>on exam 11/9/2021</p></blockquote>
<blockquote><p><strong>dushmantha</strong> <code>(Mon 28 Feb 2022 14:16)</code> - <em>Upvotes: 2</em></p><p>On exam 2021/08/31</p></blockquote>
<blockquote><p><strong>Skandinov</strong> <code>(Sun 24 Oct 2021 11:21)</code> - <em>Upvotes: 1</em></p><p>how&#x27;s 1 yes?</p></blockquote>
<blockquote><p><strong>gamezone25</strong> <code>(Mon 25 Oct 2021 10:40)</code> - <em>Upvotes: 7</em></p><p>&quot;The compute is created within your workspace region as a resource that can be shared with other users in your workspace.&quot;
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-attach-compute-cluster?tabs=python#what-is-a-compute-cluster</p></blockquote>

</details>

---

[<< Previous Question](question_195.md) | [Home](/index.md) | [Next Question >>](question_197.md)
