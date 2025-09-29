# Question 390

You use the Azure Machine Learning Python SDK to define a pipeline that consists of multiple steps.

When you run the pipeline, you observe that some steps do not run. The cached output from a previous run is used instead.

You need to ensure that every step in the pipeline is run, even if the parameters and contents of the source directory have not changed since the previous run.

What are two possible ways to achieve this goal? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- A.Use a PipelineData object that references a datastore other than the default datastore.
- B.Set the regenerate_outputs property of the pipeline to True.
- C.Set the allow_reuse property of each step in the pipeline to False.
- D.Restart the compute cluster where the pipeline experiment is configured to run.
- E.Set the outputs property of each step in the pipeline to True.

<details>
  <summary>Show Suggested Answer</summary>

<strong>BC</strong><br>

<p>B: If regenerate_outputs is set to True, a new submit will always force generation of all step outputs, and disallow data reuse for any step of this run. Once this run is complete, however, subsequent runs may reuse the results of this run.</p>
<p>C: Keep the following in mind when working with pipeline steps, input/output data, and step reuse.</p>
<p>✑ If data used in a step is in a datastore and allow_reuse is True, then changes to the data change won&#x27;t be detected. If the data is uploaded as part of the snapshot (under the step&#x27;s source_directory), though this is not recommended, then the hash will change and will trigger a rerun.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.pipelinestep https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/intro-to-pipelines/aml-pipelines-getting- started.ipynb</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jul 2023 14:19)</code> - <em>Upvotes: 9</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Wed 27 Nov 2024 10:15)</code> - <em>Upvotes: 1</em></p><p>The other answers an nonsensical.</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Mon 18 Mar 2024 09:47)</code> - <em>Upvotes: 3</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Thu 25 Jan 2024 10:46)</code> - <em>Upvotes: 2</em></p><p>correct</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Mon 06 Nov 2023 23:10)</code> - <em>Upvotes: 1</em></p><p>on 6 Nov 2021</p></blockquote>
<blockquote><p><strong>santoshpandit</strong> <code>(Fri 23 Jun 2023 02:15)</code> - <em>Upvotes: 3</em></p><p>correct</p></blockquote>
<blockquote><p><strong>HkIsCrazY</strong> <code>(Wed 21 Jun 2023 14:57)</code> - <em>Upvotes: 4</em></p><p>seems correct!</p></blockquote>

</details>

---

[<< Previous Question](question_389.md) | [Home](../index.md) | [Next Question >>](question_391.md)
