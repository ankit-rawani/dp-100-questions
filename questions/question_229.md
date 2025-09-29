# Question 229

You plan to use the Hyperdrive feature of Azure Machine Learning to determine the optimal hyperparameter values when training a model.

You must use Hyperdrive to try combinations of the following hyperparameter values:

✑ learning_rate: any value between 0.001 and 0.1

✑ batch_size: 16, 32, or 64

You need to configure the search space for the Hyperdrive experiment.

Which two parameter expressions should you use? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

* A.a choice expression for learning_rate
* B.a uniform expression for learning_rate
* C.a normal expression for batch_size
* D.a choice expression for batch_size
* E.a uniform expression for batch_size

<details>
  <summary>Show Suggested Answer</summary>

  <strong>BD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>michaelmorar</strong> <code>(Fri 08 Dec 2023 07:46)</code> - <em>Upvotes: 6</em></p><p>Correct!</p></blockquote>
<blockquote><p><strong>Deathking15</strong> <code>(Thu 14 Nov 2024 21:35)</code> - <em>Upvotes: 2</em></p><p>B,D is the correct answer. Learning_rate requires a continuous option, and A (Choice) is discrete. Batch_size requires a discrete option, and D (Choice) is the only.</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Fri 28 Jun 2024 11:55)</code> - <em>Upvotes: 2</em></p><p>A, D - ChatGPT
To configure the search space for the Hyperdrive experiment with the given hyperparameters, you should use the following parameter expressions:

A. A choice expression for learning_rate: This allows you to specify a discrete set of values for the learning rate, which in this case would be any value between 0.001 and 0.1.

D. A choice expression for batch_size: This allows you to specify a discrete set of values for the batch size, which in this case would be 16, 32, or 64.

The correct options are A and D.

Choice expressions are suitable for discrete values, while uniform expressions are suitable for continuous values. Since the learning rate can take any value between 0.001 and 0.1 (a continuous range), a choice expression is not appropriate. Similarly, a normal expression is not applicable to the batch size since it expects a continuous distribution, whereas batch size is discrete with specific values.

Therefore, the correct parameter expressions to configure the search space for the Hyperdrive experiment are:

A. A choice expression for learning_rate
D. A choice expression for batch_size</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Fri 28 Jun 2024 11:58)</code> - <em>Upvotes: 3</em></p><p>B, D - I Apologize</p></blockquote>
<blockquote><p><strong>ahson0124</strong> <code>(Thu 15 Feb 2024 13:46)</code> - <em>Upvotes: 2</em></p><p>Exam DP-100 topic 3 question 48 discussion</p></blockquote>
<blockquote><p><strong>datamijn</strong> <code>(Tue 02 Aug 2022 08:59)</code> - <em>Upvotes: 3</em></p><p>on exam 2/8/2021</p></blockquote>
<blockquote><p><strong>erp31</strong> <code>(Sun 31 Jul 2022 02:52)</code> - <em>Upvotes: 2</em></p><p>on exam 30/07/2021</p></blockquote>

</details>

---

[<< Previous Question](question_228.md) | [Home](/index.md) | [Next Question >>](question_230.md)
