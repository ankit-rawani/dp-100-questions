# Question 462

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You train a classification model by using a logistic regression algorithm.

You must be able to explain the model's predictions by calculating the importance of each feature, both as an overall global relative importance value and as a measure of local importance for a specific set of predictions.

You need to create an explainer that you can use to retrieve the required global and local feature importance values.

Solution: Create a PFIExplainer.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>shivaborusu</strong> <code>(Sat 15 May 2021 14:00)</code> - <em>Upvotes: 38</em></p><p>There is no Local Importance Explanation for Permutation Feature Importance.
Mimic and Tabular Explainers has it.The answer is YES</p></blockquote>
<blockquote><p><strong>aziti</strong> <code>(Thu 01 Jul 2021 02:34)</code> - <em>Upvotes: 5</em></p><p>Mimic explainer is based on the idea of training global surrogate models to mimic blackbox models. The way I see it it seems as if Mimic  explainer is one with only global importance
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability</p></blockquote>
<blockquote><p><strong>ralucabala</strong> <code>(Thu 21 Oct 2021 17:51)</code> - <em>Upvotes: 1</em></p><p>I was thinking the same way, but it says it&#x27;s a Logistic Regression not Linear and not decision tree or the other surrogate models supported by Mimix Explainer. So, do we have explainability for logistic regressions also or not?</p></blockquote>
<blockquote><p><strong>ralucabala</strong> <code>(Thu 21 Oct 2021 17:52)</code> - <em>Upvotes: 1</em></p><p>Found it here https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability-aml</p></blockquote>
<blockquote><p><strong>aziti</strong> <code>(Thu 01 Jul 2021 02:35)</code> - <em>Upvotes: 2</em></p><p>my bad you&#x27;re correct</p></blockquote>
<blockquote><p><strong>Abhinav_nasaiitkgp</strong> <code>(Fri 23 Jul 2021 20:54)</code> - <em>Upvotes: 10</em></p><p>Answer is Yes
Mimic explains both local and global feature importance
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability-automl</p></blockquote>
<blockquote><p><strong>slashssab</strong> <code>(Fri 15 Apr 2022 11:10)</code> - <em>Upvotes: 7</em></p><p>Question is about PFIExplainer, so answer should be &quot;No&quot;</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 24 Aug 2023 00:49)</code> - <em>Upvotes: 3</em></p><p>B. No. The PFIExplainer doesn&#x27;t support local feature importance explanations.</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sun 18 Dec 2022 02:52)</code> - <em>Upvotes: 1</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Mon 12 Dec 2022 14:23)</code> - <em>Upvotes: 3</em></p><p>PFI cannot do local / instance level!</p></blockquote>
<blockquote><p><strong>eeah</strong> <code>(Fri 14 Oct 2022 23:50)</code> - <em>Upvotes: 2</em></p><p>Ans is NO. This was the practice test official answer. Global/local arguments from discussion are correct.</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 13 Sep 2022 05:00)</code> - <em>Upvotes: 5</em></p><p>PFIExplainer is the only explainer that does not support local importance. So it does not meet the reqs in this case. Answer is B</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Tue 14 Jun 2022 17:34)</code> - <em>Upvotes: 1</em></p><p>The Answer should be NO</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Wed 08 Jun 2022 16:19)</code> - <em>Upvotes: 4</em></p><p>PFI can explain the overall behavior of any underlying model but does not explain individual predictions.</p></blockquote>
<blockquote><p><strong>akuamorgan</strong> <code>(Wed 30 Mar 2022 14:04)</code> - <em>Upvotes: 5</em></p><p>y all these confusion? Mimic and tabular support global n local. PFI only support global. so the answer is No. the PFI solution doesnt meet the goal</p></blockquote>
<blockquote><p><strong>frida321</strong> <code>(Sun 27 Mar 2022 12:59)</code> - <em>Upvotes: 4</em></p><p>I suppose it should be NO. PFI can&#x27;t explain local importance</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Tue 25 Jan 2022 06:01)</code> - <em>Upvotes: 1</em></p><p>You need to create an explainer that you can use to retrieve the required global and local feature importance values.
Solution: Create a PFIExplainer.
Does the solution meet the goal?

????</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Sun 26 Dec 2021 19:42)</code> - <em>Upvotes: 2</em></p><p>answer should be Yes
Permutation Feature Importance (PFI) model explainer canonly be used to explain how strongly the features contribute to the prediction at the dataset level, itdoesn’t support evaluation of local importances.
Mimic Explainer can be used for interpreting both the global and local importance of features,
Tabular Explainer can be used for interpreting both the global and local importance of features</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Thu 08 Aug 2024 01:13)</code> - <em>Upvotes: 1</em></p><p>then why you said yes?</p></blockquote>
<blockquote><p><strong>iamnagesh</strong> <code>(Fri 17 Dec 2021 11:18)</code> - <em>Upvotes: 1</em></p><p>https://docs.microsoft.com/en-us/learn/modules/explain-machine-learning-models-with-azure-machine-learning/3-explainers</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Mon 20 Sep 2021 03:08)</code> - <em>Upvotes: 4</em></p><p>in the sample notebook comment its states that &quot;
# Note: Do not run this cell if using PFIExplainer, it does not support local explanations&quot;
So answer is Yes. Given answer No is wrong.
ref: https://github.com/interpretml/interpret-community/blob/master/notebooks/advanced-feature-transformations-explain-local.ipynb</p></blockquote>

</details>

---

[<< Previous Question](question_461.md) | [Home](/index.md) | [Next Question >>](question_463.md)
