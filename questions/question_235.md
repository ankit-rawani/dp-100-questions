# Question 235

You have a comma-separated values (CSV) file containing data from which you want to train a classification model.

You are using the Automated Machine Learning interface in Azure Machine Learning studio to train the classification model. You set the task type to Classification.

You need to ensure that the Automated Machine Learning process evaluates only linear models.

What should you do?

* A.Add all algorithms other than linear ones to the blocked algorithms list.
* B.Set the Exit criterion option to a metric score threshold.
* C.Clear the option to perform automatic featurization.
* D.Clear the option to enable deep learning.
* E.Set the task type to Regression.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>sreemenon23</strong> <code>(Fri 25 Dec 2020 11:56)</code> - <em>Upvotes: 51</em></p><p>Answer is A</p></blockquote>
<blockquote><p><strong>sachinrkp</strong> <code>(Sun 27 Dec 2020 15:20)</code> - <em>Upvotes: 11</em></p><p>Answer A is correct
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-automated-ml-for-ml-models</p></blockquote>
<blockquote><p><strong>Chishti</strong> <code>(Sun 23 Jun 2024 19:34)</code> - <em>Upvotes: 1</em></p><p>A would be the right answer, However, I&#x27;m shocked to see the given here.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 19 Apr 2024 02:45)</code> - <em>Upvotes: 1</em></p><p>Question&#x27;s keyword &#x27;need to ensure that the Automated Machine Learning process evaluates only linear models&#x27; . 

Answer&#x27;s keyword &#x27;Add all algorithms other than linear ones to the blocked algorithms list.&#x27; - it is all enough. --&gt; Choose A.</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Sat 20 Jan 2024 14:46)</code> - <em>Upvotes: 3</em></p><p>On exam 20 July 2023.</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Thu 28 Dec 2023 13:03)</code> - <em>Upvotes: 1</em></p><p>A - ChatGPT
To ensure that the Automated Machine Learning process evaluates only linear models for a classification task in Azure Machine Learning studio, you should:

A. Add all algorithms other than linear ones to the blocked algorithms list.

By adding non-linear algorithms to the blocked algorithms list, you restrict the Automated Machine Learning process to only consider linear models for training. This ensures that only linear models will be evaluated and selected during the automated process.

Therefore, the correct option is A. Add all algorithms other than linear ones to the blocked algorithms list.</p></blockquote>
<blockquote><p><strong>krishna1818</strong> <code>(Wed 29 Nov 2023 11:48)</code> - <em>Upvotes: 1</em></p><p>seems option A</p></blockquote>
<blockquote><p><strong>casiopa</strong> <code>(Fri 09 Jun 2023 11:32)</code> - <em>Upvotes: 3</em></p><p>Clearly answer A</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Tue 07 Jun 2022 12:39)</code> - <em>Upvotes: 5</em></p><p>Answer is A</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Thu 03 Mar 2022 08:32)</code> - <em>Upvotes: 2</em></p><p>got 2/9/21</p></blockquote>
<blockquote><p><strong>erp31</strong> <code>(Mon 31 Jan 2022 03:54)</code> - <em>Upvotes: 2</em></p><p>on exam 30/07/2021</p></blockquote>
<blockquote><p><strong>ali25</strong> <code>(Mon 04 Oct 2021 08:28)</code> - <em>Upvotes: 4</em></p><p>A
Blocked algorithms 	Algorithms you want to exclude from the training job</p></blockquote>
<blockquote><p><strong>SMA_1</strong> <code>(Fri 17 Sep 2021 20:50)</code> - <em>Upvotes: 3</em></p><p>Answer is (A) as you block any model other than linear ones.</p></blockquote>
<blockquote><p><strong>ZeeshanNawaz</strong> <code>(Tue 10 Aug 2021 23:52)</code> - <em>Upvotes: 3</em></p><p>A is the answer</p></blockquote>
<blockquote><p><strong>Nugi</strong> <code>(Mon 15 Feb 2021 06:29)</code> - <em>Upvotes: 2</em></p><p>Answer is A: Add all algorithms other than linear ones to the blocked algorithms list.</p></blockquote>
<blockquote><p><strong>amelia</strong> <code>(Tue 29 Dec 2020 13:09)</code> - <em>Upvotes: 6</em></p><p>Answer is A
https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-first-experiment-automated-ml</p></blockquote>
<blockquote><p><strong>Alberto_Lugo</strong> <code>(Sat 26 Dec 2020 19:56)</code> - <em>Upvotes: 7</em></p><p>A is the correct one</p></blockquote>

</details>

---

[<< Previous Question](question_234.md) | [Home](/index.md) | [Next Question >>](question_236.md)
