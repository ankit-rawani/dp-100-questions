# Question 8

This question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the recommendation satisfies the requirements.

You have been tasked with evaluating your model on a partial data sample via k-fold cross-validation.

You have already configured a k parameter as the number of splits. You now have to configure the k parameter for the cross-validation with the usual value choice.

Recommendation: You configure the use of the value k=3.

Will the requirements be satisfied?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>saurabh288</strong> <code>(Thu 22 Jul 2021 06:51)</code> - <em>Upvotes: 13</em></p><p>Usual choice is key word here and usual choice is K=5 or 10. So answer is B.</p></blockquote>
<blockquote><p><strong>gaint</strong> <code>(Mon 05 Jul 2021 05:15)</code> - <em>Upvotes: 7</em></p><p>Answer should be A</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Sun 25 Jul 2021 07:02)</code> - <em>Upvotes: 3</em></p><p>Agree. Why can&#x27;t be 3?  3 is not “the usual value choice”？</p></blockquote>
<blockquote><p><strong>emmanuelodenyire</strong> <code>(Thu 26 Sep 2024 10:02)</code> - <em>Upvotes: 3</em></p><p>I will go with B.
The answer to the question is B. No. The recommendation to use k=3 is a common practice in k-fold cross-validation, but it may not necessarily satisfy the requirements in every case. It depends on the specific requirements of the task and the characteristics of the data sample.

For example, if the data sample is small, using k=3 may not provide enough training data for the model to learn from, resulting in a high variance in the evaluation metric. In this case, a larger value of k may be more appropriate. On the other hand, if the data sample is very large, using k=3 may result in a low bias but high variance, in which case a smaller value of k may be more appropriate.

Therefore, it&#x27;s important to consider the specific requirements and characteristics of the task and data sample when choosing the value of k for k-fold cross-validation. In general, the recommendation to use k=3 is a good starting point, but it may not always be the best choice.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 17 Feb 2024 11:08)</code> - <em>Upvotes: 1</em></p><p>The usual choice for k in k-fold cross-validation, especially in the context of evaluating machine learning models, is typically k=5 or k=10</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 20 Oct 2023 09:33)</code> - <em>Upvotes: 1</em></p><p>Default value k = 10</p></blockquote>
<blockquote><p><strong>lookaaaa</strong> <code>(Mon 21 Nov 2022 21:50)</code> - <em>Upvotes: 1</em></p><p>Usually we would choose k = 10</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Thu 17 Nov 2022 15:21)</code> - <em>Upvotes: 1</em></p><p>k-fold involves many more procedures, not only k configuration</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Wed 15 Jun 2022 12:38)</code> - <em>Upvotes: 1</em></p><p>I have no idea for this one, usual value = 10 default, and in designer you cannot change that, but you can add a partition and sample step to set K=3, so what is the question asking for???</p></blockquote>
<blockquote><p><strong>Thornehead</strong> <code>(Sat 26 Mar 2022 01:09)</code> - <em>Upvotes: 1</em></p><p>Usually K = 5 or 10. So B is the correct answer.</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sat 12 Mar 2022 08:54)</code> - <em>Upvotes: 1</em></p><p>Ok.. it says &quot;Usual value choice&quot; -- I guess then the answer is No... it should be 5 or 10.</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sat 12 Mar 2022 08:53)</code> - <em>Upvotes: 2</em></p><p>I don&#x27;t think anyone restricts you from selecting 3.</p></blockquote>
<blockquote><p><strong>Tsardoz</strong> <code>(Sun 16 Jan 2022 09:54)</code> - <em>Upvotes: 3</em></p><p>You can use as many splits as you want. It all depends on the data. Train/test/validate is basically 3 splits that are just swapped around. 3 is perfectly fine.</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Wed 15 Dec 2021 08:15)</code> - <em>Upvotes: 1</em></p><p>3 is not the usual value choice</p></blockquote>
<blockquote><p><strong>sim39</strong> <code>(Tue 07 Sep 2021 09:51)</code> - <em>Upvotes: 2</em></p><p>k can absolutely be 3</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Tue 31 Aug 2021 11:03)</code> - <em>Upvotes: 2</em></p><p>answer is correct</p></blockquote>
<blockquote><p><strong>dijaa</strong> <code>(Sat 28 Aug 2021 05:52)</code> - <em>Upvotes: 4</em></p><p>answer is correct, the default is 10</p></blockquote>
<blockquote><p><strong>dushmantha</strong> <code>(Mon 30 Aug 2021 09:51)</code> - <em>Upvotes: 3</em></p><p>Not only 10, sometime 5 is commonly used</p></blockquote>

</details>

---

[<< Previous Question](question_7.md) | [Home](/index.md) | [Next Question >>](question_9.md)
