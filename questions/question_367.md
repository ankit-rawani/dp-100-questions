# Question 367

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You manage an Azure Machine Learning workspace. The Python script named script.py reads an argument named training_data. The training_data argument specifies the path to the training data in a file named dataset1.csv.

You plan to run the script.py Python script as a command job that trains a machine learning model.

You need to provide the command to pass the path for the dataset as a parameter value when you submit the script as a training job.

Solution: python script.py --training_data dataset1.csv

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>avinyc</strong> <code>(Wed 08 Jan 2025 02:59)</code> - <em>Upvotes: 1</em></p><p>No. Correct method in Azure ML is:

python script.py --training_data ${{inputs.training_data}}</p></blockquote>
<blockquote><p><strong>colin1919</strong> <code>(Fri 06 Dec 2024 09:34)</code> - <em>Upvotes: 1</em></p><p>No, the path is not specified</p></blockquote>
<blockquote><p><strong>D0ktor</strong> <code>(Tue 19 Nov 2024 22:53)</code> - <em>Upvotes: 2</em></p><p>Absolutely yes</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Wed 23 Oct 2024 13:36)</code> - <em>Upvotes: 2</em></p><p>this should be yes</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Thu 28 Nov 2024 23:36)</code> - <em>Upvotes: 1</em></p><p>where is the path specified?</p></blockquote>

</details>

---

[<< Previous Question](question_366.md) | [Home](/index.md) | [Next Question >>](question_368.md)
