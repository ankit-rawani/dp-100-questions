# Question 150

You plan to use automated machine learning by using Azure Machine Learning Python SDK v2 to train a regression model. You have data that has features with missing values, and categorical features with few distinct values.

You need to control whether automated machine learning automatically imputes missing values and encode categorical features as part of the training task.

Which enum of the automl package should you use?

- A.ForecastHorizonMode
- B.RegressionModels
- C.FeaturizationMode
- D.RegressionPrimaryMetrics

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>f82411e</strong> <code>(Wed 28 May 2025 11:45)</code> - <em>Upvotes: 1</em></p><p>A. ForecastHorizonMode: relacionado con series temporales, no aplicable aquí.

B. RegressionModels: especifica qué modelos usar, pero no controla la featurization.

D. RegressionPrimaryMetrics: define la métrica de evaluación, no el preprocesamiento.</p></blockquote>

<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 12:12)</code> - <em>Upvotes: 2</em></p><p>Correct: C. FeaturizationMode
Constructor:
FeaturizationMode(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

Fields:
AUTO, CUSTOM, OFF

See https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.automl.featurizationmode?view=azure-python</p></blockquote>

<blockquote><p><strong>Mikku123</strong> <code>(Sat 03 Feb 2024 00:27)</code> - <em>Upvotes: 3</em></p><p>correct!</p></blockquote>

</details>

---

[<< Previous Question](question_149.md) | [Home](../index.md) | [Next Question >>](question_151.md)
