# Question 69

DRAG DROP -

You are analyzing a raw dataset that requires cleaning.

You must perform transformations and manipulations by using Azure Machine Learning Studio.

You need to identify the correct modules to perform the transformations.

Which modules should you choose? To answer, drag the appropriate modules to the correct scenarios. Each module may be used once, more than once, or not at all.

You may need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

Select and Place:

![Question Image](../images/q69_q_0008700001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q69_ans_0_0008700002.png" alt="Answer Image"><br>

<p>Box 1: Clean Missing Data -</p>
<p>Box 2: SMOTE -</p>
<p>Use the SMOTE module in Azure Machine Learning Studio to increase the number of underepresented cases in a dataset used for machine learning. SMOTE is a better way of increasing the number of rare cases than simply duplicating existing cases.</p>
<p>Box 3: Convert to Indicator Values</p>
<p>Use the Convert to Indicator Values module in Azure Machine Learning Studio. The purpose of this module is to convert columns that contain categorical values into a series of binary indicator columns that can more easily be used as features in a machine learning model.</p>
<p>Box 4: Remove Duplicate Rows -</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/smote https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/convert-to-indicator-values</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Tehseen</strong> <code>(Sat 24 Jun 2023 11:25)</code> - <em>Upvotes: 16</em></p><p>Seems true</p></blockquote>
<blockquote><p><strong>azurelearner666</strong> <code>(Wed 10 Apr 2024 15:03)</code> - <em>Upvotes: 6</em></p><p>Correct!
Note that &quot;Convert to indicator values&quot; (re-encode Categorical values into binary columns) is also called One-Hot Encoding, https://docs.microsoft.com/en-us/learn/modules/prepare-data-for-machine-learning-azure-databricks/6-perform-data-encoding</p></blockquote>
<blockquote><p><strong>DodoScript</strong> <code>(Tue 20 Aug 2024 13:57)</code> - <em>Upvotes: 4</em></p><p>Answer is correct</p></blockquote>
<blockquote><p><strong>k1ngs1zed</strong> <code>(Sat 13 Apr 2024 06:45)</code> - <em>Upvotes: 3</em></p><p>Correct!</p></blockquote>

</details>

---

[<< Previous Question](question_68.md) | [Home](../index.md) | [Next Question >>](question_70.md)
