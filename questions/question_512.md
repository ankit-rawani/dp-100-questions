# Question 512

You need to visually identify whether outliers exist in the Age column and quantify the outliers before the outliers are removed.

Which three Azure Machine Learning Studio modules should you use? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

- A.Create Scatterplot
- B.Summarize Data
- C.Clip Values
- D.Replace Discrete Values
- E.Build Counting Transform

<details>
  <summary>Show Suggested Answer</summary>

<strong>ABC</strong><br>

<p>B: To have a global view, the summarize data module can be used. Add the module and connect it to the data set that needs to be visualized.</p>
<p>A: One way to quickly identify Outliers visually is to create scatter plots.</p>
<p>C: The easiest way to treat the outliers in Azure ML is to use the Clip Values module. It can identify and optionally replace data values that are above or below a specified threshold.</p>
<p>You can use the Clip Values module in Azure Machine Learning Studio, to identify and optionally replace data values that are above or below a specified threshold. This is useful when you want to remove outliers or replace them with a mean, a constant, or other substitute value.</p>
<p>Reference:</p>
<p>https://blogs.msdn.microsoft.com/azuredev/2017/05/27/data-cleansing-tools-in-azure-machine-learning/ https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/clip-values</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>concernedCitizen</strong> <code>(Fri 14 Jan 2022 17:10)</code> - <em>Upvotes: 13</em></p><p>Option C is a method to fix outliers, not visualize them</p></blockquote>
<blockquote><p><strong>Sjefen</strong> <code>(Mon 18 Sep 2023 12:19)</code> - <em>Upvotes: 3</em></p><p>That&#x27;s not a problem, the combination of the 3 answers are supposed to do the required actions, not every option doing everything.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sun 25 Aug 2024 22:49)</code> - <em>Upvotes: 1</em></p><p>The &quot;Clip Values&quot; module in Azure Machine Learning Studio is used to limit the values in a column to a specified range. This can be useful in cases where there are extreme values that need to be limited to a certain threshold. However, this module does not identify or quantify outliers in a dataset. Therefore, it would not be useful for the task of identifying and quantifying outliers in the &quot;Age&quot; column.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sun 25 Aug 2024 22:48)</code> - <em>Upvotes: 3</em></p><p>The three Azure Machine Learning Studio modules that should be used to visually identify and quantify outliers in the Age column before they are removed are:

A. Create Scatterplot: This module can be used to create a scatter plot of the data, which allows for visual identification of outliers.

B. Summarize Data: This module can be used to calculate basic statistics for the Age column, such as mean, median, standard deviation, and quartiles, which can help to identify outliers.

E. Build Counting Transform: This module can be used to create a frequency distribution of the Age column, which can help to identify outliers that occur with low frequency.

Therefore, the correct answers are A, B, and E. The modules C and D are not relevant for identifying and quantifying outliers in the Age column.</p></blockquote>

<blockquote><p><strong>BTAB</strong> <code>(Mon 15 Jul 2024 12:35)</code> - <em>Upvotes: 1</em></p><p>Each correct answer presents part of the solution.  Therefore, the question asks to visualize before removing. Since A &amp; B are visualizations, and C does the removing, all 3 answers are part of the solution.  But we need to do A &amp; B before we utilize C.  Answer is correct.

This brings up a good point with Microsoft tests. Make sure to understand sequencing questions vs. questions that say each answer PRESENTS part of the solution.</p></blockquote>

<blockquote><p><strong>TheCyanideLancer</strong> <code>(Sat 22 Jul 2023 05:37)</code> - <em>Upvotes: 1</em></p><p>The give answer seems to be right, below text from documentation regarding clip values module - 
https://docs.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/clip-values

Module overview
This article describes how to use the Clip Values module in Machine Learning Studio (classic), to identify and optionally replace data values that are above or below a specified threshold. This is useful when you want to remove outliers or replace them with a mean, a constant, or other substitute value</p></blockquote>

<blockquote><p><strong>RyanTsai</strong> <code>(Sun 19 Mar 2023 16:09)</code> - <em>Upvotes: 4</em></p><p>ans: A,B,E</p></blockquote>
<blockquote><p><strong>bdsrca</strong> <code>(Tue 28 Feb 2023 15:39)</code> - <em>Upvotes: 4</em></p><p>. Create Scatterplot
.Summarize Data
.Build Counting Transform</p></blockquote>
<blockquote><p><strong>Lucario95</strong> <code>(Wed 23 Nov 2022 12:04)</code> - <em>Upvotes: 2</em></p><p>QUESTION &quot;You need to visually identify whether outliers exist in the Age column and quantify the outliers BEFORE the outliers are removed.&quot;

Thus answer C is part of the answer</p></blockquote>

<blockquote><p><strong>hima618</strong> <code>(Sun 20 Mar 2022 07:30)</code> - <em>Upvotes: 2</em></p><p>question is only about visualization, so option c is incorrect.</p></blockquote>
<blockquote><p><strong>Laredo</strong> <code>(Sat 21 May 2022 02:02)</code> - <em>Upvotes: 8</em></p><p>solution is correct
1. visually identify whether outliers exist in the Age column and
2. quantify the outliers before 
3. the outliers are removed.</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Sun 25 Sep 2022 18:38)</code> - <em>Upvotes: 1</em></p><p>I agree</p></blockquote>
<blockquote><p><strong>Dasist</strong> <code>(Tue 27 Sep 2022 17:19)</code> - <em>Upvotes: 1</em></p><p>They ask to identify and visualize the outliers. Removing them is not asked. Therefore it&#x27;s only A and B</p></blockquote>
<blockquote><p><strong>Dasist</strong> <code>(Wed 28 Sep 2022 12:52)</code> - <em>Upvotes: 3</em></p><p>Seems like it cannot be only A and B as the question ask THREE modules not two. Then I must agree with C. Question is ambiguous</p></blockquote>

</details>

---

[<< Previous Question](question_511.md) | [Home](../index.md) | [Next Question >>](question_513.md)
