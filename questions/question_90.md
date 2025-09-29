# Question 90

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are a data scientist using Azure Machine Learning Studio.

You need to normalize values to produce an output column into bins to predict a target column.

Solution: Apply an Equal Width with Custom Start and Stop binning mode.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>dija123</strong> <code>(Mon 12 Dec 2022 17:48)</code> - <em>Upvotes: 8</em></p><p>I believe Quantile normalization is the correct answer</p></blockquote>
<blockquote><p><strong>SnowCheetah</strong> <code>(Sat 25 Jun 2022 08:00)</code> - <em>Upvotes: 6</em></p><p>&quot;Equal Width with Custom Start and Stop binning mode&quot;
only do binning but with goal it&#x27;s require normalized as well as binning problem. Thus that&#x27;s incorrect

@Askme101 provide possible answer using MDL is correct one https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins</p></blockquote>

<blockquote><p><strong>Hisayuki</strong> <code>(Mon 04 Nov 2024 01:02)</code> - <em>Upvotes: 2</em></p><p>Should use Quantiles. The quantile method assigns values to bins based on percentile ranks, because you need to normalize, while Equal Width puts the data into each bin at the same interval between starting and ending values.</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Mon 08 Jan 2024 11:22)</code> - <em>Upvotes: 1</em></p><p>Option A</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Thu 30 Mar 2023 07:32)</code> - <em>Upvotes: 1</em></p><p>Group Data into Bins
https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/group-data-into-bins</p></blockquote>
<blockquote><p><strong>Aleem</strong> <code>(Fri 06 May 2022 05:53)</code> - <em>Upvotes: 5</em></p><p>Entropy MDL may be the best answer, but the question is whether this solution meets the goal stated. The solution stated may not be optimal but does bin the values.</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Thu 05 May 2022 14:20)</code> - <em>Upvotes: 6</em></p><p>Entropy MDL is not available in designer. The answer applies only to studio(classic). If asked in Designer context, I think the answer is actually Yes.</p></blockquote>
<blockquote><p><strong>Askme101</strong> <code>(Sun 26 Dec 2021 13:21)</code> - <em>Upvotes: 3</em></p><p>Entropy MDL is the correct answer see below https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/group-data-into-bins</p></blockquote>
<blockquote><p><strong>concernedCitizen</strong> <code>(Tue 13 Jul 2021 16:13)</code> - <em>Upvotes: 3</em></p><p>&#x27;A&#x27; is correct per the link:
&quot;Equal Width with Custom Start and Stop: This method is like the Equal Width option, but you can specify both lower and upper bin boundaries.&quot;</p></blockquote>
<blockquote><p><strong>Rickii</strong> <code>(Fri 16 Jul 2021 14:28)</code> - <em>Upvotes: 5</em></p><p>Correct answer is B. Bcoz u have target column.</p></blockquote>
<blockquote><p><strong>juandante</strong> <code>(Mon 17 May 2021 10:00)</code> - <em>Upvotes: 2</em></p><p>Answer B</p></blockquote>
<blockquote><p><strong>methodidacte</strong> <code>(Wed 20 Jan 2021 07:44)</code> - <em>Upvotes: 1</em></p><p>&quot;Studio&quot; is now called &quot;Designer&quot;</p></blockquote>

</details>

---

[<< Previous Question](question_89.md) | [Home](../index.md) | [Next Question >>](question_91.md)
