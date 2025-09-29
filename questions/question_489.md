# Question 489

You create a binary classification model. You use the Fairlearn package to assess model fairness.

You must eliminate the need to retrain the model.

You need to implement the Fairlearn package.

Which algorithm should you use?

- A.fairlearn.reductions.ExponentiatedGradient
- B.fairlearn.postprocessing.ThresholdOptimizer
- C.fairlearnpreprocessing.CorrelationRemover
- D.fairlearn.reductions.GridSearch

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>bbigwolf</strong> <code>(Fri 01 Sep 2023 06:00)</code> - <em>Upvotes: 8</em></p><p>Should be B</p></blockquote>
<blockquote><p><strong>cert_pz</strong> <code>(Sun 01 Dec 2024 12:32)</code> - <em>Upvotes: 3</em></p><p>It states that the need to retrain the model should not apply, you can &quot;enforce&quot; fairness in a Model in 3 ways, before the training (preprocessing), during the training (inprocessing) and after the training (postprocessing). The Corrolation Remover is a preprocessing technique, therefore you would need to retrain the model. The correct answer is B.</p></blockquote>
<blockquote><p><strong>3than</strong> <code>(Fri 22 Nov 2024 17:08)</code> - <em>Upvotes: 1</em></p><p>Nothing about fairlearn on MS Learn?</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 13 Sep 2024 09:12)</code> - <em>Upvotes: 2</em></p><p>The correct answer is B. fairlearn.postprocessing.ThresholdOptimizer.

The ThresholdOptimizer algorithm in the Fairlearn package is a post-processing technique that you can use to adjust the threshold of a binary classification model’s predictions to improve fairness, without needing to retrain the model. This makes it a suitable choice given your requirement to eliminate the need to retrain the model. The other options listed are either preprocessing techniques or in-processing techniques which would require retraining of the model.</p></blockquote>

<blockquote><p><strong>Tommo565</strong> <code>(Wed 27 Mar 2024 11:44)</code> - <em>Upvotes: 1</em></p><p>As per other comments, B</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 24 Feb 2024 16:58)</code> - <em>Upvotes: 1</em></p><p>The ThresholdOptimizer algorithm allows you to adjust the decision threshold of the binary classification model to improve the balance between the accuracy of the model and the fairness of the model&#x27;s predictions. This algorithm takes the original binary classification model as input and produces a new, fairer model without the need for retraining. Others require retraining the model.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 24 Feb 2024 16:45)</code> - <em>Upvotes: 1</em></p><p>The correct sequence of actions is:
B) Register each training file as a new datastore
D) Add a new parameter in the module indicating the path to the training file
E) Publish a training pipeline
C) Run the training pipeline by using the studio portal
Action A is not required as the path to the training file will be specified through the new parameter added in step 2.</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Sat 10 Feb 2024 20:05)</code> - <em>Upvotes: 1</em></p><p>IT should be B</p></blockquote>
<blockquote><p><strong>BTAB</strong> <code>(Sun 14 Jan 2024 13:04)</code> - <em>Upvotes: 1</em></p><p>We want post processing, not pre processing</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Tue 09 Jan 2024 19:46)</code> - <em>Upvotes: 1</em></p><p>CorrelationRemover is a preprocessing tool -so that suggests you need to train again. I&#x27;ll vote for B.</p></blockquote>
<blockquote><p><strong>Wayland</strong> <code>(Thu 14 Sep 2023 02:53)</code> - <em>Upvotes: 3</em></p><p>B
https://docs.microsoft.com/en-us/training/modules/detect-mitigate-unfairness-models-with-azure-machine-learning/4-mitigate-with-fairlearn</p></blockquote>

</details>

---

[<< Previous Question](question_488.md) | [Home](../index.md) | [Next Question >>](question_490.md)
