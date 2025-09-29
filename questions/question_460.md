# Question 460

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You train a classification model by using a logistic regression algorithm.

You must be able to explain the model's predictions by calculating the importance of each feature, both as an overall global relative importance value and as a measure of local importance for a specific set of predictions.

You need to create an explainer that you can use to retrieve the required global and local feature importance values.

Solution: Create a MimicExplainer.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>OlivierM</strong> <code>(Mon 10 May 2021 13:47)</code> - <em>Upvotes: 36</em></p><p>Is this correct? The documentation explicitly says that PFIExplainer is the only explainer that does not support local importance</p></blockquote>
<blockquote><p><strong>chevyli</strong> <code>(Wed 08 Mar 2023 04:17)</code> - <em>Upvotes: 2</em></p><p>The solution is incorrect, nor its explanation</p></blockquote>
<blockquote><p><strong>shivaborusu</strong> <code>(Sat 15 May 2021 14:00)</code> - <em>Upvotes: 20</em></p><p>The answer is NO, there is no local explainer for PFI</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 18 Nov 2024 04:08)</code> - <em>Upvotes: 1</em></p><p>How MimicExplainer works
MimicExplainer works by training a simple, interpretable model (such as linear regression, decision trees, etc.) to mimic the behavior of the original complex model. The core idea of ​​this method is:

Train a new model so that its output is as close as possible to the output of the original model.
Use this new model to explain the original model because the new model itself is easy to interpret.</p></blockquote>

<blockquote><p><strong>deyoz</strong> <code>(Thu 08 Aug 2024 00:50)</code> - <em>Upvotes: 1</em></p><p>I think answer is No because, a mimic explainer is used to help interpret decisions made my black box models such as ANN. The one in this case is logistic regression, which isn&#x27;t  considered blackbox. However, i am not sure why Mimic explainer cannot bed used in logistic regression?</p></blockquote>
<blockquote><p><strong>Beauterham</strong> <code>(Sat 15 Jun 2024 12:49)</code> - <em>Upvotes: 1</em></p><p>Answer is No
 You can pass global and local but only return 1 value.

Parameters
explanation_types
list[str]
Required
A list of strings representing types of explanations desired. Currently, &#x27;global&#x27; and &#x27;local&#x27; are supported. Both may be passed in at once; only one explanation will be returned.
https://learn.microsoft.com/en-us/python/api/azureml-interpret/azureml.interpret.mimic_wrapper.mimicwrapper?view=azure-ml-py</p></blockquote>

<blockquote><p><strong>VuTon2025</strong> <code>(Fri 03 Nov 2023 15:34)</code> - <em>Upvotes: 1</em></p><p>NO. The solution is  PIPEExplainer does not support local. Ref:
  https://learn.microsoft.com/en-us/training/modules/explain-machine-learning-models-with-azure-machine-learning/3-explainers</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 24 Aug 2023 00:43)</code> - <em>Upvotes: 1</em></p><p>A  Yes</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sun 18 Dec 2022 02:51)</code> - <em>Upvotes: 2</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 13 Sep 2022 04:57)</code> - <em>Upvotes: 2</em></p><p>PFIExplainer is the only explainer that does not support local importance</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Sat 16 Jul 2022 05:03)</code> - <em>Upvotes: 1</em></p><p>The Question is

Solution: Create a MimicExplainer.
Does the solution meet the goal?

Ans should be NO as PFIE does not support local feature importance</p></blockquote>

<blockquote><p><strong>dija123</strong> <code>(Tue 14 Jun 2022 17:32)</code> - <em>Upvotes: 6</em></p><p>The answer should be Yes for Mimicexplainer.</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Mon 24 Apr 2023 08:39)</code> - <em>Upvotes: 1</em></p><p>Only PFIeplainer can&#x27;t support local.</p></blockquote>
<blockquote><p><strong>thhvancouver</strong> <code>(Mon 31 Jan 2022 18:07)</code> - <em>Upvotes: 8</em></p><p>Examtopic: The comments for PFIExplainer is switched with that of Mimicexplainer...</p></blockquote>
<blockquote><p><strong>Geezee999</strong> <code>(Wed 02 Nov 2022 00:17)</code> - <em>Upvotes: 3</em></p><p>Thank you for clarifying this for me as I was almost confused</p></blockquote>
<blockquote><p><strong>VJPrakash</strong> <code>(Fri 28 Jan 2022 18:11)</code> - <em>Upvotes: 16</em></p><p>The answer should be YES.
The question is - does the solution(Create a Mimicexplainer work). 
Based on the documentation - both Mimic and tabular explainer will be able to explain global and local, feature importance

https://docs.microsoft.com/en-us/learn/modules/explain-machine-learning-models-with-azure-machine-learning/3-explainers</p></blockquote>

<blockquote><p><strong>Moshekwa</strong> <code>(Mon 31 Jan 2022 00:02)</code> - <em>Upvotes: 2</em></p><p>According to the documentation A is the answer</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Tue 25 Jan 2022 06:00)</code> - <em>Upvotes: 2</em></p><p>The question is??
Solution: Create a MimicExplainer.
Does the solution meet the goal?</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Sun 26 Dec 2021 19:39)</code> - <em>Upvotes: 4</em></p><p>answer should be No
Permutation Feature Importance (PFI) model explainer canonly be used to explain how strongly the features contribute to the prediction at the dataset level, itdoesn’t support evaluation of local importances.
Mimic Explainer can be used for interpreting both the global andlocal importance of features,
Tabular Explainer can be used for interpreting both the globaland local importance of features</p></blockquote>
<blockquote><p><strong>iamnagesh</strong> <code>(Fri 17 Dec 2021 11:18)</code> - <em>Upvotes: 2</em></p><p>https://docs.microsoft.com/en-us/learn/modules/explain-machine-learning-models-with-azure-machine-learning/3-explainers</p></blockquote>
<blockquote><p><strong>hachascloud</strong> <code>(Sat 31 Jul 2021 16:22)</code> - <em>Upvotes: 3</em></p><p>Anseer is NO. answers for this scenario are inverted</p></blockquote>

</details>

---

[<< Previous Question](question_459.md) | [Home](../index.md) | [Next Question >>](question_461.md)
