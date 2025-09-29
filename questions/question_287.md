# Question 287

HOTSPOT -

You use an Azure Machine Learning workspace.

You create the following Python code:

![Question Image](images/q287_q_0031300001.png)

For each of the following statements, select Yes if the statement is true. Otherwise, select No.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q287_q_0031300002.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q287_ans_0_0031400001.png" alt="Answer Image"><br>
<p>Box 1: No -</p>
<p>Environment is a required parameter. The environment to use for the run. If no environment is specified, azureml.core.runconfig.DEFAULT_CPU_IMAGE will be used as the Docker image for the run.</p>
<p>The following example shows how to instantiate a new environment. from azureml.core import Environment myenv = Environment(name=&quot;myenv&quot;)</p>
<p>Box 2: Yes -</p>
<p>Parameter compute_target: The compute target where training will happen. This can either be a ComputeTarget object, the name of an existing ComputeTarget, or the string &quot;local&quot;. If no compute target is specified, your local machine will be used.</p>
<p>Box 3: Yes -</p>
<p>Parameter source_directory. A local directory containing code files needed for a run.</p>
<p>Parameter script. The file path relative to the source_directory of the script to be run.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.scriptrunconfig https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment.environment</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>445f1bd</strong> <code>(Fri 25 Jul 2025 01:34)</code> - <em>Upvotes: 1</em></p><p>From https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.scriptrunconfig?view=azure-ml-py.....

compute_target

AbstractComputeTarget or str
The compute target where training will happen. This can either be a ComputeTarget object, the name of an existing ComputeTarget, or the string &quot;local&quot;. If no compute target is specified, your local machine will be used.</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Wed 30 Oct 2024 10:02)</code> - <em>Upvotes: 2</em></p><p>how do we know it&#x27;s local compute?</p></blockquote>
<blockquote><p><strong>a6cb3b0</strong> <code>(Fri 22 Mar 2024 17:25)</code> - <em>Upvotes: 2</em></p><p>No-Yes-Yes
for 2nd:
The compute target where training will happen. This can either be a ComputeTarget object, the name of an existing ComputeTarget, or the string &quot;local&quot;. If no compute target is specified, your local machine will be used.
see: https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.scriptrunconfig?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>haby</strong> <code>(Mon 18 Dec 2023 18:15)</code> - <em>Upvotes: 2</em></p><p>No - Yes - Yes; 
for 2nd , compute_target = None by default, which means if not setting, run on local compute by default</p></blockquote>
<blockquote><p><strong>ferren</strong> <code>(Mon 11 Sep 2023 00:48)</code> - <em>Upvotes: 1</em></p><p>type in chat gpt and answer is No No Yes</p></blockquote>
<blockquote><p><strong>Batman160591</strong> <code>(Mon 26 Jun 2023 21:42)</code> - <em>Upvotes: 3</em></p><p>The default environment will be created: No
    The training script will run on local compute: No
    A script run configuration runs a training script named train.py located in the directory defined by the project_folder variable: Yes</p></blockquote>
<blockquote><p><strong>giusecozza</strong> <code>(Wed 07 Sep 2022 13:10)</code> - <em>Upvotes: 3</em></p><p>I&#x27;m skeptic about Box3: &quot;A ScriptRunConfig object is used to configure the information necessary for submitting a training run as part of an Experiment&quot;...so it should &quot;configure&quot;, not &quot;run&quot;...isn&#x27;t it?

https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.scriptrunconfig?view=azure-ml-py</p></blockquote>

</details>

---

[<< Previous Question](question_286.md) | [Home](/index.md) | [Next Question >>](question_288.md)
