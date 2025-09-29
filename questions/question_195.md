# Question 195

You create a batch inference pipeline by using the Azure ML SDK. You configure the pipeline parameters by executing the following code:

![Question Image](../images/q195_q_0016700001.png)

You need to obtain the output from the pipeline execution.

Where will you find the output?

- A.the digit_identification.py script
- B.the debug log
- C.the Activity Log in the Azure portal for the Machine Learning workspace
- D.the Inference Clusters tab in Machine Learning studio
- E.a file named parallel_run_step.txt located in the output folder

<details>
  <summary>Show Suggested Answer</summary>

<strong>E</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Mon 11 Jul 2022 14:01)</code> - <em>Upvotes: 11</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Sat 27 Jul 2024 12:15)</code> - <em>Upvotes: 2</em></p><p>By default, the ParallelRunStep class writes its output to a file named parallel_run_step.txt in the specified output directory. This file contains the concatenated output from all the mini-batches processed by the pipeline. Each line in the file represents the output from a single mini-batch.</p></blockquote>
<blockquote><p><strong>ahson0124</strong> <code>(Thu 15 Feb 2024 13:43)</code> - <em>Upvotes: 4</em></p><p>In exam on 2023-02-15</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Sat 16 Dec 2023 11:35)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/migrate-to-v2-execution-parallel-run-step</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Mon 08 Jan 2024 17:42)</code> - <em>Upvotes: 2</em></p><p>https://learn.microsoft.com/en-us/python/api/azureml-pipeline-steps/azureml.pipeline.steps.parallelrunconfig?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Sat 22 Apr 2023 10:46)</code> - <em>Upvotes: 3</em></p><p>on exam 04/22/2022</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 14 Mar 2023 05:15)</code> - <em>Upvotes: 2</em></p><p>Given answer is correct</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Tue 14 Feb 2023 09:18)</code> - <em>Upvotes: 2</em></p><p>Correct</p></blockquote>

</details>

---

[<< Previous Question](question_194.md) | [Home](../index.md) | [Next Question >>](question_196.md)
