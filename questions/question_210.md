# Question 210

You are performing a filter-based feature selection for a dataset to build a multi-class classifier by using Azure Machine Learning Studio.

The dataset contains categorical features that are highly correlated to the output label column.

You need to select the appropriate feature scoring statistical method to identify the key predictors.

Which method should you use?

* A.Kendall correlation
* B.Spearman correlation
* C.Chi-squared
* D.Pearson correlation

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Yilu</strong> <code>(Thu 12 Nov 2020 05:37)</code> - <em>Upvotes: 47</em></p><p>I think the answer should be C. Chi-squared as both label and features are categorical.</p></blockquote>
<blockquote><p><strong>roncil</strong> <code>(Sat 12 Aug 2023 14:00)</code> - <em>Upvotes: 1</em></p><p>agreed, chi-squared for categoric</p></blockquote>
<blockquote><p><strong>febriyanasn</strong> <code>(Tue 10 Aug 2021 03:16)</code> - <em>Upvotes: 3</em></p><p>Chi-Squared: Labels and features can be text or numeric. Use this method for computing feature importance for two categorical columns.

https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/filter-based-feature-selection</p></blockquote>
<blockquote><p><strong>Gitty</strong> <code>(Fri 12 Feb 2021 10:25)</code> - <em>Upvotes: 15</em></p><p>C is the answer. Your choice of a filter selection method depends in part on what sort of input data you have. The requirement for all Pearson Correlation, Spearman Correlation and Fisher Score methods is &quot;features must be numeric&quot;. But for Chi Squared, the requirement is &quot;features can be text or numeric&quot; so you can use this method for computing feature importance for categorical columns.

See the table at this link:
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/filter-based-feature-selection</p></blockquote>
<blockquote><p><strong>Laredo</strong> <code>(Tue 18 May 2021 23:15)</code> - <em>Upvotes: 1</em></p><p>i agree. Besides, the dataset here has categorical features while Pearson Corr. is for continuous variables.</p></blockquote>
<blockquote><p><strong>nicorg5</strong> <code>(Fri 13 Sep 2024 07:01)</code> - <em>Upvotes: 1</em></p><p>I think the correct is C too</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Thu 20 Jun 2024 07:59)</code> - <em>Upvotes: 1</em></p><p>The best statistical method to use for filter-based feature selection in this multi-class classification scenario with categorical features is Chi-squared.

The chi-squared test measures dependence between categorical variables. It will identify categorical features that have a statistically significant correlation with the label column.</p></blockquote>
<blockquote><p><strong>InversaRadice</strong> <code>(Mon 03 Jun 2024 14:11)</code> - <em>Upvotes: 1</em></p><p>Its fun because in this answer explanation is stated:
&quot;Pearson&#x27;s correlation coefficient is the test statistics that measures the statistical relationship, or association, between two 
__continuous variables__.&quot; so the answer can&#x27;t be Pearson ... !!!</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Wed 27 Dec 2023 21:30)</code> - <em>Upvotes: 1</em></p><p>C - ChatGPT</p></blockquote>
<blockquote><p><strong>mkk888</strong> <code>(Mon 25 Dec 2023 19:57)</code> - <em>Upvotes: 1</em></p><p>Chi-sqaure works for categorical data the rest don&#x27;t so it should be the answer</p></blockquote>
<blockquote><p><strong>krishna1818</strong> <code>(Wed 29 Nov 2023 11:25)</code> - <em>Upvotes: 1</em></p><p>When features as well as label are categorical values we can use chi-squared method</p></blockquote>
<blockquote><p><strong>ajay0011</strong> <code>(Sat 07 Oct 2023 03:57)</code> - <em>Upvotes: 1</em></p><p>C is correct</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 15 Aug 2023 21:32)</code> - <em>Upvotes: 1</em></p><p>C is the answer.</p></blockquote>
<blockquote><p><strong>Padilha</strong> <code>(Wed 19 Jul 2023 22:51)</code> - <em>Upvotes: 1</em></p><p>Those &quot;correct answers&quot; were not made by data scientists for sure.</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Wed 14 Sep 2022 04:40)</code> - <em>Upvotes: 2</em></p><p>Chi-squared. It&#x27;s categorial.</p></blockquote>
<blockquote><p><strong>newuu</strong> <code>(Wed 15 Jun 2022 14:06)</code> - <em>Upvotes: 3</em></p><p>The answer should be C. 
Chi-Squared
      Feature -&gt; Numeric | Text
      Label -&gt;  Numeric | Text

Pearson | Kendall | Spearman | Fisher Score
     Feature -&gt; Numeric
     Label -&gt;  Numeric | Text

https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/filter-based-feature-selection</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Mon 13 Jun 2022 16:36)</code> - <em>Upvotes: 1</em></p><p>Agree with C</p></blockquote>
<blockquote><p><strong>RyanTsai</strong> <code>(Tue 22 Mar 2022 07:40)</code> - <em>Upvotes: 1</em></p><p>agree: Chi-squared</p></blockquote>
<blockquote><p><strong>slash_nyk</strong> <code>(Sun 16 Jan 2022 04:54)</code> - <em>Upvotes: 2</em></p><p>the answer is C</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Sat 27 Nov 2021 17:52)</code> - <em>Upvotes: 2</em></p><p>Answer is definitely C: Chi Squared is used in Categorical features and . Pearson is used for continuous not categorical</p></blockquote>

</details>

---

[<< Previous Question](question_209.md) | [Home](/index.md) | [Next Question >>](question_211.md)
