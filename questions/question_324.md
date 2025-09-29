# Question 324

You need to evaluate the potential risk of exposing personal information based on the values of epsilon and delta for differential privacy. You create a privacy report.

What does an epsilon value greater than one represent?

- A.The privacy of data is preserved and there is limited impact on data accuracy.
- B.There is a high risk of exposing the actual data that is uses to generate the report.
- C.The data used in the report is very noisy.

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>bobML</strong> <code>(Wed 11 Sep 2024 10:44)</code> - <em>Upvotes: 2</em></p><p>An epsilon value greater than one represents:

B. There is a high risk of exposing the actual data that is used to generate the report.

When epsilon is greater than one, it indicates that the privacy guarantee is weakened, and there is a higher risk of revealing sensitive or personal information from the data used in the report. A larger epsilon allows for more noise in the data, which can reduce privacy protection. Typically, smaller values of epsilon are preferred to provide stronger privacy guarantees.</p></blockquote>

<blockquote><p><strong>Nghia1</strong> <code>(Thu 06 Jun 2024 22:34)</code> - <em>Upvotes: 2</em></p><p>That is correct:
 epsilon is a non-negative value that provides an inverse measure of the amount of noise added to the data. A low epsilon results in a dataset with a greater level of privacy, while a high epsilon results in a dataset that is closer to the original data.</p></blockquote>
<blockquote><p><strong>vish9</strong> <code>(Mon 13 May 2024 19:15)</code> - <em>Upvotes: 1</em></p><p>Looks correct.</p></blockquote>

</details>

---

[<< Previous Question](question_323.md) | [Home](../index.md) | [Next Question >>](question_325.md)
