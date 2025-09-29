# Question 482

DRAG DROP -

You have several machine learning models registered in an Azure Machine Learning workspace.

You must use the Fairlearn dashboard to assess fairness in a selected model.

Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Select and Place:

![Question Image](images/q482_q_0044900001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q482_ans_0_0045000001.png" alt="Answer Image"><br>
<p>Step 1: Select a model feature to be evaluated.</p>
<p>Step 2: Select a binary classification or regression model.</p>
<p>Register your models within Azure Machine Learning. For convenience, store the results in a dictionary, which maps the id of the registered model (a string in name:version format) to the predictor itself.</p>
<p>Example:</p>
<p>model_dict = {}</p>
<p>lr_reg_id = register_model(&quot;fairness_logistic_regression&quot;, lr_predictor) model_dict[lr_reg_id] = lr_predictor svm_reg_id = register_model(&quot;fairness_svm&quot;, svm_predictor) model_dict[svm_reg_id] = svm_predictor</p>
<p>Step 3: Select a metric to be measured</p>
<p>Precompute fairness metrics.</p>
<p>Create a dashboard dictionary using Fairlearn&#x27;s metrics package.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-fairness-aml</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ranjsi01</strong> <code>(Tue 25 Jan 2022 20:12)</code> - <em>Upvotes: 11</em></p><p>model, feature, metric (just switch a and b in answer area)</p></blockquote>
<blockquote><p><strong>giusecozza</strong> <code>(Thu 08 Sep 2022 08:37)</code> - <em>Upvotes: 1</em></p><p>Yes, it seems the right order. Just take a look at the notebook from MS Learn:

https://microsoftlearning.github.io/mslearn-dp100/instructions/15-detect-unfairness.html</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 25 Oct 2022 06:07)</code> - <em>Upvotes: 3</em></p><p>Answers do not need to be in order.
Smple Code:
sf = { &#x27;Race&#x27;: A_test.race, &#x27;Sex&#x27;: A_test.sex }

from fairlearn.metrics._group_metric_set import _create_group_metric_set

dash_dict = _create_group_metric_set(y_true=Y_test,
                                    predictions=ys_pred,
                                    sensitive_features=sf,
                                    prediction_type=&#x27;binary_classification&#x27;)

https://learn.microsoft.com/zh-tw/azure/machine-learning/how-to-machine-learning-fairness-aml</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 25 Oct 2022 06:10)</code> - <em>Upvotes: 2</em></p><p>My fault, the answers need to be in order.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 24 Feb 2023 05:09)</code> - <em>Upvotes: 6</em></p><p>The three actions that you should perform in sequence to use the Fairlearn dashboard to assess fairness in a selected model are:

Select a binary classification or regression model: Fairlearn is a toolkit for assessing and improving fairness in binary classification and regression models. Therefore, you need to select a model that falls into one of these two categories.

Select a metric to be measured: After selecting the model, you need to choose a metric to be measured. Fairlearn provides a range of fairness metrics, such as demographic parity, equalized odds, and equal opportunity, that can be used to assess how the model performs across different groups.

Select a model feature to be evaluated: Once you have selected the model and the metric, you need to choose a model feature to be evaluated. This could be any feature that you believe may have an impact on the fairness of the model, such as race, gender, or age. You can use Fairlearn to analyze the model&#x27;s performance across different subgroups based on this feature.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 24 Jun 2024 09:39)</code> - <em>Upvotes: 3</em></p><p>Fairlearn works with binary classification or regression models, so you need to select one of these first.
Next, you need to choose what metric you want to use to measure fairness.
Finally, you select which feature of the model you want to evaluate for fairness.</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Sun 01 Dec 2024 18:03)</code> - <em>Upvotes: 1</em></p><p>I agree</p></blockquote>
<blockquote><p><strong>vv_bb</strong> <code>(Sun 26 Nov 2023 12:49)</code> - <em>Upvotes: 1</em></p><p>model, feature, metric

https://youtu.be/1Au1z9CtLq4?si=lIJumgmRfsC7Ad2V&amp;t=2346</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sat 18 Jun 2022 01:52)</code> - <em>Upvotes: 2</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Tue 14 Jun 2022 17:26)</code> - <em>Upvotes: 1</em></p><p>it can be only binary classifier or regression model
select a feature
select a  performance metric
select a fairness metric</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Fri 18 Mar 2022 09:48)</code> - <em>Upvotes: 4</em></p><p>on exam 18/03/2022</p></blockquote>

</details>

---

[<< Previous Question](question_481.md) | [Home](/index.md) | [Next Question >>](question_483.md)
