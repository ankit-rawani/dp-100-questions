# Question 19

This question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the recommendation satisfies the requirements.

You are in the process of creating a machine learning model. Your dataset includes rows with null and missing values.

You plan to make use of the Clean Missing Data module in Azure Machine Learning Studio to detect and fix the null and missing values in the dataset.

Recommendation: You make use of the Custom substitution value option.

Will the requirements be satisfied?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>endeesa</strong> <code>(Thu 26 Sep 2024 10:07)</code> - <em>Upvotes: 1</em></p><p>As there is a lack of information regarding the dataset in question, utilizing Custom Substitution would be advantageous. This allows for greater control in selecting appropriate substitutions that align with the data, resulting in a favourable outcome. Therefore, the answer is yes.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Thu 26 Sep 2024 10:07)</code> - <em>Upvotes: 3</em></p><p>See latest reference document at here https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/clean-missing-data?view=azureml-api-2#:~:text=Custom%20substitution%20value%3A%20Use%20this%20option%20to%20specify%20a%20placeholder%20value 

Quote &#x27;For Cleaning Mode, select one of the following options for replacing or removing missing values: Custom substitution value: Use this option to specify a placeholder value (such as a 0 or NA) that applies to all missing values. The value that you specify as a replacement must be compatible with the data type of the column.&#x27;

Yes. We can use &#x27;Custom substitution value&#x27;.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Thu 26 Sep 2024 10:07)</code> - <em>Upvotes: 3</em></p><p>https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/clean-missing-data#bkmk_ReplaceMissing

- Replace using MICE (Multivariate Imputation using Chained Equations)
- Custom substitution value (*)
- Replace with mean
- Replace with median: Calculates the column median value, and uses the median value as the replacement for any missing value in the column.
- Replace with mode
- Remove entire row
- Replace using Probabilistic PCA

&#x27;rows with null and missing values&#x27;, so no removing entire row.

I choose YES (*)</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Tue 20 Feb 2024 12:52)</code> - <em>Upvotes: 1</em></p><p>If the requirement is to effectively handle missing values in a way that preserves the integrity of the dataset for machine learning purposes, you might need to consider other options as well, such as imputation methods (mean, median, mode, MICE) that can maintain statistical properties of the dataset. The best method depends on the nature of your data and the specific requirements of your machine learning model.</p></blockquote>
<blockquote><p><strong>Ratz</strong> <code>(Thu 30 Nov 2023 00:05)</code> - <em>Upvotes: 1</em></p><p>Answer B: All the replace missing value options apply to the column. The question talks about randomly missing values in the row. Hence removing the row will be ideal.</p></blockquote>
<blockquote><p><strong>mhmichiel</strong> <code>(Mon 06 Mar 2023 13:35)</code> - <em>Upvotes: 2</em></p><p>You dont know the dataset and therefore you cant assume A is correct. This means B is correct in this case. The only option that could be correct withoud seing the dataset is to remove the rows when missing values exist.</p></blockquote>
<blockquote><p><strong>Gary_Chambers</strong> <code>(Fri 03 Feb 2023 06:17)</code> - <em>Upvotes: 1</em></p><p>I think the tricky part is the null values. Clean missing data lets you input for that but doesn&#x27;t address the null or NaN values.</p></blockquote>
<blockquote><p><strong>Mirjalol</strong> <code>(Wed 01 Feb 2023 09:07)</code> - <em>Upvotes: 1</em></p><p>Answer is &#x27;A&#x27;, here is the reference for those who have doubts: https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/clean-missing-data</p></blockquote>
<blockquote><p><strong>meysa</strong> <code>(Tue 31 Jan 2023 14:53)</code> - <em>Upvotes: 1</em></p><p>If the columns have different data types, we can not set one custom substitution for all the missing values. The only strategy that can apply to all data types is the mode.</p></blockquote>
<blockquote><p><strong>roncil</strong> <code>(Tue 17 Jan 2023 04:50)</code> - <em>Upvotes: 1</em></p><p>yes the answer is A.</p></blockquote>
<blockquote><p><strong>KIshor1212</strong> <code>(Tue 29 Nov 2022 14:02)</code> - <em>Upvotes: 2</em></p><p>Custom substitution value: Use this option to specify a placeholder value (such as a 0 or NA) that applies to all missing values. The value that you specify as a replacement must be compatible with the data type of the column.

https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/clean-missing-data</p></blockquote>
<blockquote><p><strong>FlexingD</strong> <code>(Sat 05 Nov 2022 02:39)</code> - <em>Upvotes: 2</em></p><p>Should be A</p></blockquote>
<blockquote><p><strong>dinhhungitsoft</strong> <code>(Fri 21 Oct 2022 04:03)</code> - <em>Upvotes: 2</em></p><p>A is correct, Clean Missing Data module also provides &quot;Custom substitution value&quot; cleaning mode</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sat 12 Mar 2022 10:34)</code> - <em>Upvotes: 3</em></p><p>Since it says custom, the answer would be Yes. A</p></blockquote>
<blockquote><p><strong>Mirjalol</strong> <code>(Wed 01 Feb 2023 09:02)</code> - <em>Upvotes: 4</em></p><p>What a ridiculous answer you are giving? The question did not mention &#x27;custom&#x27; only suggested answer is custom option... If you see word &#x27;custom&#x27;, do you always choose it as correct answer?</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Sun 30 Jan 2022 15:54)</code> - <em>Upvotes: 1</em></p><p>answer should be YES, because we can use &#x27;0&#x27; for numeric and &#x27;na&#x27; for text columns</p></blockquote>
<blockquote><p><strong>zaidurfshahr</strong> <code>(Wed 20 Apr 2022 18:22)</code> - <em>Upvotes: 3</em></p><p>If you use a 0 for numeric, it is a value that you add to that particular row/cell. And this will impact your predictions. It should be a NO.</p></blockquote>

</details>

---

[<< Previous Question](question_18.md) | [Home](/index.md) | [Next Question >>](question_20.md)
