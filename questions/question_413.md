# Question 413

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You create an Azure Machine Learning pipeline named pipeline1 with two steps that contain Python scripts. Data processed by the first step is passed to the second step.

You must update the content of the downstream data source of pipeline1 and run the pipeline again.

You need to ensure the new run of pipeline1 fully processes the updated content.

Solution: Set the allow_reuse parameter of the PythonScriptStep object of both steps to False.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>PI_Team</strong> <code>(Sun 25 Feb 2024 11:53)</code> - <em>Upvotes: 2</em></p><p>Yes, the solution meets the goal. Setting the allow_reuse parameter of the PythonScriptStep object of both steps to False will ensure that the new run of pipeline1 fully processes the updated content. When the allow_reuse parameter is set to False, the step will always be re-run, even if its inputs and parameters have not changed. This means that when you update the content of the downstream data source of pipeline1 and run the pipeline again, both steps will be re-run and the updated content will be fully processed.

SaM</p></blockquote>

<blockquote><p><strong>BR_CS</strong> <code>(Wed 21 Feb 2024 13:42)</code> - <em>Upvotes: 1</em></p><p>Actually I don&#x27;t get the question as they talk about changing data downstream of pipeline1 in which case there is no reason at all to run the pipeline again. But still, If ensuring that the pipeline runs is the aim, &quot;yes&quot; is the correct answer.</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Mon 04 Dec 2023 12:57)</code> - <em>Upvotes: 1</em></p><p>ChatGPT-3.5

The correct solution in this case would be to set the allow_reuse parameter of the PythonScriptStep object of both steps to False.

Setting allow_reuse to False ensures that the outputs of the previous run of each step are not reused in subsequent runs. This is important because, in this scenario, the content of the downstream data source has been updated. If allow_reuse is set to True, the pipeline run would reuse the outputs of the previous run, which means it would not fully process the updated content.

By setting allow_reuse to False, the pipeline ensures that each step is re-executed, starting from the updated data source. This guarantees that the new run of pipeline1 fully processes the updated content and incorporates the changes made to the downstream data source.</p></blockquote>

<blockquote><p><strong>snegnik</strong> <code>(Mon 04 Dec 2023 13:05)</code> - <em>Upvotes: 4</em></p><p>But I think it is not true. the regenerate_outputs solution focuses on the overall pipeline run and regenerating all outputs, while the allow_reuse solution focuses on individual steps and ensuring their outputs are not reused. In the context of updating the downstream data source and running the pipeline again to fully process the updated content, setting regenerate_outputs to True at the pipeline run submission level would be the appropriate solution. Thuse, the answer is NO.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Fri 06 Sep 2024 01:51)</code> - <em>Upvotes: 1</em></p><p>Actually the job of both the parameters are same but are used in different object. allow_reuse is used in PythonScriptStep and regenerate_output is used in Pipeline.submit</p></blockquote>
<blockquote><p><strong>karu_m</strong> <code>(Thu 16 Nov 2023 09:18)</code> - <em>Upvotes: 4</em></p><p>Should be yes</p></blockquote>
<blockquote><p><strong>sap_dg</strong> <code>(Fri 29 Sep 2023 03:07)</code> - <em>Upvotes: 2</em></p><p>It should be Yes</p></blockquote>
<blockquote><p><strong>esimsek</strong> <code>(Wed 27 Sep 2023 10:59)</code> - <em>Upvotes: 1</em></p><p>Should not it be yes?</p></blockquote>

</details>

---

[<< Previous Question](question_412.md) | [Home](../index.md) | [Next Question >>](question_414.md)
