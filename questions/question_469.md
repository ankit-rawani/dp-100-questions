# Question 469

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are creating a model to predict the price of a student's artwork depending on the following variables: the student's length of education, degree type, and art form.

You start by creating a linear regression model.

You need to evaluate the linear regression model.

Solution: Use the following metrics: Relative Squared Error, Coefficient of Determination, Accuracy, Precision, Recall, F1 score, and AUC.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>
<p>Relative Squared Error, Coefficient of Determination are good metrics to evaluate the linear regression model, but the others are metrics for classification models.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/evaluate-model</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>deyoz</strong> <code>(Thu 08 Aug 2024 02:07)</code> - <em>Upvotes: 1</em></p><p>This is weird, you have option r2, which is most appropriate metric to evaluate regression model. Also, RSE. So, the solution meets the requirements, even though the metrices related with classifcations are listed as an options.</p></blockquote>

</details>

---

[<< Previous Question](question_468.md) | [Home](/index.md) | [Next Question >>](question_470.md)
