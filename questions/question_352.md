# Question 352

HOTSPOT

-

You create an Azure Machine Learning workspace.

You are developing a Python SDK v2 noteboot to perform custom model training in the workspace. The notebook code imports all required packages.

You need to complete the Python SDK v2 code to include a training script, environment, and compute information.

How should you complete the code? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](../images/q352_q_image562.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q352_ans_0_image563.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>apz333</strong> <code>(Mon 19 Aug 2024 11:27)</code> - <em>Upvotes: 2</em></p><p>Shouldn&#x27;t box 2 be &quot;component&quot;, I don&#x27;t think create_or_update accepts anything like &quot;command&quot;:
https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.mlclient?view=azure-python#azure-ai-ml-mlclient-create-or-update</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Tue 03 Sep 2024 18:14)</code> - <em>Upvotes: 2</em></p><p>You are correct
create_or_update(entity: T, **kwargs) -&gt; T
entity
Union[Job , Model, Environment, Component , Datastore]</p></blockquote>
<blockquote><p><strong>tamagochi13</strong> <code>(Fri 13 Sep 2024 01:19)</code> - <em>Upvotes: 4</em></p><p>component does not have experiment_name parameter. also here is example where create_or_update used for command: 
https://learn.microsoft.com/en-us/training/modules/run-training-script-command-job-azure-machine-learning/3-run-script-command-job</p></blockquote>

</details>

---

[<< Previous Question](question_351.md) | [Home](../index.md) | [Next Question >>](question_353.md)
