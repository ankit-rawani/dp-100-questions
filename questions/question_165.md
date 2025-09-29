# Question 165

You manage an Azure Machine Learning workspace named Workspace1.

You plan to create a pipeline in the Azure Machine Learning Studio designer. The pipeline must include a custom component.

You need to ensure the custom component can be used in the pipeline.

What should you do first?

* A.Create a pipeline endpoint.
* B.Add a linked service to Workspace1.
* C.Upload a .json file to Workspace1.
* D.Create a datastore.
* E.Upload a .yaml file to Workspace1.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>E</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jl420</strong> <code>(Wed 13 Nov 2024 01:41)</code> - <em>Upvotes: 1</em></p><p>Although E seems correct, it assumes the custom component already exists. However, the question does not say &quot;import existing&quot;, it says &quot;must include&quot; which means I can create it on the fly IN DESIGNER GUI without ever using a YAML file, unless I want to export it. What IS required for any pipeline component to work is D. Create a DATASTORE. In fact, this should be the first thing before you can upload a YAML. Going with D. as the answer, although I admit it could still be E and was just poorly written.</p></blockquote>
<blockquote><p><strong>PrenCarr</strong> <code>(Sun 06 Oct 2024 20:05)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>

</details>

---

[<< Previous Question](question_164.md) | [Home](/index.md) | [Next Question >>](question_166.md)
