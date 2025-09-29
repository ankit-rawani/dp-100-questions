# Question 117

You manage an Azure Machine Learning workspace by using the Azure CLI ml extension v2.

You need to define a YAML schema to create a compute cluster.

Which schema should you use?

- A.https://azuremlschemas.azureedge.net/latest/computeInstance.schema.json
- B.https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json
- C.https://azuremlschemas.azureedge.net/latest/vmCompute.schema.json
- D.https://azuremlschemas.azureedge.net/latest/kubernetesCompute.schema.json

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 01 Dec 2024 10:02)</code> - <em>Upvotes: 2</em></p><p>amlCompute.schema.json: This schema is specifically designed for Azure Machine Learning compute clusters, which are used for training machine learning models. It supports configurations for scalable and managed compute clusters that can handle automated machine learning, machine learning pipelines, and Azure Machine Learning designer training.</p></blockquote>
<blockquote><p><strong>orionduo</strong> <code>(Thu 29 Feb 2024 04:54)</code> - <em>Upvotes: 2</em></p><p>Correct
compute cluster: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json
compute instance: https://azuremlschemas.azureedge.net/latest/computeInstance.schema.json
Attached Virtual Machine: 	https://azuremlschemas.azureedge.net/latest/vmCompute.schema.json
Attached Azure Arc-enabled Kubernetes (KubernetesCompute): https://azuremlschemas.azureedge.net/latest/kubernetesCompute.schema.json</p></blockquote>
<blockquote><p><strong>labriji</strong> <code>(Mon 23 Oct 2023 17:41)</code> - <em>Upvotes: 3</em></p><p>Correct Answer is B, here is the link to the docs: https://learn.microsoft.com/en-us/azure/machine-learning/reference-yaml-overview?view=azureml-api-2#:~:text=model.schema.json-,Compute,-Reference</p></blockquote>

</details>

---

[<< Previous Question](question_116.md) | [Home](../index.md) | [Next Question >>](question_118.md)
