# Question 163

HOTSPOT

-

You manage an Azure subscription that contains the following resources:

![Question Image](../images/q163_q_image566.png)

You plan to implement a solution that will automatically trigger the retraining of the model implemented by MLPipeline1. The trigger must be invoked if data drift is detected in Dataset1.

You need to select the components to invoke and run the solution. The solution must minimize coding implementation and maintenance efforts.

Which components should you select? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](../images/q163_q_image567.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q163_ans_0_image568.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>445f1bd</strong> <code>(Mon 21 Jul 2025 14:37)</code> - <em>Upvotes: 1</em></p><p>Event grid

Logic apps (since it says minimal code)</p></blockquote>

<blockquote><p><strong>jefimija</strong> <code>(Mon 14 Oct 2024 12:03)</code> - <em>Upvotes: 3</em></p><p>Invoke Component: Azure Event Grid
Run Component: Azure Functions</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Mon 28 Oct 2024 12:31)</code> - <em>Upvotes: 1</em></p><p>Or it could be Logic Apps

Can someone explain the difference between Azure Functins and Logic Apps?</p></blockquote>

<blockquote><p><strong>nposteraro</strong> <code>(Fri 27 Jun 2025 13:39)</code> - <em>Upvotes: 1</em></p><p>I think it&#x27;s Logic App since is a visual designer with minimal or no code, whereas Functions is more code-centric</p></blockquote>

</details>

---

[<< Previous Question](question_162.md) | [Home](../index.md) | [Next Question >>](question_164.md)
