# Question 518

HOTSPOT -

You need to configure the Feature Based Feature Selection module based on the experiment requirements and datasets.

How should you configure the module properties? To answer, select the appropriate options in the dialog box in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q518_q_0036200001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q518_ans_0_0036300001.png" alt="Answer Image"><br>
<p>Box 1: Mutual Information.</p>
<p>The mutual information score is particularly useful in feature selection because it maximizes the mutual information between the joint distribution and target variables in datasets with many dimensions.</p>
<p>Box 2: MedianValue -</p>
<p>MedianValue is the feature column, , it is the predictor of the dataset.</p>
<p>Scenario: The MedianValue and AvgRoomsinHouse columns both hold data in numeric format. You need to select a feature selection algorithm to analyze the relationship between the two columns in more detail.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/filter-based-feature-selection</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jed_elhak</strong> <code>(Thu 19 Sep 2024 15:48)</code> - <em>Upvotes: 5</em></p><p>You must prioritize the columns of data for predicting the outcome(The mutual information score measures the contribution of a variable towards reducing uncertainty about the value of another variable: namely, the label). You must use non-parametric statistics to measure relationships. i think asnwer is Mutual information</p></blockquote>
<blockquote><p><strong>iuolu</strong> <code>(Tue 07 May 2024 00:16)</code> - <em>Upvotes: 1</em></p><p>Fisher test is better, it is similar to Chi squared but fisher is more exact, choose Fisher score</p></blockquote>
<blockquote><p><strong>jed_elhak</strong> <code>(Thu 19 Sep 2024 15:37)</code> - <em>Upvotes: 1</em></p><p>fisher is parmametric</p></blockquote>
<blockquote><p><strong>jed_elhak</strong> <code>(Thu 19 Sep 2024 15:38)</code> - <em>Upvotes: 1</em></p><p>and chi squared also is parapetric theay asked for non parametric</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Tue 19 Mar 2024 12:58)</code> - <em>Upvotes: 3</em></p><p>I think the answer is Fisher Score 

Fisher Score:	Label can be text or numeric but features must be numeric.
Mutual Information: Labels and features can be text or numeric. Use this method for computing feature importance for two categorical columns.
Chi Squared: Labels and features can be text or numeric. Use this method for computing feature importance for two categorical columns.</p></blockquote>
<blockquote><p><strong>Abhinav_nasaiitkgp</strong> <code>(Sun 21 Jan 2024 21:21)</code> - <em>Upvotes: 2</em></p><p>Since both MedianValue and Averagenumber of house is numerical variable, we should use Fisher Price</p></blockquote>
<blockquote><p><strong>jackreacher</strong> <code>(Thu 23 Nov 2023 03:33)</code> - <em>Upvotes: 4</em></p><p>The answer should be Fisher Score since the label and the features are numeric values. Chi Squared and Mutual information for categorical values.</p></blockquote>
<blockquote><p><strong>swatidorge</strong> <code>(Sun 12 Nov 2023 09:27)</code> - <em>Upvotes: 2</em></p><p>By the definition of Mutual Information, a low value should mean that one feature does not give me information about the other and by the definition of Chi Square, a low value of Chi Square means that the two features must be independent.

Hence i guess Chi square is not used and mutual information is used</p></blockquote>
<blockquote><p><strong>user11111</strong> <code>(Fri 01 Sep 2023 05:12)</code> - <em>Upvotes: 2</em></p><p>The answer is counts. Chi square and mutual information applies to categorical data.
Since there is only 1 feature we looking at meaning there&#x27;s only one dataset it cannot be Fisher.
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/filter-based-feature-selection</p></blockquote>
<blockquote><p><strong>jackreacher</strong> <code>(Thu 23 Nov 2023 03:38)</code> - <em>Upvotes: 2</em></p><p>Count don&#x27;t require label, so it cannot be</p></blockquote>
<blockquote><p><strong>nato16</strong> <code>(Sat 30 Sep 2023 18:50)</code> - <em>Upvotes: 1</em></p><p>Target column is MedianValue is contious variables, so I don&#x27;t see any reason to use Chi Square. In addion, Fisher test and Chi Sqaure can be exchanged with each other.</p></blockquote>

</details>

---

[<< Previous Question](question_517.md) | [Home](/index.md) | [Next Question >>](question_519.md)
