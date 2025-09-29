# Question 327

DRAG DROP

-

You have an Azure Machine Learning workspace. You are running an experiment on your local computer.

You need to ensure that you can use MLflow Tracking with Azure Machine Learning Python SDK v2 to store metrics and artifacts from your local experiment runs m the workspace.

In which order should you perform the actions? To answer, move all actions from the list of actions to the answer area and arrange them in the correct order.

![Question Image](images/q327_q_image504.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q327_ans_0_image505.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>phdykd</strong> <code>(Fri 26 Jan 2024 15:54)</code> - <em>Upvotes: 5</em></p><p>D,C,B,A</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 23 Feb 2024 13:07)</code> - <em>Upvotes: 1</em></p><p>I feel like both should be ok, does it really matter if we get the URL before importing? no it doesnt.. so either way should be ok</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Thu 01 Aug 2024 07:31)</code> - <em>Upvotes: 1</em></p><p>Don&#x27;t you need MLClient before getting access to your workspace? Then only DCBA would be correct.</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Wed 27 Nov 2024 01:06)</code> - <em>Upvotes: 3</em></p><p>I was confused a bit as to why you need to go to Azure portal. It turns out that in the portal on the overview page you can get the MLflow tracking URI. I can&#x27;t find it in the Machine learning Studio though. The answer provided is correct.</p></blockquote>
<blockquote><p><strong>Gpblax</strong> <code>(Thu 06 Jun 2024 10:52)</code> - <em>Upvotes: 2</em></p><p>A,B,C,D
Login to workspace
Get the tracking URI for your workspace
import mlflow
set_tracking_uri

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow-configure-tracking?view=azureml-api-2&amp;tabs=cli%2Cmlflow</p></blockquote>
<blockquote><p><strong>Gpblax</strong> <code>(Thu 06 Jun 2024 10:54)</code> - <em>Upvotes: 3</em></p><p>Sorry it is D,B,C,A</p></blockquote>

</details>

---

[<< Previous Question](question_326.md) | [Home](/index.md) | [Next Question >>](question_328.md)
