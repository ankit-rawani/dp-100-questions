# Question 474

DRAG DROP -

You have a model with a large difference between the training and validation error values.

You must create a new model and perform cross-validation.

You need to identify a parameter set for the new model using Azure Machine Learning Studio.

Which module you should use for each step? To answer, drag the appropriate modules to the correct steps. Each module may be used once or more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

Select and Place:

![Question Image](../images/q474_q_0044100001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q474_ans_0_0044100002.png" alt="Answer Image"><br>

<p>Box 1: Split data -</p>
<p>Box 2: Partition and Sample -</p>
<p>Box 3: Two-Class Boosted Decision Tree</p>
<p>Box 4: Tune Model Hyperparameters</p>
<p>Integrated train and tune: You configure a set of parameters to use, and then let the module iterate over multiple combinations, measuring accuracy until it finds a</p>
<p>&quot;best&quot; model. With most learner modules, you can choose which parameters should be changed during the training process, and which should remain fixed.</p>
<p>We recommend that you use Cross-Validate Model to establish the goodness of the model given the specified parameters. Use Tune Model Hyperparameters to identify the optimal parameters.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/partition-and-sample</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>priyalnish</strong> <code>(Mon 13 Jul 2020 15:45)</code> - <em>Upvotes: 98</em></p><p>According to below link;
https://docs.microsoft.com/en-us/azure/machine-learning/studio/algorithm-parameters-optimize
1. Two-Class Boosted Decision Tree
2. Partition and Sample
3. Tune Model Hyperparameters
4. Tune Model Hyperparameters</p></blockquote>
<blockquote><p><strong>Gitty</strong> <code>(Thu 13 Aug 2020 02:16)</code> - <em>Upvotes: 2</em></p><p>correct</p></blockquote>
<blockquote><p><strong>jay2323</strong> <code>(Tue 06 Jul 2021 20:19)</code> - <em>Upvotes: 2</em></p><p>Why is 3 and 4 have the same answer?</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Sun 25 Jul 2021 06:10)</code> - <em>Upvotes: 1</em></p><p>Train, evaluate, and compare
The same Tune Model Hyperparameters module trains all the models that correspond to the parameter set,</p></blockquote>
<blockquote><p><strong>SnowCheetah</strong> <code>(Sat 26 Jun 2021 09:02)</code> - <em>Upvotes: 1</em></p><p>This is a correct Answer</p></blockquote>
<blockquote><p><strong>VJPrakash</strong> <code>(Fri 30 Jul 2021 17:07)</code> - <em>Upvotes: 2</em></p><p>Thanks for the link. These answers are accurate based on the documentation.</p></blockquote>
<blockquote><p><strong>Yilu</strong> <code>(Tue 12 May 2020 05:20)</code> - <em>Upvotes: 9</em></p><p>box 1 and 4 got swapped</p></blockquote>
<blockquote><p><strong>jl420</strong> <code>(Mon 11 Nov 2024 14:44)</code> - <em>Upvotes: 1</em></p><p>Step	Module
Define the parameter scope	- Tune Model Hyperparameters
Define the cross-validation settings	- Partition and Sample
Define the metric	- Tune Model Hyperparameters
Train, evaluate, and compare	- Two-Class Boosted Decision Tree</p></blockquote>
<blockquote><p><strong>jl420</strong> <code>(Mon 11 Nov 2024 14:52)</code> - <em>Upvotes: 1</em></p><p>Ignore this is wrong. Given answer is correct -&gt; Split, Part, Boost, Tune</p></blockquote>
<blockquote><p><strong>BR_CS</strong> <code>(Thu 17 Aug 2023 15:11)</code> - <em>Upvotes: 2</em></p><p>The answers in the comments seem to make no sense, just like the answers shown. Was the image changed?</p></blockquote>
<blockquote><p><strong>ZoeJ</strong> <code>(Thu 27 Apr 2023 07:15)</code> - <em>Upvotes: 2</em></p><p>I think this is an out-dated question</p></blockquote>
<blockquote><p><strong>ck1729</strong> <code>(Wed 20 Jan 2021 21:50)</code> - <em>Upvotes: 2</em></p><p>how come the answers below say selecting the model first? shouldn&#x27;t we split the data first and feed in the training data to the model?</p></blockquote>
<blockquote><p><strong>kath3624</strong> <code>(Mon 29 Jun 2020 16:48)</code> - <em>Upvotes: 4</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/studio/algorithm-parameters-optimize
box 1:  Boosted Decision Tree
box 2:  Partition and Sample
box 3:  Tune Model Hyperparameters 
box 4:</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Mon 22 Mar 2021 05:01)</code> - <em>Upvotes: 1</em></p><p>4th also hyperparmeters too</p></blockquote>
<blockquote><p><strong>pepmir</strong> <code>(Thu 25 Jun 2020 19:48)</code> - <em>Upvotes: 3</em></p><p>Tune Hyperparams belongs to Train Module. So 4 is correct.</p></blockquote>
<blockquote><p><strong>davo123</strong> <code>(Wed 20 May 2020 09:32)</code> - <em>Upvotes: 2</em></p><p>Box 1 should be Two Class Boosted?</p></blockquote>
<blockquote><p><strong>abofficial</strong> <code>(Wed 18 Nov 2020 07:20)</code> - <em>Upvotes: 6</em></p><p>I think box 1 should be tune hyperparameters.. take note of the keyword &#x27;parameter scope&#x27;</p></blockquote>

</details>

---

[<< Previous Question](question_473.md) | [Home](../index.md) | [Next Question >>](question_475.md)
