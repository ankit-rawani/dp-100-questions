# Question 384

You use Azure Machine Learning designer to create a real-time service endpoint. You have a single Azure Machine Learning service compute resource.

You train the model and prepare the real-time pipeline for deployment.

You need to publish the inference pipeline as a web service.

Which compute type should you use?

- A.a new Machine Learning Compute resource
- B.Azure Kubernetes Services
- C.HDInsight
- D.the existing Machine Learning Compute resource
- E.Azure Databricks

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Mon 11 Jul 2022 14:18)</code> - <em>Upvotes: 7</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sun 20 Oct 2024 07:07)</code> - <em>Upvotes: 1</em></p><p>B, for deployment phase, AKS. Not powerful computer for training model.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 22 Feb 2024 20:54)</code> - <em>Upvotes: 2</em></p><p>D. the existing Machine Learning Compute resource

Since you already have a single Azure Machine Learning service compute resource, it is recommended to use it to publish the inference pipeline as a web service. This will help you to minimize the cost and simplify the deployment process.</p></blockquote>

<blockquote><p><strong>michaelmorar</strong> <code>(Mon 11 Dec 2023 18:16)</code> - <em>Upvotes: 3</em></p><p>AKS always the solution for these types of problems.</p></blockquote>
<blockquote><p><strong>andre999</strong> <code>(Tue 21 Jun 2022 07:33)</code> - <em>Upvotes: 4</em></p><p>The answer is correct: Azure Kubernetes Service (AKS) is used for Real-time inference.</p></blockquote>
<blockquote><p><strong>Lucario95</strong> <code>(Mon 16 May 2022 13:26)</code> - <em>Upvotes: 1</em></p><p>Doesn&#x27;t the question refer to which compute to use to deploy the pipeline, thus answer D being correct?</p></blockquote>
<blockquote><p><strong>azure1000</strong> <code>(Mon 01 Aug 2022 08:26)</code> - <em>Upvotes: 2</em></p><p>It says you need to publish the model, thus Aks</p></blockquote>
<blockquote><p><strong>ZeeshanNawaz</strong> <code>(Fri 11 Feb 2022 01:06)</code> - <em>Upvotes: 1</em></p><p>Why the existing compute can&#x27;t be used?</p></blockquote>
<blockquote><p><strong>Zwi3b3l</strong> <code>(Fri 25 Feb 2022 18:40)</code> - <em>Upvotes: 6</em></p><p>As per https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target only AKS can be used for real-time interference</p></blockquote>

</details>

---

[<< Previous Question](question_383.md) | [Home](../index.md) | [Next Question >>](question_385.md)
