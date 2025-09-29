# Question 431

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You train and register an Azure Machine Learning model.

You plan to deploy the model to an online endpoint.

You need to ensure that applications will be able to use the authentication method with a non-expiring artifact to access the model.

Solution: Create a managed online endpoint and set the value of its auth_mode parameter to aml_token. Deploy the model to the online endpoint.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>damaldon</strong> <code>(Sun 07 Jul 2024 18:21)</code> - <em>Upvotes: 3</em></p><p>Correct.
When consuming an online endpoint from a client, you can use either a key or a token. Keys don&#x27;t expire, tokens do.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-authenticate-online-endpoint?view=azureml-api-2&amp;tabs=python</p></blockquote>

</details>

---

[<< Previous Question](question_430.md) | [Home](../index.md) | [Next Question >>](question_432.md)
