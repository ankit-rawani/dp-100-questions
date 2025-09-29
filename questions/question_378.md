# Question 378

You train a machine learning model.

You must deploy the model as a real-time inference service for testing. The service requires low CPU utilization and less than 48 MB of RAM. The compute target for the deployed service must initialize automatically while minimizing cost and administrative overhead.

Which compute target should you use?

- A.Azure Container Instance (ACI)
- B.attached Azure Databricks cluster
- C.Azure Kubernetes Service (AKS) inference cluster
- D.Azure Machine Learning compute cluster

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

<p>Azure Container Instances (ACI) are suitable only for small models less than 1 GB in size.</p>
<p>Use it for low-scale CPU-based workloads that require less than 48 GB of RAM.</p>
<p>Note: Microsoft recommends using single-node Azure Kubernetes Service (AKS) clusters for dev-test of larger models.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/id-id/azure/machine-learning/how-to-deploy-and-where</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Mon 11 Jul 2022 14:17)</code> - <em>Upvotes: 7</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sat 12 Oct 2024 09:12)</code> - <em>Upvotes: 1</em></p><p>&#x27;minimizing cost&#x27; --&gt; use Azure Container Instance (ACI), not Azure Kubernetes Service (AKS).

&#x27;minimizing administrative overhead&#x27; --&gt; use Docker/container, not Azure App Service.

Conclusion: Azure Container Instance (ACI).</p></blockquote>

<blockquote><p><strong>michaelmorar</strong> <code>(Sun 10 Dec 2023 21:11)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-deploy-azure-container-instance

&quot;ACI is suitable only for small models that are under 1 GB in size. We recommend using single-node AKS to dev-test larger models.&quot;</p></blockquote>

<blockquote><p><strong>AjoseO</strong> <code>(Fri 03 Mar 2023 06:37)</code> - <em>Upvotes: 4</em></p><p>On Exam: 03 March 2022</p></blockquote>
<blockquote><p><strong>treadst0ne</strong> <code>(Mon 20 Jun 2022 18:50)</code> - <em>Upvotes: 3</em></p><p>Answer is correct.
https://docs.microsoft.com/en-gb/azure/machine-learning/concept-compute-target</p></blockquote>
<blockquote><p><strong>BigSoda</strong> <code>(Wed 18 May 2022 07:32)</code> - <em>Upvotes: 1</em></p><p>40MB -&gt; 48GB?</p></blockquote>
<blockquote><p><strong>mayank25</strong> <code>(Fri 06 May 2022 18:08)</code> - <em>Upvotes: 1</em></p><p>ACI are also suitable for small models less than 1 GB in size.</p></blockquote>
<blockquote><p><strong>ralucabala</strong> <code>(Thu 21 Apr 2022 14:46)</code> - <em>Upvotes: 1</em></p><p>Why not AKS Cluster as it&#x27;s required for real-time inferencing?</p></blockquote>
<blockquote><p><strong>dushmantha</strong> <code>(Tue 30 Aug 2022 05:28)</code> - <em>Upvotes: 2</em></p><p>Because AKS is the costliest deployment solution. And it only should use in production deployments</p></blockquote>
<blockquote><p><strong>azure1000</strong> <code>(Mon 01 Aug 2022 08:09)</code> - <em>Upvotes: 1</em></p><p>I think because they mentioned low scaling and testing with min cost. Thats why ACI</p></blockquote>
<blockquote><p><strong>cab123</strong> <code>(Mon 25 Apr 2022 16:28)</code> - <em>Upvotes: 6</em></p><p>I think it is because this is for testing and not production</p></blockquote>

</details>

---

[<< Previous Question](question_377.md) | [Home](../index.md) | [Next Question >>](question_379.md)
