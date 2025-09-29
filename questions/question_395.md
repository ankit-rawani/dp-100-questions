# Question 395

DRAG DROP -

You use Azure Machine Learning to deploy a model as a real-time web service.

You need to create an entry script for the service that ensures that the model is loaded when the service starts and is used to score new data as it is received.

Which functions should you include in the script? To answer, drag the appropriate functions to the correct actions. Each function may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

Select and Place:

![Question Image](../images/q395_q_0039800001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q395_ans_0_0039800002.png" alt="Answer Image"><br>

<p>Box 1: init()</p>
<p>The entry script has only two required functions, init() and run(data). These functions are used to initialize the service at startup and run the model using request data passed in by a client. The rest of the script handles loading and running the model(s).</p>
<p>Box 2: run()</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-existing-model</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Mon 11 Jul 2022 14:21)</code> - <em>Upvotes: 6</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sun 20 Oct 2024 10:26)</code> - <em>Upvotes: 1</em></p><p>init(): Called once at the beginning of the process, so use for any costly or common preparation like loading the model.

run(): Called for each mini batch to perform the scoring.

https://learn.microsoft.com/en-us/training/modules/deploy-model-batch-endpoint/4-deploy-custom-model-batch-endpoint#create-the-scoring-script</p></blockquote>

<blockquote><p><strong>rohanpal636</strong> <code>(Mon 19 Aug 2024 06:54)</code> - <em>Upvotes: 1</em></p><p>Idk keksl</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Fri 03 Mar 2023 07:57)</code> - <em>Upvotes: 4</em></p><p>On Exam: 03 March 2022</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Sat 03 Sep 2022 07:38)</code> - <em>Upvotes: 2</em></p><p>on 2/9/21</p></blockquote>
<blockquote><p><strong>Moshekwa</strong> <code>(Sat 30 Jul 2022 01:00)</code> - <em>Upvotes: 4</em></p><p>Given answer is correct as per link

https://docs.microsoft.com/en-us/learn/modules/deploy-batch-inference-pipelines-with-azure-machine-learning/2-batch-inference-pipelines</p></blockquote>

<blockquote><p><strong>Orangecm</strong> <code>(Fri 08 Apr 2022 16:57)</code> - <em>Upvotes: 1</em></p><p>Having checked the link provided, it seems init() and predict() are more appropriate ?</p></blockquote>
<blockquote><p><strong>ACSC</strong> <code>(Mon 11 Apr 2022 13:33)</code> - <em>Upvotes: 17</em></p><p>No. Answer is correct. init() and run(). Predict() is not used to score new data.</p></blockquote>

</details>

---

[<< Previous Question](question_394.md) | [Home](/index.md) | [Next Question >>](question_396.md)
