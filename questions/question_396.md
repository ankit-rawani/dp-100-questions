# Question 396

You use the Azure Machine Learning SDK to run a training experiment that trains a classification model and calculates its accuracy metric.

The model will be retrained each month as new data is available.

You must register the model for use in a batch inference pipeline.

You need to register the model and ensure that the models created by subsequent retraining experiments are registered only if their accuracy is higher than the currently registered model.

What are two possible ways to achieve this goal? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

* A.Specify a different name for the model each time you register it.
* B.Register the model with the same name each time regardless of accuracy, and always use the latest version of the model in the batch inferencing pipeline.
* C.Specify the model framework version when registering the model, and only register subsequent models if this value is higher.
* D.Specify a property named accuracy with the accuracy metric as a value when registering the model, and only register subsequent models if their accuracy is  higher than the accuracy property value of the currently registered model.
* E.Specify a tag named accuracy with the accuracy metric as a value when registering the model, and only register subsequent models if their accuracy is higher than the accuracy tag value of the currently registered model.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>DE</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>kty</strong> <code>(Sun 19 Sep 2021 05:38)</code> - <em>Upvotes: 33</em></p><p>I agree, D and E</p></blockquote>
<blockquote><p><strong>pddddd</strong> <code>(Sat 08 May 2021 08:34)</code> - <em>Upvotes: 15</em></p><p>DE is correct</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 14:14)</code> - <em>Upvotes: 1</em></p><p>D, E are both correct</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Mon 05 Aug 2024 20:53)</code> - <em>Upvotes: 1</em></p><p>model_framework is used to filter the result based on the framework used to train the model (such as pytorch or tensorflow). So, definitely, D and E are the answers.</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Mon 07 Aug 2023 12:45)</code> - <em>Upvotes: 5</em></p><p>I wonder why those question are not fixed. I paid for the subscription but it is not worth if solutions are not correct.</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Sun 23 Jul 2023 13:50)</code> - <em>Upvotes: 3</em></p><p>Another One to fix, Can wee please correct for the future customers?</p></blockquote>
<blockquote><p><strong>Mckay_</strong> <code>(Thu 13 Apr 2023 18:27)</code> - <em>Upvotes: 3</em></p><p>C&#x27;mon ExamTopic, the answers are obvious here! D and E are the answers.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sun 11 Dec 2022 15:04)</code> - <em>Upvotes: 2</em></p><p>Is C missing something, does not sounds like an answer</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Tue 11 Oct 2022 13:29)</code> - <em>Upvotes: 3</em></p><p>DE are the only ones which take into account the accuracy value hence the correct answers.</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Sat 03 Sep 2022 06:57)</code> - <em>Upvotes: 2</em></p><p>On Exam: 03 March 2022</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Tue 14 Jun 2022 17:01)</code> - <em>Upvotes: 3</em></p><p>I agree with DE</p></blockquote>
<blockquote><p><strong>Peishi</strong> <code>(Sat 21 May 2022 17:22)</code> - <em>Upvotes: 3</em></p><p>agree on D&amp;E</p></blockquote>
<blockquote><p><strong>slash_nyk</strong> <code>(Sun 16 Jan 2022 11:23)</code> - <em>Upvotes: 5</em></p><p>I agree with D and E</p></blockquote>
<blockquote><p><strong>Jolin130</strong> <code>(Fri 14 May 2021 15:34)</code> - <em>Upvotes: 11</em></p><p>I go for DE</p></blockquote>

</details>

---

[<< Previous Question](question_395.md) | [Home](/index.md) | [Next Question >>](question_397.md)
