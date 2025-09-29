# Question 363

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You manage an Azure Machine Learning workspace. The Python script named script.py reads an argument named training_data. The training_data argument specifies the path to the training data in a file named dataset1.csv.

You plan to run the script.py Python script as a command job that trains a machine learning model.

You need to provide the command to pass the path for the dataset as a parameter value when you submit the script as a training job.

Solution: python script.py --training_data ${{inputs.training_data}}

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Shudharsanan</strong> <code>(Thu 12 Dec 2024 11:47)</code> - <em>Upvotes: 2</em></p><p>only partially correct.. need to define the &#x27;inputs&#x27; along</p></blockquote>

</details>

---

[<< Previous Question](question_362.md) | [Home](/index.md) | [Next Question >>](question_364.md)
