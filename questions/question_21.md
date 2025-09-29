# Question 21

HOTSPOT -

Complete the sentence by selecting the correct option in the answer area.

Hot Area:

![Question Image](images/q21_q_0002600001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q21_ans_0_0002700001.jpg" alt="Answer Image"><br>
<p>Replace using Probabilistic PCA: Compared to other options, such as Multiple Imputation using Chained Equations (MICE), this option has the advantage of not requiring the application of predictors for each column. Instead, it approximates the covariance for the full dataset. Therefore, it might offer better performance for datasets that have missing values in many columns.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/clean-missing-data</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>pancman</strong> <code>(Wed 13 Apr 2022 18:40)</code> - <em>Upvotes: 19</em></p><p>I don&#x27;t think that this is a real exam question. Median and custom substitution techniques don&#x27;t require a predictor either.</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Sat 27 May 2023 18:58)</code> - <em>Upvotes: 5</em></p><p>Replace using Probabilistic PCA: Replaces the missing values by using a linear model that analyzes the correlations between the columns and estimates a low-dimensional approximation of the data, from which the full data is reconstructed. The underlying dimensionality reduction is a probabilistic form of Principal Component Analysis (PCA), and it implements a variant of the model proposed in the Journal of the Royal Statistical Society, Series B 21(3), 611–622 by Tipping and Bishop.

Compared to other options, such as Multiple Imputation using Chained Equations (MICE), this option has the advantage of not requiring the application of predictors for each column. Instead, it approximates the covariance for the full dataset. Therefore, it might offer better performance for datasets that have missing values in many columns.
https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/clean-missing-data</p></blockquote>
<blockquote><p><strong>geethavkr</strong> <code>(Thu 15 Aug 2024 18:46)</code> - <em>Upvotes: 1</em></p><p>correct..  Outdated but in previous versions it says
Replace using Probabilistic PCA: Replaces the missing values by using a linear model that analyzes the correlations between the columns and estimates a low-dimensional approximation of the data, from which the full data is reconstructed. The underlying dimensionality reduction is a probabilistic form of Principal Component Analysis (PCA), and it implements a variant of the model proposed in the Journal of the Royal Statistical Society, Series B 21(3), 611–622 by Tipping and Bishop.

Compared to other options, such as Multiple Imputation using Chained Equations (MICE), this option has the advantage of not requiring the application of predictors for each column. Instead, it approximates the covariance for the full dataset. Therefore, it might offer better performance for datasets that have missing values in many columns.</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Tue 28 May 2024 05:42)</code> - <em>Upvotes: 1</em></p><p>I think this is an outdated question.
as of may 2024, PCA is no longer in the clean missing data module.
reference: https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/clean-missing-data?view=azureml-api-2

however, in the past, PCA did in the clean missing data module.
reference:https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/clean-missing-data

at the time of the question was created, PCA may be correct.
but now, i thick is either median or custom substitution value.</p></blockquote>
<blockquote><p><strong>InversaRadice</strong> <code>(Fri 01 Dec 2023 07:15)</code> - <em>Upvotes: 2</em></p><p>answer is 100% correct ...
Replace using Probabilistic PCA: ...
Compared to other options, such as Multiple Imputation using Chained Equations (MICE), this option has the advantage of not requiring the application of predictors for each column.
https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/clean-missing-data</p></blockquote>
<blockquote><p><strong>eternaleclipse</strong> <code>(Sun 22 Oct 2023 15:20)</code> - <em>Upvotes: 1</em></p><p>What pancman said. outdated question</p></blockquote>
<blockquote><p><strong>IvanTT</strong> <code>(Mon 16 Oct 2023 07:42)</code> - <em>Upvotes: 1</em></p><p>It can&#x27;t be &quot;A. Probabilistic PCA&quot; because it isn&#x27;t an option for the Clean Missing Data module. Here is the reference: https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/clean-missing-data?view=azureml-api-2
It could be &quot;D. Custom Substitution Value&quot;. The option &quot;B. Median&quot; isn&#x27;t the exact option for the module which it&#x27;s &quot;Replace with median&quot;.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 06 Oct 2023 23:47)</code> - <em>Upvotes: 1</em></p><p>Qutote &quot;Replace using Probabilistic PCA: Replaces the missing values by using a linear model that analyzes the correlations between the columns and estimates a low-dimensional approximation of the data, from which the full data is reconstructed. The underlying dimensionality reduction is a probabilistic form of Principal Component Analysis (PCA), and it implements a variant of the model proposed in the Journal of the Royal Statistical Society, Series B 21(3), 611–622 by Tipping and Bishop.

