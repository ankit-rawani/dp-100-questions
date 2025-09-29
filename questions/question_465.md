# Question 465

You are determining if two sets of data are significantly different from one another by using Azure Machine Learning Studio.

Estimated values in one set of data may be more than or less than reference values in the other set of data. You must produce a distribution that has a constant

Type I error as a function of the correlation.

You need to produce the distribution.

Which type of distribution should you produce?

* A.Unpaired t-test with a two-tail option
* B.Unpaired t-test with a one-tail option
* C.Paired t-test with a one-tail option
* D.Paired t-test with a two-tail option

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>David_Tadeu</strong> <code>(Tue 12 Apr 2022 15:13)</code> - <em>Upvotes: 5</em></p><p>&quot;A two-tailed test is appropriate if the estimated value is greater or less than a certain range of values, for example, whether a test taker may score above or below a specific range of scores.&quot; https://en.wikipedia.org/wiki/One-_and_two-tailed_tests</p></blockquote>
<blockquote><p><strong>jl420</strong> <code>(Mon 11 Nov 2024 13:56)</code> - <em>Upvotes: 1</em></p><p>While the question does not state whether the datasets are paired, it actually seems more likely that the data is paired. Here’s why:

&quot;Estimated values in one set of data may be more than or less than reference values in the other set of data&quot;:

This wording suggests a comparison between estimated values and reference values. Often, estimated values are paired with reference values to evaluate accuracy or difference. For example, you might be comparing predicted values with observed values, which is a classic paired scenario.
&quot;Constant Type I error as a function of correlation&quot;:

Maintaining a constant Type I error rate as a function of correlation typically implies that the correlation between two sets of data points (e.g., estimated vs. reference) is being taken into account. This is a key aspect of a paired t-test, where the test accounts for the natural pairing and potential correlation within the pairs.

That said, D is correct answer. Probably. Maybe.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 18 May 2024 06:07)</code> - <em>Upvotes: 2</em></p><p>If we assume that the two data sets are uncorrelated, then choose the unpaired t-test. If the two data sets are related (for example, two measurements from the same set of samples), choose a paired t-test. The question does not clearly state whether the data sets are paired, but based on common data comparison scenarios, we can infer that they are paired.</p></blockquote>
<blockquote><p><strong>ZoeJ</strong> <code>(Thu 27 Apr 2023 06:23)</code> - <em>Upvotes: 1</em></p><p>i think the given answer is correct</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 24 Feb 2023 02:17)</code> - <em>Upvotes: 2</em></p><p>Option C is the correct answer: Paired t-test with a one-tail option.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sun 12 Jun 2022 14:38)</code> - <em>Upvotes: 2</em></p><p>I guess two tails due to two data set are extremely negatively correlated???
Not sure whether that is the ask from the question though, cannot find any reference from azureml
Purely statistically speaking, I agree with one tail paired test</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sun 13 Mar 2022 06:15)</code> - <em>Upvotes: 3</em></p><p>Answer is D Paired t test with two test. But I highly doubt this question is still being asked</p></blockquote>
<blockquote><p><strong>spaceykacey</strong> <code>(Wed 03 Nov 2021 05:49)</code> - <em>Upvotes: 1</em></p><p>Is this question still being asked?</p></blockquote>
<blockquote><p><strong>spaceykacey</strong> <code>(Wed 03 Nov 2021 05:51)</code> - <em>Upvotes: 1</em></p><p>since its from ML Studio (Classic)</p></blockquote>
<blockquote><p><strong>bdsrca</strong> <code>(Mon 30 Aug 2021 00:02)</code> - <em>Upvotes: 2</em></p><p>A distribution that has a constant
Type I error as a function of the correlation.   = Paired</p></blockquote>
<blockquote><p><strong>saurabhk1</strong> <code>(Thu 04 Mar 2021 17:10)</code> - <em>Upvotes: 4</em></p><p>It should be Unpaired as Each pair of scores is independent of every other pair.
And , one tail, we are looking for only inequality(more or less)</p></blockquote>
<blockquote><p><strong>lucazav</strong> <code>(Thu 15 Oct 2020 10:16)</code> - <em>Upvotes: 2</em></p><p>This picture is taken from Wikipedia: https://en.wikipedia.org/wiki/Student&#x27;s_t-test#Unpaired_and_paired_two-sample_t-tests</p></blockquote>
<blockquote><p><strong>Zhuo</strong> <code>(Mon 25 May 2020 08:04)</code> - <em>Upvotes: 1</em></p><p>Why paired?</p></blockquote>
<blockquote><p><strong>JUEI</strong> <code>(Sat 25 Jul 2020 06:24)</code> - <em>Upvotes: 4</em></p><p>I think the keyword is &quot;sets&quot; which is of &quot;pairs&quot; as the definition Choose a paired t-test when these conditions apply:

You have a matched pairs of scores. For example, you might have two different measures per person, or matched pairs of individuals (such as a husband and wife).

Each pair of scores is independent of every other pair.

The sampling distribution of d is normal.

A paired t-test is useful when comparing related cases. By averaging the differences between the scores of the paired cases, you can determine whether the total difference is statistically significant.</p></blockquote>
<blockquote><p><strong>yanbin43</strong> <code>(Tue 24 Nov 2020 12:17)</code> - <em>Upvotes: 12</em></p><p>The key phrase is &quot;reference values in the other set of data&quot;. It indicates that the two sets of data come from the same source hence paired.</p></blockquote>
<blockquote><p><strong>hendrata</strong> <code>(Mon 08 Jun 2020 21:21)</code> - <em>Upvotes: 2</em></p><p>I agree it should be unpaired</p></blockquote>
<blockquote><p><strong>mhall1</strong> <code>(Wed 24 Jun 2020 05:33)</code> - <em>Upvotes: 19</em></p><p>Paired because they are estimated and reference values of the same thing (or at least I took that as implied). Thus, they are related and should vary together.</p></blockquote>
<blockquote><p><strong>agu_elli</strong> <code>(Thu 16 Sep 2021 21:35)</code> - <em>Upvotes: 1</em></p><p>It always will be &quot;values of the same thing&quot; since they are testing the same variable (hypothesis). For me, it is unpair since you can&#x27;t find another link (apart from the one you are testing. An example of pair is the e before and after effect of a pharmaceutical treatment on the same group of people.</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Sun 04 Jun 2023 14:30)</code> - <em>Upvotes: 1</em></p><p>Where did you find it in the description?</p></blockquote>

</details>

---

[<< Previous Question](question_464.md) | [Home](/index.md) | [Next Question >>](question_466.md)
