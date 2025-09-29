# Question 62

You are creating a machine learning model. You have a dataset that contains null rows.

You need to use the Clean Missing Data module in Azure Machine Learning Studio to identify and resolve the null and missing data in the dataset.

Which parameter should you use?

* A.Replace with mean
* B.Remove entire column
* C.Remove entire row
* D.Hot Deck
* E.Custom substitution value
* F.Replace with mode

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 14:48)</code> - <em>Upvotes: 8</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>sar77</strong> <code>(Wed 16 Jul 2025 03:33)</code> - <em>Upvotes: 1</em></p><p>For a dataset with null rows, the most fitting parameter in Azure Machine Learning Studio’s Clean Missing Data module would be:

C. Remove entire row</p></blockquote>
<blockquote><p><strong>Ejire</strong> <code>(Sat 30 Nov 2024 10:09)</code> - <em>Upvotes: 1</em></p><p>The correct answer is C.
If you need voucher for any DP or AI exam contact me on +2348139103938</p></blockquote>
<blockquote><p><strong>krishna1818</strong> <code>(Wed 29 Nov 2023 10:23)</code> - <em>Upvotes: 1</em></p><p>Remove the entire row if there are less number of missing values</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Fri 27 Oct 2023 08:47)</code> - <em>Upvotes: 2</em></p><p>Null rows means the entire the row is null so C</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Thu 22 Sep 2022 14:47)</code> - <em>Upvotes: 1</em></p><p>Remove entire row: removes a row which contains a null value for a specified (it is a parameter of this procedure) set of columns</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 13 Sep 2022 10:28)</code> - <em>Upvotes: 2</em></p><p>&quot;Null Rows&quot;  So I am going with C</p></blockquote>
<blockquote><p><strong>guddusao</strong> <code>(Thu 27 Jan 2022 12:25)</code> - <em>Upvotes: 1</em></p><p>I think mode will work both numerical and categorical data. May be mode can impute the missing value.</p></blockquote>
<blockquote><p><strong>Abdulraoufhakeem</strong> <code>(Mon 03 Jan 2022 12:56)</code> - <em>Upvotes: 2</em></p><p>I agree to answer C</p></blockquote>
<blockquote><p><strong>Haet</strong> <code>(Mon 25 Oct 2021 06:33)</code> - <em>Upvotes: 3</em></p><p>Answer C is correct</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Fri 17 Sep 2021 08:01)</code> - <em>Upvotes: 3</em></p><p>A, B, C and F are valid.</p></blockquote>
<blockquote><p><strong>Dasist</strong> <code>(Mon 27 Sep 2021 14:26)</code> - <em>Upvotes: 6</em></p><p>They are not since we are only targeting NULL rows. C is correct</p></blockquote>
<blockquote><p><strong>Abhinav_nasaiitkgp</strong> <code>(Thu 15 Jul 2021 08:43)</code> - <em>Upvotes: 3</em></p><p>How other options are not valid? We can impute missing values with mean median and mode also. Something is missing in the question</p></blockquote>
<blockquote><p><strong>allanm</strong> <code>(Mon 15 Nov 2021 20:58)</code> - <em>Upvotes: 6</em></p><p>If you have ENTIRE rows that are null, chances are you don&#x27;t need them.</p></blockquote>
<blockquote><p><strong>Adrien_B</strong> <code>(Tue 10 Aug 2021 13:30)</code> - <em>Upvotes: 6</em></p><p>&quot;You have a dataset that contains null rows&quot; : If all the columns are Null for the row you don&#x27;t need to keep it</p></blockquote>
<blockquote><p><strong>ck1729</strong> <code>(Mon 19 Jul 2021 20:58)</code> - <em>Upvotes: 2</em></p><p>you can replace with mean or mode only if the column is of integer type since the values are nulls here it implies the data type is String or text. and hence from the options give only remove rows looks like the correct answer.</p></blockquote>
<blockquote><p><strong>ML_Novice</strong> <code>(Sat 14 May 2022 12:10)</code> - <em>Upvotes: 1</em></p><p>hello ck1729 
Does null means that the data type is only String or text ? 
Does this implies that missing values for integers and float are Nan and not Null? 
Otherwise how can we know the datatype of the missing values pleas</p></blockquote>

</details>

---

[<< Previous Question](question_61.md) | [Home](/index.md) | [Next Question >>](question_63.md)
