# Question 433

DRAG DROP

-

You train and register a model by using the Azure Machine Learning Python SDK v2 on a local workstation. Python 3.7 and Visual Studio Code are installed on the workstation.

When you try to deploy the model into production to a Kubernetes online endpoint, you experience an error in the scoring script that causes deployment to fail.

You need to debug the service on the local workstation before deploying the service to production.

Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

![Question Image](images/q433_q_image532.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q433_ans_0_image533.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>damaldon</strong> <code>(Sun 07 Jul 2024 18:55)</code> - <em>Upvotes: 2</em></p><p>Correct.
ml_client.begin_create_or_update(online_deployment, local=True)

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-troubleshoot-online-endpoints?view=azureml-api-2&amp;tabs=python</p></blockquote>

</details>

---

[<< Previous Question](question_432.md) | [Home](/index.md) | [Next Question >>](question_434.md)
