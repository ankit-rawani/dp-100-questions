# Question 303

You use the Azure Machine Learning Python SDK to create a batch inference pipeline.

You must publish the batch inference pipeline so that business groups in your organization can use the pipeline. Each business group must be able to specify a different location for the data that the pipeline submits to the model for scoring.

You need to publish the pipeline.

What should you do?

- A.Create multiple endpoints for the published pipeline service and have each business group submit jobs to its own endpoint.
- B.Define a PipelineParameter object for the pipeline and use it to specify the business group-specific input dataset for each pipeline run.
- C.Define a OutputFileDatasetConfig object for the pipeline and use the object to specify the business group-specific input dataset for each pipeline run.
- D.Have each business group run the pipeline on local compute and use a local file for the input data.

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 09:02)</code> - <em>Upvotes: 1</em></p><p>Create multiple endpoints: Creating multiple endpoints for each business group is not efficient or scalable. It also complicates the management and maintenance of the pipeline.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 25 Jan 2024 03:02)</code> - <em>Upvotes: 1</em></p><p>B PipelineParameter</p></blockquote>
<blockquote><p><strong>fqc</strong> <code>(Mon 20 Nov 2023 11:47)</code> - <em>Upvotes: 2</em></p><p>A PipelineParameter object can be used to specify a parameter that can be passed to the pipeline when it is run. In this case, the parameter can be used to specify the location of the input dataset for the business group. This allows each business group to specify a different location for the data that the pipeline submits to the model for scoring.</p></blockquote>
<blockquote><p><strong>sap_dg</strong> <code>(Wed 27 Sep 2023 17:37)</code> - <em>Upvotes: 1</em></p><p>Correct!</p></blockquote>

</details>

---

[<< Previous Question](question_302.md) | [Home](../index.md) | [Next Question >>](question_304.md)
