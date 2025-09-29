# Question 102

HOTSPOT -

You create a new Azure Databricks workspace.

You configure a new cluster for long-running tasks with mixed loads on the compute cluster as shown in the image below.

![Question Image](images/q102_q_0014000001.png)

Use the drop-down menus to select the answer choice that completes each statement based on the information presented in the graphic.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q102_q_0014100001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q102_ans_0_0014100002.jpg" alt="Answer Image"><br>
<p>Box 1: No -</p>
<p>Running user code in separate processes is not possible in Scala.</p>
<p>Box 2: No -</p>
<p>Autoscaling is enabled. Minimum 2 workers, Maximum 8 workers.</p>
<p>Reference:</p>
<p>https://docs.databricks.com/clusters/configure.html</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>michaelmorar</strong> <code>(Sun 04 Dec 2022 08:41)</code> - <em>Upvotes: 12</em></p><p>Correct answer:

Scala code will be executed inside the Spark JVM (per machine) that is shared between all users, so you can get access to everything that is inside JVM.

https://learn.microsoft.com/en-us/answers/questions/924587/azure-databricks-scala-on-high-concurrency-cluster.html

High Concurrency clusters can run workloads developed in SQL, Python, and R. The performance and security of High Concurrency clusters is provided by running user code in separate processes, which is not possible in Scala.

https://learn.microsoft.com/en-us/azure/databricks/clusters/configure#--high-concurrency-clusters</p></blockquote>
<blockquote><p><strong>hiyoww</strong> <code>(Sun 07 Apr 2024 08:53)</code> - <em>Upvotes: 1</em></p><p>this question is seem related to DP-203 data engineering exam more</p></blockquote>
<blockquote><p><strong>cyberfriends</strong> <code>(Fri 13 Oct 2023 16:05)</code> - <em>Upvotes: 1</em></p><p>why not yes and yes&gt;???</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Mon 28 Oct 2024 11:34)</code> - <em>Upvotes: 1</em></p><p>Pool = None
- no parallel processes

Number of workers vary between 2 and 8 so not fixed</p></blockquote>

</details>

---

[<< Previous Question](question_101.md) | [Home](/index.md) | [Next Question >>](question_103.md)
