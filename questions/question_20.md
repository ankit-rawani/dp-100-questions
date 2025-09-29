# Question 20

This question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the recommendation satisfies the requirements.

You are in the process of creating a machine learning model. Your dataset includes rows with null and missing values.

You plan to make use of the Clean Missing Data module in Azure Machine Learning Studio to detect and fix the null and missing values in the dataset.

Recommendation: You make use of the Remove entire row option.

Will the requirements be satisfied?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>klowqw</strong> <code>(Fri 02 Sep 2022 18:41)</code> - <em>Upvotes: 8</em></p><p>not really
if you have just a null in a one cell, you don&#x27;t have to delete the whole row</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Fri 09 Dec 2022 13:03)</code> - <em>Upvotes: 1</em></p><p>Good point!</p></blockquote>
<blockquote><p><strong>Mirjalol</strong> <code>(Wed 01 Feb 2023 09:13)</code> - <em>Upvotes: 3</em></p><p>Answer is correct. 
Here is the reference: https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/clean-missing-data</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Sun 30 Jan 2022 15:57)</code> - <em>Upvotes: 6</em></p><p>correct</p></blockquote>
<blockquote><p><strong>Gabonia</strong> <code>(Fri 19 Aug 2022 13:35)</code> - <em>Upvotes: 1</em></p><p>I agree</p></blockquote>
<blockquote><p><strong>vkm_97</strong> <code>(Mon 17 Mar 2025 05:26)</code> - <em>Upvotes: 2</em></p><p>Azure Machine Learning Studio provides multiple ways to handle missing data, including mean, median, mode, and custom substitution.
Avoid deleting rows unless absolutely necessary, as it can introduce bias and reduce the dataset size.
The best approach depends on the context, but Microsoft emphasizes data preservation wherever possible.</p></blockquote>
<blockquote><p><strong>ZIMARAKI</strong> <code>(Thu 26 Sep 2024 10:09)</code> - <em>Upvotes: 1</em></p><p>From Microsoft Documentation:
This component supports multiple types of operations for &quot;cleaning&quot; missing values, including:

Replacing missing values with a placeholder, mean, or other value
Completely removing rows and columns that have missing values
Inferring values based on statistical methods</p></blockquote>

<blockquote><p><strong>fcoguerrero88</strong> <code>(Fri 08 Sep 2023 15:27)</code> - <em>Upvotes: 2</em></p><p>That&#x27;s fine, but that is an option that the module allows you, however, it is not advisable to delete an entire row for a null value when there are relevant columns for the model and it has records in the dataset. I think that from that point of view, the correct answer is B.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Thu 26 Sep 2024 10:09)</code> - <em>Upvotes: 2</em></p><p>CLEANING MODE: REMOVE ENTIRE ROW

Quote &#x27;Remove entire row: Completely removes any row in the dataset that has one or more missing values. This is useful if the missing value can be considered randomly missing.&#x27;</p></blockquote>

<blockquote><p><strong>james2033</strong> <code>(Thu 26 Sep 2024 10:09)</code> - <em>Upvotes: 2</em></p><p>https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/clean-missing-data#bkmk_ReplaceMissing

- Replace using MICE (Multivariate Imputation using Chained Equations)
- Custom substitution value
- Replace with mean
- Replace with median: Calculates the column median value, and uses the median value as the replacement for any missing value in the column.
- Replace with mode
- Remove entire row (\*)
- Replace using Probabilistic PCA

&#x27;rows with null and missing values&#x27;, we can removing entire row.

I choose YES (\*)</p></blockquote>

<blockquote><p><strong>evangelist</strong> <code>(Thu 26 Sep 2024 10:09)</code> - <em>Upvotes: 1</em></p><p>allowed options:
The Clean Missing Data module offers several options for handling missing data, including:

Remove entire row: Removes any row with missing values.
Replace using mean/median/mode: Replaces missing values with the mean, median, or mode of the column.
Replace with custom value: Replaces missing values with a custom value specified by the user.
Replace using MICE: Uses Multiple Imputation by Chained Equations to replace missing values.</p></blockquote>

<blockquote><p><strong>mhmichiel</strong> <code>(Mon 06 Mar 2023 13:35)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>
<blockquote><p><strong>ManuelHenriques</strong> <code>(Sat 25 Feb 2023 11:54)</code> - <em>Upvotes: 1</em></p><p>What if you dataset is not very large and it gets compromised with removing rows? As we do not have that information I think it is not suitable to go for remove rows, so B.</p></blockquote>
<blockquote><p><strong>Cococo</strong> <code>(Sun 19 Feb 2023 04:35)</code> - <em>Upvotes: 2</em></p><p>Read this again - &quot;to detect and fix the null and missing values&quot; FIX, not remove them, not delete them, not get rid of them but FIX (replace with median is the answer I think).

Remove entire row: Completely removes any row in the dataset with one or more missing values.</p></blockquote>

<blockquote><p><strong>Mirjalol</strong> <code>(Wed 01 Feb 2023 09:13)</code> - <em>Upvotes: 2</em></p><p>Answer is correct. 
Here is the reference: https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/clean-missing-data</p></blockquote>

</details>

---

[<< Previous Question](question_19.md) | [Home](../index.md) | [Next Question >>](question_21.md)
