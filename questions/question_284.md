# Question 284

You use the following code to define the steps for a pipeline: from azureml.core import Workspace, Experiment, Run from azureml.pipeline.core import Pipeline from azureml.pipeline.steps import PythonScriptStep ws = Workspace.from_config()

. . .

step1 = PythonScriptStep(name="step1", ...)

step2 = PythonScriptsStep(name="step2", ...)

pipeline_steps = [step1, step2]

You need to add code to run the steps.

Which two code segments can you use to achieve this goal? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

* A.experiment = Experiment(workspace=ws, name='pipeline-experiment') run = experiment.submit(config=pipeline_steps)
* B.run = Run(pipeline_steps)
* C.pipeline = Pipeline(workspace=ws, steps=pipeline_steps) experiment = Experiment(workspace=ws, name='pipeline-experiment') run = experiment.submit(pipeline)
* D.pipeline = Pipeline(workspace=ws, steps=pipeline_steps) run = pipeline.submit(experiment_name='pipeline-experiment')

<details>
  <summary>Show Suggested Answer</summary>

  <strong>CD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>pancman</strong> <code>(Tue 11 Oct 2022 19:18)</code> - <em>Upvotes: 20</em></p><p>The given answer of C &amp; D is correct. Some people commented that they think it should be A &amp; C. Don&#x27;t let this confuse you as answer A is certainly wrong. You can&#x27;t use [step1, step2] as a config to experiment submit, as given in the answer A. You need to create a pipeline object and provide it as the config.
Refer to experiment class for proof:  https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment(class)?view=azure-ml-py#azureml-core-experiment-submit</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Fri 16 Aug 2024 08:16)</code> - <em>Upvotes: 1</em></p><p>References: 
https://learn.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.pipeline(class)?view=azure-ml-py

https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment(class)?view=azure-ml-py#azureml-core-experiment-submit</p></blockquote>
<blockquote><p><strong>azurelearner666</strong> <code>(Fri 14 Oct 2022 07:58)</code> - <em>Upvotes: 2</em></p><p>Thanks for clarifying!</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Mon 06 Jan 2025 01:57)</code> - <em>Upvotes: 1</em></p><p>Options C and D</p></blockquote>
<blockquote><p><strong>haby</strong> <code>(Tue 18 Jun 2024 14:12)</code> - <em>Upvotes: 1</em></p><p>C for me. 
For A, you can&#x27;t submit [step1, step2] parameters only; For D, you can&#x27;t submit a string name only.  Correct way is to submit Pipeline Obj or RunConfig Obj, not a list or string.</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Thu 06 Jun 2024 09:02)</code> - <em>Upvotes: 1</em></p><p>Only option C is correct

Options A and B are incorrect because they either submit the steps directly to the experiment without creating a Pipeline object (Option A), or try to create a Run object directly from the steps without creating a Pipeline or Experiment object (Option B). Both of these approaches will result in errors.

Option D correctly creates a Pipeline object and then submits the pipeline with the experiment name. However, please note that the submit method of the Pipeline class does not take an experiment_name argument. Instead, it takes an Experiment object. So, the correct code should be:

pipeline = Pipeline(workspace=ws, steps=pipeline_steps)
experiment = Experiment(workspace=ws, name=&#x27;pipeline-experiment&#x27;)
run = pipeline.submit(experiment)</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sat 20 Apr 2024 04:51)</code> - <em>Upvotes: 1</em></p><p>Constructor azurelm.pipeline.core.pipeline.Pipeline() 

https://learn.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.pipeline.pipeline?view=azure-ml-py#constructor

Pipeline(workspace, steps, ...)</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Sat 23 Sep 2023 14:03)</code> - <em>Upvotes: 1</em></p><p>CD is correct</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Wed 23 Aug 2023 20:48)</code> - <em>Upvotes: 1</em></p><p>The correct command for pipeline run is as below
experiment.submit()

Only A and C has this command.
D has command pipeline.submit(), which is incorrect</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Wed 23 Aug 2023 21:00)</code> - <em>Upvotes: 1</em></p><p>An Azure Machine Learning experiment represent the collection of trials used to validate a user&#x27;s hypothesis. In Azure Machine Learning, an experiment is represented by the Experiment class and a trial is represented by the Run class.

An Azure Machine Learning pipeline is an independently executable workflow of a complete machine learning task.

In an experiment, we execute a pipeline, and this is why we use experiment.submit(pipeline)

It is not that in a pipeline, we execute an experiment, and that is why pipeline.submit(experiment) is wrong</p></blockquote>
<blockquote><p><strong>Arend78</strong> <code>(Fri 16 Jun 2023 12:27)</code> - <em>Upvotes: 1</em></p><p>I also think it&#x27;s A &amp; C: In the Azure documentations, I have only found examples of 
run = experiment.submit(pipeline) 
and no examples of 
run = pipeline.submit(experiment_name=&#x27;pipeline-experiment&#x27;)

Please reply if you don&#x27;t agree</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Wed 23 Aug 2023 20:41)</code> - <em>Upvotes: 1</em></p><p>I think so too. Also there is no definition of the experiment &#x27;pipeline-experiment&#x27; in the code</p></blockquote>
<blockquote><p><strong>zehraoneexam</strong> <code>(Mon 19 Sep 2022 07:43)</code> - <em>Upvotes: 2</em></p><p>correct answer.</p></blockquote>
<blockquote><p><strong>Sjefen</strong> <code>(Sat 17 Sep 2022 11:23)</code> - <em>Upvotes: 1</em></p><p>I think A &amp; C as well</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Mon 12 Sep 2022 11:03)</code> - <em>Upvotes: 1</em></p><p>C and are correct. As per below. A is not correct because the submit() expects a Pipeline object. not a list. 
https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.experiment.experiment?view=azure-ml-py#azureml-core-experiment-experiment-submit</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Fri 29 Jul 2022 20:48)</code> - <em>Upvotes: 2</em></p><p>sorry i think it should be A and C</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Tue 19 Jul 2022 15:36)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>

</details>

---

[<< Previous Question](question_283.md) | [Home](/index.md) | [Next Question >>](question_285.md)
