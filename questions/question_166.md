# Question 166

You have an Azure Machine Learning workspace and a serverless Spark compute resource.

You plan to run the same Spark session every 40 minutes. Each session runs for 15 minutes.

During testing, you observe a 15-minute delay at the start of the Spark sessions.

You need to reduce the delay to less than 1 minute.

What should you do?

* A.Configure the session timeout to be 25 minutes.
* B.Increase the number of nodes to 16.
* C.Enable dynamically allocated executors.
* D.Enable an isolated compute.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jl420</strong> <code>(Wed 13 Nov 2024 01:43)</code> - <em>Upvotes: 2</em></p><p>By configuring the session timeout to be 25 minutes, you allow the Spark session to remain active between runs, preventing it from shutting down between each 40-minute interval. Since each session runs for 15 minutes, setting the timeout to 25 minutes keeps the session warm and reduces the initialization delay.</p></blockquote>

</details>

---

[<< Previous Question](question_165.md) | [Home](/index.md) | [Next Question >>](question_167.md)
