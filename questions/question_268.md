# Question 268

HOTSPOT -

You are using C-Support Vector classification to do a multi-class classification with an unbalanced training dataset. The C-Support Vector classification using

Python code shown below:

![Question Image](../images/q268_q_0029700001.png)

You need to evaluate the C-Support Vector classification code.

Which evaluation statement should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q268_q_0029800001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q268_ans_0_0029800002.png" alt="Answer Image"><br>

<p>Box 1: Automatically adjust weights inversely proportional to class frequencies in the input data</p>
<p>The ג€balancedג€ mode uses the values of y to automatically adjust weights inversely proportional to class frequencies in the input data as n_samples / (n_classes * np.bincount(y)).</p>
<p>Box 2: Penalty parameter -</p>
<p>Parameter: C : float, optional (default=1.0)</p>
<p>Penalty parameter C of the error term.</p>
<p>Reference:</p>
<p>https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Panos11</strong> <code>(Wed 27 Nov 2024 11:51)</code> - <em>Upvotes: 2</em></p><p>correct</p></blockquote>
<blockquote><p><strong>mis96</strong> <code>(Wed 07 Feb 2024 16:12)</code> - <em>Upvotes: 4</em></p><p>Correct</p></blockquote>

</details>

---

[<< Previous Question](question_267.md) | [Home](../index.md) | [Next Question >>](question_269.md)
