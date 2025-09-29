# Question 459

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You train a classification model by using a logistic regression algorithm.

You must be able to explain the model's predictions by calculating the importance of each feature, both as an overall global relative importance value and as a measure of local importance for a specific set of predictions.

You need to create an explainer that you can use to retrieve the required global and local feature importance values.

Solution: Create a TabularExplainer.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>hendriktytgatpwc</strong> <code>(Tue 14 Sep 2021 16:16)</code> - <em>Upvotes: 26</em></p><p>This answer should be YES:
Tabular Explainer can explain local and global plus it works with Logistic Regression, only explainer that doesn&#x27;t explain local is PFI explainer</p></blockquote>
<blockquote><p><strong>Moshekwa</strong> <code>(Mon 31 Jan 2022 00:03)</code> - <em>Upvotes: 2</em></p><p>Answer is indeed Yes..

https://docs.microsoft.com/en-us/learn/modules/explain-machine-learning-models-with-azure-machine-learning/3-explainers</p></blockquote>

<blockquote><p><strong>PI_Team</strong> <code>(Tue 11 Jun 2024 14:41)</code> - <em>Upvotes: 1</em></p><p>Correct answer is YES</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 24 Aug 2023 00:46)</code> - <em>Upvotes: 1</em></p><p>A Yes. Based on the documentation - both Mimic and tabular explainer will be able to explain global and local, feature importance https://docs.microsoft.com/en-us/learn/modules/explain-machine-learning-models-with-azure-machine-learning/3-explainers.</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sun 18 Dec 2022 02:51)</code> - <em>Upvotes: 1</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 13 Sep 2022 04:58)</code> - <em>Upvotes: 2</em></p><p>PFIExplainer is the only explainer that does not support local importance</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Tue 14 Jun 2022 17:33)</code> - <em>Upvotes: 2</em></p><p>The answer should be Yes for Tabular Explainer</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Sun 26 Dec 2021 19:39)</code> - <em>Upvotes: 3</em></p><p>answer should be yes
Permutation Feature Importance (PFI) model explainer canonly be used to explain how strongly the features contribute to the prediction at the dataset level, itdoesn’t support evaluation of local importances.
Mimic Explainer can be used for interpreting both the global andlocal importance of features,
Tabular Explainer can be used for interpreting both the globaland local importance of features</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Sun 26 Dec 2021 19:38)</code> - <em>Upvotes: 1</em></p><p>answer should be yes
Tabular Explainer can be used for interpreting both the global and local importance of features</p></blockquote>
<blockquote><p><strong>iamnagesh</strong> <code>(Fri 17 Dec 2021 11:17)</code> - <em>Upvotes: 1</em></p><p>https://docs.microsoft.com/en-us/learn/modules/explain-machine-learning-models-with-azure-machine-learning/3-explainers</p></blockquote>
<blockquote><p><strong>jasonbourne7158</strong> <code>(Sun 07 Nov 2021 07:05)</code> - <em>Upvotes: 2</em></p><p>It should be: Yes.</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Sat 18 Sep 2021 08:18)</code> - <em>Upvotes: 4</em></p><p>PFIExplainer does not support local explanations.</p></blockquote>
<blockquote><p><strong>Anty85</strong> <code>(Wed 22 Sep 2021 11:13)</code> - <em>Upvotes: 3</em></p><p>Yet the tabular one does, so the provided answer is wrong...</p></blockquote>
<blockquote><p><strong>hendriktytgatpwc</strong> <code>(Tue 14 Sep 2021 16:16)</code> - <em>Upvotes: 1</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability-aml</p></blockquote>

</details>

---

[<< Previous Question](question_458.md) | [Home](../index.md) | [Next Question >>](question_460.md)
