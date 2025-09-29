# Question 217

You are solving a classification task.

You must evaluate your model on a limited data sample by using k-fold cross-validation. You start by configuring a k parameter as the number of splits.

You need to configure the k parameter for the cross-validation.

Which value should you use?

- A.k=1
- B.k=10
- C.k=0.5
- D.k=0.9

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

<p>Leave One Out (LOO) cross-validation</p>
<p>Setting K = n (the number of observations) yields n-fold and is called leave-one out cross-validation (LOO), a special case of the K-fold approach.</p>
<p>LOO CV is sometimes useful but typically doesn&#x27;t shake up the data enough. The estimates from each fold are highly correlated and hence their average can have high variance.</p>
<p>This is why the usual choice is K=5 or 10. It provides a good compromise for the bias-variance tradeoff.</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>rjile</strong> <code>(Tue 23 Nov 2021 11:07)</code> - <em>Upvotes: 10</em></p><p>The choice of k is usually 5 or 10</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Fri 28 Jun 2024 11:20)</code> - <em>Upvotes: 1</em></p><p>B - ChatGPT
When performing k-fold cross-validation to evaluate a classification model, you need to choose an appropriate value for the parameter k, which represents the number of splits or folds.

In this scenario, the most commonly used value for k is:

B. k = 10

Setting k to 10 means that the dataset will be divided into 10 equal-sized folds or subsets. The cross-validation process will then run 10 iterations, where each iteration uses 9 folds for training and 1 fold for validation. This allows for a comprehensive evaluation of the model&#x27;s performance on different subsets of the data.

It&#x27;s worth noting that the choice of k can depend on factors such as the size of the dataset, the available computational resources, and the specific requirements of the task at hand. However, a value of k=10 is often considered a good starting point and is commonly used in practice for cross-validation.

Therefore, option B (k = 10) is the appropriate value to configure the k parameter for the cross-validation in this classification task.</p></blockquote>

<blockquote><p><strong>serggar</strong> <code>(Sat 11 Sep 2021 15:15)</code> - <em>Upvotes: 3</em></p><p>isn&#x27;t this duplicated?</p></blockquote>
<blockquote><p><strong>gbganalyst</strong> <code>(Fri 24 Jun 2022 09:37)</code> - <em>Upvotes: 2</em></p><p>Not at all.</p></blockquote>

</details>

---

[<< Previous Question](question_216.md) | [Home](../index.md) | [Next Question >>](question_218.md)
