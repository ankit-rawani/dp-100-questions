# Question 453

You manage an Azure Machine Learning workspace that includes a batch endpoint.

You plan to deploy a model to the batch endpoint.

You need to configure compute for the deployment.

Which compute should you use?

* A.Remote VM
* B.AmlCompute instance
* C.Azure Batch
* D.Kubernetes cluster

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>negin</strong> <code>(Thu 26 Jun 2025 17:51)</code> - <em>Upvotes: 1</em></p><p>Kubernetes (AKS) is used for real-time (online) endpoints, not batch endpoints. Batch endpoints do not support AKS or other Kubernetes-based compute targets.</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Thu 09 Jan 2025 04:20)</code> - <em>Upvotes: 1</em></p><p>Azure Batch</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Tue 03 Dec 2024 11:13)</code> - <em>Upvotes: 1</em></p><p>Batch endpoints run on compute clusters and support both Azure Machine Learning compute clusters (AmlCompute) and Kubernetes clusters. Clusters are a shared resource, therefore, one cluster can host one or many batch deployments (along with other workloads, if desired).

Create a compute named batch-cluster, as shown in the following code. You can adjust as needed and reference your compute using azureml:&lt;your-compute-name&gt;.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-batch-model-deployments?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>Heleon</strong> <code>(Tue 19 Nov 2024 15:33)</code> - <em>Upvotes: 1</em></p><p>D is correct. Only clusters 
Batch endpoints run on compute clusters and support both Azure Machine Learning compute clusters (AmlCompute) and Kubernetes clusters. Clusters are a shared resource, therefore, one cluster can host one or many batch deployments (along with other workloads, if desired).</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Wed 13 Nov 2024 23:36)</code> - <em>Upvotes: 1</em></p><p>Seems like D is correct.</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Wed 13 Nov 2024 23:35)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-batch-model-deployments?view=azureml-api-2&amp;tabs=cli</p></blockquote>

</details>

---

[<< Previous Question](question_452.md) | [Home](/index.md) | [Next Question >>](question_454.md)
