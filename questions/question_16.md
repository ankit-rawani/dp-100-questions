# Question 16

This question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the recommendation satisfies the requirements.

You are in the process of creating a machine learning model. Your dataset includes rows with null and missing values.

You plan to make use of the Clean Missing Data module in Azure Machine Learning Studio to detect and fix the null and missing values in the dataset.

Recommendation: You make use of the Replace with median option.

Will the requirements be satisfied?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>synapse</strong> <code>(Sat 12 Mar 2022 10:27)</code> - <em>Upvotes: 13</em></p><p>This is an incomplete question. We don&#x27;t know what type of data it is. Continuous or categorical. If it&#x27;s continuous  then it&#x27;s A else its B</p></blockquote>
<blockquote><p><strong>Xsytt419</strong> <code>(Wed 29 Dec 2021 21:25)</code> - <em>Upvotes: 6</em></p><p>should the answer be YES?</p></blockquote>
<blockquote><p><strong>lianaliam</strong> <code>(Fri 06 Jun 2025 10:07)</code> - <em>Upvotes: 1</em></p><p>replace with mean  for replace missing values</p></blockquote>
<blockquote><p><strong>Vinit9</strong> <code>(Thu 26 Sep 2024 10:05)</code> - <em>Upvotes: 1</em></p><p>Using the Clean Missing Data module in Azure Machine Learning Studio with the Replace with median option can help detect and fix null and missing values in your dataset. The Replace with median option replaces missing values in a dataset with the median value of the corresponding column. This method of imputing missing values can provide a good balance between preserving the overall distribution of the data and avoiding the introduction of extreme values. By using the Clean Missing Data module with the Replace with median option, you can help ensure that your dataset is cleaned and ready for use in creating a machine learning model, satisfying the requirements.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Thu 26 Sep 2024 10:05)</code> - <em>Upvotes: 2</em></p><p>https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/clean-missing-data#bkmk_ReplaceMissing

- Replace using MICE (Multivariate Imputation using Chained Equations)
- Custom substitution value
- Replace with mean
- Replace with median: Calculates the column median value, and uses the median value as the replacement for any missing value in the column. (\*)
- Replace with mode
- Remove entire row
- Replace using Probabilistic PCA

&#x27;rows with null and missing values&#x27;, so no removing entire row.

I choose YES (\*), it is A.</p></blockquote>

<blockquote><p><strong>Xsesi</strong> <code>(Mon 29 Jul 2024 14:06)</code> - <em>Upvotes: 1</em></p><p>Since we do not know the type of data. Replace with mode would be prefer if the data is categorical.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Mon 26 Feb 2024 05:16)</code> - <em>Upvotes: 2</em></p><p>Answer is no, median is not appropriate to replace missing values of categorical columns.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Tue 20 Feb 2024 12:49)</code> - <em>Upvotes: 1</em></p><p>A is correct</p></blockquote>
<blockquote><p><strong>Ratz</strong> <code>(Thu 30 Nov 2023 00:07)</code> - <em>Upvotes: 2</em></p><p>Answer B: All the replace missing value options apply to the column. The question talks about randomly missing values in the row. Hence removing the row will be ideal.</p></blockquote>
<blockquote><p><strong>eternaleclipse</strong> <code>(Tue 17 Oct 2023 12:52)</code> - <em>Upvotes: 2</em></p><p>No. because we don&#x27;t know the TYPE of data it is. To simply replace with median may not work. What if it was text instead of numerical?</p></blockquote>
<blockquote><p><strong>rakeshmk</strong> <code>(Wed 27 Sep 2023 08:22)</code> - <em>Upvotes: 1</em></p><p>Missing value replacement depends on the nature of your data..median is robust to outliers. Also one can go for mean..</p></blockquote>
<blockquote><p><strong>PradhanManva</strong> <code>(Sun 24 Sep 2023 18:17)</code> - <em>Upvotes: 1</em></p><p>This is the answer.</p></blockquote>
<blockquote><p><strong>mefor</strong> <code>(Mon 14 Aug 2023 15:33)</code> - <em>Upvotes: 1</em></p><p>Yes, using the &quot;Replace with median&quot; option in the Clean Missing Data module in Azure Machine Learning Studio can help satisfy the requirements of dealing with null and missing values in your machine learning dataset. The median is a suitable option for replacing missing values in numerical features because it&#x27;s less sensitive to outliers compared to the mean.

By choosing this option, the module will identify columns with missing values and replace those missing values with the median value of each respective column. This can help maintain the integrity of your dataset and ensure that your machine learning model receives meaningful input data.

However, keep in mind that the choice of replacement strategy can also depend on the nature of your data and the specific requirements of your machine learning problem. It&#x27;s always a good practice to assess the impact of different imputation methods on your model&#x27;s performance to find the best strategy for your particular case.</p></blockquote>

<blockquote><p><strong>endeesa</strong> <code>(Thu 08 Jun 2023 20:26)</code> - <em>Upvotes: 1</em></p><p>We simply dont have enough information about the dataset to know if Median substitution will work, so the answer is No</p></blockquote>
<blockquote><p><strong>ManuelHenriques</strong> <code>(Mon 27 Feb 2023 12:46)</code> - <em>Upvotes: 4</em></p><p>You should not assume that it is correct to use median if you don&#x27;t know if data is continuous or not so B</p></blockquote>
<blockquote><p><strong>Obhee</strong> <code>(Tue 24 Jan 2023 16:51)</code> - <em>Upvotes: 1</em></p><p>Replace with median: Calculates the column median value, and uses the median value as the replacement for any missing value in the column.

Applies only to columns that have Integer or Double data types. See the Technical notes section for more information.
https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/clean-missing-data</p></blockquote>

<blockquote><p><strong>KIshor1212</strong> <code>(Tue 29 Nov 2022 14:00)</code> - <em>Upvotes: 1</em></p><p>eplace with median: Calculates the column median value, and uses the median value as the replacement for any missing value in the column.

Applies only to columns that have Integer or Double data types.

https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/clean-missing-data</p></blockquote>

<blockquote><p><strong>KIshor1212</strong> <code>(Tue 29 Nov 2022 14:00)</code> - <em>Upvotes: 1</em></p><p>** Replace with median</p></blockquote>

</details>

---

[<< Previous Question](question_15.md) | [Home](../index.md) | [Next Question >>](question_17.md)
