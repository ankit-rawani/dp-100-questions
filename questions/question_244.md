# Question 244

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You create a model to forecast weather conditions based on historical data.

You need to create a pipeline that runs a processing script to load data from a datastore and pass the processed data to a machine learning model training script.

Solution: Run the following code:

![Question Image](images/q244_q_0025200001.png)

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>
<p>The two steps are present: process_step and train_step</p>
<p>The training data input is not setup correctly.</p>
<p>Note:</p>
<p>Data used in pipeline can be produced by one step and consumed in another step by providing a PipelineData object as an output of one step and an input of one or more subsequent steps.</p>
<p>PipelineData objects are also used when constructing Pipelines to describe step dependencies. To specify that a step requires the output of another step as input, use a PipelineData object in the constructor of both steps.</p>
<p>For example, the pipeline train step depends on the process_step_output output of the pipeline process step: from azureml.pipeline.core import Pipeline, PipelineData from azureml.pipeline.steps import PythonScriptStep datastore = ws.get_default_datastore() process_step_output = PipelineData(&quot;processed_data&quot;, datastore=datastore) process_step = PythonScriptStep(script_name=&quot;process.py&quot;, arguments=[&quot;--data_for_train&quot;, process_step_output], outputs=[process_step_output], compute_target=aml_compute, source_directory=process_directory) train_step = PythonScriptStep(script_name=&quot;train.py&quot;, arguments=[&quot;--data_for_train&quot;, process_step_output], inputs=[process_step_output], compute_target=aml_compute, source_directory=train_directory) pipeline = Pipeline(workspace=ws, steps=[process_step, train_step])</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.pipelinedata?view=azure-ml-py</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>kty</strong> <code>(Sun 18 Sep 2022 20:03)</code> - <em>Upvotes: 14</em></p><p>datastore = ws.get_default_datastore()
   process_step_output = PipelineData(&quot;processed_data&quot;, datastore=datastore)
   process_step = PythonScriptStep(script_name=&quot;process.py&quot;,
                                   arguments=[&quot;--data_for_train&quot;, process_step_output],
                                   outputs=[process_step_output],
                                   compute_target=aml_compute,
                                   source_directory=process_directory)
   train_step = PythonScriptStep(script_name=&quot;train.py&quot;,
                                 arguments=[&quot;--data_for_train&quot;, process_step_output],
                                 inputs=[process_step_output],
                                 compute_target=aml_compute,
                                 source_directory=train_directory)

   pipeline = Pipeline(workspace=ws, steps=[process_step, train_step])</p></blockquote>
<blockquote><p><strong>ML_Novice</strong> <code>(Wed 17 May 2023 11:15)</code> - <em>Upvotes: 2</em></p><p>how the first preprocess step doesn&#x27;t require any input entry?
thanks for your response</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Fri 29 Nov 2024 15:09)</code> - <em>Upvotes: 1</em></p><p>Where is input for process_step?</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Tue 27 Sep 2022 03:37)</code> - <em>Upvotes: 8</em></p><p>only line#2 should be fixed: data_output = PipelineData(&quot;processed_data&quot;, datastore=datastore)</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Fri 29 Nov 2024 15:20)</code> - <em>Upvotes: 1</em></p><p>I think this should be better
datastore = ws.get_default_datastore()
input_data = PipelineData(&quot;input_data&quot;, datastore=datastore)
process_step_output = PipelineData(&quot;processed_data&quot;, datastore=datastore)
model_output = PipelineData(&quot;trained_model&quot;, datastore=datastore)

process_step = PythonScriptStep(script_name=&quot;process.py&quot;,
arguments=[&quot;--data_for_train&quot;, input_data],
inputs=[input_data],
outputs=[process_step_output],
compute_target=aml_compute,
source_directory=process_directory)

train_step = PythonScriptStep(script_name=&quot;train.py&quot;,
arguments=[&quot;--processed_data&quot;, process_step_output, &quot;--output_model&quot;, model_output],
inputs=[process_step_output],
outputs=[model_output],
compute_target=aml_compute,
source_directory=train_directory)

pipeline = Pipeline(workspace=ws, steps=[process_step, train_step])</p></blockquote>
<blockquote><p><strong>skrjha20</strong> <code>(Thu 30 Mar 2023 09:20)</code> - <em>Upvotes: 2</em></p><p>Code should be as below.
datastore = ws.get_default_datastore()
   process_step_output = PipelineData(&quot;processed_data&quot;, datastore=datastore)
   process_step = PythonScriptStep(script_name=&quot;process.py&quot;,
                                   arguments=[&quot;--data_for_train&quot;, process_step_output],
                                   outputs=[process_step_output],
                                   compute_target=aml_compute,
                                   source_directory=process_directory)
   train_step = PythonScriptStep(script_name=&quot;train.py&quot;,
                                 arguments=[&quot;--data_for_train&quot;, process_step_output],
                                 inputs=[process_step_output],
                                 compute_target=aml_compute,
                                 source_directory=train_directory)

   pipeline = Pipeline(workspace=ws, steps=[process_step, train_step])

However in 2 nd line tried to use read_csv() which is wrong</p></blockquote>
<blockquote><p><strong>SnowCheetah</strong> <code>(Sun 25 Dec 2022 15:37)</code> - <em>Upvotes: 2</em></p><p>https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.pipelinedata?view=azure-ml-py

This one is incorrect since process_step_output is set up incorrectly

in order to set up whole pipeline you should connect all components ( compute node, datastore) set within workspace because when code is running. The resources will generate within your Azure Machine Learning resource which mean reading data locally will not to be able to read when compute note is spawn.</p></blockquote>

</details>

---

[<< Previous Question](question_243.md) | [Home](/index.md) | [Next Question >>](question_245.md)
