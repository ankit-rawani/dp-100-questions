# Question 372

You deploy a model as an Azure Machine Learning real-time web service using the following code.

![Question Image](images/q372_q_0037600001.png)

The deployment fails.

You need to troubleshoot the deployment failure by determining the actions that were performed during deployment and identifying the specific action that failed.

Which code segment should you run?

* A.service.get_logs()
* B.service.state
* C.service.serialize()
* D.service.update_deployment_state()

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>
<p>You can print out detailed Docker engine log messages from the service object. You can view the log for ACI, AKS, and Local deployments. The following example demonstrates how to print the logs.</p>
<p># if you already have the service object handy</p>
<p>print(service.get_logs())</p>
<p># if you only know the name of the service (note there might be multiple services with the same name but different version number) print(ws.webservices[&#x27;mysvc&#x27;].get_logs())</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-troubleshoot-deployment</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>SaulG</strong> <code>(Thu 08 Jun 2023 08:03)</code> - <em>Upvotes: 10</em></p><p>A is the correct answer.</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Tue 18 Jun 2024 01:49)</code> - <em>Upvotes: 1</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Mon 18 Mar 2024 09:46)</code> - <em>Upvotes: 3</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Sun 03 Mar 2024 06:37)</code> - <em>Upvotes: 1</em></p><p>On 03 March 2022</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Mon 06 Nov 2023 23:05)</code> - <em>Upvotes: 2</em></p><p>on Exam 6 Nov 2021</p></blockquote>

</details>

---

[<< Previous Question](question_371.md) | [Home](/index.md) | [Next Question >>](question_373.md)
