# Question 31

You make use of Azure Machine Learning Studio to develop a linear regression model. You perform an experiment to assess various algorithms.

Which of the following is an algorithm that reduces the variances between actual and predicted values?

* A.Fast Forest Quantile Regression
* B.Poisson Regression
* C.Boosted Decision Tree Regression
* D.Linear Regression

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>RyanTsai</strong> <code>(Sun 19 Sep 2021 10:05)</code> - <em>Upvotes: 22</em></p><p>should be linear regression</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Fri 15 Apr 2022 10:25)</code> - <em>Upvotes: 3</em></p><p>Linear regression minimizes the sum of squares, i.e. it minimizes S=Sum[(y_i-f_i)^2,{i,1,n}], where y_i is the actual value and f_i the predicted value (we can see it as the average). 

Since the variance of {y_i} is S/n, minimizing S is equivalent to minimizing the variance.</p></blockquote>
<blockquote><p><strong>jed_elhak</strong> <code>(Mon 13 Sep 2021 22:42)</code> - <em>Upvotes: 16</em></p><p>Correct answer is C :
 It builds each regression tree in a step-wise fashion, using a predefined loss function to measure the error in each step and correct for it in the next. Thus the prediction model is actually an ensemble of weaker prediction models.
reference:https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/boosted-decision-tree-regression</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Sat 25 Dec 2021 18:52)</code> - <em>Upvotes: 1</em></p><p>Agree with you</p></blockquote>
<blockquote><p><strong>sar77</strong> <code>(Sat 12 Jul 2025 01:27)</code> - <em>Upvotes: 1</em></p><p>Boosted Decision Tree Regression, including Azure ML’s Boosted Decision Tree (based on LightGBM/MART), is designed to minimize errors between actual and predicted values by sequentially fitting trees that correct previous residuals. This iterative boosting process both reduces bias and lowers variance, resulting in more accurate predictions .</p></blockquote>
<blockquote><p><strong>PatAms538</strong> <code>(Tue 17 Jun 2025 22:18)</code> - <em>Upvotes: 1</em></p><p>The Linear Regression is built upon the F-test. The logic of the F-test: the amount of systematic variance divided by the amount of unsystematic variance</p></blockquote>
<blockquote><p><strong>brzhanyu</strong> <code>(Sun 13 Oct 2024 02:56)</code> - <em>Upvotes: 1</em></p><p>The correct answer is Boosted Decision Tree Regression.

Boosted Decision Tree Regression is an algorithm that reduces the variance between actual and predicted values by iteratively combining multiple weak learners (decision trees) to create a stronger, more accurate model. This helps minimize the differences between the predicted values and the actual values by focusing on the errors made by previous models.

Linear regression, while useful for linear relationships, does not specifically focus on reducing variance in the way ensemble methods like boosting do.</p></blockquote>
<blockquote><p><strong>6c3c83d</strong> <code>(Tue 07 May 2024 15:34)</code> - <em>Upvotes: 1</em></p><p>D is linear and reduces the mean squared error which is the variance between actual and predicted. Regression trees do that too but are not linear</p></blockquote>
<blockquote><p><strong>GHill1982</strong> <code>(Tue 23 Jan 2024 21:18)</code> - <em>Upvotes: 2</em></p><p>Linear regression computes the linear relationship between a dependent variable and one or more independent features. It uses the ordinary least squares method to minimize the sum of the squared errors between the actual and predicted values.</p></blockquote>
<blockquote><p><strong>jdada</strong> <code>(Fri 10 Nov 2023 16:04)</code> - <em>Upvotes: 2</em></p><p>D. Linear Regression</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Thu 12 Oct 2023 08:46)</code> - <em>Upvotes: 5</em></p><p>Question keyword &#x27;develop a linear regression model&#x27;. Answer keyword &#x27;Linear regression&#x27; make (D) is correct answer.

https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/linear-regression?view=azureml-api-2

Quote: &#x27;create a linear regression model&#x27; , &#x27;Linear regression is a common statistical method, ...&#x27;</p></blockquote>
<blockquote><p><strong>Nadine_nm</strong> <code>(Thu 17 Aug 2023 12:21)</code> - <em>Upvotes: 2</em></p><p>I think the question is poorly asked, since the algorithme used depends mainy on the data.
The answer is linear regression, since Poisson regression is actually a form of generalized linear modeling and is often considered a non-linear regression model due to its underlying mathematical structure. Also Boosted decision tree, in a non linear regression as well.</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Sat 15 Jul 2023 14:30)</code> - <em>Upvotes: 1</em></p><p>Boosted decision tree regression a non-linear regression model.</p></blockquote>
<blockquote><p><strong>endeesa</strong> <code>(Thu 08 Jun 2023 21:36)</code> - <em>Upvotes: 1</em></p><p>Boosting will definitely reduce the variances</p></blockquote>
<blockquote><p><strong>daviduzo</strong> <code>(Wed 21 Jun 2023 06:32)</code> - <em>Upvotes: 1</em></p><p>But the the question says we&#x27;re trying to develop a linear regression model. Shouldn&#x27;t the influence the option and it&#x27;s supposed to be D</p></blockquote>
<blockquote><p><strong>NickRafe</strong> <code>(Sat 29 Apr 2023 01:28)</code> - <em>Upvotes: 1</em></p><p>Answer should be C. Reference:
https://www.kdd.org/kdd2016/papers/files/adf0653-poyarkovA.pdf</p></blockquote>
<blockquote><p><strong>EXAMTOPICS2134</strong> <code>(Mon 17 Apr 2023 19:35)</code> - <em>Upvotes: 1</em></p><p>Decision trees are non linear. Unlike Linear regression there is no equation to express relationship between independent and dependent variables</p></blockquote>
<blockquote><p><strong>bibabrian</strong> <code>(Sat 15 Apr 2023 01:02)</code> - <em>Upvotes: 2</em></p><p>guys I know some of these questions are crap but read carefully it says &quot;assess various algorithms.&quot;, which means a boosting algorithm like Boosted Decision Tree Regression makes sense.</p></blockquote>
<blockquote><p><strong>bvkr</strong> <code>(Tue 28 Mar 2023 16:05)</code> - <em>Upvotes: 1</em></p><p>ChatGPT answer: Option D: Linear Regression, is an algorithm that can help to reduce the variances between actual and predicted values in a linear regression model.</p></blockquote>
<blockquote><p><strong>sahithi2004</strong> <code>(Mon 20 Mar 2023 05:49)</code> - <em>Upvotes: 1</em></p><p>Boosted Decision Tree Regression is an algorithm that reduces the variances between actual and predicted values.
Linear regression aims to find the best linear relationship between the independent and dependent variables, while Fast Forest Quantile Regression is a regression algorithm that can provide estimates of conditional quantiles of the response variable. Poisson Regression is used when the dependent variable is a count or frequency, and the relationship between the dependent and independent variables is modelled using a Poisson distribution.</p></blockquote>

</details>

---

[<< Previous Question](question_30.md) | [Home](/index.md) | [Next Question >>](question_32.md)
