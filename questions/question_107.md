# Question 107

You are profiling data by using Azure Machine Learning studio.

You need to detect columns with odd or missing values.

Which statistic should you analyze?

* A.Profile
* B.Std deviation
* C.Error count
* D.Type

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ajay0011</strong> <code>(Tue 04 Apr 2023 00:56)</code> - <em>Upvotes: 9</em></p><p>To detect columns with odd or missing values, you should analyze the Error count statistic.

The Error count statistic represents the number of missing or malformed values in each column of your dataset. Analyzing this statistic allows you to detect columns with missing values or with values that don&#x27;t conform to the expected data type.

The Profile statistic provides a summary of the statistical properties of each column, such as the minimum, maximum, mean, median, and quartiles. The Std deviation statistic represents the variation of each column around its mean value. These statistics are useful to understand the distribution and variability of the data, but they don&#x27;t provide information about missing or malformed values.

The Type statistic represents the data type of each column, such as integer, float, or string. While this statistic is useful to understand the structure of the dataset, it doesn&#x27;t provide information about missing or malformed values.

Therefore, the correct answer is option C: Error count.</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Sun 17 Nov 2024 16:24)</code> - <em>Upvotes: 1</em></p><p>C. Error count</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Mon 25 Mar 2024 17:42)</code> - <em>Upvotes: 2</em></p><p>on exam 3/25/2024</p></blockquote>
<blockquote><p><strong>Kanwal001</strong> <code>(Mon 28 Aug 2023 19:34)</code> - <em>Upvotes: 4</em></p><p>On exam 28 Aug 2023</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Thu 20 Jul 2023 13:22)</code> - <em>Upvotes: 2</em></p><p>On exam 20 July 2023.</p></blockquote>
<blockquote><p><strong>Jin_22</strong> <code>(Wed 22 Mar 2023 13:03)</code> - <em>Upvotes: 3</em></p><p>C. Error count

To detect columns with odd or missing values, you should analyze the &quot;Error count&quot; statistic. The Error count metric provides information on the number of missing or null values present in each column. By analyzing this metric, you can identify columns that have a high number of missing or null values, which may indicate issues with the data quality or the data collection process. Additionally, you can also identify columns with odd or unexpected values that do not fit the data distribution or that have a high number of outliers.</p></blockquote>

</details>

---

[<< Previous Question](question_106.md) | [Home](/index.md) | [Next Question >>](question_108.md)
