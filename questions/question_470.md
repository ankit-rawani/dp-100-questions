# Question 470

You are a data scientist creating a linear regression model.

You need to determine how closely the data fits the regression line.

Which metric should you review?

* A.Root Mean Square Error
* B.Coefficient of determination
* C.Recall
* D.Precision
* E.Mean absolute error

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>BilJon</strong> <code>(Sat 27 Mar 2021 10:44)</code> - <em>Upvotes: 10</em></p><p>Shouldn&#x27;t be E? 
Mean absolute error (MAE) measures how close the predictions are to the actual outcomes; thus, a lower score is better.</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 12 Apr 2022 21:43)</code> - <em>Upvotes: 3</em></p><p>MAE is irrelevant to the question. You are being asked which metric measures how closely data fits the regression line. The given answer of R2 is correct.</p></blockquote>
<blockquote><p><strong>tomiskolc</strong> <code>(Thu 29 Apr 2021 15:08)</code> - <em>Upvotes: 5</em></p><p>but you won&#x27;t know what is &#x27;lower&#x27;. i mean you will get a number MAE = 250, it can be a good fit for example R2 = 0,95. If you get an other dataset you get MAE = 5 , but it stuill can be bad fit, it can be R2 = 0,2 . So you cant say about the fit based on only MAE (or RMSE) , but R2 can explain how good is the fit.</p></blockquote>
<blockquote><p><strong>bakemi5105</strong> <code>(Fri 28 May 2021 09:46)</code> - <em>Upvotes: 1</em></p><p>it was not asked wether the metric is in a specific range. So its not an argument to the exam question.</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Sun 11 Jul 2021 14:24)</code> - <em>Upvotes: 7</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 11:45)</code> - <em>Upvotes: 1</em></p><p>The coefficient of determination (R-squared) is the most appropriate metric to determine how closely the data fits the regression line. It represents the proportion of the variance in the dependent variable that is predictable from the independent variable(s).</p></blockquote>
<blockquote><p><strong>bbe8966</strong> <code>(Sat 22 Jun 2024 11:12)</code> - <em>Upvotes: 1</em></p><p>correct!</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 18 May 2024 06:17)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Wed 14 Dec 2022 21:15)</code> - <em>Upvotes: 2</em></p><p>CoD or R-squared</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sun 12 Jun 2022 13:52)</code> - <em>Upvotes: 2</em></p><p>This question is poorly written, no definition of &#x27;fits&#x27;, I guess normally R2 is think of how fit it is ... but really you need define what fit is in the particular situation, otherwise, A / E could be candidates as well ...</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 12 Apr 2022 21:44)</code> - <em>Upvotes: 4</em></p><p>Given answer is correct. Coefficient of determination, often referred to as R2 measures how closely data fits the regression line.</p></blockquote>
<blockquote><p><strong>Shanggavee</strong> <code>(Fri 22 Oct 2021 13:54)</code> - <em>Upvotes: 3</em></p><p>correct answer is B</p></blockquote>
<blockquote><p><strong>dijaa</strong> <code>(Sat 28 Aug 2021 10:50)</code> - <em>Upvotes: 5</em></p><p>R-squared is a statistical measure of how close the data are to the fitted regression line. It is also known as the coefficient of determination,</p></blockquote>
<blockquote><p><strong>pwell</strong> <code>(Sun 27 Jun 2021 14:01)</code> - <em>Upvotes: 4</em></p><p>The answer B is correct R^2 measures how closely data fits a regression line</p></blockquote>
<blockquote><p><strong>bakemi5105</strong> <code>(Fri 28 May 2021 09:49)</code> - <em>Upvotes: 1</em></p><p>Would say E - MAE directly is using the difference between the prediction and the true value.
RMSE and R2 are both using squared distance for the residual</p></blockquote>
<blockquote><p><strong>ali25</strong> <code>(Mon 05 Apr 2021 07:59)</code> - <em>Upvotes: 1</em></p><p>A model is considered to &quot;fit&quot; the data well if the difference between observed and predicted values is small. 
Coefficient of determination, often referred to as R2, represents the predictive power of the model as a value between 0 and 1. Zero means the model is random (explains nothing); 1 means there is a perfect &quot;fit&quot;. However, caution should be used in interpreting R2 values, as low values can be entirely normal and high values can be suspect.</p></blockquote>
<blockquote><p><strong>ali25</strong> <code>(Mon 05 Apr 2021 08:22)</code> - <em>Upvotes: 1</em></p><p>The most common interpretation of the coefficient of determination is how well the regression model fits the observed data. For example, a coefficient of determination of 60% shows that 60% of the data fit the regression model. Generally, a higher coefficient indicates a better fit for the model.</p></blockquote>

</details>

---

[<< Previous Question](question_469.md) | [Home](/index.md) | [Next Question >>](question_471.md)
