# Question 423

HOTSPOT

-

You create an Azure Machine learning workspace. The workspace contains a folder named src. The folder contains a Python script named script1.py.

You use the Azure Machine Learning Python SDK v2 to create a control script. You must use the control script to run script1.py as part of a training job.

You need to complete the section of script that defines the job parameters.

How should you complete the script? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q423_q_image526.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q423_ans_0_image527.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>MonayiYC</strong> <code>(Fri 21 Jun 2024 02:48)</code> - <em>Upvotes: 3</em></p><p>from azure.ai.ml import command

# configure job
job = command(
    code=&quot;./src&quot;,
    command=&quot;python train.py --training_data diabetes.csv&quot;,
    environment=&quot;AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest&quot;,
    compute=&quot;aml-cluster&quot;,
    display_name=&quot;train-model&quot;,
    experiment_name=&quot;train-classification-model&quot;
    )</p></blockquote>
<blockquote><p><strong>vv_bb</strong> <code>(Sat 25 May 2024 11:08)</code> - <em>Upvotes: 2</em></p><p>Command + Code

https://learn.microsoft.com/en-us/training/modules/run-training-script-command-job-azure-machine-learning/3-run-script-command-job</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Sun 07 Jan 2024 19:08)</code> - <em>Upvotes: 2</em></p><p>Answers: command and path

my_job_inputs = {
    &quot;input_data&quot;: Input(
            type=AssetTypes.MLTABLE,
            path=filedataset_asset,
            mode=InputOutputModes.EVAL_MOUNT</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Sun 07 Jan 2024 19:09)</code> - <em>Upvotes: 1</em></p><p>my_job_inputs = {
    &quot;input_data&quot;: Input(
            type=AssetTypes.MLTABLE,
            path=filedataset_asset,
            mode=InputOutputModes.EVAL_MOUNT
    )
}

job = command(
    code=&quot;./src&quot;,  # Local path where the code is stored
    command=&quot;ls ${{inputs.input_data}}&quot;,
    inputs=my_job_inputs,
    environment=&quot;&lt;environment_name&gt;:&lt;version&gt;&quot;,
    compute=&quot;cpu-cluster&quot;,</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Sun 07 Jan 2024 19:10)</code> - <em>Upvotes: 4</em></p><p>Sorry, correct answer: command and code
job = command(
    code=&quot;./src&quot;,  # Local path where the code is stored
    command=&quot;ls ${{inputs.input_data}}&quot;,
    inputs=my_job_inputs,
    environment=&quot;&lt;environment_name&gt;:&lt;version&gt;&quot;,
    compute=&quot;cpu-cluster&quot;,</p></blockquote>

</details>

---

[<< Previous Question](question_422.md) | [Home](/index.md) | [Next Question >>](question_424.md)
