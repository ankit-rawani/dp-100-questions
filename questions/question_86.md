# Question 86

HOTSPOT -

You are evaluating a Python NumPy array that contains six data points defined as follows: data = [10, 20, 30, 40, 50, 60]

You must generate the following output by using the k-fold algorithm implantation in the Python Scikit-learn machine learning library: train: [10 40 50 60], test: [20 30] train: [20 30 40 60], test: [10 50] train: [10 20 30 50], test: [40 60]

You need to implement a cross-validation to generate the output.

How should you complete the code segment? To answer, select the appropriate code segment in the dialog box in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q86_q_0010800001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q86_ans_0_0010900001.png" alt="Answer Image"><br>
<p>Box 1: k-fold -</p>
<p>Box 2: 3 -</p>
<p>K-Folds cross-validator provides train/test indices to split data in train/test sets. Split dataset into k consecutive folds (without shuffling by default).</p>
<p>The parameter n_splits ( int, default=3) is the number of folds. Must be at least 2.</p>
<p>Box 3: data -</p>
<p>Example: Example:</p>
<p>&gt;&gt;&gt;</p>
<p>&gt;&gt;&gt; from sklearn.model_selection import KFold</p>
<p>&gt;&gt;&gt; X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])</p>
<p>&gt;&gt;&gt; y = np.array([1, 2, 3, 4])</p>
<p>&gt;&gt;&gt; kf = KFold(n_splits=2)</p>
<p>&gt;&gt;&gt; kf.get_n_splits(X)</p>
<p>&gt;&gt;&gt; print(kf)</p>
<p>KFold(n_splits=2, random_state=None, shuffle=False)</p>
<p>&gt;&gt;&gt; for train_index, test_index in kf.split(X):</p>
<p>...    print(&quot;TRAIN:&quot;, train_index, &quot;TEST:&quot;, test_index)</p>
<p>...    X_train, X_test = X[train_index], X[test_index]</p>
<p>...    y_train, y_test = y[train_index], y[test_index]</p>
<p>TRAIN: [2 3] TEST: [0 1]</p>
<p>TRAIN: [0 1] TEST: [2 3]</p>
<p>Reference:</p>
<p>https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>podval</strong> <code>(Tue 12 Jan 2021 19:45)</code> - <em>Upvotes: 23</em></p><p>Proper syntax:
from sklearn.model_selection import KFold</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Sat 29 Oct 2022 18:56)</code> - <em>Upvotes: 4</em></p><p>If the actual question is written with &#x27;k-fold&#x27; instead of &#x27;Kfold&#x27;, that&#x27;s just stupid.</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 14:55)</code> - <em>Upvotes: 5</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Wed 07 Aug 2024 15:22)</code> - <em>Upvotes: 2</em></p><p>from sklearn.model_selection import KFold
from numpy import array
import numpy as np

data = array([10,20,30,40,50,60])

k_fold = KFold(n_splits=3, shuffle=True,random_state=1)
for train, test in k_fold, np.split(data):
    print(f&#x27;train: {train}, test: {test}&#x27;)</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Tue 23 Jul 2024 09:36)</code> - <em>Upvotes: 1</em></p><p>&quot;-&quot; shoud be read as &quot;=&quot;</p></blockquote>
<blockquote><p><strong>Hisayuki</strong> <code>(Sat 04 May 2024 00:17)</code> - <em>Upvotes: 3</em></p><p>You&#x27;re gonna create three set of Train and Test dataset with Shuffling. So, the n_splits should be 3 in kfold.
- train: [10 40 50 60], test: [20 30]
- train: [20 30 40 60], test: [10 50]
- train: [10 20 30 50], test: [40 60]</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Wed 16 Nov 2022 12:45)</code> - <em>Upvotes: 2</em></p><p>Might be a typo, but overall is correct</p></blockquote>

</details>

---

[<< Previous Question](question_85.md) | [Home](/index.md) | [Next Question >>](question_87.md)
