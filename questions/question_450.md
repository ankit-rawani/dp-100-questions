# Question 450

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Machine Learning workspace named Workspace1. Workspace1 has a registered MLflow model named model1 with PyFunc flavor.

You plan to deploy model1 to an online endpoint named endpoint1 without egress connectivity by using Azure Machine Learning Python SDK v2.

You have the following code:

![Question Image](images/q450_q_image571.png)

You need to add a parameter to the ManagedOnlineDeployment object to ensure the model deploys successfully.

Solution: Add the environment parameter.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>nposteraro</strong> <code>(Thu 21 Nov 2024 11:22)</code> - <em>Upvotes: 2</em></p><p>When you deploy your MLflow model to an online endpoint, you don&#x27;t need to specify a scoring script or an environment—this functionality is known as no-code deployment.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models-online-endpoints?view=azureml-api-2&amp;tabs=cli</p></blockquote>
<blockquote><p><strong>D0ktor</strong> <code>(Mon 18 Nov 2024 19:19)</code> - <em>Upvotes: 2</em></p><p>Environment is needed but not enought to meet requierements</p></blockquote>
<blockquote><p><strong>f2a9aa5</strong> <code>(Fri 28 Jun 2024 10:01)</code> - <em>Upvotes: 1</em></p><p>To deploy an MLflow model to an online endpoint in Azure Machine Learning without egress connectivity, you can use model packaging. Here’s how:

First, ensure that your workspace has no public network access.
Package your MLflow model using the --with-package flag:

az ml online-deployment create --with-package --endpoint-name $ENDPOINT_NAME -f blue-deployment.yml --all-traffic

Replace $ENDPOINT_NAME with your desired endpoint name.

This approach allows you to avoid the need for an internet connection while deploying MLflow models.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-mlflow-models-online-endpoints?view=azureml-api-2&amp;tabs=cli</p></blockquote>
<blockquote><p><strong>cryodax</strong> <code>(Sat 15 Jun 2024 19:34)</code> - <em>Upvotes: 1</em></p><p>The ManagedOnlineDeployment class requires the following parameters:

name: str: Name of the deployment resource.
model: str | Model | None: Model entity for the endpoint deployment, defaults to None.
code_configuration: CodeConfiguration | None: Code Configuration, defaults to None.
environment: str | Environment | None: Environment entity for the endpoint deployment, defaults to None.
These are the minimum required parameters to create an instance of the ManagedOnlineDeployment class. All other parameters are optional and have default values. Please note that while model, code_configuration, and environment are optional in the constructor, they are typically necessary for a successful deployment. If not provided in the constructor, they should be set before deployment.</p></blockquote>

</details>

---

[<< Previous Question](question_449.md) | [Home](/index.md) | [Next Question >>](question_451.md)
