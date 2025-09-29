# Question 507

You need to implement a model development strategy to determine a user's tendency to respond to an ad.

Which technique should you use?

- A.Use a Relative Expression Split module to partition the data based on centroid distance.
- B.Use a Relative Expression Split module to partition the data based on distance travelled to the event.
- C.Use a Split Rows module to partition the data based on distance travelled to the event.
- D.Use a Split Rows module to partition the data based on centroid distance.

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

<p>Split Data partitions the rows of a dataset into two distinct sets.</p>
<p>The Relative Expression Split option in the Split Data module of Azure Machine Learning Studio is helpful when you need to divide a dataset into training and testing datasets using a numerical expression.</p>
<p>Relative Expression Split: Use this option whenever you want to apply a condition to a number column. The number could be a date/time field, a column containing age or dollar amounts, or even a percentage. For example, you might want to divide your data set depending on the cost of the items, group people by age ranges, or separate data by a calendar date.</p>
<p>Scenario:</p>
<p>Local market segmentation models will be applied before determining a user&#x27;s propensity to respond to an advertisement.</p>
<p>The distribution of features across training and production data are not consistent</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/split-data</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>juandante</strong> <code>(Mon 22 Apr 2024 15:45)</code> - <em>Upvotes: 9</em></p><p>Seems the answer is indeed &quot;Relative Expression Split&quot;</p></blockquote>
<blockquote><p><strong>Codia</strong> <code>(Thu 17 Oct 2024 20:47)</code> - <em>Upvotes: 1</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/split-data-using-regular-expression</p></blockquote>

</details>

---

[<< Previous Question](question_506.md) | [Home](../index.md) | [Next Question >>](question_508.md)
