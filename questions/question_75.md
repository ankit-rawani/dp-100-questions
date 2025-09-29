# Question 75

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are using Azure Machine Learning Studio to perform feature engineering on a dataset.

You need to normalize values to produce a feature column grouped into bins.

Solution: Apply an Entropy Minimum Description Length (MDL) binning mode.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>GaborO</strong> <code>(Fri 23 Oct 2020 08:55)</code> - <em>Upvotes: 30</em></p><p>MDL doesn&#x27;t normalize values, so I think the correct answer is B.</p></blockquote>
<blockquote><p><strong>meswapnilspal</strong> <code>(Sun 01 Nov 2020 15:51)</code> - <em>Upvotes: 8</em></p><p>It is not just &#x27;MDL&#x27;, it is &#x27;entropy MDL binning mode&#x27;.</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Thu 06 Jan 2022 07:03)</code> - <em>Upvotes: 4</em></p><p>I agree: https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins

See the table &quot;Module parameters&quot;

Name 	Range 	Type 	Default 	Description
Binning mode 	List 	QuantizationMode 	Quantiles 	Choose a binning method
Quantile normalization 	any 	BinningNormalization 		Choose the method for normalizing quantiles

For BinningNormalization should be used Quantile Normalization.</p></blockquote>
<blockquote><p><strong>febriyanasn</strong> <code>(Mon 09 Aug 2021 12:38)</code> - <em>Upvotes: 4</em></p><p>agree with GaborO, it should be Quantile Normalization and not Entropy MDL

&quot;If you select the Quantiles binning mode, use the Quantile normalization option to determine how values are normalized prior to sorting into quantiles. Note that normalizing values transforms the values, but does not affect the final number of bins&quot;

https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins

https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins#bkmk_Effects</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Sat 24 Sep 2022 09:23)</code> - <em>Upvotes: 8</em></p><p>According to https://docs.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/group-data-into-bins,

you can specify the following binning modes:
   - Entropy MDL
   - Quantiles
   - Equal Width
   - Custom Edges
   - Equal Width with Custom Start and Stop
From all of these, the only binning mode which supports normalization is Quantiles. In particular, Entropy MDL does NOT support normalization.</p></blockquote>
<blockquote><p><strong>astone42</strong> <code>(Mon 13 Jan 2025 10:38)</code> - <em>Upvotes: 1</em></p><p>It&#x27;s deprecated and out of scope after 16th January 2025.</p></blockquote>
<blockquote><p><strong>SanjayPatwardhan</strong> <code>(Thu 26 Dec 2024 04:42)</code> - <em>Upvotes: 1</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Wed 12 Jun 2024 12:26)</code> - <em>Upvotes: 1</em></p><p>There is no use of entropy when normalizing data.</p></blockquote>
<blockquote><p><strong>InversaRadice</strong> <code>(Sun 02 Jun 2024 07:17)</code> - <em>Upvotes: 1</em></p><p>MDL is correct</p></blockquote>
<blockquote><p><strong>Ahmed_Gehad</strong> <code>(Tue 23 Jan 2024 12:28)</code> - <em>Upvotes: 1</em></p><p>The answer is B. No.
Entropy Minimum Description Length (MDL) binning is a technique that can be used to group values into bins. However, it is not a normalization technique. Normalization is a technique that is used to scale values so that they have a similar range.
In this case, the goal is to normalize values to produce a feature column grouped into bins. However, the solution of applying an Entropy MDL binning mode will not achieve this goal. Instead, you should use a normalization technique, such as min-max normalization or z-score normalization.</p></blockquote>
<blockquote><p><strong>pranav33</strong> <code>(Thu 21 Dec 2023 16:24)</code> - <em>Upvotes: 1</em></p><p>B. No

The solution described does not meet the goal of normalizing values to produce a feature column grouped into bins. Entropy Minimum Description Length (MDL) is a criterion used for model selection and not specifically for binning or normalization of data. MDL is typically used for tasks like feature selection or model complexity estimation, but not for creating bins. To achieve the goal of normalizing values and creating bins, other techniques such as equal-width binning or equal-frequency binning can be used.</p></blockquote>
<blockquote><p><strong>mamau</strong> <code>(Sat 12 Aug 2023 20:18)</code> - <em>Upvotes: 1</em></p><p>Correct answer B 
https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/group-data-into-bins</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 02 Aug 2023 19:44)</code> - <em>Upvotes: 1</em></p><p>No. EMDL binning is used for feature selection, not for feature engineering.</p></blockquote>
<blockquote><p><strong>Mebyxu</strong> <code>(Sun 30 Jul 2023 00:16)</code> - <em>Upvotes: 1</em></p><p>Correct answer is B</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Tue 13 Jun 2023 15:42)</code> - <em>Upvotes: 2</em></p><p>Option A (Yes)</p></blockquote>
<blockquote><p><strong>zehraoneexam</strong> <code>(Thu 15 Sep 2022 05:24)</code> - <em>Upvotes: 1</em></p><p>It is true. Because quantile is unsupervised .</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 13 Sep 2022 12:40)</code> - <em>Upvotes: 2</em></p><p>MDL does not normalize</p></blockquote>
<blockquote><p><strong>Maunik</strong> <code>(Mon 10 Jan 2022 15:26)</code> - <em>Upvotes: 2</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins - Correct answer seems to be A. In in graph it mentions normalized data in to bins</p></blockquote>
<blockquote><p><strong>Haet</strong> <code>(Tue 12 Oct 2021 08:26)</code> - <em>Upvotes: 2</em></p><p>The answer is Entropy MDL reason if you see the explanation it says they want feature column group into bins this is done by only Entropy MDL and not in Quantile Normalization.</p></blockquote>
<blockquote><p><strong>allanm</strong> <code>(Mon 15 Nov 2021 21:24)</code> - <em>Upvotes: 2</em></p><p>Incorrect. The question requirements states that the data has to be normalised and then binned. You cannot do Normalisation with entropy MDL, it must be quantile normalisation first.</p></blockquote>
<blockquote><p><strong>111ssy</strong> <code>(Sun 28 Feb 2021 00:29)</code> - <em>Upvotes: 3</em></p><p>Entropy MDL: This method requires that you select the column you want to predict and the column or columns that you want to group into bins. It then makes a pass over the data and attempts to determine the number of bins that minimizes the entropy. In other words, it chooses a number of bins that allows the data column to best predict the target column. It then returns the bin number associated with each row of your data in a column named &lt;colname&gt;quantized. 

https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins</p></blockquote>

</details>

---

[<< Previous Question](question_74.md) | [Home](/index.md) | [Next Question >>](question_76.md)
