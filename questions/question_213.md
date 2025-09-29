# Question 213

You are building a regression model for estimating the number of calls during an event.

You need to determine whether the feature values achieve the conditions to build a Poisson regression model.

Which two conditions must the feature set contain? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

* A.The label data must be a negative value.
* B.The label data must be whole numbers.
* C.The label data must be non-discrete.
* D.The label data must be a positive value.
* E.The label data can be positive or negative.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>BD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Arif001300</strong> <code>(Fri 30 Oct 2020 16:18)</code> - <em>Upvotes: 17</em></p><p>Answer is B and D</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 02 Dec 2024 12:17)</code> - <em>Upvotes: 1</em></p><p>Poison regression is about number of count and it has to be positive and whole number.</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Thu 28 Dec 2023 12:15)</code> - <em>Upvotes: 1</em></p><p>B, D - ChatGPT</p></blockquote>
<blockquote><p><strong>krishna1818</strong> <code>(Wed 29 Nov 2023 11:31)</code> - <em>Upvotes: 1</em></p><p>yes Poisson distribution is applicable for whole numbers which are positive</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Tue 22 Nov 2022 14:57)</code> - <em>Upvotes: 1</em></p><p>The definition for Poisson Regression is that Y must be counts, so it is a positive integer</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Mon 13 Jun 2022 16:58)</code> - <em>Upvotes: 2</em></p><p>Agree with B &amp; D</p></blockquote>
<blockquote><p><strong>anjurad</strong> <code>(Mon 25 Oct 2021 20:23)</code> - <em>Upvotes: 1</em></p><p>The outcome variable in a Poisson regression cannot have negative numbers, so input variables cannot be negative + Poisson regression is often used for modelling count data (whole numbers)</p></blockquote>
<blockquote><p><strong>lance_96</strong> <code>(Sat 11 Sep 2021 07:45)</code> - <em>Upvotes: 2</em></p><p>I also share the answer B &amp; D. If you answer only B, you risk that the final count could be negative, as whole numbers in general also include negative whole numbers.</p></blockquote>
<blockquote><p><strong>saurabhk1</strong> <code>(Sat 04 Sep 2021 15:10)</code> - <em>Upvotes: 1</em></p><p>I think, the answer is only B, Poison distribution can be used for count only. Count is a discrete quantity(Whole number). 

When we talk about the positive number, they can be whole or real number. i mean, 4 and 4.2 are both positive number. But, 4 is a whole number.</p></blockquote>
<blockquote><p><strong>nikhilmehra</strong> <code>(Sat 21 Aug 2021 19:41)</code> - <em>Upvotes: 2</em></p><p>Agree it should be B &amp; D</p></blockquote>
<blockquote><p><strong>Askme101</strong> <code>(Sat 26 Jun 2021 13:47)</code> - <em>Upvotes: 3</em></p><p>Agree it should be B &amp;D</p></blockquote>

</details>

---

[<< Previous Question](question_212.md) | [Home](/index.md) | [Next Question >>](question_214.md)
