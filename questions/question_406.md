# Question 406

You use the Azure Machine Learning designer to create and run a training pipeline.

The pipeline must be run every night to inference predictions from a large volume of files. The folder where the files will be stored is defined as a dataset.

You need to publish the pipeline as a REST service that can be used for the nightly inferencing run.

What should you do?

* A.Create a batch inference pipeline
* B.Set the compute target for the pipeline to an inference cluster
* C.Create a real-time inference pipeline
* D.Clone the pipeline

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>
<p>Azure Machine Learning Batch Inference targets large inference jobs that are not time-sensitive. Batch Inference provides cost-effective inference compute scaling, with unparalleled throughput for asynchronous applications. It is optimized for high-throughput, fire-and-forget inference over large collections of data.</p>
<p>You can submit a batch inference job by pipeline_run, or through REST calls with a published pipeline.</p>
<p>Reference:</p>
<p>https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/parallel-run/README.md</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>BTAB</strong> <code>(Sun 14 Jul 2024 10:58)</code> - <em>Upvotes: 1</em></p><p>Correct</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Wed 24 Apr 2024 06:04)</code> - <em>Upvotes: 2</em></p><p>Correct.</p></blockquote>

</details>

---

[<< Previous Question](question_405.md) | [Home](/index.md) | [Next Question >>](question_407.md)
