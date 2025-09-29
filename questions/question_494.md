# Question 494

You manage an Azure Machine Learning workspace. You build a model for which you must configure a Responsible AI dashboard.

Based on what you learn from the dashboard, you must perform the following activities:

• Determine what must be done to get a desirable outcome from the model.

• Identify the features that have the most direct effect on your outcome of interest.

You need to select the components to use for the Responsible AI dashboard configuration.

Which two components should you add? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

- A.error analysis
- B.counterfactuals
- C.explanation
- D.causal

<details>
  <summary>Show Suggested Answer</summary>

<strong>BD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>sar77</strong> <code>(Tue 15 Jul 2025 02:12)</code> - <em>Upvotes: 1</em></p><p>Counterfactuals help you determine what minimal changes to input features would lead to a different (more desirable) model outcome. This directly supports your goal of figuring out what must be done to achieve a better result.

Explanation (also known as feature importance or model interpretability) identifies which features most strongly influence the model’s predictions. This helps you pinpoint the features that have the most direct effect on your outcome of interest.</p></blockquote>

<blockquote><p><strong>KeiNek</strong> <code>(Wed 12 Feb 2025 12:37)</code> - <em>Upvotes: 1</em></p><p>Use what-if counterfactuals when you need to:
Provide solutions to users and determine what they can do to get a desirable outcome from the model.

Use causal inference when you need to:
Identify the features that have the most direct effect on your outcome of interest.

Ref :
https://learn.microsoft.com/en-us/azure/machine-learning/concept-causal-inference?view=azureml-api-2
https://learn.microsoft.com/en-us/azure/machine-learning/concept-counterfactual-analysis?view=azureml-api-2</p></blockquote>

<blockquote><p><strong>D0ktor</strong> <code>(Sun 17 Nov 2024 16:19)</code> - <em>Upvotes: 1</em></p><p>I would say explanation rather than causal. Why not explanation?</p></blockquote>
<blockquote><p><strong>Fefnut</strong> <code>(Wed 20 Nov 2024 09:08)</code> - <em>Upvotes: 1</em></p><p>I agree CD. 
- Counterfactuals just shows how a model is affected by &quot;directed noise&quot; on the data.
- Explanation, however, can show what input feature is important for a given prediction. If you get the desired prediction/outcome, you can do local analysis to identify the features that have the most direct effect on your outcome of interest.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>MatSAV</strong> <code>(Sun 17 Nov 2024 14:44)</code> - <em>Upvotes: 1</em></p><p>correct, BD</p></blockquote>
<blockquote><p><strong>kfgg</strong> <code>(Tue 22 Oct 2024 03:39)</code> - <em>Upvotes: 1</em></p><p>Use what-if counterfactuals when you need to:

Examine fairness and reliability criteria as a decision evaluator by perturbing sensitive attributes such as gender and ethnicity, and then observing whether model predictions change.
Debug specific input instances in depth.
Provide solutions to users and determine what they can do to get a desirable outcome from the model.
https://learn.microsoft.com/en-us/azure/machine-learning/concept-counterfactual-analysis?view=azureml-api-2

Finally, if we wanted to purely use historic data to identify the features that have the most direct effect on our outcome of interest, in this case the score, we can use causal analysis.</p></blockquote>

</details>

---

[<< Previous Question](question_493.md) | [Home](../index.md) | [Next Question >>](question_495.md)
