# Question 492

You have a dataset that contains salary information for users. You plan to generate an aggregate salary report that shows average salaries by city.

Privacy of individuals must be preserved without impacting accuracy, completeness, or reliability of the data. The aggregation must be statistically consistent with the distribution of the original data. You must return an approximation of the data instead of the raw data.

You need to apply a differential privacy approach.

What should you do?

- A.Add noise to the salary data during the analysis
- B.Encrypt the salary data before analysis
- C.Remove the salary data
- D.Convert the salary data to the average column value

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>bbigwolf</strong> <code>(Wed 01 Mar 2023 07:21)</code> - <em>Upvotes: 12</em></p><p>Should be A</p></blockquote>
<blockquote><p><strong>giusecozza</strong> <code>(Sat 04 Mar 2023 09:36)</code> - <em>Upvotes: 2</em></p><p>agree. Isn&#x27;it about responsible AI?</p></blockquote>
<blockquote><p><strong>GHill1982</strong> <code>(Wed 17 Jul 2024 19:11)</code> - <em>Upvotes: 1</em></p><p>The correct answer is A. Add noise to the salary data during the analysis.</p></blockquote>
<blockquote><p><strong>ferren</strong> <code>(Sat 24 Feb 2024 23:21)</code> - <em>Upvotes: 1</em></p><p>Bard says it is A</p></blockquote>
<blockquote><p><strong>BR_CS</strong> <code>(Sat 17 Feb 2024 16:58)</code> - <em>Upvotes: 1</em></p><p>The question in unclear. If the statistics in only there to report average per city the answer is correct when the salary column is filled with the average per city. Distribution statistics will not work anymore, though. Adding noise WILL change the data ever so slightly.</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Fri 22 Sep 2023 03:48)</code> - <em>Upvotes: 1</em></p><p>Answer is A</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 24 Aug 2023 19:29)</code> - <em>Upvotes: 3</em></p><p>A. Add noise to the salary data during the analysis.
To apply differential privacy, you need to add noise to the salary data during analysis. Adding noise is a technique to introduce randomness to the data in a way that preserves privacy while minimizing the impact on the accuracy, completeness, and reliability of the data. Differential privacy provides a formal guarantee that the data will be protected against privacy attacks.
Converting the salary data to the average column value (option D) does not provide differential privacy. This option would eliminate the salary data altogether and only show the average salary by city, but it would not preserve the statistical properties of the original data or provide any privacy protection.</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Thu 10 Aug 2023 19:06)</code> - <em>Upvotes: 1</em></p><p>it should be A, because we are adding noising to be sure we mask data</p></blockquote>
<blockquote><p><strong>BTAB</strong> <code>(Thu 13 Jul 2023 02:00)</code> - <em>Upvotes: 1</em></p><p>A.  Adding noise that is consistent with the data is the correct answer.</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Sun 09 Jul 2023 18:50)</code> - <em>Upvotes: 2</em></p><p>Encrypting or averaging don&#x27;t meet the requirement.</p></blockquote>
<blockquote><p><strong>roxas8569</strong> <code>(Fri 09 Jun 2023 06:19)</code> - <em>Upvotes: 1</em></p><p>https://microsoft.github.io/azureml-ops-accelerator/4-Migrate/1-KeyAzureMLConceptsForOps.html#differential-privacy</p></blockquote>
<blockquote><p><strong>PremPatrick</strong> <code>(Wed 17 May 2023 07:04)</code> - <em>Upvotes: 1</em></p><p>should be A</p></blockquote>

</details>

---

[<< Previous Question](question_491.md) | [Home](../index.md) | [Next Question >>](question_493.md)
