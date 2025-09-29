# Question 517

You need to select a feature extraction method.

Which method should you use?

* A.Mutual information
* B.Mood's median test
* C.Kendall correlation
* D.Permutation Feature Importance

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jackreacher</strong> <code>(Tue 23 Nov 2021 03:49)</code> - <em>Upvotes: 8</em></p><p>Linear regression module -
When you train a Linear Regression module, you must determine the best features to use in a model. You can choose standard metrics provided to measure performance before and after the feature importance process completes. 

So the answer should be permutation feature importance</p></blockquote>
<blockquote><p><strong>111ssy</strong> <code>(Fri 03 Dec 2021 20:56)</code> - <em>Upvotes: 4</em></p><p>&quot;In this module, feature values are randomly shuffled, one column at a time, and the performance of the model is measured before and after. You can choose one of the standard metrics provided to measure performance.&quot;

https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/permutation-feature-importance</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sat 12 Oct 2024 04:31)</code> - <em>Upvotes: 4</em></p><p>Feature extraction method: 
1) Pearson&#x27;s correlation
2) Kendall&#x27;s rank correlation
3) Spearman&#x27;s rank correlation

https://www.phdata.io/blog/data-science-stats-review/

The question given 4 choices, has one choice for &quot;Kendall correlation&quot; --&gt; Choose C - Kendall correaltion for FEATURE EXTRACTION METHOD.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Mon 26 Feb 2024 00:54)</code> - <em>Upvotes: 1</em></p><p>Mutual information is a widely used feature extraction method in machine learning, especially in the context of feature selection. It is a statistical method that measures the amount of information that one feature provides about the other.

The main advantage of mutual information is that it can capture non-linear dependencies between variables, making it a powerful technique for extracting relevant features from complex data sets. It is also a computationally efficient method, which can handle high-dimensional data sets.

On the other hand, Mood&#x27;s median test, Kendall correlation, and Permutation Feature Importance are not feature extraction methods, but rather statistical tests or feature importance measures that can be used in the context of feature selection. They do not provide a direct way of extracting features from the data, but rather help in identifying the most relevant features for a given problem.

Therefore, in this case, the best option is to choose Mutual information as a feature extraction method.</p></blockquote>

</details>

---

[<< Previous Question](question_516.md) | [Home](/index.md) | [Next Question >>](question_518.md)
