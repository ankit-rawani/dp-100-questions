# Question 281

You create and register a model in an Azure Machine Learning workspace.

You must use the Azure Machine Learning SDK to implement a batch inference pipeline that uses a ParallelRunStep to score input data using the model. You must specify a value for the ParallelRunConfig compute_target setting of the pipeline step.

You need to create the compute target.

Which class should you use?

* A.BatchCompute
* B.AdlaCompute
* C.AmlCompute
* D.AksCompute

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>
<p>Compute target to use for ParallelRunStep. This parameter may be specified as a compute target object or the string name of a compute target in the workspace.</p>
<p>The compute_target target is of AmlCompute or string.</p>
<p>Note: An Azure Machine Learning Compute (AmlCompute) is a managed-compute infrastructure that allows you to easily create a single or multi-node compute.</p>
<p>The compute is created within your workspace region as a resource that can be shared with other users</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-contrib-pipeline-steps/azureml.contrib.pipeline.steps.parallelrunconfig https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.amlcompute(class)</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>AjoseO</strong> <code>(Fri 03 Mar 2023 06:36)</code> - <em>Upvotes: 6</em></p><p>On 03 March 2022</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 24 Jul 2024 18:33)</code> - <em>Upvotes: 1</em></p><p>The AmlCompute class is used in Azure Machine Learning for managing compute targets. It&#x27;s designed for running machine learning workloads and supports various VM sizes for scaling resources according to the workload&#x27;s needs.

ParallelRunStep, which you want to use for your batch inference pipeline, can efficiently use AmlCompute instances to parallelize and speed up the processing.</p></blockquote>
<blockquote><p><strong>Jin_22</strong> <code>(Fri 15 Mar 2024 14:26)</code> - <em>Upvotes: 1</em></p><p>C. AmlCompute.

Explanation:
To create a compute target for use with Azure Machine Learning, you can create an instance of the appropriate ComputeTarget class in the azureml.core.compute package. In this case, the compute target must support distributed processing, which is required for the ParallelRunStep. The AmlCompute class is the only class listed that provides this capability.

BatchCompute is not a valid compute target class in the azureml.core.compute package. Instead, it is a service provided by Azure that enables you to run large-scale, high-performance batch jobs.

AdlaCompute is a compute target class in the azureml.core.compute package, but it is not designed for distributed processing. Instead, it is used to manage Azure Data Lake Analytics clusters.

AksCompute is a compute target class in the azureml.core.compute package that enables you to use an Azure Kubernetes Service (AKS) cluster for machine learning workloads. While AKS is capable of distributed processing, this compute target is not specifically designed for use with the ParallelRunStep.</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sun 12 Mar 2023 12:09)</code> - <em>Upvotes: 2</em></p><p>AmlCompute is the correct answer.</p></blockquote>
<blockquote><p><strong>Xsytt419</strong> <code>(Fri 30 Dec 2022 18:17)</code> - <em>Upvotes: 2</em></p><p>Why not D?</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Fri 03 Feb 2023 22:14)</code> - <em>Upvotes: 3</em></p><p>batch inferencing is asynchronus and doesn&#x27;t require scaling and low latency like production real time inferencing would so no need for any costly AKS. batch inferencing relies on parallel processing instead for achieving efficiency.</p></blockquote>
<blockquote><p><strong>[Removed]</strong> <code>(Tue 03 Jan 2023 16:01)</code> - <em>Upvotes: 2</em></p><p>The docs specifically mention AML: https://docs.microsoft.com/en-us/python/api/azureml-contrib-pipeline-steps/azureml.contrib.pipeline.steps.parallelrunconfig

I assume D could be correct too, but the question is phrased as &#x27;which SHOULD you use&#x27; and AML is prefereable - not sure why though</p></blockquote>
<blockquote><p><strong>RAHULsingla</strong> <code>(Wed 04 Jan 2023 18:21)</code> - <em>Upvotes: 1</em></p><p>Apparently webservices are not used with pipeline. Not sure why.</p></blockquote>

</details>

---

[<< Previous Question](question_280.md) | [Home](/index.md) | [Next Question >>](question_282.md)
