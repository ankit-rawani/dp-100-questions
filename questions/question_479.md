# Question 479

HOTSPOT -

You train a classification model by using a decision tree algorithm.

You create an estimator by running the following Python code. The variable feature_names is a list of all feature names, and class_names is a list of all class names. from interpret.ext.blackbox import TabularExplainer explainer = TabularExplainer(model, x_train, features=feature_names, classes=class_names)

You need to explain the predictions made by the model for all classes by determining the importance of all features.

For each of the following statements, select Yes if the statement is true. Otherwise, select No.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q479_q_0044800001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q479_ans_0_image620.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>claudiapatricia777</strong> <code>(Sat 09 Apr 2022 14:26)</code> - <em>Upvotes: 16</em></p><p>Answer is : Yes: No doubt - 2 - Yes: feature and class are optional arguments - 3 - Yes: Mimic also supports Tree based algorithms.</p></blockquote>
<blockquote><p><strong>Ben999</strong> <code>(Sun 29 Dec 2024 06:00)</code> - <em>Upvotes: 1</em></p><p>Y,Y,N. - For MimicExplainer you would need to import the MimicExplainer class, which is not the case here.</p></blockquote>
<blockquote><p><strong>dushmantha</strong> <code>(Mon 28 Feb 2022 10:25)</code> - <em>Upvotes: 8</em></p><p>Answer should be
yes: no doubt
no: there is no way that explainer knows what is class variable
yes: explainers has no restrictions to be used in a tree based method</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Thu 08 Aug 2024 02:50)</code> - <em>Upvotes: 1</em></p><p>field classes is optional</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Thu 08 Aug 2024 02:54)</code> - <em>Upvotes: 1</em></p><p>oh yes i overlooked the phrase &quot;as expected&quot; . i totally agree with your answer. the tone of the question give some hint that the model works without these parameters , but might not work as expected.</p></blockquote>
<blockquote><p><strong>haby</strong> <code>(Sat 22 Jun 2024 18:02)</code> - <em>Upvotes: 1</em></p><p>1- Yes
2- No - features and classes fields are optional, true, but without adding them, they work but can&#x27;t work &quot;as expected&quot;
3- Yes</p></blockquote>
<blockquote><p><strong>haby</strong> <code>(Sat 22 Jun 2024 18:05)</code> - <em>Upvotes: 1</em></p><p>My bad, 2nd is Yes. features and classes only change visualization result.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 24 Aug 2023 03:47)</code> - <em>Upvotes: 2</em></p><p>YYY.
2 - Yes: feature and class are optional arguments</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 24 Aug 2023 03:46)</code> - <em>Upvotes: 1</em></p><p>YES YES YES</p></blockquote>
<blockquote><p><strong>casiopa</strong> <code>(Mon 12 Jun 2023 09:53)</code> - <em>Upvotes: 1</em></p><p>1-Yes
2-Yes
3-No

3- could be a NO because for a MimicExplainer you would need to specify the argument: explainable_model. Otherwise, a MimicExplainer is a valid choice.

Ex:
explainer = MimicExplainer(model, x_train, explainable_model=DecisionTreeExplainableModel, features=feature_names, classes=class_names)</p></blockquote>

<blockquote><p><strong>pancman</strong> <code>(Thu 13 Oct 2022 03:20)</code> - <em>Upvotes: 1</em></p><p>You can refer to TabularExplainer documentation here:
https://interpret-community.readthedocs.io/en/latest/api_reference/interpret_community.html?highlight=tabularexplainer#interpret_community.TabularExplainer</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Wed 08 Jun 2022 18:00)</code> - <em>Upvotes: 3</em></p><p>1- Yes
2- Yes as &quot;features&quot; and &quot;classes&quot; fields are optional
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability-aml
3- Yes</p></blockquote>
<blockquote><p><strong>azayra</strong> <code>(Thu 28 Apr 2022 10:36)</code> - <em>Upvotes: 2</em></p><p>yes , yes and yes</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Thu 03 Mar 2022 08:42)</code> - <em>Upvotes: 1</em></p><p>on 2/9/21</p></blockquote>
<blockquote><p><strong>saurabh288</strong> <code>(Fri 21 Jan 2022 16:12)</code> - <em>Upvotes: 3</em></p><p>MimicExplainer can also be used here.</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 15:25)</code> - <em>Upvotes: 6</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>Srik33</strong> <code>(Tue 04 Jan 2022 18:11)</code> - <em>Upvotes: 3</em></p><p>Why cant MIMIC be used here , they also can be used for Linerar Regression black box models</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Tue 25 Jan 2022 16:32)</code> - <em>Upvotes: 1</em></p><p>You can use one of the following interpretable models as your surrogate model: LightGBM (LGBMExplainableModel), Linear Regression (LinearExplainableModel)

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability</p></blockquote>

<blockquote><p><strong>thhvancouver</strong> <code>(Mon 31 Jan 2022 18:28)</code> - <em>Upvotes: 5</em></p><p>According to the documentation: You can use one of the following interpretable models as your surrogate model: LightGBM (LGBMExplainableModel), Linear Regression (LinearExplainableModel), Stochastic Gradient Descent explainable model (SGDExplainableModel), and Decision Tree (DecisionTreeExplainableModel). So a MimicExplainer can also be used with Decision Tree.</p></blockquote>

</details>

---

[<< Previous Question](question_478.md) | [Home](/index.md) | [Next Question >>](question_480.md)
