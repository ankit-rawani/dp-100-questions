# Question 373

You create a batch inference pipeline by using the Azure ML SDK. You run the pipeline by using the following code: from azureml.pipeline.core import Pipeline from azureml.core.experiment import Experiment pipeline = Pipeline(workspace=ws, steps=[parallelrun_step]) pipeline_run = Experiment(ws, 'batch_pipeline').submit(pipeline)

You need to monitor the progress of the pipeline execution.

What are two possible ways to achieve this goal? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- A.Run the following code in a notebook:
- B.Use the Inference Clusters tab in Machine Learning Studio.
- C.Use the Activity log in the Azure portal for the Machine Learning workspace.
- D.Run the following code in a notebook:
- E.Run the following code and monitor the console output from the PipelineRun object:

<details>
  <summary>Show Suggested Answer</summary>

<strong>DE</strong><br>

<p>A batch inference job can take a long time to finish. This example monitors progress by using a Jupyter widget. You can also manage the job&#x27;s progress by using:</p>
<p>✑ Azure Machine Learning Studio.</p>
<p>✑ Console output from the PipelineRun object.</p>
<p>from azureml.widgets import RunDetails</p>
<p>RunDetails(pipeline_run).show()</p>
<p>pipeline_run.wait_for_completion(show_output=True)</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-parallel-run-step#monitor-the-parallel-run-job</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Arend78</strong> <code>(Wed 19 Jun 2024 09:41)</code> - <em>Upvotes: 9</em></p><p>After a lot of searching I have found examples of both D and E.
If I understand correctly, both types of logging point to the Portal with a link, where the run details can be inspected

D: from azureml.widgets import RunDetails  
RunDetails(pipeline_run).show()

https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/classification-credit-card-fraud/auto-ml-classification-credit-card-fraud.ipynb

E: pipeline = Pipeline(workspace=ws, steps=[batch_score_step])
pipeline_run = Experiment(ws, &quot;Tutorial-Batch-Scoring&quot;).submit(pipeline)

# This will output information of the pipeline run, including the link to the details page of **portal**. Wait the run for completion and show output log to console

pipeline_run.wait_for_completion(show_output=True)
https://github.com/Azure/MachineLearningNotebooks/blob/master/tutorials/machine-learning-pipelines-advanced/tutorial-pipeline-batch-scoring-classification.ipynb</p></blockquote>

<blockquote><p><strong>Arend78</strong> <code>(Wed 19 Jun 2024 09:51)</code> - <em>Upvotes: 2</em></p><p>The solution under D uses a Widget in a Notebook to track the Pipeline progress</p></blockquote>
<blockquote><p><strong>Arend78</strong> <code>(Wed 19 Jun 2024 10:07)</code> - <em>Upvotes: 1</em></p><p>https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/machine-learning-pipelines/parallel-run show the use of both answers together</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Sun 21 Apr 2024 07:35)</code> - <em>Upvotes: 1</em></p><p>E is correct.
https://learn.microsoft.com/zh-tw/python/api/azureml-pipeline-core/azureml.pipeline.core.run.pipelinerun?view=azure-ml-py

D can show status but seems for training model.
Question request is batch inference pipleline.
But in doc &quot;A widget is asynchronous and provides updates until training finishes.&quot;
https://learn.microsoft.com/en-us/python/api/azureml-widgets/azureml.widgets.rundetails?view=azure-ml-py</p></blockquote>

<blockquote><p><strong>BTAB</strong> <code>(Fri 12 Jul 2024 00:47)</code> - <em>Upvotes: 1</em></p><p>E &amp; D correct.  Since it is a batch inference model D will work.</p></blockquote>

</details>

---

[<< Previous Question](question_372.md) | [Home](../index.md) | [Next Question >>](question_374.md)
