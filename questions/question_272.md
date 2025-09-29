# Question 272

You are performing clustering by using the K-means algorithm.

You need to define the possible termination conditions.

Which three conditions can you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- A.Centroids do not change between iterations.
- B.The residual sum of squares (RSS) rises above a threshold.
- C.The residual sum of squares (RSS) falls below a threshold.
- D.A fixed number of iterations is executed.
- E.The sum of distances between centroids reaches a maximum.

<details>
  <summary>Show Suggested Answer</summary>

<strong>ACD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>nikhilmehra</strong> <code>(Tue 15 Aug 2023 20:21)</code> - <em>Upvotes: 7</em></p><p>Correct Answer</p></blockquote>
<blockquote><p><strong>nikhilmehra</strong> <code>(Tue 15 Aug 2023 20:21)</code> - <em>Upvotes: 5</em></p><p>AD: The algorithm terminates when the centroids stabilize or when a specified number of iterations are completed.
C: A measure of how well the centroids represent the members of their clusters is the residual sum of squares or RSS, the squared distance of each vector from its centroid summed over all vectors. RSS is the objective function and our goal is to minimize it.
References:
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/k-means-clustering https://nlp.stanford.edu/IR-book/html/htmledition/k-means-1.html</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Fri 19 Jul 2024 14:52)</code> - <em>Upvotes: 2</em></p><p>correct.

AD: The algorithm terminates when the centroids stabilize or when a specified number of iterations are completed.
C: A measure of how well the centroids represent the members of their clusters is the residual sum of squares or RSS, the squared distance of each vector from its centroid summed over all vectors. RSS is the objective function and our goal is to minimize it.</p></blockquote>

<blockquote><p><strong>J_AR</strong> <code>(Mon 01 Jul 2024 14:04)</code> - <em>Upvotes: 1</em></p><p>Link is outdated.</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Fri 14 Jun 2024 10:51)</code> - <em>Upvotes: 1</em></p><p>Answer : ACD</p></blockquote>
<blockquote><p><strong>zoo1997</strong> <code>(Sat 18 May 2024 21:57)</code> - <em>Upvotes: 1</em></p><p>Is this still being tested, as it is part of the ML Studio Classic.</p></blockquote>

</details>

---

[<< Previous Question](question_271.md) | [Home](../index.md) | [Next Question >>](question_273.md)
