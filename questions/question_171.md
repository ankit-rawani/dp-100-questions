# Question 171

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Machine Learning workspace that includes an AmlCompute cluster and a batch endpoint.

You clone a repository that contains an MLflow model to your local computer.

You need to ensure that you can deploy the model to the batch endpoint.

Solution: Register the model in the workspace.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>f82411e</strong> <code>(Thu 29 May 2025 12:51)</code> - <em>Upvotes: 1</em></p><p>A - SI</p></blockquote>
<blockquote><p><strong>jl420</strong> <code>(Thu 07 Nov 2024 17:17)</code> - <em>Upvotes: 1</em></p><p>Registering the model is the required next step. Followed by creating a deployment config to deploy the batch endpoint using existing cluster.</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Tue 29 Oct 2024 13:26)</code> - <em>Upvotes: 1</em></p><p>A. Yes

Explanation:

Registering the MLflow model in the Azure Machine Learning workspace is a necessary step before deploying the model to a batch endpoint. The model must be registered so that it can be referenced during deployment. Once registered, you can create a batch deployment that uses the model along with the appropriate compute resources. Therefore, registering the model meets the goal of ensuring that the model can be deployed to the batch endpoint.</p></blockquote>

</details>

---

[<< Previous Question](question_170.md) | [Home](/index.md) | [Next Question >>](question_172.md)
