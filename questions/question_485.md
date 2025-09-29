# Question 485

You develop a machine learning project on a local machine. The project uses the Azure Machine Learning SDK for Python. You use Git as version control for scripts.

You submit a training run that returns a Run object.

You need to retrieve the active Git branch for the training run.

Which two code segments should you use? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

- A.details = run.get_environment()
- B.details.properties['azureml.git.branch']
- C.details.properties['azureml.git.commit']
- D.details = run.get_details()

<details>
  <summary>Show Suggested Answer</summary>

<strong>BD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>giusecozza</strong> <code>(Fri 03 Mar 2023 16:41)</code> - <em>Upvotes: 6</em></p><p>should be B &amp; D, it is clearly explained here: https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml-core-run-get-details</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 25 Apr 2023 07:55)</code> - <em>Upvotes: 1</em></p><p>But the return type of get_details() is dict,not Run Object.</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 25 Apr 2023 08:14)</code> - <em>Upvotes: 1</em></p><p>Oh~I got it.You got a Run object! I read it wrong.</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 25 Apr 2023 08:17)</code> - <em>Upvotes: 1</em></p><p>B ref:https://learn.microsoft.com/en-us/azure/machine-learning/concept-train-model-git-integration</p></blockquote>
<blockquote><p><strong>GHill1982</strong> <code>(Wed 17 Jul 2024 05:21)</code> - <em>Upvotes: 1</em></p><p>To retrieve the active Git branch for the training run, you need to use the following two code segments:
D. details = run.get_details()
B. details.properties[‘azureml.git.branch’]
The first code segment gets the details of the run object, which includes information about the Git repository and branch that the source files came from. The second code segment accesses the property that stores the name of the active Git branch.</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Wed 06 Sep 2023 12:45)</code> - <em>Upvotes: 1</em></p><p>D, then B. 	
giusecozza  provided the link explaining.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 24 Aug 2023 14:28)</code> - <em>Upvotes: 1</em></p><p>To retrieve the active Git branch for the training run, you should use the following code segments:

Retrieve the Run object:
css
Copy code
run = &lt;insert code to submit a training run that returns a Run object&gt;
Retrieve the run details:
css
Copy code
details = run.get_details()
Access the Git branch property from the run details:
css
Copy code
branch = details[&#x27;properties&#x27;][&#x27;azureml.git.branch&#x27;]
Therefore, the correct code segments are B and D.</p></blockquote>

<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Thu 10 Aug 2023 19:14)</code> - <em>Upvotes: 2</em></p><p>The sequence of code is D and then B

details = run.get_details()
and then you can use details.properties[&#x27;azureml.git.branch&#x27;]</p></blockquote>

<blockquote><p><strong>BTAB</strong> <code>(Fri 14 Jul 2023 11:51)</code> - <em>Upvotes: 1</em></p><p>B - https://learn.microsoft.com/en-us/azure/machine-learning/concept-train-model-git-integration
D - https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml-core-run-get-details</p></blockquote>
<blockquote><p><strong>Mckay_</strong> <code>(Fri 14 Apr 2023 18:01)</code> - <em>Upvotes: 1</em></p><p>The question did not mention anything about committing any changes.</p></blockquote>
<blockquote><p><strong>Mckay_</strong> <code>(Fri 14 Apr 2023 18:00)</code> - <em>Upvotes: 2</em></p><p>The answers should be B &amp; D.</p></blockquote>

</details>

---

[<< Previous Question](question_484.md) | [Home](../index.md) | [Next Question >>](question_486.md)
