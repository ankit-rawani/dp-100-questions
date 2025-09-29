# Question 365

You manage an Azure Machine Learning workspace.

You choose the uri_folder data type as an output of a pipeline component.

You need to define the data access mode that is supported by your configuration.

Which mode should you define?

- A.eval_upload
- B.rw_mount
- C.download
- D.ro_mount

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>D0ktor</strong> <code>(Tue 19 Nov 2024 22:51)</code> - <em>Upvotes: 1</em></p><p>RW correct</p></blockquote>
<blockquote><p><strong>AzureGeek79</strong> <code>(Sat 12 Oct 2024 03:19)</code> - <em>Upvotes: 1</em></p><p>B. rw_mount is the correct answer.

This mode allows the output directory to be a mounted directory, which is suitable for uri_folder data type outputs. It provides read-write access to the output location, enabling the component to write its output directly to the mounted directory.</p></blockquote>

</details>

---

[<< Previous Question](question_364.md) | [Home](../index.md) | [Next Question >>](question_366.md)
