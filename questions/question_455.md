# Question 455

DRAG DROP

-

You set up a machine learning workflow as an automated process. You have an Owner role in an Azure subscription that contains the Azure Machine Learning workspace.

You must set up an authentication method that allows an automated process to authenticate to the workspace without requiring user interaction.

You need to set up the authentication for the Azure Machine Learning workspace.

Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

NOTE: More than one order of answer choices is correct. You will receive credit for any of the correct orders you select.

![Question Image](images/q455_q_image588.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q455_ans_0_image589.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jl420</strong> <code>(Mon 11 Nov 2024 13:33)</code> - <em>Upvotes: 4</em></p><p>1. Create a service principal in Microsoft Entra ID by registering a new application

This involves creating a new application registration in Azure Active Directory (AAD). A service principal represents an application or automated process, allowing it to authenticate securely.
Add a client secret, write a description for your key, and select duration

2. After registering the application, generate a client secret. The client secret acts as a password for the service principal and is required for authentication.
Select Access Control (IAM) and grant the Contributor role for the service principal

3. Grant the service principal the necessary permissions to access the Azure Machine Learning workspace by assigning the Contributor role. This allows the service principal to create, modify, and delete resources within the workspace.

Summary of the Correct Order:
Create a service principal in Microsoft Entra ID by registering a new application
Add a client secret, write a description for your key, and select duration
Select Access Control (IAM) and grant the Contributor role for the service principal</p></blockquote>

</details>

---

[<< Previous Question](question_454.md) | [Home](/index.md) | [Next Question >>](question_456.md)
