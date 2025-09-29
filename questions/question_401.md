# Question 401

You use the Azure Machine Learning designer to create and run a training pipeline. You then create a real-time inference pipeline.

You must deploy the real-time inference pipeline as a web service.

What must you do before you deploy the real-time inference pipeline?

- A.Run the real-time inference pipeline.
- B.Create a batch inference pipeline.
- C.Clone the training pipeline.
- D.Create an Azure Machine Learning compute cluster.

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>pancman</strong> <code>(Wed 12 Oct 2022 19:41)</code> - <em>Upvotes: 10</em></p><p>The given answer is correct. A compute target such as AKS needs to be created in order to do inferencing real-time.</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Thu 17 Aug 2023 23:52)</code> - <em>Upvotes: 1</em></p><p>Agreed. Azure Machine Learning endpoints can be used for either Real-time inference or Batch inference.
https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Fri 16 Sep 2022 13:35)</code> - <em>Upvotes: 7</em></p><p>A is the correct answer</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Wed 09 Aug 2023 00:42)</code> - <em>Upvotes: 3</em></p><p>I do not quite get this. The question asks what you must do before you deploy the real-time inference pipeline, and A is to run the real-time inference pipeline. If A is right, you must run the real-time inference pipeline before you deploy the real-time inference pipeline. That cannot be right, can it?</p></blockquote>
<blockquote><p><strong>445f1bd</strong> <code>(Sun 27 Jul 2025 21:58)</code> - <em>Upvotes: 1</em></p><p>Before you can deploy a real-time inference pipeline as a web service in Azure Machine Learning Designer, you must first run the real-time inference pipeline successfully. This execution ensures that the pipeline is validated, and a trained model exists in the experiment history. Only after a successful run can you proceed to deploy it as a web service.</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Wed 08 Jan 2025 04:21)</code> - <em>Upvotes: 2</em></p><p>D. Create an Azure Machine Learning compute cluster.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 14:26)</code> - <em>Upvotes: 2</em></p><p>Answer is D, A has nothing to do before deploy</p></blockquote>
<blockquote><p><strong>shareefudin</strong> <code>(Sun 10 Nov 2024 16:49)</code> - <em>Upvotes: 2</em></p><p>D is correct, because it says about deployment, this means we have think about deployment only not about whether person has run the inference-pipeline for testing</p></blockquote>
<blockquote><p><strong>haby</strong> <code>(Wed 19 Jun 2024 14:02)</code> - <em>Upvotes: 1</em></p><p>A for me. 
&quot;You use the Azure Machine Learning designer to create and run a training pipeline&quot; means you have run training pipeline but it doesn&#x27;t mean you have run Inferencing Pipeline. You must run inferencing pipeline at least once before deployment.</p></blockquote>
<blockquote><p><strong>FH17</strong> <code>(Thu 07 Mar 2024 19:54)</code> - <em>Upvotes: 1</em></p><p>A is the one</p></blockquote>
<blockquote><p><strong>abcd9999</strong> <code>(Thu 01 Feb 2024 07:05)</code> - <em>Upvotes: 4</em></p><p>To deploy a real-time inference pipeline, you have to run the pipeline at least once (submit before you deploy it) 
https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-designer-automobile-price-deploy?view=azureml-api-1</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 27 Jan 2024 03:35)</code> - <em>Upvotes: 3</em></p><p>D. Create an Azure Machine Learning compute cluster.

In order to deploy a real-time inference pipeline as a web service in Azure Machine Learning, you need to have a compute target, and this can be an Azure Machine Learning Compute Cluster. This is where your model will be hosted and run when you deploy it. The other options are not necessary before deploying the inference pipeline. Running the pipeline or creating a batch inference pipeline isn&#x27;t required before deployment. Cloning the training pipeline also has no direct bearing on deploying the real-time inference pipeline.</p></blockquote>

<blockquote><p><strong>colin1919</strong> <code>(Mon 01 Jan 2024 15:26)</code> - <em>Upvotes: 2</em></p><p>&quot;You use the Azure Machine Learning designer to create and run a training pipeline. You then create a real-time inference pipeline&quot;. This means that you already ran the training pipeline, because otherwise you would not have been able to create a real-time inferencing pipeline. So the only logical in my view would be D.</p></blockquote>
<blockquote><p><strong>ZoeJ</strong> <code>(Fri 27 Oct 2023 03:08)</code> - <em>Upvotes: 2</em></p><p>I think the given answer is correct</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Fri 08 Sep 2023 11:30)</code> - <em>Upvotes: 1</em></p><p>Exactly this question was on exam 07/March/2023</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 23 Aug 2023 19:02)</code> - <em>Upvotes: 1</em></p><p>D. Create an Azure Machine Learning compute cluster.</p></blockquote>
<blockquote><p><strong>Sammour</strong> <code>(Thu 13 Apr 2023 08:24)</code> - <em>Upvotes: 1</em></p><p>AKS is not given as one of the options, so i&#x27;d vote for A</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sun 18 Dec 2022 02:51)</code> - <em>Upvotes: 2</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sun 11 Dec 2022 15:10)</code> - <em>Upvotes: 4</em></p><p>A is correct!  You must have a target already, so you can train a pipeline, which is a given</p></blockquote>

</details>

---

[<< Previous Question](question_400.md) | [Home](../index.md) | [Next Question >>](question_402.md)
