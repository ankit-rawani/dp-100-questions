# Question 410

You train and register a machine learning model. You create a batch inference pipeline that uses the model to generate predictions from multiple data files.

You must publish the batch inference pipeline as a service that can be scheduled to run every night.

You need to select an appropriate compute target for the inference service.

Which compute target should you use?

- A.Azure Machine Learning compute instance
- B.Azure Machine Learning compute cluster
- C.Azure Kubernetes Service (AKS)-based inference cluster
- D.Azure Container Instance (ACI) compute target

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>BTAB</strong> <code>(Fri 13 Jan 2023 03:18)</code> - <em>Upvotes: 10</em></p><p>I think the confusion here is real-time vs batch.  A real-time inference pipeline should use AKS.  This is a BATCH inference pipeline.  The answer is B.</p></blockquote>
<blockquote><p><strong>manualrg</strong> <code>(Sun 29 Jan 2023 12:58)</code> - <em>Upvotes: 2</em></p><p>I agree the answer is B. Indeed, in the example notebook: Create a Batch Inferencing Service
https://github.com/MicrosoftLearning/mslearn-dp100/blob/main/10%20-%20Create%20a%20Batch%20Inferencing%20Service.ipynb
Existing compute cluster resource is checked and set as pipeline compute target:
try:
    # Check for existing compute target
    inference_cluster = ComputeTarget(workspace=ws, name=cluster_name)
...
parallel_run_config = ParallelRunConfig(
    source_directory=experiment_folder,
    entry_script=&quot;batch_diabetes.py&quot;,
    mini_batch_size=&quot;5&quot;,
    error_threshold=10,
    output_action=&quot;append_row&quot;,
    environment=batch_env,
    compute_target=inference_cluster,
    node_count=2)</p></blockquote>
<blockquote><p><strong>445f1bd</strong> <code>(Sun 27 Jul 2025 22:08)</code> - <em>Upvotes: 1</em></p><p>Azure Machine Learning compute cluster (option B) is intended for scalable, parallel workloads and is the recommended target for batch pipelines.

Compute instance (option A) is for development and interactive work, not production/scheduled batch jobs.

AKS (option C) and ACI (option D) are for real-time (online) inference, not batch inference.</p></blockquote>

<blockquote><p><strong>avinyc</strong> <code>(Thu 09 Jan 2025 00:20)</code> - <em>Upvotes: 1</em></p><p>Azure Machine Learning compute clusters are designed to handle batch workloads efficiently, which aligns with the requirement of processing multiple data files</p></blockquote>
<blockquote><p><strong>nposteraro</strong> <code>(Mon 18 Nov 2024 11:54)</code> - <em>Upvotes: 1</em></p><p>I think it&#x27;s C: https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2#compute-targets-for-inference</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 09 Jun 2024 08:41)</code> - <em>Upvotes: 1</em></p><p>C is for real time B for batch</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Thu 30 May 2024 01:24)</code> - <em>Upvotes: 1</em></p><p>based on the SDK V2 Doc: https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2#compute-targets-for-inference</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Thu 24 Aug 2023 16:34)</code> - <em>Upvotes: 1</em></p><p>Azure Kubernetes Service (AKS) is a managed Kubernetes service that simplifies the deployment and management of a Kubernetes cluster in Azure1. An AKS-based inference cluster can be used to deploy machine learning models for real-time inferencing, but it is not the best choice for running batch inference jobs. For batch inference, you would want to use a compute target that can distribute the processing of large amounts of data across multiple nodes in the cloud</p></blockquote>
<blockquote><p><strong>BTAB</strong> <code>(Fri 13 Jan 2023 03:18)</code> - <em>Upvotes: 3</em></p><p>Voting B</p></blockquote>
<blockquote><p><strong>Crusader2k13</strong> <code>(Thu 15 Dec 2022 11:23)</code> - <em>Upvotes: 3</em></p><p>I think the answer B is indeed correct! There is no wording about a &quot;production-level&quot; or &quot;heavy-workload&quot; deployment (this would always hint to AKS), and according to the documentation:

https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target

a compute-cluster supports job-scheduling aka scheduling to run every night, and scales up and down depending on the configuration.</p></blockquote>

<blockquote><p><strong>silva_831</strong> <code>(Wed 16 Nov 2022 06:48)</code> - <em>Upvotes: 1</em></p><p>Yes, Answer should be AKS</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Mon 24 Oct 2022 03:23)</code> - <em>Upvotes: 3</em></p><p>Answer should be AKS.

Compute targets for inference:
1.Local web service
2.Azure Machine Learning endpoints
3.Azure Machine Learning Kubernetes
4.Azure Container Instances (SDK/CLI v1 only)

https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target</p></blockquote>

<blockquote><p><strong>ZoeJ</strong> <code>(Thu 27 Apr 2023 03:22)</code> - <em>Upvotes: 1</em></p><p>I agree with you</p></blockquote>
<blockquote><p><strong>amokrane_mancer</strong> <code>(Tue 18 Oct 2022 12:35)</code> - <em>Upvotes: 3</em></p><p>It should be aks !</p></blockquote>
<blockquote><p><strong>claps92</strong> <code>(Fri 09 Sep 2022 07:49)</code> - <em>Upvotes: 2</em></p><p>why not AKS?</p></blockquote>

</details>

---

[<< Previous Question](question_409.md) | [Home](../index.md) | [Next Question >>](question_411.md)
