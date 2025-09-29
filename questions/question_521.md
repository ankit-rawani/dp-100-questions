# Question 521

DRAG DROP -

You need to correct the model fit issue.

Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Select and Place:

![Question Image](../images/q521_q_0046700001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q521_ans_0_0046800001.png" alt="Answer Image"><br>

<p>Step 1: Augment the data -</p>
<p>Scenario: Columns in each dataset contain missing and null values. The datasets also contain many outliers.</p>
<p>Step 2: Add the Bayesian Linear Regression module.</p>
<p>Scenario: You produce a regression model to predict property prices by using the Linear Regression and Bayesian Linear Regression modules.</p>
<p>Step 3: Configure the regularization weight.</p>
<p>Regularization typically is used to avoid overfitting. For example, in L2 regularization weight, type the value to use as the weight for L2 regularization. We recommend that you use a non-zero value to avoid overfitting.</p>
<p>Scenario:</p>
<p>Model fit: The model shows signs of overfitting. You need to produce a more refined regression model that reduces the overfitting.</p>
<p>Incorrect Answers:</p>
<p>Multiclass Decision Jungle module:</p>
<p>Decision jungles are a recent extension to decision forests. A decision jungle consists of an ensemble of decision directed acyclic graphs (DAGs).</p>
<p>L-BFGS:</p>
<p>L-BFGS stands for &quot;limited memory Broyden-Fletcher-Goldfarb-Shanno&quot;. It can be found in the wwo-Class Logistic Regression module, which is used to create a logistic regression model that can be used to predict two (and only two) outcomes.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/linear-regression</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>james2033</strong> <code>(Sat 12 Oct 2024 04:55)</code> - <em>Upvotes: 1</em></p><p>Question keyword &quot;You produce a regression model to predict property prices by using the Linear Regression and Bayesian Linear Regression modules.&quot; --&gt; 
First block, sure for &quot;Augment the data&quot;.
Third block, sure for &quot;Configure the regulation weight.&quot;
remain part, Second block, choose &quot;Add the Bayesian Linear Regression module&quot; based on question&#x27;s keyword.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Mon 26 Feb 2024 02:46)</code> - <em>Upvotes: 1</em></p><p>given answer is ok</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Mon 26 Feb 2024 02:46)</code> - <em>Upvotes: 3</em></p><p>Augment the data to increase the size of the training set and potentially improve the model&#x27;s ability to capture patterns in the data.
Add the Bayesian linear regression module, which may provide a better fit for the data than the standard linear regression module.
Configure the regularization weight to help prevent overfitting and improve generalization performance.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Mon 26 Feb 2024 02:43)</code> - <em>Upvotes: 1</em></p><p>Augment the data: This can help to increase the size and diversity of the training data, which may improve the performance of the model.

Configure the regularization weight: Regularization can help to prevent overfitting by adding a penalty term to the loss function. Adjusting the regularization weight can help to find an optimal balance between model complexity and generalization.

Decrease the memory size for L-BFGS: This can help to reduce the computational resources required for training the model, which can improve the efficiency and speed of the training process.

Adding the other modules (ordinal regression, two-class averaged perception, multiclass decision jungle) would not be appropriate for a regression problem, and adding the Bayesian Linear Regression module was already mentioned in the scenario.</p></blockquote>

<blockquote><p><strong>azure1000</strong> <code>(Sat 06 Aug 2022 06:40)</code> - <em>Upvotes: 3</em></p><p>Augmentation and regularization is correct. but not sure for Bayesian model</p></blockquote>
<blockquote><p><strong>azayra</strong> <code>(Fri 28 Oct 2022 16:38)</code> - <em>Upvotes: 1</em></p><p>You must set up the experiment to cross-validate the Linear Regression and Bayesian Linear Regression modules to evaluate performance.</p></blockquote>
<blockquote><p><strong>mangeshb1981</strong> <code>(Fri 12 Aug 2022 11:28)</code> - <em>Upvotes: 1</em></p><p>What should be the answer then?</p></blockquote>

</details>

---

[<< Previous Question](question_520.md) | [Home](../index.md)
