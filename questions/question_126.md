# Question 126

You use the Azure Machine Learning SDK for Python v1 and notebooks to train a model. You create a compute target, an environment, and a training script by using Python code.

You need to prepare information to submit a training run.

Which class should you use?

- A.ScriptRun
- B.ScriptRunConfig
- C.RunConfiguration
- D.Run

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 01 Dec 2024 10:32)</code> - <em>Upvotes: 1</em></p><p># Define the script run configuration
src = ScriptRunConfig(source_directory=&#x27;.&#x27;,
                      script=&#x27;train.py&#x27;,
                      compute_target=compute_target,
                      environment=env)</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Thu 25 Jan 2024 12:17)</code> - <em>Upvotes: 2</em></p><p>from azureml.core import ScriptRunConfig

# Create a ScriptRunConfig object

run_config = ScriptRunConfig(
name=&quot;my-training-run&quot;,
script=&quot;train.py&quot;,
compute_target=&quot;my-compute-target&quot;,
environment=&quot;my-environment&quot;,
)

# Submit the run

run = run_config.submit()

# Wait for the run to complete

run.wait_for_completion()</p></blockquote>

<blockquote><p><strong>krishna1818</strong> <code>(Wed 29 Nov 2023 10:56)</code> - <em>Upvotes: 1</em></p><p>ScriptRunConfig()</p></blockquote>
<blockquote><p><strong>Dp_100_11</strong> <code>(Fri 24 Nov 2023 14:18)</code> - <em>Upvotes: 2</em></p><p>The correct class to use for preparing information to submit a training run in the given scenario is B. ScriptRunConfig.

from azureml.core import ScriptRunConfig, Environment, Workspace

# Create a ScriptRunConfig

script_run_config = ScriptRunConfig(source_directory=&#x27;path/to/scripts&#x27;,
script=&#x27;train.py&#x27;,
compute_target=&#x27;my_compute_target&#x27;,
environment=&#x27;my_environment&#x27;)

# Submit the training run

run = Experiment(workspace=Workspace.get(&#x27;my_workspace&#x27;), name=&#x27;my_experiment&#x27;).submit(script_run_config)</p></blockquote>

<blockquote><p><strong>ajay0011</strong> <code>(Sun 22 Oct 2023 04:03)</code> - <em>Upvotes: 3</em></p><p>To submit a training run in Azure Machine Learning using Python code, you should create a ScriptRunConfig object. This class defines the configuration information needed for running a training script on a compute target. The ScriptRunConfig class allows you to specify the compute target, the environment, the training script, and any script arguments or data references needed by the script.</p></blockquote>

</details>

---

[<< Previous Question](question_125.md) | [Home](../index.md) | [Next Question >>](question_127.md)
