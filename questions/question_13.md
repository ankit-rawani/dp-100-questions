# Question 13

You need to consider the underlined segment to establish whether it is accurate.

To transform a categorical feature into a binary indicator, you should make use of the Clean Missing Data module.

Select `No adjustment required` if the underlined segment is accurate. If the underlined segment is inaccurate, select the accurate option.

* A.No adjustment required.
* B.Convert to Indicator Values
* C.Apply SQL Transformation
* D.Group Categorical Values

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Peeking</strong> <code>(Sun 16 Jul 2023 01:40)</code> - <em>Upvotes: 6</em></p><p>This is equivalent to one-hot encoding of a categorical column</p></blockquote>
<blockquote><p><strong>Sjefen</strong> <code>(Sun 18 Sep 2022 10:41)</code> - <em>Upvotes: 5</em></p><p>Correct</p></blockquote>
<blockquote><p><strong>lianaliam</strong> <code>(Fri 06 Jun 2025 10:20)</code> - <em>Upvotes: 1</em></p><p>OHC for categirical column</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 21:03)</code> - <em>Upvotes: 2</em></p><p>The answer is correct. B

&quot;....the Convert to Indicator Values module in Machine Learning Studio (classic). The purpose of this module is to convert columns that contain categorical values into a series of binary indicator columns that can more easily be used as features in a machine learning model.&quot;
See https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/convert-to-indicator-values</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 21:04)</code> - <em>Upvotes: 1</em></p><p>Usage tips
&gt;&gt; If the column contains missing values, a separate indicator column is created for the missing category, with this name: &lt;source column&gt;- Missing

See https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/convert-to-indicator-values#usage-tips</p></blockquote>
<blockquote><p><strong>amiria7</strong> <code>(Thu 10 Aug 2023 15:00)</code> - <em>Upvotes: 1</em></p><p>The answer is correct</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 11 Apr 2023 02:49)</code> - <em>Upvotes: 3</em></p><p>Correct</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Mon 12 Sep 2022 09:37)</code> - <em>Upvotes: 2</em></p><p>correct</p></blockquote>

</details>

---

[<< Previous Question](question_12.md) | [Home](/index.md) | [Next Question >>](question_14.md)
