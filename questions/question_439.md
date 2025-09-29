# Question 439

You run Azure Machine Learning training experiments. The training scripts directory contains 100 files that includes a file named .amlignore. The directory also contains subdirectories named ./outputs and ./logs.

There are 20 files in the training scripts directory that must be excluded from the snapshot to the compute targets. You create a file named .gitignore in the root of the directory. You add the names of the 20 files to the .gitignore file. These 20 files continue to be copied to the compute targets.

You need to exclude the 20 files.

What should you do?

- A.Copy the contents of the file named .gitignore to the file named .amlignore.
- B.Move the file named .gitignore to the ./outputs directory.
- C.Move the file named .gitignore to the ./logs directory.
- D.Add the contents of the file named .amlignore to the file named .gitignore.

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>nposteraro</strong> <code>(Tue 19 Nov 2024 13:21)</code> - <em>Upvotes: 1</em></p><p>If both files exist, the .amlignore file is used and the .gitignore file is unused.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-set-up-training-targets?view=azureml-api-1</p></blockquote>
<blockquote><p><strong>AlenC</strong> <code>(Wed 18 Oct 2023 02:25)</code> - <em>Upvotes: 1</em></p><p>I think it is A.  Based on the reference, if there are both .amlignore and .gitignore existing, .amlignore would be used instead of the .gitignore.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-set-up-training-targets?view=azureml-api-1</p></blockquote>

</details>

---

[<< Previous Question](question_438.md) | [Home](../index.md) | [Next Question >>](question_440.md)
