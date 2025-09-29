# Question 509

You need to implement a new cost factor scenario for the ad response models as illustrated in the performance curve exhibit.

Which technique should you use?

- A.Set the threshold to 0.5 and retrain if weighted Kappa deviates +/- 5% from 0.45.
- B.Set the threshold to 0.05 and retrain if weighted Kappa deviates +/- 5% from 0.5.
- C.Set the threshold to 0.2 and retrain if weighted Kappa deviates +/- 5% from 0.6.
- D.Set the threshold to 0.75 and retrain if weighted Kappa deviates +/- 5% from 0.15.

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

<p>Scenario:</p>
<p>Performance curves of current and proposed cost factor scenarios are shown in the following diagram:</p>
<img src="../images/q509_ref_4_0033400001.png" alt="Reference Image"><br>
<p>The ad propensity model uses a cut threshold is 0.45 and retrains occur if weighted Kappa deviated from 0.1 +/- 5%.</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>michaelmorar</strong> <code>(Sun 16 Jun 2024 06:28)</code> - <em>Upvotes: 2</em></p><p>Makes sense according to the provided explanation.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Mon 18 Dec 2023 14:06)</code> - <em>Upvotes: 1</em></p><p>Kappa = (P0 - Pe) / (1 - Pe)</p></blockquote>

</details>

---

[<< Previous Question](question_508.md) | [Home](../index.md) | [Next Question >>](question_510.md)
