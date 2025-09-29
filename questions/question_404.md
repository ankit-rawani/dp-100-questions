# Question 404

You are developing a machine learning model.

You must inference the machine learning model for testing.

You need to use a minimal cost compute target.

Which two compute targets should you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- A.Azure Machine Learning Kubernetes
- B.Azure Databricks
- C.Remote VM
- D.Local web service
- E.Azure Container Instances

<details>
  <summary>Show Suggested Answer</summary>

<strong>DE</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>sap_dg</strong> <code>(Sat 01 Apr 2023 04:26)</code> - <em>Upvotes: 7</em></p><p>The inference is for testing. We do not need a Web Service. Answer should be C and E</p></blockquote>
<blockquote><p><strong>nposteraro</strong> <code>(Mon 18 Nov 2024 12:09)</code> - <em>Upvotes: 1</em></p><p>I think it&#x27;s C and D: https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2#compute-targets-for-inferen</p></blockquote>
<blockquote><p><strong>sanctafrax</strong> <code>(Sun 02 Feb 2025 15:44)</code> - <em>Upvotes: 1</em></p><p>Why remote VM? VM&#x27;s are relatively expensive to run. in principle all answers can support a deployment.  VM&#x27;s are always on and therefore are always paid for. Azure container instance isnt. At least its serverless and therefore you dont pay for overhead. I agree with D but disagree with C.</p></blockquote>
<blockquote><p><strong>haby</strong> <code>(Tue 19 Dec 2023 15:47)</code> - <em>Upvotes: 2</em></p><p>C &amp; D. 
Based on my exp, most expensive is Databricks, AKS/ACI with GPU support are the next one, then AKS/ACI w/o GPU, last one is VM. 
All of them are available as a compute target for Auto ML/ML pipelines [https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2], so I will choose CD for minimal cost.</p></blockquote>
<blockquote><p><strong>ZoeJ</strong> <code>(Thu 27 Apr 2023 04:09)</code> - <em>Upvotes: 3</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2#compute-targets-for-inference
I think the given answer is correct</p></blockquote>

</details>

---

[<< Previous Question](question_403.md) | [Home](../index.md) | [Next Question >>](question_405.md)
