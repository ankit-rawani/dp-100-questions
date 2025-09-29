# Question 405

You create an Azure Machine Learning workspace.

You must configure an event handler to send an email notification when data drift is detected in the workspace datasets. You must minimize development efforts.

You need to configure an Azure service to send the notification.

Which Azure service should you use?

- A.Azure Logic Apps
- B.Azure Automation runbook
- C.Azure Function apps
- D.Azure DevOps pipeline

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 20:31)</code> - <em>Upvotes: 1</em></p><p>A is correct.

Azure Logic Apps: Azure Logic Apps is an ideal choice for setting up automated workflows, like sending email notifications in response to specific triggers or events. In this case, an event handler can be configured in Azure Logic Apps to monitor data drift in Azure Machine Learning workspace datasets. When data drift is detected, the logic app can automatically send an email notification. This approach is efficient and requires minimal development effort, aligning with the requirement to minimize development efforts.

Azure Automation runbook: operations management and process automation within Azure environments. They are not the most direct or efficient method for setting up email notifications in response to data drift events in Azure Machine Learning.

Azure Function apps: could technically be used to detect data drift and send email notifications, it would require more development effort compared to using Azure Logic Apps.

Azure DevOps pipeline: primarily used for CI/CD processes, not typically used for monitoring data drift or sending email notifications.</p></blockquote>

<blockquote><p><strong>Kvcper333</strong> <code>(Thu 12 Oct 2023 08:31)</code> - <em>Upvotes: 1</em></p><p>imo correct</p></blockquote>

</details>

---

[<< Previous Question](question_404.md) | [Home](../index.md) | [Next Question >>](question_406.md)
