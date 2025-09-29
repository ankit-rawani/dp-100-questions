# Question 140

You manage an Azure Machine Learning workspace named workspace1.

You must develop Python SDK v2 code to add a compute instance to workspace1. The code must import all required modules and call the constructor of the ComputeInstance class.

You need to add the instantiated compute instance to workspace1.

What should you use?

- A.constructor of the azure.ai.ml.ComputeSchedule class
- B.constructor of the azure.ai.ml.ComputePowerAction enum
- C.begin_create_or_update method of an instance of the azure.ai.ml.MLCIient class
- D.set_resources method of an instance of the azure.ai.ml.Command class

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 01 Dec 2024 14:24)</code> - <em>Upvotes: 1</em></p><p>begin_create_or_update create instance asynchrounously, given answer is correct</p></blockquote>
<blockquote><p><strong>mackcsc</strong> <code>(Wed 27 Mar 2024 19:06)</code> - <em>Upvotes: 2</em></p><p>Correct</p></blockquote>
<blockquote><p><strong>Batman160591</strong> <code>(Wed 20 Dec 2023 23:15)</code> - <em>Upvotes: 2</em></p><p>Seems correct.
To add a compute instance to an Azure Machine Learning workspace using the Python SDK v2, you should use:

C. begin_create_or_update method of an instance of the azure.ai.ml.MLCIient class</p></blockquote>

</details>

---

[<< Previous Question](question_139.md) | [Home](../index.md) | [Next Question >>](question_141.md)
