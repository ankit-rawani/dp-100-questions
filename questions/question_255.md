# Question 255

You create a pipeline in designer to train a model that predicts automobile prices.

Because of non-linear relationships in the data, the pipeline calculates the natural log (Ln) of the prices in the training data, trains a model to predict this natural log of price value, and then calculates the exponential of the scored label to get the predicted price.

The training pipeline is shown in the exhibit. (Click the Training pipeline tab.)

Training pipeline -

![Question Image](images/q255_q_0026700001.png)

You create a real-time inference pipeline from the training pipeline, as shown in the exhibit. (Click the Real-time pipeline tab.)

Real-time pipeline -

![Question Image](images/q255_q_0026800001.jpg)

You need to modify the inference pipeline to ensure that the web service returns the exponential of the scored label as the predicted automobile price and that client applications are not required to include a price value in the input values.

Which three modifications must you make to the inference pipeline? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

* A.Connect the output of the Apply SQL Transformation to the Web Service Output module.
* B.Replace the Web Service Input module with a data input that does not include the price column.
* C.Add a Select Columns module before the Score Model module to select all columns other than price.
* D.Replace the training dataset module with a data input that does not include the price column.
* E.Remove the Apply Math Operation module that replaces price with its natural log from the data flow.
* F.Remove the Apply SQL Transformation module from the data flow.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>ACE</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>scipio</strong> <code>(Tue 16 Nov 2021 23:41)</code> - <em>Upvotes: 18</em></p><p>In contrast to other comments I think the answer ACE is correct. How you can achieve D in a pipeline? Either you change the dataset (you need to create a new one removing one column from the original training dataset), or you use C.
In other words to achieve D you need to do C!</p></blockquote>
<blockquote><p><strong>TEO96B</strong> <code>(Wed 15 Jun 2022 16:34)</code> - <em>Upvotes: 2</em></p><p>I almost agree with you, but choosing C how can I apply A hence accept the &quot;apply sql trasformation&quot; output? I mean, we should remove both &quot;apply math operation&quot; modules and then accept the sql output... I think that the answer is still incorrect, or am I missing anything?</p></blockquote>
<blockquote><p><strong>ACSC</strong> <code>(Sat 09 Oct 2021 07:53)</code> - <em>Upvotes: 7</em></p><p>A, D, E: connect the output after the last operation, you have to discard the the price column and because of this you don&#x27;t need to replace price anymore.</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Wed 05 Jun 2024 14:49)</code> - <em>Upvotes: 2</em></p><p>A. Connect the output of the Apply SQL Transformation to the Web Service Output module: This ensures that the transformed scores (actual predicted prices) are returned.

B. Replace the Web Service Input module with a data input that does not include the price column: To prevent the need for price as an input.

C. Add a Select Columns module before the Score Model module to select all columns other than price: To ensure the model uses only the necessary input features, excluding the price.</p></blockquote>
<blockquote><p><strong>vv_bb</strong> <code>(Wed 15 May 2024 20:47)</code> - <em>Upvotes: 1</em></p><p>The correct answer is ADE

Check this page, section &quot;Create and run an inference pipeline&quot;

https://microsoftlearning.github.io/AI-900-AIFundamentals/instructions/02a-create-regression-model.html</p></blockquote>
<blockquote><p><strong>eloyinaay</strong> <code>(Wed 06 Sep 2023 14:28)</code> - <em>Upvotes: 2</em></p><p>on 2023/03/6 exam!</p></blockquote>
<blockquote><p><strong>Gferreira</strong> <code>(Thu 13 Jul 2023 21:03)</code> - <em>Upvotes: 1</em></p><p>Sorry, ABE</p></blockquote>
<blockquote><p><strong>Gferreira</strong> <code>(Thu 13 Jul 2023 21:00)</code> - <em>Upvotes: 1</em></p><p>ABF . Analyze</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Sun 02 Jul 2023 20:01)</code> - <em>Upvotes: 3</em></p><p>D refers to training data which doesn&#x27;t apply in inference pipelines</p></blockquote>
<blockquote><p><strong>DaniloMagone</strong> <code>(Sat 26 Oct 2024 12:46)</code> - <em>Upvotes: 1</em></p><p>This is the exact reason that D is correct. Training data is in the Pipeline and it should not be there.</p></blockquote>
<blockquote><p><strong>amokrane_mancer</strong> <code>(Thu 20 Apr 2023 13:12)</code> - <em>Upvotes: 2</em></p><p>ACE is correct</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sun 18 Dec 2022 02:45)</code> - <em>Upvotes: 2</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>racnaoamo</strong> <code>(Sat 19 Nov 2022 08:59)</code> - <em>Upvotes: 1</em></p><p>on exam 18-5-22</p></blockquote>
<blockquote><p><strong>majma</strong> <code>(Tue 25 Oct 2022 10:33)</code> - <em>Upvotes: 1</em></p><p>I think scipio is right</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Mon 12 Sep 2022 00:14)</code> - <em>Upvotes: 1</em></p><p>ACD Looks good.</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Mon 25 Jul 2022 03:20)</code> - <em>Upvotes: 2</em></p><p>As per this answer must be ACD
https://docs.microsoft.com/en-us/learn/modules/create-regression-model-azure-machine-learning-designer/inference-pipeline?ns-enrollment-type=LearningPath&amp;ns-enrollment-id=learn.wwl.create-no-code-predictive-models-with-azure-machine-learning</p></blockquote>
<blockquote><p><strong>ferdcoz</strong> <code>(Tue 17 Dec 2024 14:59)</code> - <em>Upvotes: 1</em></p><p>It doesnt make sense you&#x27;re (C) selectin all columns other than price but at the same time replacing for a dataset that does not include the price column (D)</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Fri 29 Jul 2022 16:40)</code> - <em>Upvotes: 1</em></p><p>Agree i just checked as well. ACD is correct</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Tue 07 Jun 2022 16:29)</code> - <em>Upvotes: 3</em></p><p>I agree with ACE</p></blockquote>
<blockquote><p><strong>leo99</strong> <code>(Mon 06 Jun 2022 13:31)</code> - <em>Upvotes: 3</em></p><p>Answer is correct. Remember, we need to modify the real-time pipeline. A: connect the output of SQL transformation to the web service output to return the exponential of predicted label. The model was trained to predict the natural log of the prices. C &amp; E: since we are doing inferencing, we don&#x27;t need the target variable.</p></blockquote>
<blockquote><p><strong>tunaktunak</strong> <code>(Thu 26 May 2022 11:19)</code> - <em>Upvotes: 3</em></p><p>On exam 26/11/2021</p></blockquote>

</details>

---

[<< Previous Question](question_254.md) | [Home](/index.md) | [Next Question >>](question_256.md)
