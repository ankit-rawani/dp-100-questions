# Question 495

You create an Azure Machine Learning workspace.

You must configure an event-driven workflow to automatically trigger upon completion of training runs in the workspace. The solution must minimize the administrative effort to configure the trigger.

You need to configure an Azure service to automatically trigger the workflow.

Which Azure service should you use?

- A.Event Grid subscription
- B.Azure Automation runbook
- C.Event Hubs Capture
- D.Event Hubs consumer

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 20:17)</code> - <em>Upvotes: 2</em></p><p>The Correct answer is: A. Event Grid subscription

Justification:
Event Grid subscription: is the most suitable choice for creating event-driven workflows in Azure. When a training run is completed in an Azure ML workspace, Event Grid can be used to trigger a workflow automatically. This approach requires minimal administrative effort, as you can subscribe to specific events (like training run completion) and respond to them without constant polling or manual intervention.

Wrong Answers:

B. Azure Automation runbook: is more suitable for scenarios where you need to automate complex, multi-step processes and often require more administrative effort to set up triggers based on specific events in Azure Machine Learning.

C. Event Hubs Capture: is designed to automatically capture the streaming data in Event Hubs and save it to a storage account.

D. Event Hubs consumer: is part of the Event Hubs service and is used to read and process the stream of events. It is not a tool for triggering workflows based on specific events within Azure Machine Learning workspaces. It requires more effort to configure.</p></blockquote>

<blockquote><p><strong>sar77</strong> <code>(Tue 08 Jul 2025 04:45)</code> - <em>Upvotes: 1</em></p><p>You should use Azure Event Grid to automatically trigger your workflow upon completion of training runs in your Azure Machine Learning workspace. Event Grid can publish events such as &quot;run completion&quot; from Azure Machine Learning, allowing you to set up event-driven workflows with minimal administrative effort. These events can then be consumed by services like Azure Logic Apps, which can further automate downstream actions</p></blockquote>
<blockquote><p><strong>Jin_22</strong> <code>(Wed 20 Sep 2023 08:57)</code> - <em>Upvotes: 1</em></p><p>To configure an event-driven workflow to automatically trigger upon completion of training runs in the workspace, you should use Azure Event Grid subscription. Azure Machine Learning emits the following event types: Model registered, Model deployed, Run completed, and Dataset drift detected. When an event is triggered, the Event Grid service sends data about that event to subscribing endpoint. You can set up event-driven applications, processes, or CI/CD workflows based on Azure Machine Learning events, such as failure notification emails or ML pipeline runs, when certain conditions are detected by Azure Event Grid</p></blockquote>

</details>

---

[<< Previous Question](question_494.md) | [Home](../index.md) | [Next Question >>](question_496.md)
