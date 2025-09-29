# Question 379

HOTSPOT -

You are a lead data scientist for a project that tracks the health and migration of birds. You create a multi-image classification deep learning model that uses a set of labeled bird photos collected by experts. You plan to use the model to develop a cross-platform mobile app that predicts the species of bird captured by app users.

You must test and deploy the trained model as a web service. The deployed model must meet the following requirements:

✑ An authenticated connection must not be required for testing.

✑ The deployed model must perform with low latency during inferencing.

✑ The REST endpoints must be scalable and should have a capacity to handle large number of requests when multiple end users are using the mobile application.

You need to verify that the web service returns predictions in the expected JSON format when a valid REST request is submitted.

Which compute resources should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q379_q_0037200001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q379_ans_0_image617.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Lucario95</strong> <code>(Fri 14 May 2021 15:28)</code> - <em>Upvotes: 42</em></p><p>So the right answers should be gpu-cluster for test and AKS for production?</p></blockquote>
<blockquote><p><strong>Marnil</strong> <code>(Fri 29 Apr 2022 11:50)</code> - <em>Upvotes: 1</em></p><p>Why would you need a GPU cluster for testing? Isn&#x27;t testing just comparing predictions with actual labels?</p></blockquote>
<blockquote><p><strong>Marnil</strong> <code>(Fri 29 Apr 2022 12:01)</code> - <em>Upvotes: 7</em></p><p>Nvm, you need cluster (or aks) for gpu support. 
https://docs.microsoft.com/en-gb/azure/machine-learning/concept-compute-target

How come a third of answers on this site are incorrect, and that I cannot delete my own comments from discussions</p></blockquote>
<blockquote><p><strong>mtrdhar19841234</strong> <code>(Mon 19 Apr 2021 21:14)</code> - <em>Upvotes: 15</em></p><p>Why not AKS cluster?</p></blockquote>
<blockquote><p><strong>gamezone25</strong> <code>(Tue 20 Apr 2021 18:53)</code> - <em>Upvotes: 8</em></p><p>I agree with the AKS cluster. The documentation says that AKS should be used for real-time inference, which is not supported by the GPU compute cluster.
https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target#deploy</p></blockquote>
<blockquote><p><strong>ACSC</strong> <code>(Sun 02 May 2021 10:00)</code> - <em>Upvotes: 2</em></p><p>Agree. Answer is AKS for both.</p></blockquote>
<blockquote><p><strong>SaudMeethal</strong> <code>(Sun 09 May 2021 10:08)</code> - <em>Upvotes: 4</em></p><p>If security isn&#x27;t required for testing, shouldn&#x27;t the gpu-compute cluster do the job here? AKS should be used for production only.</p></blockquote>
<blockquote><p><strong>dijaa</strong> <code>(Fri 30 Apr 2021 19:58)</code> - <em>Upvotes: 1</em></p><p>in which?</p></blockquote>
<blockquote><p><strong>natrave</strong> <code>(Sun 02 May 2021 10:33)</code> - <em>Upvotes: 4</em></p><p>I second this. It has to be AKS cluster as low latency and GPU are required in the question:
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where?tabs=azcli#choose-a-compute-target</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Sun 31 Dec 2023 19:43)</code> - <em>Upvotes: 10</em></p><p>Correct answers: 
- Test: ds-workstation notebook VM
- Production: AKS-compute cluster

Test: ds-workstation notebook VM
Since the requirement for the testing environment is that it must not require an authenticated connection, then none of the cluster options (CPU, AKS, GPU) would be fit for use as a Testing resource. This is because these online cluster resources do not recommend and highly discourage to have unauthenticated connection due to obvious security concerns. DSVM offers an isolated or controlled environment, where unauthenticated access is temporarily allowed, but this would be an exception rather than the norm.

Production: AKS-compute cluster
The AKS (Azure Kubernetes Service) cluster is better for both (1) low latency and (2) scalability, unlike GPU cluster which is designed for low latency not for scalability, which is a requirement for the PROD env.</p></blockquote>
<blockquote><p><strong>jl420</strong> <code>(Fri 08 Nov 2024 19:13)</code> - <em>Upvotes: 2</em></p><p>THIS IS THE WAY!</p></blockquote>
<blockquote><p><strong>InversaRadice</strong> <code>(Sat 09 Dec 2023 10:20)</code> - <em>Upvotes: 1</em></p><p>Another misleading question: there is no clue about cost requirements, which will lead to the proper answer...</p></blockquote>
<blockquote><p><strong>A_PL300</strong> <code>(Mon 18 Sep 2023 23:19)</code> - <em>Upvotes: 4</em></p><p>Question like this one on 4-Sept-2023 exam</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 26 Jul 2023 19:54)</code> - <em>Upvotes: 5</em></p><p>Test:
A) ds-workstation notebook VM

