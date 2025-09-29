# Question 476

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are creating a model to predict the price of a student's artwork depending on the following variables: the student's length of education, degree type, and art form.

You start by creating a linear regression model.

You need to evaluate the linear regression model.

Solution: Use the following metrics: Mean Absolute Error, Root Mean Absolute Error, Relative Absolute Error, Accuracy, Precision, Recall, F1 score, and AUC.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

<p>Accuracy, Precision, Recall, F1 score, and AUC are metrics for evaluating classification models.</p>
<p>Note: Mean Absolute Error, Root Mean Absolute Error, Relative Absolute Error are OK for the linear regression model.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/evaluate-model</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Carkeys</strong> <code>(Sun 26 Sep 2021 03:17)</code> - <em>Upvotes: 5</em></p><p>some of the metrics are useful for evaluating the model and some are not, it says as much  in the provided answer

The question being, how is this a Y/N question? anybody else get tripped up by this?

Do I answer no if I can find one evaluation method that doesn&#x27;t make sense? etc.</p></blockquote>

<blockquote><p><strong>deyoz</strong> <code>(Thu 08 Aug 2024 02:39)</code> - <em>Upvotes: 1</em></p><p>what would be the answer if there were R2 aswell as an options?</p></blockquote>
<blockquote><p><strong>Andrexx</strong> <code>(Wed 12 May 2021 21:11)</code> - <em>Upvotes: 1</em></p><p>Agree with the answer</p></blockquote>
<blockquote><p><strong>clownfishman</strong> <code>(Tue 30 Mar 2021 01:35)</code> - <em>Upvotes: 3</em></p><p>... but this is asking for a linear regression model, so the answer should be TRUE</p></blockquote>
<blockquote><p><strong>shivaborusu</strong> <code>(Mon 10 May 2021 05:38)</code> - <em>Upvotes: 7</em></p><p>You do not have Precision, Recall, F1 score for a linear regression model. You will have it for only classification. Don&#x27;t get confused with Logistic Regression</p></blockquote>

</details>

---

[<< Previous Question](question_475.md) | [Home](../index.md) | [Next Question >>](question_477.md)
