# Question 266

You use the Two-Class Neural Network module in Azure Machine Learning Studio to build a binary classification model. You use the Tune Model

Hyperparameters module to tune accuracy for the model.

You need to configure the Tune Model Hyperparameters module.

Which two values should you use? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

* A.Number of hidden nodes
* B.Learning Rate
* C.The type of the normalizer
* D.Number of learning iterations
* E.Hidden layer specification

<details>
  <summary>Show Suggested Answer</summary>

  <strong>BD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>parimrt</strong> <code>(Wed 19 May 2021 01:21)</code> - <em>Upvotes: 59</em></p><p>The correct answer is B and D.</p></blockquote>
<blockquote><p><strong>conniekdl</strong> <code>(Tue 27 Jul 2021 09:11)</code> - <em>Upvotes: 11</em></p><p>Agree. ACE are structure related parameters which are not changed during the training process, but B and D are parameters that govern the training process. 
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters</p></blockquote>
<blockquote><p><strong>hendrata</strong> <code>(Tue 08 Jun 2021 21:50)</code> - <em>Upvotes: 17</em></p><p>The idea here is that, ABC are hyperparameters that Azure can figure out for you, but it needs D and E.
why D? Because Azure needs to know when to stop. I.e. it can&#x27;t run forever
why E? Because you need to tell Azure what to &quot;sweep over&quot;. Is it to sweep over hidden layer breadth? Depth? both? for each of these sweep runs, it tries a permutation of learning rate and kernel function etc</p></blockquote>
<blockquote><p><strong>Maunik</strong> <code>(Sat 16 Jul 2022 14:46)</code> - <em>Upvotes: 1</em></p><p>I think D and E - See below
https://towardsdatascience.com/what-are-hyperparameters-and-how-to-tune-the-hyperparameters-in-a-deep-neural-network-d0604917584a</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Thu 05 Dec 2024 16:33)</code> - <em>Upvotes: 1</em></p><p>The correct answer is B and D.</p></blockquote>
<blockquote><p><strong>pritamchatterjee09</strong> <code>(Fri 06 Sep 2024 17:02)</code> - <em>Upvotes: 1</em></p><p>BDE
https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-neural-network?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sun 21 Jul 2024 20:42)</code> - <em>Upvotes: 1</em></p><p>A. Number of hidden nodes
B. Learning Rate</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sun 21 Jul 2024 20:31)</code> - <em>Upvotes: 1</em></p><p>A. Number of hidden nodes
B. Learning Rate</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Wed 27 Mar 2024 16:55)</code> - <em>Upvotes: 1</em></p><p>B and D</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 21 Feb 2024 20:58)</code> - <em>Upvotes: 1</em></p><p>A. Number of hidden nodes
B. Learning Rate

When configuring the Tune Model Hyperparameters module to tune accuracy for a Two-Class Neural Network model in Azure Machine Learning Studio, you should select the hyperparameters you want to tune. In this case, you should select the number of hidden nodes and the learning rate. These are two of the most important hyperparameters for a neural network and can significantly impact the accuracy of the model. The other options listed (C, D, and E) are not relevant hyperparameters for the Two-Class Neural Network module. The type of normalizer is a preprocessing step and is not a hyperparameter for the model. The number of learning iterations and the hidden layer specification are both set by the Two-Class Neural Network module and cannot be directly tuned using the Tune Model Hyperparameters module.</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Thu 04 Jan 2024 18:53)</code> - <em>Upvotes: 1</em></p><p>Learning rate and hidden layer specification. No idea why (ironically) the community vote is tied at 50-50 on question about binary classification :)</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Sun 29 Oct 2023 03:14)</code> - <em>Upvotes: 1</em></p><p>As per Parimt&#x27;s explanation</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Sun 29 Oct 2023 03:14)</code> - <em>Upvotes: 1</em></p><p>Please delete the above - Should be B/D</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Fri 20 Oct 2023 08:17)</code> - <em>Upvotes: 1</em></p><p>Answer only D?
Other options are not in properties of Tune Model Hyperparameters .

Tune Model Hyperparameters Properties:
Sweep Method
Maximum number of runs
Random seed
Label Column
Metric

https://learn.microsoft.com/zh-tw/previous-versions/azure/machine-learning/studio-module-reference/tune-model-hyperparameters</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Sun 15 Jan 2023 06:10)</code> - <em>Upvotes: 2</em></p><p>Yes correct ans looks to be B and D as when I ran a small expt in designer using tune hyperparameter module and nn, I get the below output for sweep data preview with these column headers-

Number of learning iterations
Learning rate
mean_test_Mean absolute error
mean_test_Root of mean squared error
mean_test_Relative absolute error
mean_test_Relative squared error
mean_test_Coefficient of determination
rank</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Wed 07 Dec 2022 19:55)</code> - <em>Upvotes: 1</em></p><p>B and D</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Fri 18 Mar 2022 19:31)</code> - <em>Upvotes: 5</em></p><p>the answer is &#x27;B&#x27; and &#x27;D&#x27;
if &#x27;D&#x27; and &#x27;E&#x27; are correct then &#x27;A&#x27; i also has to be correct.</p></blockquote>
<blockquote><p><strong>Neuron</strong> <code>(Wed 02 Feb 2022 21:42)</code> - <em>Upvotes: 7</em></p><p>B and D: The 2-class Neural Network has only 2 parameters that can be set to &quot;range&quot; (instead of &quot;single parameter&quot;), which in turn can be learned by the Tune Model Hyperparameters module: 1) number of iterations 2) Learning rate.</p></blockquote>
<blockquote><p><strong>DanielGP</strong> <code>(Sat 22 Jan 2022 12:57)</code> - <em>Upvotes: 7</em></p><p>B and D

Below some text from the &quot;Two-Class Neural Network module&quot;:

4. For &quot;Learning rate&quot;, define the size of the step taken at each iteration, before correction. A larger value for
learning rate can cause the model to converge faster, but it can overshoot local minima.
5. For &quot;Number of learning iterations&quot;, specify the maximum number of times the algorithm should process
the training cases.</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Mon 25 Jul 2022 06:20)</code> - <em>Upvotes: 2</em></p><p>I agree... you explained the exact point of the question!</p></blockquote>
<blockquote><p><strong>RyanWL</strong> <code>(Wed 19 Jan 2022 14:28)</code> - <em>Upvotes: 5</em></p><p>I think is B and D</p></blockquote>

</details>

---

[<< Previous Question](question_265.md) | [Home](/index.md) | [Next Question >>](question_267.md)
