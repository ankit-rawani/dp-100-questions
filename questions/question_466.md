# Question 466

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are creating a model to predict the price of a student's artwork depending on the following variables: the student's length of education, degree type, and art form.

You start by creating a linear regression model.

You need to evaluate the linear regression model.

Solution: Use the following metrics: Mean Absolute Error, Root Mean Absolute Error, Relative Absolute Error, Relative Squared Error, and the Coefficient of

Determination.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>
<p>The following metrics are reported for evaluating regression models. When you compare models, they are ranked by the metric you select for evaluation.</p>
<p>Mean absolute error (MAE) measures how close the predictions are to the actual outcomes; thus, a lower score is better.</p>
<p>Root mean squared error (RMSE) creates a single value that summarizes the error in the model. By squaring the difference, the metric disregards the difference between over-prediction and under-prediction.</p>
<p>Relative absolute error (RAE) is the relative absolute difference between expected and actual values; relative because the mean difference is divided by the arithmetic mean.</p>
<p>Relative squared error (RSE) similarly normalizes the total squared error of the predicted values by dividing by the total squared error of the actual values.</p>
<p>Mean Zero One Error (MZOE) indicates whether the prediction was correct or not. In other words: ZeroOneLoss(x,y) = 1 when x!=y; otherwise 0.</p>
<p>Coefficient of determination, often referred to as R2, represents the predictive power of the model as a value between 0 and 1. Zero means the model is random</p>
<p>(explains nothing); 1 means there is a perfect fit. However, caution should be used in interpreting R2 values, as low values can be entirely normal and high values can be suspect.</p>
<p>AUC.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/evaluate-model</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 11:44)</code> - <em>Upvotes: 1</em></p><p>The metrics listed (Mean Absolute Error, Root Mean Squared Error, Relative Absolute Error, Relative Squared Error, and Coefficient of Determination) are all appropriate for evaluating a linear regression model. These metrics provide different insights into the model&#x27;s performance and prediction accuracy.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 18 May 2024 06:15)</code> - <em>Upvotes: 1</em></p><p>MAE and RMSE provide insight into the average error and error variance.
RAE and RSE help to understand the model&#x27;s performance relative to a baseline model.
R² shows the goodness of fit of the model</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Thu 08 Feb 2024 03:00)</code> - <em>Upvotes: 1</em></p><p>R2 is a must and we can have any other metric to evaluate the difference between actual and predicted values. Though RMSE is not mentioned, it is still sufficient to evaluate the model with given options.</p></blockquote>
<blockquote><p><strong>vprowerty</strong> <code>(Sat 27 Jan 2024 13:06)</code> - <em>Upvotes: 1</em></p><p>I would say the answer is &quot;no&quot; because one of the provided options
&quot;Root Mean Absolute Error&quot; is not an existing error measure, the correct would be Root Mean Squared Error (RMSE)</p></blockquote>
<blockquote><p><strong>dijaa</strong> <code>(Sat 28 Aug 2021 11:07)</code> - <em>Upvotes: 3</em></p><p>correct</p></blockquote>
<blockquote><p><strong>aaodiall1</strong> <code>(Tue 24 Aug 2021 15:40)</code> - <em>Upvotes: 1</em></p><p>correct answer</p></blockquote>

</details>

---

[<< Previous Question](question_465.md) | [Home](/index.md) | [Next Question >>](question_467.md)
