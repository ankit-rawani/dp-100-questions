# Question 481

HOTSPOT -

A biomedical research company plans to enroll people in an experimental medical treatment trial.

You create and train a binary classification model to support selection and admission of patients to the trial. The model includes the following features: Age,

Gender, and Ethnicity.

The model returns different performance metrics for people from different ethnic groups.

You need to use Fairlearn to mitigate and minimize disparities for each category in the Ethnicity feature.

Which technique and constraint should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q481_q_0045100001.jpg)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q481_ans_0_0045200001.jpg" alt="Answer Image"><br>
<p>Box 1: Grid Search -</p>
<p>Fairlearn open-source package provides postprocessing and reduction unfairness mitigation algorithms: ExponentiatedGradient, GridSearch, and</p>
<p>ThresholdOptimizer.</p>
<p>Note: The Fairlearn open-source package provides postprocessing and reduction unfairness mitigation algorithms types:</p>
<p>✑ Reduction: These algorithms take a standard black-box machine learning estimator (e.g., a LightGBM model) and generate a set of retrained models using a sequence of re-weighted training datasets.</p>
<p>✑ Post-processing: These algorithms take an existing classifier and the sensitive feature as input.</p>
<p>Box 2: Demographic parity -</p>
<p>The Fairlearn open-source package supports the following types of parity constraints: Demographic parity, Equalized odds, Equal opportunity, and Bounded group loss.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>phdykd</strong> <code>(Tue 30 Jul 2024 14:43)</code> - <em>Upvotes: 3</em></p><p>ChatGPT
Technique: a-Grid search
Constraint: d-Demographic parity</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Tue 04 Jun 2024 15:53)</code> - <em>Upvotes: 4</em></p><p>I don&#x27;t understand why not just throw out the &quot;ethnicity&quot; variable?</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Fri 08 Mar 2024 12:32)</code> - <em>Upvotes: 4</em></p><p>Exactly this question was on exam 07/March/2023</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 24 Feb 2024 15:01)</code> - <em>Upvotes: 2</em></p><p>To mitigate and minimize disparities for each category in the Ethnicity feature using Fairlearn, you should use the technique of &quot;Grid search&quot; and the constraint of &quot;Demographic parity&quot;.

Grid search is a technique used in Fairlearn to find the optimal combination of algorithmic choices and hyperparameters that minimize the difference in performance across subpopulations. This technique allows you to search through a range of potential models and select the one that achieves the best fairness-accuracy trade-off.

Demographic parity is a constraint used in Fairlearn that aims to ensure that the predicted outcomes are statistically independent of the protected attribute (in this case, ethnicity). This means that the proportion of positive outcomes (admission to the trial) should be the same across all ethnic groups.

Therefore, by using the Grid search technique to find the optimal model that satisfies the Demographic parity constraint, you can mitigate and minimize disparities for each category in the Ethnicity feature.</p></blockquote>
<blockquote><p><strong>fvil</strong> <code>(Tue 07 Nov 2023 15:47)</code> - <em>Upvotes: 3</em></p><p>Appeared on exam 07/11/2022</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Wed 14 Jun 2023 13:48)</code> - <em>Upvotes: 1</em></p><p>Grid search is good for sure ...
However,
Demographic parity: ensure that an equal number of positive predictions are made in each group
False-positive rate parity: ensure that each group contains a comparable ratio of false-positive predictions
So, which one is better ???</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Thu 15 Jun 2023 12:25)</code> - <em>Upvotes: 1</em></p><p>This question might be wrongly worded, Grid Search is only good for binary feature, ethnicity is categorical so, it cannot be really used ...</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Wed 25 Jan 2023 20:21)</code> - <em>Upvotes: 2</em></p><p>correct. 

https://docs.microsoft.com/en-us/learn/modules/detect-mitigate-unfairness-models-with-azure-machine-learning/4-mitigate-with-fairlearn</p></blockquote>

</details>

---

[<< Previous Question](question_480.md) | [Home](/index.md) | [Next Question >>](question_482.md)
