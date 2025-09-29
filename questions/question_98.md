# Question 98

HOTSPOT -

You are using an Azure Machine Learning workspace. You set up an environment for model testing and an environment for production.

The compute target for testing must minimize cost and deployment efforts. The compute target for production must provide fast response time, autoscaling of the deployed service, and support real-time inferencing.

You need to configure compute targets for model testing and production.

Which compute targets should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q98_q_0012900001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q98_ans_0_0013000001.png" alt="Answer Image"><br>
<p>Box 1: Local web service -</p>
<p>The Local web service compute target is used for testing/debugging. Use it for limited testing and troubleshooting. Hardware acceleration depends on use of libraries in the local system.</p>
<p>Box 2: Azure Kubernetes Service (AKS)</p>
<p>Azure Kubernetes Service (AKS) is used for Real-time inference.</p>
<p>Recommended for production workloads.</p>
<p>Use it for high-scale production deployments. Provides fast response time and autoscaling of the deployed service</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>michaelmorar</strong> <code>(Sun 04 Dec 2022 08:30)</code> - <em>Upvotes: 13</em></p><p>&quot;You need to configure compute targets for model testing and production.&quot;
Suggests that we don&#x27;t need a target for training and evaluation, ONLY to test the deployed model. Therefore: &#x27;Local Web Service&#x27; for Test, and AKS for PROD.</p></blockquote>
<blockquote><p><strong>ahson0124</strong> <code>(Wed 15 Feb 2023 13:40)</code> - <em>Upvotes: 6</em></p><p>On exam 2023-02-15</p></blockquote>
<blockquote><p><strong>sanctafrax</strong> <code>(Thu 18 Jul 2024 09:16)</code> - <em>Upvotes: 1</em></p><p>Question states it is for model testing. Therefore ACI is not needed, Local Webservice should be fine. AKS is required for prod</p></blockquote>
<blockquote><p><strong>daviskv74</strong> <code>(Sun 15 Oct 2023 06:58)</code> - <em>Upvotes: 4</em></p><p>Chat GPT says for testing, ACI suitable</p></blockquote>
<blockquote><p><strong>prabhjot</strong> <code>(Sat 27 Jan 2024 08:05)</code> - <em>Upvotes: 1</em></p><p>i agress ACI for testing and for Production AKS</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Wed 08 Mar 2023 12:12)</code> - <em>Upvotes: 4</em></p><p>Exactly this question was on exam 07/March/2023</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Sun 08 Jan 2023 11:54)</code> - <em>Upvotes: 1</em></p><p>https://www.techtarget.com/searchcloudcomputing/definition/Azure-Container-Instances#:~:text=Azure%20Container%20Instances%20is%20a%20service%20that%20enables,having%20to%20provision%20or%20manage%20any%20underlying%20infrastructure.</p></blockquote>
<blockquote><p><strong>PremPatrick</strong> <code>(Fri 18 Nov 2022 07:55)</code> - <em>Upvotes: 2</em></p><p>LocalWebservice for testing (not sure though!)
https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target</p></blockquote>
<blockquote><p><strong>FlexingD</strong> <code>(Sat 05 Nov 2022 07:22)</code> - <em>Upvotes: 4</em></p><p>ACI for testing + 1</p></blockquote>
<blockquote><p><strong>reddragondms</strong> <code>(Mon 26 Sep 2022 07:30)</code> - <em>Upvotes: 1</em></p><p>Local web services and azure container instances are listed under compute targets for inference, not training targets.

Wouldn&#x27;t the order for &quot;minimize cost and deployment efforts&quot; for testing be first &quot;Local computer&quot; then &quot;Azure ML compute cluster&quot;? 

https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target</p></blockquote>
<blockquote><p><strong>claps92</strong> <code>(Mon 12 Sep 2022 15:40)</code> - <em>Upvotes: 3</em></p><p>ACI for testing (minimizes the deployment effort)</p></blockquote>
<blockquote><p><strong>klowqw</strong> <code>(Thu 01 Sep 2022 14:18)</code> - <em>Upvotes: 2</em></p><p>ACI for testing</p></blockquote>
<blockquote><p><strong>klowqw</strong> <code>(Fri 02 Sep 2022 19:36)</code> - <em>Upvotes: 1</em></p><p>Local for testing</p></blockquote>

</details>

---

[<< Previous Question](question_97.md) | [Home](/index.md) | [Next Question >>](question_99.md)
