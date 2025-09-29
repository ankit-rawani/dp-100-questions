# Question 448

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have an Azure Machine Learning workspace. You connect to a terminal session from the Notebooks page in Azure Machine Learning studio.

You plan to add a new Jupyter kernel that will be accessible from the same terminal session.

You need to perform the task that must be completed before you can add the new kernel.

Solution: Create a compute instance.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 10:59)</code> - <em>Upvotes: 5</em></p><p>The correct solution would likely involve preparing the Python environment for the new kernel within the existing compute instance, rather than creating a new compute instance.</p></blockquote>
<blockquote><p><strong>D0ktor</strong> <code>(Mon 18 Nov 2024 19:13)</code> - <em>Upvotes: 1</em></p><p>Creating a compute instance is indeed necessary to support a Jupyter kernel, as it provides the necessary infrastructure for running notebooks and adding kernels. So, this solution does meet the goal.</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Sun 02 Jun 2024 04:47)</code> - <em>Upvotes: 3</em></p><p>The compute instance needs to be created first before you can even have a terminal session</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 18 May 2024 03:12)</code> - <em>Upvotes: 2</em></p><p>This does the job</p></blockquote>

</details>

---

[<< Previous Question](question_447.md) | [Home](../index.md) | [Next Question >>](question_449.md)
