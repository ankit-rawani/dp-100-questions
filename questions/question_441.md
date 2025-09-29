# Question 441

You build a data pipeline in an Azure Machine Learning workspace by using the Azure Machine Learning SDK for Python.

You need to run a Python script as a pipeline step.

Which two classes could you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- A.PythonScriptStep
- B.AutoMLStep
- C.CommandStep
- D.StepRun

<details>
  <summary>Show Suggested Answer</summary>

<strong>AC</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 10:43)</code> - <em>Upvotes: 1</em></p><p>AC is the correct answer.</p></blockquote>
<blockquote><p><strong>Techlover74</strong> <code>(Mon 19 Feb 2024 20:14)</code> - <em>Upvotes: 1</em></p><p>AC is the correct answer. StepRun is used for the submitted pipeline.</p></blockquote>
<blockquote><p><strong>zishankamal</strong> <code>(Sat 17 Feb 2024 02:18)</code> - <em>Upvotes: 1</em></p><p>A and C
python_script_step: Contains functionality to create an Azure ML Pipeline step that runs Python script.
command_step: Contains functionality to create an Azure ML Pipeline step that runs commands.
from azureml.pipeline.steps import CommandStep
trainStep = CommandStep(name=&#x27;train step&#x27;,
                    command=&#x27;python train.py arg1 arg2&#x27;,
                    source_directory=project_folder,
                    compute_target=compute_target)</p></blockquote>
<blockquote><p><strong>ferren</strong> <code>(Wed 23 Aug 2023 05:27)</code> - <em>Upvotes: 1</em></p><p>chatgpt says AC</p></blockquote>
<blockquote><p><strong>BR_CS</strong> <code>(Thu 17 Aug 2023 14:19)</code> - <em>Upvotes: 3</em></p><p>A, C

python_script_step , CommandStep</p></blockquote>

<blockquote><p><strong>phdykd</strong> <code>(Thu 27 Jul 2023 19:37)</code> - <em>Upvotes: 2</em></p><p>A, C

python_script_step , CommandStep</p></blockquote>

<blockquote><p><strong>Michael_AUT</strong> <code>(Tue 25 Jul 2023 19:18)</code> - <em>Upvotes: 1</em></p><p>AB
python_script_step	Contains functionality to create an Azure ML Pipeline step that runs Python script.
automl_step	Contains functionality for adding and managing an automated ML pipeline step in Azure Machine Learning.</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 07 Jul 2023 20:22)</code> - <em>Upvotes: 1</em></p><p>Ans. AB
https://learn.microsoft.com/en-us/python/api/azureml-pipeline-steps/?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>vv_bb</strong> <code>(Sat 25 Nov 2023 19:25)</code> - <em>Upvotes: 2</em></p><p>Nope, the answer is A + C
While B = AutoMLStep is a valid option for the pipeline step, it doesn&#x27;t solve the task of &quot;...You need to run a Python script as a pipeline step....&quot;</p></blockquote>

</details>

---

[<< Previous Question](question_440.md) | [Home](../index.md) | [Next Question >>](question_442.md)
