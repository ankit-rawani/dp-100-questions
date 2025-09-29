# Question 428

You use the Azure Machine Learning SDK v2 for Python and notebooks to train a model. You use Python code to create a compute target, an environment, and a training script.

You need to prepare information to submit a training job.

Which class should you use?

- A.MLClient
- B.BuildContext
- C.EndpointConnection
- D.command

<details>
  <summary>Show Suggested Answer</summary>

<strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 10:20)</code> - <em>Upvotes: 1</em></p><p>D is correct</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Wed 07 Feb 2024 03:57)</code> - <em>Upvotes: 1</em></p><p>i overlooked word &quot;preparing&quot; and thought to submit.  Anyway after the preparation, to submit the for job run, the required class in ml_client. 
correct answer is command, which is class to prepare or configure a run.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 27 Jul 2023 18:50)</code> - <em>Upvotes: 2</em></p><p>command.

To run this script, you&#x27;ll use a command that executes main.py Python script located under ./sdk/python/jobs/single-step/lightgbm/iris/src/. The command will be run by submitting it as a job to Azure ML.</p></blockquote>

<blockquote><p><strong>damaldon</strong> <code>(Fri 07 Jul 2023 18:26)</code> - <em>Upvotes: 2</em></p><p>Correct.
#import required libraries
from azure.ai.ml import MLClient, command
from azure.ai.ml.entities import Environment
from azure.identity import DefaultAzureCredential

#connect to the workspace
ml_client = MLClient.from_config(DefaultAzureCredential())

# set up pytorch environment

env = Environment(
image=&quot;mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04&quot;,
conda_file=&quot;pytorch-env.yml&quot;,
name=&quot;pytorch-env&quot;
)

# define the command

command_job = command(
code=&quot;./src&quot;,
command=&quot;train.py&quot;,
environment=env,
compute=&quot;cpu-cluster&quot;,
)

returned_job = ml_client.jobs.create_or_update(command_job)
returned_job</p></blockquote>

</details>

---

[<< Previous Question](question_427.md) | [Home](../index.md) | [Next Question >>](question_429.md)
