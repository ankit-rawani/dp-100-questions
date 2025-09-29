# Question 516

HOTSPOT -

You need to set up the Permutation Feature Importance module according to the model training requirements.

Which properties should you select? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q516_q_0035900001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q516_ans_0_0036000001.png" alt="Answer Image"><br>

<p>Box 1: Accuracy -</p>
<p>Scenario: You want to configure hyperparameters in the model learning process to speed the learning phase by using hyperparameters. In addition, this configuration should cancel the lowest performing runs at each evaluation interval, thereby directing effort and resources towards models that are more likely to be successful.</p>
<p>Box 2: R-Squared</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Alexandra</strong> <code>(Wed 05 Jan 2022 12:39)</code> - <em>Upvotes: 18</em></p><p>because it is required to produce ROC curve, I think f-score is the correct answer for the classification task</p></blockquote>
<blockquote><p><strong>spaceykacey</strong> <code>(Fri 12 May 2023 07:49)</code> - <em>Upvotes: 1</em></p><p>yes but why R2 as measure of performance?</p></blockquote>
<blockquote><p><strong>hendrata</strong> <code>(Thu 09 Dec 2021 20:45)</code> - <em>Upvotes: 6</em></p><p>Why would we select Accuracy? This is a regression problem and not a classification problem, I would have thought we only need to select one of the answers in the regression box only.</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Tue 20 Sep 2022 12:42)</code> - <em>Upvotes: 1</em></p><p>this is indeed classification. check option again</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sun 25 Aug 2024 23:46)</code> - <em>Upvotes: 1</em></p><p>For the Permutation Feature Importance module, the following metrics should be selected for measuring performance:

Metric for measuring performance for classification:

A) F-Score
Metric for measuring performance for regression:

D) MAE or A) RMSE (depending on the specific requirements of the model training)</p></blockquote>

<blockquote><p><strong>JJason</strong> <code>(Tue 23 May 2023 08:34)</code> - <em>Upvotes: 3</em></p><p>why not RMSE?</p></blockquote>
<blockquote><p><strong>Abhinav_nasaiitkgp</strong> <code>(Thu 21 Jul 2022 20:09)</code> - <em>Upvotes: 4</em></p><p>Completely weird options as for classification we can use precision, recall and F score and Accuracy. Any option is not wrong.</p></blockquote>
<blockquote><p><strong>swatidorge</strong> <code>(Thu 12 May 2022 08:18)</code> - <em>Upvotes: 1</em></p><p>why not precision for classifications?</p></blockquote>
<blockquote><p><strong>geraldhermannerich</strong> <code>(Fri 04 Mar 2022 13:38)</code> - <em>Upvotes: 1</em></p><p>Isn&#x27;t MAE a continous metric, hence not applicable here?</p></blockquote>

</details>

---

[<< Previous Question](question_515.md) | [Home](/index.md) | [Next Question >>](question_517.md)
