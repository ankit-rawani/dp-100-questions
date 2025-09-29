# Question 333

You have an Azure Machine Learning workspace. You build a deep learning model.

You need to publish a GPU-enabled model as a web service.

Which two compute targets can you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

* A.Azure Kubernetes Service (AKS)
* B.Azure Container Instances (ACI)
* C.Local web service
* D.Azure Machine Learning compute clusters

<details>
  <summary>Show Suggested Answer</summary>

  <strong>AB</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>PI_Team</strong> <code>(Wed 23 Aug 2023 13:56)</code> - <em>Upvotes: 7</em></p><p>Azure Container Instances (ACI) does support GPU-based deployments, which can be used to accelerate the execution of deep learning models. You can use ACI to deploy a GPU-enabled model as a web service in an Azure Machine Learning workspace.

Regarding Azure Machine Learning compute clusters, you are also correct that they cannot be used as a deployment target for web services. Compute clusters are used for training and batch scoring workloads, not for deploying models as web services.

In summary, the correct answer to your question is A. Azure Kubernetes Service (AKS) and B. Azure Container Instances (ACI). 

Check the link: https://learn.microsoft.com/en-us/azure/container-instances/container-instances-gpu

SaM</p></blockquote>
<blockquote><p><strong>Nagamori</strong> <code>(Sat 17 Jun 2023 03:58)</code> - <em>Upvotes: 6</em></p><p>answer is AD.</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Tue 07 Jan 2025 04:00)</code> - <em>Upvotes: 1</em></p><p>Answer should be A and D</p></blockquote>
<blockquote><p><strong>colin1919</strong> <code>(Mon 09 Dec 2024 14:29)</code> - <em>Upvotes: 1</em></p><p>ACI is for small/insignificant deployments (low CPU and RAM), so by logic it&#x27;s not making sense to have GPU enabled on them.</p></blockquote>
<blockquote><p><strong>testgm</strong> <code>(Mon 02 Dec 2024 15:29)</code> - <em>Upvotes: 1</em></p><p>To run certain compute-intensive workloads on Azure Container Instances, deploy your container groups with GPU resources. The container instances in the group can access one or more NVIDIA Tesla GPUs while running container workloads such as CUDA and deep learning applications.</p></blockquote>
<blockquote><p><strong>jl420</strong> <code>(Fri 08 Nov 2024 18:05)</code> - <em>Upvotes: 1</em></p><p>Only A&amp;B support GPU and should be used for inference (web service). D can have GPU but meant for training.</p></blockquote>
<blockquote><p><strong>teku_</strong> <code>(Fri 05 Jul 2024 08:25)</code> - <em>Upvotes: 1</em></p><p>this is correct</p></blockquote>
<blockquote><p><strong>teku_</strong> <code>(Fri 05 Jul 2024 08:28)</code> - <em>Upvotes: 1</em></p><p>well, i think its AB.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 09 Jun 2024 12:35)</code> - <em>Upvotes: 1</em></p><p>AB correct</p></blockquote>
<blockquote><p><strong>Krista2023A</strong> <code>(Sun 17 Sep 2023 04:49)</code> - <em>Upvotes: 3</em></p><p>Answer - AD
Azure Compute Instances do not support GPU, only use for low-scale CPU-based workloads. Reference https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>hiyoww</strong> <code>(Wed 10 Apr 2024 15:55)</code> - <em>Upvotes: 2</em></p><p>B. Azure Container Instances (ACI)
not Azure Compute Instances</p></blockquote>
<blockquote><p><strong>abcd9999</strong> <code>(Wed 02 Aug 2023 06:38)</code> - <em>Upvotes: 1</em></p><p>ACI doesn&#x27;t support GPU</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Tue 04 Jul 2023 12:38)</code> - <em>Upvotes: 2</em></p><p>Answer AD</p></blockquote>

</details>

---

[<< Previous Question](question_332.md) | [Home](/index.md) | [Next Question >>](question_334.md)