Compared to other options, such as Multiple Imputation using Chained Equations (MICE), this option has the advantage of not requiring the application of predictors for each column.&quot;

Reference https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/clean-missing-data#:~:text=this%20option%20has%20the%20advantage%20of%20not%20requiring%20the%20application%20of%20predictors%20for%20each%20column.</p></blockquote>
<blockquote><p><strong>rakeshmk</strong> <code>(Wed 27 Sep 2023 08:35)</code> - <em>Upvotes: 3</em></p><p>PCA is a dimensionality reduction technique.. Median can be the answer</p></blockquote>
<blockquote><p><strong>PradhanManva</strong> <code>(Sun 24 Sep 2023 18:20)</code> - <em>Upvotes: 1</em></p><p>PCA -This is the answer.</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Tue 25 Apr 2023 10:07)</code> - <em>Upvotes: 3</em></p><p>Correct answer is medain - it only calulates the medain from the given column, no other columns required

pca - needs predictors to calculate the probabilities
smote - needs predictors to generate synthetic samples for the minority class
csv - doesn&#x27;t really need predictors per se, but still requires some knoweldge about the data to pick the right value</p></blockquote>
<blockquote><p><strong>Truman</strong> <code>(Mon 10 Apr 2023 18:01)</code> - <em>Upvotes: 1</em></p><p>One data cleaning option that does not require predictors for each column in the Clean Missing Data module is the &quot;Replace with mean&quot; option. This option replaces missing values in a column with the mean of the available values in that column

All these options are false</p></blockquote>
<blockquote><p><strong>Vic9</strong> <code>(Mon 03 Apr 2023 15:58)</code> - <em>Upvotes: 2</em></p><p>A

https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/clean-missing-data

&quot;Replace using Probabilistic PCA: Replaces the missing values by using a linear model that analyzes the correlations between the columns and estimates a low-dimensional approximation of the data, from which the full data is reconstructed. The underlying dimensionality reduction is a probabilistic form of Principal Component Analysis (PCA), and it implements a variant of the model proposed in the Journal of the Royal Statistical Society, Series B 21(3), 611–622 by Tipping and Bishop.

Compared to other options, such as Multiple Imputation using Chained Equations (MICE), this option has the advantage of not requiring the application of predictors for each column. Instead, it approximates the covariance for the full dataset. Therefore, it might offer better performance for datasets that have missing values in many columns.&quot;</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sun 26 Feb 2023 04:34)</code> - <em>Upvotes: 2</em></p><p>A) Probabilistic PCA and C) SMOTE are not data cleaning options in the clean missing data module.

Probabilistic PCA is a technique used for dimensionality reduction and feature extraction in machine learning, and it is not specifically designed to handle missing data.

SMOTE (Synthetic Minority Over-sampling Technique) is a technique used for dealing with imbalanced datasets in machine learning, and it is not designed to handle missing data.

Therefore, the correct answer to the question &quot;..... is a data cleaning option of the clean missing data module that does not require predictors for each column&quot; is either B) Median or D) Custom substitution value.</p></blockquote>
<blockquote><p><strong>Peeking</strong> <code>(Sun 19 Feb 2023 18:26)</code> - <em>Upvotes: 2</em></p><p>PCA is wrong.</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Sun 30 Jan 2022 16:00)</code> - <em>Upvotes: 3</em></p><p>correct</p></blockquote>

</details>

---

[<< Previous Question](question_20.md) | [Home](/index.md) | [Next Question >>](question_22.md)
