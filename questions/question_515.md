# Question 515

You need to select a feature extraction method.

Which method should you use?

- A.Mutual information
- B.Pearson's correlation
- C.Spearman correlation
- D.Fisher Linear Discriminant Analysis

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

<p>Spearman&#x27;s rank correlation coefficient assesses how well the relationship between two variables can be described using a monotonic function.</p>
<p>Note: Both Spearman&#x27;s and Kendall&#x27;s can be formulated as special cases of a more general correlation coefficient, and they are both appropriate in this scenario.</p>
<p>Scenario: The MedianValue and AvgRoomsInHouse columns both hold data in numeric format. You need to select a feature selection algorithm to analyze the relationship between the two columns in more detail.</p>
<p>Incorrect Answers:</p>
<p>B: The Spearman correlation between two variables is equal to the Pearson correlation between the rank values of those two variables; while Pearson&#x27;s correlation assesses linear relationships, Spearman&#x27;s correlation assesses monotonic relationships (whether linear or not).</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/feature-selection-modules</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Mckay_</strong> <code>(Fri 14 Apr 2023 22:49)</code> - <em>Upvotes: 7</em></p><p>This can be a tricky question if you did not read the case study. It says in the case study that relationship between features should be assess using non-parametric statistics. Thus, the reason for using the spearman&#x27;s rank correlation.</p></blockquote>
<blockquote><p><strong>BTAB</strong> <code>(Sat 15 Jul 2023 12:47)</code> - <em>Upvotes: 1</em></p><p>Thanks for the evaluation.  Correct.</p></blockquote>
<blockquote><p><strong>XiaoQiang</strong> <code>(Thu 01 Jul 2021 19:15)</code> - <em>Upvotes: 7</em></p><p>how could 2 same questions get a different answer? bad quality</p></blockquote>
<blockquote><p><strong>jed_elhak</strong> <code>(Sat 19 Mar 2022 16:02)</code> - <em>Upvotes: 2</em></p><p>Correlation analysis provides a quantitative means of measuring the strength of a linear relationship between two vectors of data. Mutual information is essentially the measure of how much “knowledge” one can gain of a certain variable by knowing the value of another variable so it can&#x27;t be mututal information  spearman is the right answer</p></blockquote>
<blockquote><p><strong>BrunoCavagnaro</strong> <code>(Tue 17 Aug 2021 19:45)</code> - <em>Upvotes: 2</em></p><p>They even coment that both Pearson and Kendall  are correct answers</p></blockquote>
<blockquote><p><strong>Indranee</strong> <code>(Tue 20 Jul 2021 08:44)</code> - <em>Upvotes: 1</em></p><p>Maybe microsoft jumbles up the possible responses/answers which could appear for each test taker.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Tue 13 Aug 2024 02:02)</code> - <em>Upvotes: 1</em></p><p>The answer is definitely not D. But I am confused between three even after reading all the comments below. help!</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 25 Aug 2023 23:41)</code> - <em>Upvotes: 1</em></p><p>The question mentions &quot;feature extraction,&quot; but the given answer choices are all feature selection methods. If the question is about feature extraction, some commonly used methods are Principal Component Analysis (PCA), Independent Component Analysis (ICA), and Non-negative Matrix Factorization (NMF).

If the question is about feature selection, then the most appropriate method depends on the specific characteristics of the data and the problem at hand. Without more information about the specific characteristics of the data and the problem at hand, it is not possible to determine which method is the best choice.</p></blockquote>

<blockquote><p><strong>jed_elhak</strong> <code>(Sat 19 Mar 2022 15:59)</code> - <em>Upvotes: 5</em></p><p>Answer is correct : they asked a non parametric 
 pearson and  fisher are  parametric</p></blockquote>
<blockquote><p><strong>jed_elhak</strong> <code>(Sat 19 Mar 2022 16:02)</code> - <em>Upvotes: 1</em></p><p>Correlation analysis provides a quantitative means of measuring the strength of a linear relationship between two vectors of data. Mutual information is essentially the measure of how much “knowledge” one can gain of a certain variable by knowing the value of another variable so it can&#x27;t be mututal information spearman is the right answer</p></blockquote>
<blockquote><p><strong>levm39</strong> <code>(Thu 23 Dec 2021 08:23)</code> - <em>Upvotes: 2</em></p><p>Note: Both Spearman&#x27;s and Kendall&#x27;s can be formulated as special cases of a more general correlation coefficient, and they are both appropriate in this scenario.</p></blockquote>
<blockquote><p><strong>rabbie</strong> <code>(Tue 30 Nov 2021 03:44)</code> - <em>Upvotes: 1</em></p><p>pearson&#x27;s correlation is not a non-parametric method</p></blockquote>
<blockquote><p><strong>rabbie</strong> <code>(Tue 30 Nov 2021 03:44)</code> - <em>Upvotes: 2</em></p><p>MY BAD, IT&#x27;S SPEARMAN</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Sun 28 Nov 2021 20:06)</code> - <em>Upvotes: 1</em></p><p>Pearson is linear while spearman  and kendall are monotonic.  Pearson does not work well with outliers but there is not indication that the medianvalue and AvgRoomsInHouse  columns have outliers.

Fisher linear discriminant (FLD) analysis is not a valid option (fisher score is)
See links for difference
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/fisher-linear-discriminant-analysis

https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/filter-based-feature-selection

The answer I think is Pearson&#x27;s correlation.</p></blockquote>

<blockquote><p><strong>saurabhk1</strong> <code>(Sun 05 Sep 2021 16:02)</code> - <em>Upvotes: 3</em></p><p>The answer should be Fisher Linear Discriminant Analysis, as this is the only method in the given options, that is used for extracting features in low dimensions.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Tue 13 Aug 2024 02:00)</code> - <em>Upvotes: 1</em></p><p>Fisher LDA is definitely not the answer as it is used in classification problems not regression.</p></blockquote>

</details>

---

[<< Previous Question](question_514.md) | [Home](../index.md) | [Next Question >>](question_516.md)
