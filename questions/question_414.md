# Question 414

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You create an Azure Machine Learning pipeline named pipeline1 with two steps that contain Python scripts. Data processed by the first step is passed to the second step.

You must update the content of the downstream data source of pipeline1 and run the pipeline again.

You need to ensure the new run of pipeline1 fully processes the updated content.

Solution: Set the regenerate_outputs parameter of the pipeline1 experiment’s run submit method to True.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>VeraKo</strong> <code>(Wed 10 Jul 2024 11:53)</code> - <em>Upvotes: 1</em></p><p>The answer is Yes
&quot;regenerate_outputs: Whether to force regeneration of all step outputs and disallow data reuse for this run, default is False.&quot;

https://learn.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.pipeline.pipeline?view=azure-ml-py&amp;viewFallbackFrom=azure-ml-pyregenerate_outputs</p></blockquote>

<blockquote><p><strong>Piddi</strong> <code>(Sat 29 Apr 2023 20:51)</code> - <em>Upvotes: 2</em></p><p>Answer is Correct:
https://learn.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.pipeline.pipeline?view=azure-ml-py
regenerate_outputs
bool
default value: False
Indicates whether to force regeneration of all step outputs and disallow data reuse for this run. If False, this run may reuse results from previous runs and subsequent runs may reuse the results of this run.</p></blockquote>
<blockquote><p><strong>gogo12</strong> <code>(Fri 31 Mar 2023 17:47)</code> - <em>Upvotes: 2</em></p><p>this should be no</p></blockquote>
<blockquote><p><strong>Piddi</strong> <code>(Sat 29 Apr 2023 20:52)</code> - <em>Upvotes: 1</em></p><p>The Answers is A.</p></blockquote>
<blockquote><p><strong>sap_dg</strong> <code>(Wed 29 Mar 2023 03:08)</code> - <em>Upvotes: 1</em></p><p>Correct</p></blockquote>

</details>

---

[<< Previous Question](question_413.md) | [Home](../index.md) | [Next Question >>](question_415.md)
