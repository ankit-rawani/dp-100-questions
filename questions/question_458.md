# Question 458

You are a data scientist working for a bank and have used Azure ML to train and register a machine learning model that predicts whether a customer is likely to repay a loan.

You want to understand how your model is making selections and must be sure that the model does not violate government regulations such as denying loans based on where an applicant lives.

You need to determine the extent to which each feature in the customer data is influencing predictions.

What should you do?

* A.Enable data drift monitoring for the model and its training dataset.
* B.Score the model against some test data with known label values and use the results to calculate a confusion matrix.
* C.Use the Hyperdrive library to test the model with multiple hyperparameter values.
* D.Use the interpretability package to generate an explainer for the model.
* E.Add tags to the model registration indicating the names of the features in the training dataset.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Abhiwkudhewhud</strong> <code>(Sun 05 Dec 2021 22:12)</code> - <em>Upvotes: 7</em></p><p>explainer gives us exactlt what this question is asking ... we are asked to see if the location is having influence we are given this value after we re ure by getting the sharpley
 values</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 15:22)</code> - <em>Upvotes: 7</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 18 Nov 2024 04:10)</code> - <em>Upvotes: 1</em></p><p>Explain packages, such as Azure ML&#x27;s explain package, provide tools to generate interpreters for your models that detail how each feature affects the model&#x27;s decisions. This can help you understand the model&#x27;s decision-making process and ensure that the model is not making decisions based on inappropriate characteristics, such as residence. Therefore, this option meets the question requirements.</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Wed 12 Oct 2022 20:28)</code> - <em>Upvotes: 6</em></p><p>Given answer is correct</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 13 Sep 2022 04:45)</code> - <em>Upvotes: 4</em></p><p>azureml.interpret package to get feature importance</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Sat 16 Jul 2022 04:53)</code> - <em>Upvotes: 1</em></p><p>Fairlearn is that package, correct?</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 13 Sep 2022 04:45)</code> - <em>Upvotes: 1</em></p><p>No.. this  question is about understanding the influence of each feature. it&#x27;s azureml.interpret package</p></blockquote>
<blockquote><p><strong>Aleem</strong> <code>(Sat 06 Nov 2021 12:38)</code> - <em>Upvotes: 4</em></p><p>Answer should be to remove location features from the model so that they have zero influence.</p></blockquote>
<blockquote><p><strong>Pranav_K</strong> <code>(Mon 27 Dec 2021 17:19)</code> - <em>Upvotes: 4</em></p><p>Question says &quot;that the model does not violate government regulations such as denying loans based on where an applicant lives.&quot;  ... means there can be other factors too.. how to determine other factors ? Hence interpretability is right choice.</p></blockquote>
<blockquote><p><strong>allanm</strong> <code>(Tue 16 Nov 2021 17:00)</code> - <em>Upvotes: 16</em></p><p>While you make an excellent point, this is not one of the options listed for the answer. Please make this explicit in your statement to avoid confusing other readers.</p></blockquote>

</details>

---

[<< Previous Question](question_457.md) | [Home](/index.md) | [Next Question >>](question_459.md)