For testing purposes, using a data science workstation notebook VM would be ideal. Since you&#x27;re only testing the API responses and not focusing on large scale inferencing, a fully provisioned cluster would not be necessary.

Production:
f) aks-compute cluster

Azure Kubernetes Service (AKS) cluster is best suited for production deployment of your machine learning model. AKS offers capabilities like auto-scaling and load balancing, ensuring that your model can handle a large number of requests and perform with low latency during inferencing. It is also not necessary for the compute resource to have a GPU for inferencing, making the AKS cluster a cost-effective option.</p></blockquote>
<blockquote><p><strong>sap_dg</strong> <code>(Mon 27 Mar 2023 18:05)</code> - <em>Upvotes: 1</em></p><p>I would go for a cpu-compute cluster for testing</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 22 Feb 2023 16:52)</code> - <em>Upvotes: 2</em></p><p>CB. 
Explanation:
For testing, a CPU-based compute cluster should be sufficient since the primary requirement is to verify that the web service returns predictions in the expected JSON format. A CPU-based compute cluster is relatively cheaper and can handle moderate to low traffic during testing.

For production, an AKS (Azure Kubernetes Service) cluster is recommended as it offers scalable and efficient orchestration of containers for high traffic applications. Since the mobile app is expected to receive multiple requests from end users, a scalable and reliable production environment is required. The AKS cluster provides an authenticated connection, and Kubernetes can scale the deployed model horizontally to handle a large number of requests.

Note that GPU-based compute clusters may offer faster inferencing performance but are relatively expensive and may not be necessary for this specific project&#x27;s requirements. Additionally, the deployment of GPU-based clusters may require additional configuration and setup, which may not be practical for testing and production.</p></blockquote>
<blockquote><p><strong>giusecozza</strong> <code>(Wed 07 Sep 2022 13:36)</code> - <em>Upvotes: 8</em></p><p>Box1: I think the answer is here: &quot;When using the Azure Machine Learning SDK v2 on a compute instance or on an Azure Virtual Machine, you can use a managed identity for Azure. This workflow allows the VM to connect to the workspace using the managed identity, without storing credentials in Python code or prompting the user to authenticate. Azure Machine Learning compute clusters can also be configured to use a managed identity to access the workspace when training models.&quot;
So VM sounds good, as we are talking about testing mode on an inference process
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-setup-authentication?tabs=sdk

Box2: AKS. Definitely the best solution when dealing with low latency and scaling needs on inference process

https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Wed 08 Jun 2022 17:52)</code> - <em>Upvotes: 4</em></p><p>PROD is AKS for sure, test 3 options 
-- local
-- contain instance
-- aks
it does not required authentication, I will vote for local machine</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Tue 08 Mar 2022 06:21)</code> - <em>Upvotes: 3</em></p><p>&quot;Although compute targets like local, and Azure Machine Learning compute clusters support GPU for training and experimentation, using GPU for inference when deployed as a web service is supported only on AKS.&quot;

https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target#deploy</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Thu 03 Mar 2022 06:36)</code> - <em>Upvotes: 3</em></p><p>On 03 March 2022</p></blockquote>
<blockquote><p><strong>Maskit12</strong> <code>(Thu 16 Dec 2021 14:14)</code> - <em>Upvotes: 12</em></p><p>Train: GPU, test: DS, Production: AKS</p></blockquote>
<blockquote><p><strong>Nand4</strong> <code>(Fri 25 Feb 2022 04:26)</code> - <em>Upvotes: 1</em></p><p>I agree</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Wed 08 Dec 2021 11:37)</code> - <em>Upvotes: 1</em></p><p>Azure compute cluster is not supporting real-time inference, only batch inference
I think workstation notebook vm works with the question request

https://docs.microsoft.com/en-gb/azure/machine-learning/concept-compute-target

https://docs.microsoft.com/en-gb/azure/machine-learning/how-to-deploy-local-container-notebook-vm</p></blockquote>
<blockquote><p><strong>ML_Novice</strong> <code>(Thu 18 Nov 2021 16:51)</code> - <em>Upvotes: 1</em></p><p>what is the final good answer please?</p></blockquote>
<blockquote><p><strong>shiyu</strong> <code>(Fri 22 Oct 2021 08:54)</code> - <em>Upvotes: 1</em></p><p>So the correct answers are AKS for both?</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Fri 03 Sep 2021 07:37)</code> - <em>Upvotes: 2</em></p><p>on 2/9/21</p></blockquote>

</details>

---

[<< Previous Question](question_378.md) | [Home](/index.md) | [Next Question >>](question_380.md)
