# Question 493

HOTSPOT

-

You have a binary classifier that predicts positive cases of diabetes within two separate age groups.

The classifier exhibits a high degree of disparity between the age groups.

You need to modify the output of the classifier to maximize its degree of fairness across the age groups and meet the following requirements:

• Eliminate the need to retrain the model on which the classifier is based.

• Minimize the disparity between true positive rates and false positive rates across age groups.

Which algorithm and parity constraint should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](../images/q493_q_image448.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q493_ans_0_image449.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>GHill1982</strong> <code>(Wed 17 Jul 2024 19:14)</code> - <em>Upvotes: 1</em></p><p>Correct. To modify the output of the classifier to maximize its degree of fairness across the age groups, you should use a postprocessing algorithm and the equalized odds parity constraint.</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Wed 10 Jan 2024 17:51)</code> - <em>Upvotes: 1</em></p><p>Correct, Threshold Optimizer is for Post-processing. No re-train model needed.
https://learn.microsoft.com/en-us/azure/machine-learning/concept-fairness-ml?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>sap_dg</strong> <code>(Fri 29 Sep 2023 03:56)</code> - <em>Upvotes: 1</em></p><p>Correct!</p></blockquote>

</details>

---

[<< Previous Question](question_492.md) | [Home](/index.md) | [Next Question >>](question_494.md)
