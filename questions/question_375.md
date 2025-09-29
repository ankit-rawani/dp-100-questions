# Question 375

You train and register a model in your Azure Machine Learning workspace.

You must publish a pipeline that enables client applications to use the model for batch inferencing. You must use a pipeline with a single ParallelRunStep step that runs a Python inferencing script to get predictions from the input data.

You need to create the inferencing script for the ParallelRunStep pipeline step.

Which two functions should you include? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

* A.run(mini_batch)
* B.main()
* C.batch()
* D.init()
* E.score(mini_batch)

<details>
  <summary>Show Suggested Answer</summary>

  <strong>AD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>chaudha4</strong> <code>(Wed 04 May 2022 15:47)</code> - <em>Upvotes: 16</em></p><p>https://docs.microsoft.com/en-us/learn/modules/deploy-batch-inference-pipelines-with-azure-machine-learning/2-batch-inference-pipelines</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Tue 07 Jun 2022 12:37)</code> - <em>Upvotes: 11</em></p><p>Question was there in June 2021 Exam</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sat 12 Oct 2024 14:42)</code> - <em>Upvotes: 1</em></p><p>run(mini_batch)

init()

See https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/machine-learning-pipelines/parallel-run</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 27 Jul 2024 01:03)</code> - <em>Upvotes: 1</em></p><p>AD.

Batch inferencing service requires a scoring script to load the model and use it to predict new values. It must include two functions:
init(): Called when the pipeline is initialized.
run(mini_batch): Called for each batch of data to be processed.
Typically, you use the init function to load the model from the model registry, and use the run function to generate predictions from each batch of data and return the results. The following example script shows this pattern:</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Mon 03 Jun 2024 16:23)</code> - <em>Upvotes: 1</em></p><p>In Azure Machine Learning, the inference script is typically a Python script that defines two functions: init() and run(input_data). The init() function is called once when the model is loaded and can be used to perform any initialization tasks, such as loading additional libraries or setting up global variables. The run(input_data) function is called for each input data item and should apply the model to the input data and produce output data</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 22 Feb 2024 18:13)</code> - <em>Upvotes: 1</em></p><p>A and D</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 22 Feb 2024 18:02)</code> - <em>Upvotes: 1</em></p><p>A and E.</p></blockquote>
<blockquote><p><strong>Arend78</strong> <code>(Tue 19 Dec 2023 12:31)</code> - <em>Upvotes: 2</em></p><p>Here&#x27;s and example of a py script including init() and run(mini_batch):
https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/parallel-run/Code/digit_identification.py

This Python file is loaded by example notebook 
https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/parallel-run/file-dataset-image-inference-mnist.ipynb</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sun 18 Jun 2023 01:49)</code> - <em>Upvotes: 3</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 11 Apr 2023 20:10)</code> - <em>Upvotes: 2</em></p><p>Given answer of A&amp;D is correct.</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Mon 13 Mar 2023 02:04)</code> - <em>Upvotes: 1</em></p><p>A and D</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Fri 03 Mar 2023 06:36)</code> - <em>Upvotes: 3</em></p><p>On 03 March 2022</p></blockquote>
<blockquote><p><strong>AI247</strong> <code>(Mon 07 Nov 2022 00:03)</code> - <em>Upvotes: 1</em></p><p>on exam 2021/11/05</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Thu 20 Oct 2022 09:52)</code> - <em>Upvotes: 1</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Mon 11 Jul 2022 14:16)</code> - <em>Upvotes: 8</em></p><p>On exam 2021/7/10</p></blockquote>

</details>

---

[<< Previous Question](question_374.md) | [Home](/index.md) | [Next Question >>](question_376.md)
