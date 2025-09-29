# Question 85

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are analyzing a numerical dataset which contains missing values in several columns.

You must clean the missing values using an appropriate operation without affecting the dimensionality of the feature set.

You need to analyze a full dataset to include all values.

Solution: Calculate the column median value and use the median value as the replacement for any missing value in the column.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Aleem</strong> <code>(Thu 06 May 2021 05:50)</code> - <em>Upvotes: 34</em></p><p>&quot;You need to analyze a full dataset&quot; just means you can&#x27;t drop the rows or the columns. Replacing missing data with the median may increase the cardinality but dimensionality is only increased by adding new feature columns. Median replacement is a valid method in this case. The answer should be &quot;Yes&quot;.</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Wed 09 Mar 2022 05:54)</code> - <em>Upvotes: 2</em></p><p>I guess because they mentioned &quot;appropriate&quot; which is vague but it might be the case</p></blockquote>
<blockquote><p><strong>amarques</strong> <code>(Fri 02 Aug 2019 11:09)</code> - <em>Upvotes: 14</em></p><p>In the reference you mentioned it&#x27;s not explicit that you can only use MICE.
There&#x27;s any reason because we cannot use median?
Thank you</p></blockquote>
<blockquote><p><strong>NaishinMatiri</strong> <code>(Wed 21 Apr 2021 00:05)</code> - <em>Upvotes: 4</em></p><p>I think the answer should ONLY be the Mean. Since there are missing values in many columns and MICE uses other columns to calculate the value. Trying to calculate values where the other columns also have missing values could alter the result.</p></blockquote>
<blockquote><p><strong>andre999</strong> <code>(Mon 21 Jun 2021 08:53)</code> - <em>Upvotes: 3</em></p><p>You can also use Median for numerical values, as stated in the exercice.</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Thu 10 Oct 2024 13:13)</code> - <em>Upvotes: 1</em></p><p>if values are missing in the entire column, how do you calculate the median?</p></blockquote>
<blockquote><p><strong>haby</strong> <code>(Thu 21 Dec 2023 14:21)</code> - <em>Upvotes: 1</em></p><p>B for sure. Median is only available if the columns/rows are numeric or ordinal, if they are categorical or even string, we have to use Mode or other methods.</p></blockquote>
<blockquote><p><strong>Anjiiiiiii</strong> <code>(Thu 30 May 2024 10:08)</code> - <em>Upvotes: 2</em></p><p>The question says it&#x27;s a numerical dataset.</p></blockquote>
<blockquote><p><strong>Ahmed_Gehad</strong> <code>(Sun 23 Jul 2023 13:33)</code> - <em>Upvotes: 1</em></p><p>The solution meets the goal because it uses an appropriate operation to clean the missing values without affecting the dimensionality of the feature set. The median value is a good choice for imputing missing values because it is not affected by outliers. Additionally, the median value does not affect the dimensionality of the feature set because it is a single value.</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Mon 22 May 2023 17:28)</code> - <em>Upvotes: 2</em></p><p>I think B is True. Median replacement &quot;analyze&quot; only one column, but MICE method use all columns for one. Also we can use Probablistic PCA mothod.</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Fri 19 May 2023 10:13)</code> - <em>Upvotes: 1</em></p><p>If columns are numeric then yes, otherwise no. The problem is we dont have that information.</p></blockquote>
<blockquote><p><strong>swatidorge1010</strong> <code>(Sun 14 May 2023 15:36)</code> - <em>Upvotes: 1</em></p><p>Please change answer or justify</p></blockquote>
<blockquote><p><strong>swatidorge1010</strong> <code>(Sun 14 May 2023 15:35)</code> - <em>Upvotes: 2</em></p><p>Answer : B 
As its not mentioned all columns have numeric values.</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Mon 22 May 2023 17:30)</code> - <em>Upvotes: 2</em></p><p>It is mentioned &quot;You are analyzing a numerical dataset&quot;</p></blockquote>
<blockquote><p><strong>ajay0011</strong> <code>(Sun 02 Apr 2023 04:56)</code> - <em>Upvotes: 1</em></p><p>Yes is the answer, please change it</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Wed 14 Dec 2022 13:00)</code> - <em>Upvotes: 1</em></p><p>Agree A</p></blockquote>
<blockquote><p><strong>jlopezfelizzola</strong> <code>(Sun 18 Sep 2022 11:18)</code> - <em>Upvotes: 3</em></p><p>Should be A</p></blockquote>
<blockquote><p><strong>FU_User</strong> <code>(Wed 18 May 2022 11:21)</code> - <em>Upvotes: 3</em></p><p>It is correct as it doesn&#x27;t add or drop columns.
Also &quot;You need to analyze a full dataset&quot; can either mean that the algorithm should take the full existing dataset into account when replacing values (which this one does) or that no existing data should be deleted (median does not delete anything)</p></blockquote>
<blockquote><p><strong>VEDPRASAD</strong> <code>(Sun 27 Mar 2022 19:22)</code> - <em>Upvotes: 2</em></p><p>In an existing project we did median, with clustered dataset. so median works</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Fri 25 Mar 2022 14:46)</code> - <em>Upvotes: 4</em></p><p>Applying the mentioned method to the following dataset 

1 | 5 | - | - | 7 | 3 |
- | 0 | 2 | 2 | 7 | 4 |
2 | 6 | 9 | - | 2 | - |
3 | - | - | - | 7 | - |

would lead to 

1 | 4 | 4 | 4 | 7 | 3 |
2 | 0 | 2 | 2 | 7 | 4 |
2 | 6 | 9 | 4 | 2 | 4 |
3 | 5 | 5 | 5 | 7 | 5 |

Hence
 - missing data cleaned
 - dimensionality preserved</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Fri 25 Mar 2022 14:47)</code> - <em>Upvotes: 1</em></p><p>oops the entry (1,2) is meant to be a 5 in the dataset below</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sun 13 Mar 2022 14:10)</code> - <em>Upvotes: 4</em></p><p>Copying a good answer: &quot;You need to analyze a full dataset&quot; just means you can&#x27;t drop the rows or the columns. Replacing missing data with the median may increase the cardinality but dimensionality is only increased by adding new feature columns. Median replacement is a valid method in this case. The answer should be &quot;Yes&quot;</p></blockquote>
<blockquote><p><strong>mikosann</strong> <code>(Wed 22 Sep 2021 13:42)</code> - <em>Upvotes: 4</em></p><p>I think the answer is correct. Filling missing values with mean/median is a highly used method. It works on each column separately and independently. And it only replaces the missing values, doesn&#x27;t add any new columns or new rows to the dataset which means it doesn&#x27;t effect dimensions. Taking the mean/median of the column and replacing missing values is one of the beginner data science topics. MICE can be a better method but this doesn&#x27;t mean the answer is wrong.</p></blockquote>
<blockquote><p><strong>mikosann</strong> <code>(Wed 22 Sep 2021 13:57)</code> - <em>Upvotes: 3</em></p><p>I mean the solution is correct. Not the answer.</p></blockquote>

</details>

---

[<< Previous Question](question_84.md) | [Home](/index.md) | [Next Question >>](question_86.md)
