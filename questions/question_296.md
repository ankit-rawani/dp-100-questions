# Question 296

You are developing a two-step Azure Machine Learning pipeline by using the Azure Machine Learning SDK for Python.

You need to register the output of the pipeline as a new version of a named dataset after the run has been completed.

What should you implement?

- A.the as_input method of the OutputDatasetConfig class
- B.the register_on_complete method of the OutputDatasetConfig class
- C.the as_mount method of the DatasetConsumptionConfig class
- D.the as_download method of the DatasetConsumptionConfig class

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 08:09)</code> - <em>Upvotes: 1</em></p><p>as_input is for next step in the pipeline; register_on_complete is for dataset register after the pipeline run ends</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Sat 23 Nov 2024 05:11)</code> - <em>Upvotes: 1</em></p><p>B.
reference:
https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.data.output_dataset_config.outputdatasetconfig?view=azure-ml-py#methods</p></blockquote>
<blockquote><p><strong>Chishti</strong> <code>(Sat 06 Jul 2024 11:51)</code> - <em>Upvotes: 1</em></p><p>Yeah Option B is correct.</p></blockquote>
<blockquote><p><strong>bobML</strong> <code>(Sun 10 Mar 2024 16:14)</code> - <em>Upvotes: 2</em></p><p>B
To register the output of an Azure Machine Learning pipeline as a new version of a named dataset after the run has been completed, you should implement option B:

B. the register_on_complete method of the OutputDatasetConfig class

The register_on_complete method allows you to register the output dataset as a new version of an existing named dataset after the pipeline run is completed. This is the appropriate method for creating a new version of a named dataset in Azure Machine Learning.</p></blockquote>

<blockquote><p><strong>BR_CS</strong> <code>(Wed 21 Feb 2024 10:53)</code> - <em>Upvotes: 1</em></p><p>Seriously, is anyone checking this answers? There are so many obvious mistakes.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 24 Jan 2024 21:40)</code> - <em>Upvotes: 1</em></p><p>B https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.data.output_dataset_config.outputdatasetconfig?view=azure-ml-py#azureml-data-output-dataset-config-outputdatasetconfig-register-on-complete</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Fri 01 Dec 2023 18:18)</code> - <em>Upvotes: 1</em></p><p># Create an OutputFileDatasetConfig
output = OutputFileDatasetConfig(destination=(datastore, &#x27;output/{run-id}&#x27;))

# Register the output as a new version of a named Dataset after the run has completed

output.register_on_complete(&#x27;my-dataset&#x27;)

# Create a ScriptRunConfig

script_run_config = ScriptRunConfig(&#x27;.&#x27;, &#x27;train.py&#x27;, arguments=[output])</p></blockquote>

<blockquote><p><strong>Jin_22</strong> <code>(Sat 23 Sep 2023 18:43)</code> - <em>Upvotes: 3</em></p><p>B. The register_on_complete method of the OutputDatasetConfig class should be implemented to register the output of the pipeline as a new version of a named dataset after the run has been completed.</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Thu 21 Sep 2023 13:10)</code> - <em>Upvotes: 3</em></p><p>Correct answer is B: https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.data.output_dataset_config.outputdatasetconfig?view=azure-ml-py#azureml-data-output-dataset-config-outputdatasetconfig-register-on-complete</p></blockquote>

</details>

---

[<< Previous Question](question_295.md) | [Home](../index.md) | [Next Question >>](question_297.md)
