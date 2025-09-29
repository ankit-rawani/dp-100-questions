# Question 251

DRAG DROP -

You are building an experiment using the Azure Machine Learning designer.

You split a dataset into training and testing sets. You select the Two-Class Boosted Decision Tree as the algorithm.

You need to determine the Area Under the Curve (AUC) of the model.

Which three modules should you use in sequence? To answer, move the appropriate modules from the list of modules to the answer area and arrange them in the correct order.

Select and Place:

![Question Image](../images/q251_q_0026200001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q251_ans_0_0026300001.png" alt="Answer Image"><br>

<p>Step 1: Train Model -</p>
<p>Two-Class Boosted Decision Tree -</p>
<p>First, set up the boosted decision tree model.</p>
<p>1. Find the Two-Class Boosted Decision Tree module in the module palette and drag it onto the canvas.</p>
<p>2. Find the Train Model module, drag it onto the canvas, and then connect the output of the Two-Class Boosted Decision Tree module to the left input port of the</p>
<p>Train Model module.</p>
<p>The Two-Class Boosted Decision Tree module initializes the generic model, and Train Model uses training data to train the model.</p>
<p>3. Connect the left output of the left Execute R Script module to the right input port of the Train Model module (in this tutorial you used the data coming from the left side of the Split Data module for training).</p>
<p>This portion of the experiment now looks something like this:</p>
<img src="../images/q251_ref_19_0026400001.png" alt="Reference Image"><br>
<p>Step 2: Score Model -</p>
<p>Score and evaluate the models -</p>
<p>You use the testing data that was separated out by the Split Data module to score our trained models. You can then compare the results of the two models to see which generated better results.</p>
<p>Add the Score Model modules -</p>
<p>1. Find the Score Model module and drag it onto the canvas.</p>
<p>2. Connect the Train Model module that&#x27;s connected to the Two-Class Boosted Decision Tree module to the left input port of the Score Model module.</p>
<p>3. Connect the right Execute R Script module (our testing data) to the right input port of the Score Model module.</p>
<img src="../images/q251_ref_38_0026500001.png" alt="Reference Image"><br>
<p>Step 3: Evaluate Model -</p>
<p>To evaluate the two scoring results and compare them, you use an Evaluate Model module.</p>
<p>1. Find the Evaluate Model module and drag it onto the canvas.</p>
<p>2. Connect the output port of the Score Model module associated with the boosted decision tree model to the left input port of the Evaluate Model module.</p>
<p>3. Connect the other Score Model module to the right input port.</p>
<img src="../images/q251_ref_51_0026500002.png" alt="Reference Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ac45863</strong> <code>(Thu 07 Oct 2021 23:07)</code> - <em>Upvotes: 15</em></p><p>It&#x27;s correct</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Thu 15 Aug 2024 07:43)</code> - <em>Upvotes: 1</em></p><p>You can identify what should work by looking at the inputs and outputs of the models in designer.

&quot;Train, Score, Evaluate&quot; should work but also &quot;Tune Model Hyperparameter, Score, Evaluate&quot;. The latter should give yield an improved model compared to the former.</p></blockquote>

<blockquote><p><strong>deyoz</strong> <code>(Fri 02 Aug 2024 23:29)</code> - <em>Upvotes: 1</em></p><p>correct.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 19 Apr 2024 04:08)</code> - <em>Upvotes: 1</em></p><p>In sequence

1. Train
2. Score model
3. Evaluate</p></blockquote>
<blockquote><p><strong>MattAnya</strong> <code>(Tue 04 Jul 2023 05:49)</code> - <em>Upvotes: 3</em></p><p>on 03 Jan 2023</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 02 Dec 2022 15:12)</code> - <em>Upvotes: 3</em></p><p>not sure about the evaluate step ...
for this step you will need two scored test sets ...
one is from two class boosted decision tree ...
where is the other one from ...</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Thu 15 Aug 2024 07:37)</code> - <em>Upvotes: 1</em></p><p>you need only one, the second one is optional</p></blockquote>
<blockquote><p><strong>racnaoamo</strong> <code>(Sat 19 Nov 2022 08:58)</code> - <em>Upvotes: 1</em></p><p>on exam 18-5-22</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Apr 2022 09:50)</code> - <em>Upvotes: 2</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Sat 02 Apr 2022 21:16)</code> - <em>Upvotes: 1</em></p><p>Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>erp31</strong> <code>(Mon 31 Jan 2022 04:03)</code> - <em>Upvotes: 4</em></p><p>on exam 30/07/2021</p></blockquote>

</details>

---

[<< Previous Question](question_250.md) | [Home](../index.md) | [Next Question >>](question_252.md)
