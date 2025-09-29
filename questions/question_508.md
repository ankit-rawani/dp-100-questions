# Question 508

HOTSPOT -

You need to replace the missing data in the AccessibilityToHighway columns.

How should you configure the Clean Missing Data module? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q508_q_0033900001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q508_ans_0_0034100001.png" alt="Answer Image"><br>

<p>Box 1: Replace using MICE -</p>
<p>Replace using MICE: For each missing value, this option assigns a new value, which is calculated by using a method described in the statistical literature as</p>
<p>&quot;Multivariate Imputation using Chained Equations&quot; or &quot;Multiple Imputation by Chained Equations&quot;. With a multiple imputation method, each variable with missing data is modeled conditionally using the other variables in the data before filling in the missing values.</p>
<p>Scenario: The AccessibilityToHighway column in both datasets contains missing values. The missing data must be replaced with new data so that it is modeled conditionally using the other variables in the data before filling in the missing values.</p>
<p>Box 2: Propagate -</p>
<p>Cols with all missing values indicate if columns of all missing values should be preserved in the output.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/clean-missing-data</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Svastaric</strong> <code>(Wed 28 Aug 2024 19:01)</code> - <em>Upvotes: 7</em></p><p>I think it is in MICE definition. This method is imputing values that need to be distributed into empty column, instead of removing the columns and affecting dimensionality</p></blockquote>
<blockquote><p><strong>Anandad12</strong> <code>(Sat 24 Aug 2024 04:42)</code> - <em>Upvotes: 6</em></p><p>Cols with all missing data has default value of Remove. That is the correct answer to me. Not sure why Propagate?</p></blockquote>

</details>

---

[<< Previous Question](question_507.md) | [Home](../index.md) | [Next Question >>](question_509.md)
