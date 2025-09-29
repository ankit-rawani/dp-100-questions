# Question 473

HOTSPOT -

You are using a decision tree algorithm. You have trained a model that generalizes well at a tree depth equal to 10.

You need to select the bias and variance properties of the model with varying tree depth values.

Which properties should you select for each tree depth? To answer, select the appropriate options in the answer area.

Hot Area:

![Question Image](images/q473_q_0043900001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q473_ans_0_0044000001.png" alt="Answer Image"><br>
<p>In decision trees, the depth of the tree determines the variance. A complicated decision tree (e.g. deep) has low bias and high variance.</p>
<p>Note: In statistics and machine learning, the biasג€&quot;variance tradeoff is the property of a set of predictive models whereby models with a lower bias in parameter estimation have a higher variance of the parameter estimates across samples, and vice versa. Increasing the bias will decrease the variance. Increasing the variance will decrease the bias.</p>
<p>Reference:</p>
<p>https://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>dushmantha</strong> <code>(Mon 28 Feb 2022 10:02)</code> - <em>Upvotes: 7</em></p><p>Low depth means under fitting and higher depth means over fitting. So the selections are correct</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Tue 06 Aug 2024 10:56)</code> - <em>Upvotes: 1</em></p><p>&quot;bias: underfitting
variance: overfitting

Reference: https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 24 Aug 2023 03:14)</code> - <em>Upvotes: 2</em></p><p>In decision trees, the depth of the tree determines the variance. A complicated decision tree (e.g. deep) has low bias and high variance.  Increasing the bias will decrease the variance. Increasing the variance will decrease the bias.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Tue 13 Dec 2022 13:46)</code> - <em>Upvotes: 3</em></p><p>Correct!

The bias error is an error from erroneous assumptions in the learning algorithm. High bias can cause an algorithm to miss the relevant relations between features and target outputs (underfitting).

The variance is an error from sensitivity to small fluctuations in the training set. High variance may result from an algorithm modeling the random noise in the training data (overfitting).</p></blockquote>

</details>

---

[<< Previous Question](question_472.md) | [Home](/index.md) | [Next Question >>](question_474.md)
