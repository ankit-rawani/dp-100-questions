# Question 239

You are solving a classification task.

You must evaluate your model on a limited data sample by using k-fold cross-validation. You start by configuring a k parameter as the number of splits.

You need to configure the k parameter for the cross-validation.

Which value should you use?

- A.k=0.5
- B.k=0.01
- C.k=5
- D.k=1

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>RSMCT2011</strong> <code>(Wed 01 Jul 2020 09:26)</code> - <em>Upvotes: 16</em></p><p>The choice of k is usually 5 or 10, but there is no formal rule. As k gets larger, the difference in size between the training set and the resampling subsets gets smaller. As this difference decreases, the bias of the technique becomes smaller
https://machinelearningmastery.com/k-fold-cross-validation/</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Sun 05 Jan 2025 00:34)</code> - <em>Upvotes: 1</em></p><p>It should be C (k=5)</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Fri 22 Nov 2024 08:45)</code> - <em>Upvotes: 1</em></p><p>It&#x27;s C. usually 5 or 10.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 19 Apr 2024 03:50)</code> - <em>Upvotes: 1</em></p><p>Default value of k-fold cross-validation is 10 . https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/cross-validate-model?view=azureml-api-2#how-cross-validation-works . Choose nearest answer, it is C with k = 5 .</p></blockquote>
<blockquote><p><strong>orionduo</strong> <code>(Thu 29 Feb 2024 07:39)</code> - <em>Upvotes: 1</em></p><p>5 is correct</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Wed 14 Sep 2022 06:54)</code> - <em>Upvotes: 2</em></p><p>B. 10 is the answer</p></blockquote>
<blockquote><p><strong>roncil</strong> <code>(Sat 12 Aug 2023 21:48)</code> - <em>Upvotes: 3</em></p><p>B. 0.01 is not 10 that&#x27;s wrong. I think the best answer is 5</p></blockquote>
<blockquote><p><strong>SnowCheetah</strong> <code>(Thu 16 Dec 2021 09:48)</code> - <em>Upvotes: 4</em></p><p>based on process on elimination
K cannot be less than 1, thus 0.9, 0.5
K= 1 meaning does experiment only 1 time which shouldn&#x27;t do fo k fold validation
Thus k =10 is possible correct answer

In the choice number of K, there is not formal value that should do. https://machinelearningmastery.com/k-fold-cross-validation/</p></blockquote>

<blockquote><p><strong>levm39</strong> <code>(Tue 14 Dec 2021 14:36)</code> - <em>Upvotes: 1</em></p><p>k=5, answer is missing</p></blockquote>
<blockquote><p><strong>ATT</strong> <code>(Tue 16 Mar 2021 04:53)</code> - <em>Upvotes: 2</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/cross-validate-model</p></blockquote>

</details>

---

[<< Previous Question](question_238.md) | [Home](../index.md) | [Next Question >>](question_240.md)
