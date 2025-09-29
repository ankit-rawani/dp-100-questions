# Question 214

You plan to use automated machine learning to train a regression model. You have data that has features which have missing values, and categorical features with few distinct values.

You need to configure automated machine learning to automatically impute missing values and encode categorical features as part of the training task.

Which parameter and value pair should you use in the AutoMLConfig class?

- A.featurization = 'auto'
- B.enable_voting_ensemble = True
- C.task = 'classification'
- D.exclude_nan_labels = True
- E.enable_tf = True

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>datamijn</strong> <code>(Wed 02 Feb 2022 09:49)</code> - <em>Upvotes: 8</em></p><p>on 2/8/2021</p></blockquote>
<blockquote><p><strong>Moshekwa</strong> <code>(Sat 29 Jan 2022 22:04)</code> - <em>Upvotes: 6</em></p><p>Chosen Answer is correct
&quot; In every automated machine learning experiment, automatic scaling and normalization techniques are applied to your data by default. These techniques are types of featurization that help certain algorithms that are sensitive to features on different scales. You can enable more featurization, such as missing-values imputation, encoding, and transforms.&quot;
Source:
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-features</p></blockquote>
<blockquote><p><strong>sar77</strong> <code>(Sat 19 Jul 2025 02:19)</code> - <em>Upvotes: 1</em></p><p>In Azure Machine Learning&#x27;s AutoMLConfig, setting featurization=&#x27;auto&#x27; allows the system to automatically handle:

Imputation of missing values: Numerical and categorical features with missing data will be filled in using suitable methods (like mean, median, mode, or advanced techniques).

Encoding of categorical variables: Categorical features with few distinct values will be encoded automatically using one-hot encoding or ordinal encoding, depending on what suits the model best.</p></blockquote>

<blockquote><p><strong>evangelist</strong> <code>(Mon 02 Dec 2024 12:25)</code> - <em>Upvotes: 1</em></p><p>given answer is correct featurization =on is must</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Thu 28 Dec 2023 12:11)</code> - <em>Upvotes: 1</em></p><p>A - ChatGPT</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Wed 14 Sep 2022 06:36)</code> - <em>Upvotes: 2</em></p><p>AutoFeaturization takes care of this. A</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Thu 03 Mar 2022 08:31)</code> - <em>Upvotes: 4</em></p><p>on 2/9/21</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 15:04)</code> - <em>Upvotes: 6</em></p><p>On exam 2021/7/10</p></blockquote>

</details>

---

[<< Previous Question](question_213.md) | [Home](../index.md) | [Next Question >>](question_215.md)
