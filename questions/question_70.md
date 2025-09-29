# Question 70

DRAG DROP -

An organization uses Azure Machine Learning service and wants to expand their use of machine learning.

You have the following compute environments. The organization does not want to create another compute environment.

![Question Image](images/q70_q_0008100001.png)

You need to determine which compute environment to use for the following scenarios.

Which compute types should you use? To answer, drag the appropriate compute environments to the correct scenarios. Each compute environment may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

Select and Place:

![Question Image](images/q70_q_0008100002.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q70_ans_0_0008100003.png" alt="Answer Image"><br>
<p>Box 1: nb_server -</p>
<img src="images/q70_ref_2_0008200001.png" alt="Reference Image"><br>
<p>Box 2: mlc_cluster -</p>
<p>With Azure Machine Learning, you can train your model on a variety of resources or environments, collectively referred to as compute targets. A compute target can be a local machine or a cloud resource, such as an Azure Machine Learning Compute, Azure HDInsight or a remote virtual machine.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target https://docs.microsoft.com/en-us/azure/machine-learning/how-to-set-up-training-targets</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>stonefl</strong> <code>(Sat 18 Sep 2021 16:36)</code> - <em>Upvotes: 107</em></p><p>answer should be: mlc_cluster, aks_cluster</p></blockquote>
<blockquote><p><strong>jitsblitz</strong> <code>(Tue 15 Mar 2022 08:36)</code> - <em>Upvotes: 5</em></p><p>For production grade model training, use an Azure Machine Learning compute cluster with multi-node scaling capabilities. For production grade model deployment, use Azure Kubernetes Service cluster.
Compute Type &quot;Machine Learning Compute&quot; is &quot;Compute Clusters&quot; under Compute tab.
https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-instance</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Fri 23 Sep 2022 14:48)</code> - <em>Upvotes: 6</em></p><p>The answer should be: 
mlc_cluster
aks_cluster

Here is why: https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer#compute

When using AML designer, the supported compute targets are
   - AML compute, for TRAINING
   - AKS, for DEPLOYMENT</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Tue 30 Nov 2021 22:15)</code> - <em>Upvotes: 11</em></p><p>should be compute instance and AKS. What is machine learning compute?</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Thu 16 Sep 2021 13:10)</code> - <em>Upvotes: 8</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target
to use designer in training, it has to be &quot; compute cluster &quot;</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Thu 16 Sep 2021 13:12)</code> - <em>Upvotes: 1</em></p><p>As a web service that&#x27;s used for real-time inference. Web service deployments use one of the following compute targets:

Local computer
Azure Machine Learning compute instance
Azure Container Instances
Azure Kubernetes Service
Azure Functions</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Wed 25 Sep 2024 16:40)</code> - <em>Upvotes: 5</em></p><p>on exam 3/25/2024</p></blockquote>
<blockquote><p><strong>Kanwal001</strong> <code>(Wed 28 Feb 2024 20:27)</code> - <em>Upvotes: 4</em></p><p>On exam 28/08/2023..</p></blockquote>
<blockquote><p><strong>braupi</strong> <code>(Thu 29 Feb 2024 04:33)</code> - <em>Upvotes: 1</em></p><p>what is the answer?</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Sat 20 Jan 2024 13:58)</code> - <em>Upvotes: 3</em></p><p>This was on Exam today (20 July 2023). I chose: mlc_cluster, aks_cluster respectively.</p></blockquote>
<blockquote><p><strong>Dilesha</strong> <code>(Sat 19 Aug 2023 00:34)</code> - <em>Upvotes: 4</em></p><p>On Exam 17 Feb 2023</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 02 Aug 2023 18:14)</code> - <em>Upvotes: 2</em></p><p>Azure Machine Learning compute for training,
AKS for deployment. 
https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer#compute</p></blockquote>
<blockquote><p><strong>meysa</strong> <code>(Mon 07 Aug 2023 21:03)</code> - <em>Upvotes: 1</em></p><p>Azure Machine Learning compute cluster
Azure Machine Learning compute instance
Azure Machine Learning Kubernetes 	
for designer these three computes can be used, I think in this case compute cluster is the right answer, what is machine learning compute? compute cluster or compute instance?</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 11 Nov 2022 12:57)</code> - <em>Upvotes: 3</em></p><p>Question is very poorly written, I believe that mlc --&gt; Azure Machine Learning Compute Instance, nb_server --&gt; some external compute instance linked with Azure Machine Learning Studio????</p></blockquote>
<blockquote><p><strong>DingDongSingSong</strong> <code>(Fri 30 Sep 2022 16:18)</code> - <em>Upvotes: 2</em></p><p>Answer is: 
1. Azure ML compute instance/cluster for training using Azure ML designer.
Ref Link:https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target#azure-machine-learning-compute-managed.
The link also shows that Azure ML Designer also supports Kubernetes compute for training as well. So this answer is a little tricky

2. Deployment of web service via Azure ML designer is to Kubernetes Cluster
Ref Link: https://github.com/solliancenet/azure-machine-learning-quickstarts/blob/master/aml-visual-interface/README.md</p></blockquote>
<blockquote><p><strong>[Removed]</strong> <code>(Sat 20 Aug 2022 18:11)</code> - <em>Upvotes: 1</em></p><p>on 20Feb2022
ans I put: nlb, gpu</p></blockquote>
<blockquote><p><strong>zehraoneexam</strong> <code>(Thu 15 Sep 2022 05:15)</code> - <em>Upvotes: 2</em></p><p>there is no gpu ?</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Mon 18 Jul 2022 04:31)</code> - <em>Upvotes: 1</em></p><p>Agree with stonefl answer,the same question appeared in Coursera practice test and the explanation for this is as below -
Machine Learning Compute Cluster supports integration with AML designer training pipeline, and Azure Kubernetes Service supports integration with AML Designer.</p></blockquote>
<blockquote><p><strong>ashii007</strong> <code>(Sat 25 Jun 2022 21:09)</code> - <em>Upvotes: 1</em></p><p>this question is dated. AKS is now a validation option for designer option.</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Fri 06 May 2022 21:37)</code> - <em>Upvotes: 1</em></p><p>on exam 6 Nov 2021, but with more questions. be aware of the different steps: training, deploy,  real-time inference, and  databricks scenario...</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Apr 2022 09:41)</code> - <em>Upvotes: 1</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Sun 03 Apr 2022 20:45)</code> - <em>Upvotes: 1</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>mthombenindhl84</strong> <code>(Fri 11 Mar 2022 22:58)</code> - <em>Upvotes: 1</em></p><p>on exam 11/9/2021</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Thu 03 Mar 2022 08:23)</code> - <em>Upvotes: 2</em></p><p>on exam 2/9/21</p></blockquote>

</details>

---

[<< Previous Question](question_69.md) | [Home](/index.md) | [Next Question >>](question_71.md)
