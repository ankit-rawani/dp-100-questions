# Question 39

You make use of Azure Machine Learning Studio to create a binary classification model.

You are preparing to carry out a parameter sweep of the model to tune hyperparameters. You have to make sure that the sweep allows for every possible combination of hyperparameters to be iterated. Also, the computing resources needed to carry out the sweep must be reduced.

Which of the following actions should you take?

- A.You should consider making use of the Selective grid sweep mode.
- B.You should consider making use of the Measured grid sweep mode.
- C.You should consider making use of the Entire grid sweep mode.
- D.You should consider making use of the Random grid sweep mode.

<details>
  <summary>Show Suggested Answer</summary>

<strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>[Removed]</strong> <code>(Thu 12 Jan 2023 13:05)</code> - <em>Upvotes: 18</em></p><p>I feel like like the two requirements are conflicting: every possible combination implies Entire grid while lower computational resources implies Random grid. 
&quot;Entire grid: When you select this option, the component loops over a grid predefined by the system, to try different combinations and identify the best learner. This option is useful when you don&#x27;t know what the best parameter settings might be and want to try all possible combinations of values.&quot;

&quot;Random sweep: When you select this option, the component will randomly select parameter values over a system-defined range. You must specify the maximum number of runs that you want the component to execute. This option is useful when you want to increase model performance by using the metrics of your choice but still conserve computing resources.&quot;</p></blockquote>

<blockquote><p><strong>prabhjot</strong> <code>(Mon 29 Jan 2024 11:44)</code> - <em>Upvotes: 1</em></p><p>For ensuring every possible combination of hyperparameters is explored, the &quot;Entire grid sweep mode&quot; is the appropriate choice.</p></blockquote>
<blockquote><p><strong>lookaaaa</strong> <code>(Wed 23 Nov 2022 22:31)</code> - <em>Upvotes: 8</em></p><p>All combination + Reduce computing resource , because &quot;Research has shown that this method (Random Grid Sweep) yields the same results, but is more efficient computationally.&quot; I think D would be the best choice</p></blockquote>
<blockquote><p><strong>sim39</strong> <code>(Sun 24 Nov 2024 19:08)</code> - <em>Upvotes: 3</em></p><p>_ALLOWS_ for every possible combination doesn&#x27;t mean it has to iterate through all. The requirement to reduce compute resources obviously points us away from a full grid search.</p></blockquote>
<blockquote><p><strong>Xsesi</strong> <code>(Tue 30 Jul 2024 09:35)</code> - <em>Upvotes: 1</em></p><p>Vote for Entire Grid Sweep Mode since one requirement is every possible combination of hyperparameters to be iterated. Other options reduce computational resources yet do not satisfy this requirement.</p></blockquote>
<blockquote><p><strong>Braxus</strong> <code>(Thu 21 Mar 2024 04:46)</code> - <em>Upvotes: 1</em></p><p>&quot;Maximum number of runs on random grid: This option also controls the number of iterations over a random sampling of parameter values, but the values are not generated randomly from the specified range; instead, a matrix is created of all possible combinations of parameter values and a random sampling is taken over the matrix. This method is more efficient and less prone to regional oversampling or undersampling.&quot;</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Fri 07 Jul 2023 20:36)</code> - <em>Upvotes: 2</em></p><p>The answer is D.

Random seed ALLOWS every possible combination. It won&#x27;t go through every possible combination but any random combination is possible.</p></blockquote>

<blockquote><p><strong>endeesa</strong> <code>(Thu 08 Jun 2023 21:43)</code> - <em>Upvotes: 2</em></p><p>Question says &quot;You have to make sure that the sweep allows for every possible combination of hyperparameters to be iterated&quot;. There is no way to guarantee Random sweep will get all possible combinations, answer is C</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 01 Feb 2023 21:22)</code> - <em>Upvotes: 1</em></p><p>D. You should consider making use of the Random grid sweep mode.

The Random grid sweep mode randomly selects combinations of hyperparameters to test, reducing the number of total combinations and the computing resources needed to carry out the sweep. This method can still provide a good understanding of the relationship between hyperparameters and model performance, but may require multiple runs to converge on the optimal hyperparameters.</p></blockquote>

<blockquote><p><strong>meysa</strong> <code>(Wed 11 Jan 2023 01:21)</code> - <em>Upvotes: 3</em></p><p>If we want every possible combi9nation we need entire grid, so C is correct.</p></blockquote>
<blockquote><p><strong>Sibajene</strong> <code>(Wed 04 Jan 2023 17:29)</code> - <em>Upvotes: 4</em></p><p>C is correct..</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Sun 11 Dec 2022 12:53)</code> - <em>Upvotes: 1</em></p><p>Keyword -&gt; &quot;sweep allows for every possible combination&quot; so, option B https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/tune-model-hyperparameters</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Sun 11 Dec 2022 12:55)</code> - <em>Upvotes: 3</em></p><p>I mean, option C</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 17 Jun 2022 10:43)</code> - <em>Upvotes: 3</em></p><p>Entire grid is the only one can try all combinations,
but random sweep is low computational cost</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Fri 15 Apr 2022 12:24)</code> - <em>Upvotes: 2</em></p><p>Related with this question

https://www.examtopics.com/discussions/microsoft/view/43145-exam-dp-100-topic-2-question-80-discussion/</p></blockquote>

<blockquote><p><strong>synapse</strong> <code>(Fri 11 Mar 2022 11:18)</code> - <em>Upvotes: 1</em></p><p>Answer D. there are two reqs... entire grid and low computational cost</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Wed 15 Dec 2021 09:05)</code> - <em>Upvotes: 1</em></p><p>Random grid</p></blockquote>
<blockquote><p><strong>RyanTsai</strong> <code>(Sun 19 Sep 2021 10:10)</code> - <em>Upvotes: 4</em></p><p>ans: C</p></blockquote>
<blockquote><p><strong>Cacek</strong> <code>(Fri 20 Aug 2021 12:01)</code> - <em>Upvotes: 2</em></p><p>&quot;every possible combination&quot;, hence Entire grid sweep mode</p></blockquote>
<blockquote><p><strong>sim39</strong> <code>(Tue 07 Sep 2021 10:10)</code> - <em>Upvotes: 12</em></p><p>Because Random Grid ALLOW for every possible combination: this is the sample space for the algorithm. The &quot;entire grid&quot; option has a high computational cost</p></blockquote>

</details>

---

[<< Previous Question](question_38.md) | [Home](../index.md) | [Next Question >>](question_40.md)
