# Question 374

You create a deep learning model for image recognition on Azure Machine Learning service using GPU-based training.

You must deploy the model to a context that allows for real-time GPU-based inferencing.

You need to configure compute resources for model inferencing.

Which compute type should you use?

- A.Azure Container Instance
- B.Azure Kubernetes Service
- C.Field Programmable Gate Array
- D.Machine Learning Compute

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

<p>You can use Azure Machine Learning to deploy a GPU-enabled model as a web service. Deploying a model on Azure Kubernetes Service (AKS) is one option.</p>
<p>The AKS cluster provides a GPU resource that is used by the model for inference.</p>
<p>Inference, or model scoring, is the phase where the deployed model is used to make predictions. Using GPUs instead of CPUs offers performance advantages on highly parallelizable computation.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-inferencing-gpus</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ACSC</strong> <code>(Sat 27 Mar 2021 12:39)</code> - <em>Upvotes: 19</em></p><p>Answer is correct. AKS -&gt; GPU support</p></blockquote>
<blockquote><p><strong>D0ktor</strong> <code>(Tue 19 Nov 2024 22:58)</code> - <em>Upvotes: 1</em></p><p>AKS is the solution</p></blockquote>
<blockquote><p><strong>Ran2025</strong> <code>(Sun 01 Oct 2023 06:39)</code> - <em>Upvotes: 1</em></p><p>B is correct!  AKS supports real-time GPU-based inferencing
https://learn.microsoft.com/en-gb/azure/machine-learning/concept-compute-target?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 26 Jul 2023 19:57)</code> - <em>Upvotes: 1</em></p><p>B. Azure Kubernetes Service

Azure Kubernetes Service (AKS) provides an option to create a GPU-enabled node pool which would be suitable for real-time GPU-based inferencing. The other services listed do not provide the same level of GPU support necessary for such operations.

Keep in mind that setting up and managing a Kubernetes cluster does require some additional skills and setup compared to other Azure services, but it provides a high level of control and scalability.</p></blockquote>

<blockquote><p><strong>phdykd</strong> <code>(Wed 22 Feb 2023 17:40)</code> - <em>Upvotes: 3</em></p><p>The compute type that should be used for real-time GPU-based inferencing of a deep learning model is:
D. Machine Learning Compute

Explanation:
To enable GPU-based inferencing on a deployed model, Machine Learning Compute (MLC) should be used. MLC is a managed service provided by Azure Machine Learning that can provision compute resources for training and inferencing machine learning models. The service can be configured to allocate resources based on the required processing power, which can include GPU and CPU-based clusters.

Azure Container Instance (A) is a compute service that allows for running containerized applications without managing the underlying infrastructure, but it does not provide GPU resources. Azure Kubernetes Service (B) is a container orchestration service that can be used to manage containerized applications but requires additional configuration to enable GPU-based inferencing. Field Programmable Gate Array (C) is a hardware device that can be used to implement specific logic circuits but is not a cloud-based compute resource.</p></blockquote>

<blockquote><p><strong>austin06112000</strong> <code>(Mon 17 Jan 2022 14:02)</code> - <em>Upvotes: 1</em></p><p>Answer is correct.</p></blockquote>
<blockquote><p><strong>dwight55</strong> <code>(Thu 12 Aug 2021 16:39)</code> - <em>Upvotes: 1</em></p><p>looking for somebody to share contrib access pdf file with Q&amp;A &amp; discussion
m a i l to me at dwight (at) existiert.net
ofc does not have to be free</p></blockquote>
<blockquote><p><strong>treadst0ne</strong> <code>(Mon 21 Jun 2021 17:02)</code> - <em>Upvotes: 3</em></p><p>Answer is B.
GPU for inference when deployed as a web service is supported only on AKS.
https://docs.microsoft.com/en-gb/azure/machine-learning/concept-compute-target</p></blockquote>

</details>

---

[<< Previous Question](question_373.md) | [Home](../index.md) | [Next Question >>](question_375.md)
