# Question 253

You are creating a classification model for a banking company to identify possible instances of credit card fraud. You plan to create the model in Azure Machine

Learning by using automated machine learning.

The training dataset that you are using is highly unbalanced.

You need to evaluate the classification model.

Which primary metric should you use?

- A.normalized_mean_absolute_error
- B.AUC_weighted
- C.accuracy
- D.normalized_root_mean_squared_error
- E.spearman_correlation

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

<p>AUC_weighted is a Classification metric.</p>
<p>Note: AUC is the Area under the Receiver Operating Characteristic Curve. Weighted is the arithmetic mean of the score for each class, weighted by the number of true instances in each class.</p>
<p>Incorrect Answers:</p>
<p>A: normalized_mean_absolute_error is a regression metric, not a classification metric.</p>
<p>C: When comparing approaches to imbalanced classification problems, consider using metrics beyond accuracy such as recall, precision, and AUROC. It may be that switching the metric you optimize for during parameter selection or model selection is enough to provide desirable performance detecting the minority class.</p>
<p>D: normalized_root_mean_squared_error is a regression metric, not a classification metric.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-understand-automated-ml</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ac45863</strong> <code>(Fri 07 Apr 2023 23:25)</code> - <em>Upvotes: 16</em></p><p>It&#x27;s correct. &quot;...the AUC_weighted is a primary metric that calculates the contribution of every class based on the relative number of samples representing that class, hence is more robust against imbalance.&quot;</p></blockquote>
<blockquote><p><strong>bbhiri</strong> <code>(Sat 06 May 2023 13:33)</code> - <em>Upvotes: 7</em></p><p>B. is correct response</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Tue 18 Jun 2024 01:46)</code> - <em>Upvotes: 2</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Sun 03 Sep 2023 07:35)</code> - <em>Upvotes: 2</em></p><p>on 2/9/21</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jul 2023 14:10)</code> - <em>Upvotes: 3</em></p><p>On exam 2021/7/10</p></blockquote>

</details>

---

[<< Previous Question](question_252.md) | [Home](../index.md) | [Next Question >>](question_254.md)
