# Question 472

HOTSPOT -

You are developing a linear regression model in Azure Machine Learning Studio. You run an experiment to compare different algorithms.

The following image displays the results dataset output:

![Question Image](../images/q472_q_0043600001.png)

Use the drop-down menus to select the answer choice that answers each question based on the information presented in the image.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q472_q_0043700001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q472_ans_0_0043800001.jpg" alt="Answer Image"><br>

<p>Box 1: Boosted Decision Tree Regression</p>
<p>Mean absolute error (MAE) measures how close the predictions are to the actual outcomes; thus, a lower score is better.</p>
<p>Box 2:</p>
<p>Online Gradient Descent: If you want the algorithm to find the best parameters for you, set Create trainer mode option to Parameter Range. You can then specify multiple values for the algorithm to try.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/evaluate-model https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/linear-regression</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Sun 11 Jul 2021 14:24)</code> - <em>Upvotes: 8</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>azayra</strong> <code>(Fri 16 Jul 2021 10:29)</code> - <em>Upvotes: 6</em></p><p>You passed?</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Mon 04 Nov 2024 09:52)</code> - <em>Upvotes: 1</em></p><p>Linear Regression is not incorrect, maybe two options are correct.</p></blockquote>
<blockquote><p><strong>AzureGeek79</strong> <code>(Sat 12 Oct 2024 19:01)</code> - <em>Upvotes: 1</em></p><p>Would linear regression not be the right answer for first drop-down?</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Sun 04 Jun 2023 15:09)</code> - <em>Upvotes: 1</em></p><p>the table is not needed for the second question.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Mon 13 Jun 2022 12:40)</code> - <em>Upvotes: 4</em></p><p>Yes, the given answer is correct:
&quot;Parameter Range: If you want the algorithm to find the best parameters for you, set Create trainer mode option to Parameter Range. You can then specify multiple values for the algorithm to try.&quot;</p></blockquote>
<blockquote><p><strong>ZoeJ</strong> <code>(Thu 27 Apr 2023 07:05)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/linear-regression?view=azureml-api-2#create-a-regression-model-using-online-gradient-descent</p></blockquote>
<blockquote><p><strong>Tsardoz</strong> <code>(Sun 16 Jan 2022 09:19)</code> - <em>Upvotes: 2</em></p><p>Not sure about parameter range. The only way this would work is if you had prior knwledge of the coefficients eg. by looking at the Bayesian results. Otherwise increasing number of epochs would be the most sensible approach.</p></blockquote>

</details>

---

[<< Previous Question](question_471.md) | [Home](../index.md) | [Next Question >>](question_473.md)
