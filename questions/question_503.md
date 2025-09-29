# Question 503

You need to implement a feature engineering strategy for the crowd sentiment local models.

What should you do?

- A.Apply an analysis of variance (ANOVA).
- B.Apply a Pearson correlation coefficient.
- C.Apply a Spearman correlation coefficient.
- D.Apply a linear discriminant analysis.

<details>
  <summary>Show Suggested Answer</summary>

<strong>D</strong><br>

<p>The linear discriminant analysis method works only on continuous variables, not categorical or ordinal variables.</p>
<p>Linear discriminant analysis is similar to analysis of variance (ANOVA) in that it works by comparing the means of the variables.</p>
<p>Scenario:</p>
<p>Data scientists must build notebooks in a local environment using automatic feature engineering and model building in machine learning pipelines.</p>
<p>Experiments for local crowd sentiment models must combine local penalty detection data.</p>
<p>All shared features for local models are continuous variables.</p>
<p>Incorrect Answers:</p>
<p>B: The Pearson correlation coefficient, sometimes called Pearson&#x27;s R test, is a statistical value that measures the linear relationship between two variables. By examining the coefficient values, you can infer something about the strength of the relationship between the two variables, and whether they are positively correlated or negatively correlated.</p>
<p>C: Spearman&#x27;s correlation coefficient is designed for use with non-parametric and non-normally distributed data. Spearman&#x27;s coefficient is a nonparametric measure of statistical dependence between two variables, and is sometimes denoted by the Greek letter rho. The Spearman&#x27;s coefficient expresses the degree to which two variables are monotonically related. It is also called Spearman rank correlation, because it can be used with ordinal variables.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/fisher-linear-discriminant-analysis https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/compute-linear-correlation</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>haby</strong> <code>(Thu 20 Jun 2024 17:45)</code> - <em>Upvotes: 1</em></p><p>A,B,C are methods of Filter Feature Selection, while LDA is a Dimensionality Reduction method and works for categorical target. In this case, I will take D.</p></blockquote>
<blockquote><p><strong>ferren</strong> <code>(Tue 07 May 2024 22:22)</code> - <em>Upvotes: 1</em></p><p>chatgpt says D</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 31 Jan 2024 18:56)</code> - <em>Upvotes: 2</em></p><p>In the context of feature engineering for the crowd sentiment local models, which include audio data and need to detect similar sounds, a Pearson correlation coefficient (B) would be a suitable strategy.

The Pearson correlation coefficient measures the linear relationship between two datasets, which could be valuable in this scenario to understand which features most strongly correlate with positive or negative crowd sentiment. This could involve correlations between specific sound features in the audio data and the sentiment label.

While the other techniques mentioned (ANOVA, Spearman correlation coefficient, and linear discriminant analysis) can be useful in certain circumstances, the Pearson correlation coefficient is more relevant in this scenario where you might be dealing with continuous features (like sound frequencies or volumes) and you are interested in linear relationships with the target variable (sentiment).</p></blockquote>

<blockquote><p><strong>ning</strong> <code>(Sat 17 Dec 2022 12:26)</code> - <em>Upvotes: 1</em></p><p>MLP combined with LDA ...
As mentioned in question, MLP is used for sentiment analysis, multiple layers ...
Then my guess will be LDA for feature reduction ...
Which here is called feature engineering ...
No other things are related with feature reduction ...</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Sun 28 Nov 2021 17:49)</code> - <em>Upvotes: 2</em></p><p>these questions seems to be based on Machine Learning Studio (classic). is this still in the syllabus</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Sun 28 Nov 2021 17:51)</code> - <em>Upvotes: 2</em></p><p>This method is often used for dimensionality reduction, because it projects a set of features onto a smaller feature space while preserving the information that discriminates between classes. This not only reduces computational costs for a given classification task, but can help prevent overfitting.

To generate the scores, you provide a label column and set of numerical feature columns as inputs. The algorithm determines the optimal combination of the input columns that linearly separates each group of data while minimizing the distances within each group. The module returns a dataset containing the compact, transformed features, along with a transformation that you can save and apply to another dataset.</p></blockquote>

</details>

---

[<< Previous Question](question_502.md) | [Home](../index.md) | [Next Question >>](question_504.md)
