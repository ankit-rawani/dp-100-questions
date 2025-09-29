# Question 350

HOTSPOT

-

You perform hyperparameter tuning with Azure Machine Learning.

You create the following Python code:

![Question Image](images/q350_q_image547.png)

For each of the following statements, select Yes if the statement is true. Otherwise, select No.

![Question Image](images/q350_q_image548.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q350_ans_0_image549.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>BR_CS</strong> <code>(Sat 17 Feb 2024 12:53)</code> - <em>Upvotes: 6</em></p><p>YES, NO, YES
normal is used not lognormal</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Sun 24 Nov 2024 02:56)</code> - <em>Upvotes: 1</em></p><p>Yes No Yes
If X is normally distributed with mean μ and standard deviation σ, then 
log(X) is not normally distributed. The logarithm function is nonlinear and can distort the distribution of the original variable.
For log(X) to be normal, X must be lognormal.

Since learning_rate is normal distribution not lognormal, second one should be no.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Mon 05 Aug 2024 01:52)</code> - <em>Upvotes: 1</em></p><p>Yes, Yes, Yes.

if the distribution is normal, taking a log of the same distribution will resemble normal distribution.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Mon 05 Aug 2024 01:54)</code> - <em>Upvotes: 2</em></p><p>*lognormal</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Mon 05 Aug 2024 01:57)</code> - <em>Upvotes: 3</em></p><p>and second statement is false i think.</p></blockquote>
<blockquote><p><strong>Ran2025</strong> <code>(Mon 22 Apr 2024 05:42)</code> - <em>Upvotes: 1</em></p><p>YES YES YES

the &#x27;logarithm&#x27; word.......</p></blockquote>
<blockquote><p><strong>adescientist</strong> <code>(Tue 27 Feb 2024 13:25)</code> - <em>Upvotes: 4</em></p><p>I agree, since the the search distribution of learning rate is Normal NOT Lognormal.
The solution should be: YES, NO, YES</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 26 Jan 2024 20:08)</code> - <em>Upvotes: 3</em></p><p>YES, YES, YES</p></blockquote>

</details>

---

[<< Previous Question](question_349.md) | [Home](/index.md) | [Next Question >>](question_351.md)
