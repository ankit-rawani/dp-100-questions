# Question 162

You manage an Azure Machine Learning workspace. You design a training job that is configured with a serverless compute.

The serverless compute must have a specific instance type and count.

You need to configure the serverless compute by using Azure Machine Learning Python SDK v2.

What should you do?

- A.Specify the compute name by using the compute parameter of the command job.
- B.Configure the tier parameter to Dedicated VM.
- C.Initialize and specify the ResourceConfiguration class.
- D.Initialize AmiCompute class with size and type specification.

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>f82411e</strong> <code>(Thu 29 May 2025 11:48)</code> - <em>Upvotes: 1</em></p><p>from azure.ai.ml.entities import CommandJob, ResourceConfiguration

job = CommandJob(
...
resources=ResourceConfiguration(
instance_count=2,
instance_type=&quot;Standard_DS3_v2&quot;
)
)</p></blockquote>

<blockquote><p><strong>ulg</strong> <code>(Sun 26 Jan 2025 22:56)</code> - <em>Upvotes: 1</em></p><p>To configure serverless compute with a specific instance type and count in Azure Machine Learning using the Python SDK v2, you need to use the ResourceConfiguration class.</p></blockquote>
<blockquote><p><strong>ulg</strong> <code>(Sun 26 Jan 2025 22:57)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-serverless-compute?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Fri 03 Jan 2025 23:58)</code> - <em>Upvotes: 1</em></p><p>Correct answer should be ResourceConfiguration (C). The AmlCompute class is used for creating managed compute clusters, not for configuring serverless compute.</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Sun 01 Dec 2024 02:54)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.amlcompute(class)?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>AzureGeek79</strong> <code>(Mon 30 Sep 2024 01:21)</code> - <em>Upvotes: 1</em></p><p>Given answer is correct.</p></blockquote>

</details>

---

[<< Previous Question](question_161.md) | [Home](../index.md) | [Next Question >>](question_163.md)
