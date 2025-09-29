# Question 432

You manage an Azure Machine Learning workspace. You develop a machine learning model.

You must deploy the model to use a low-priority VM with a pricing discount.

You need to deploy the model.

Which compute target should you use?

* A.Azure Kubernetes Service (AKS)
* B.Azure Machine Learning compute clusters
* C.Azure Container Instances (ACI)
* D.Local deployment

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 10:26)</code> - <em>Upvotes: 1</em></p><p>Azure Machine Learning compute clusters: This option allows you to use low-priority VMs, which are VMs with a significant pricing discount. Low-priority VMs are less expensive than dedicated VMs, but they come with the risk of being preempted if Azure needs the capacity for higher-priority tasks. This makes them a cost-effective option for non-critical workloads or those that can handle interruptions.</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 07 Jul 2023 18:41)</code> - <em>Upvotes: 1</em></p><p>Correct.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-low-priority-batch?view=azureml-api-2&amp;tabs=sdk#creating-batch-deployments-with-low-priority-vms</p></blockquote>

</details>

---

[<< Previous Question](question_431.md) | [Home](/index.md) | [Next Question >>](question_433.md)
