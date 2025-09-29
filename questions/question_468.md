# Question 468

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are creating a model to predict the price of a student's artwork depending on the following variables: the student's length of education, degree type, and art form.

You start by creating a linear regression model.

You need to evaluate the linear regression model.

Solution: Use the following metrics: Accuracy, Precision, Recall, F1 score, and AUC.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Mon 18 Nov 2024 07:16)</code> - <em>Upvotes: 2</em></p><p>These metrics are not suitable for evaluating a linear regression model because they are designed for classification tasks, not for predicting continuous numerical values.

For a linear regression model, the appropriate metrics would be:

Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
Relative Absolute Error (RAE)
Relative Squared Error (RSE)
Coefficient of Determination (R²)</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Wed 14 Jun 2023 20:10)</code> - <em>Upvotes: 2</em></p><p>These metrics apply to classification.</p></blockquote>
<blockquote><p><strong>cega</strong> <code>(Fri 07 Oct 2022 17:10)</code> - <em>Upvotes: 4</em></p><p>Those are for a classification model, not a regression model. The answer is correct</p></blockquote>

</details>

---

[<< Previous Question](question_467.md) | [Home](/index.md) | [Next Question >>](question_469.md)
