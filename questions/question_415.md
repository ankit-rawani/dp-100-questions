# Question 415

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You create an Azure Machine Learning pipeline named pipeline1 with two steps that contain Python scripts. Data processed by the first step is passed to the second step.

You must update the content of the downstream data source of pipeline1 and run the pipeline again.

You need to ensure the new run of pipeline1 fully processes the updated content.

Solution: Change the value of the compute_target parameter of the PythonScriptStep object in the two steps.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>445f1bd</strong> <code>(Sun 27 Jul 2025 23:06)</code> - <em>Upvotes: 1</em></p><p>Changing the compute_target (the cluster or compute the step runs on) creates a new hash for the step configuration. This breaks the step cache, causing Azure ML to rerun the step even if inputs haven’t changed, thus ensuring your steps re-execute and process the updated content.


Yes, this will work.
It’s a bit of a workaround, but it will ensure steps rerun and do not use cached results.</p></blockquote>
<blockquote><p><strong>sap_dg</strong> <code>(Sun 29 Sep 2024 03:11)</code> - <em>Upvotes: 2</em></p><p>Correct</p></blockquote>

</details>

---

[<< Previous Question](question_414.md) | [Home](/index.md) | [Next Question >>](question_416.md)
