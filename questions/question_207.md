# Question 207

You create a multi-class image classification deep learning model that uses the PyTorch deep learning framework.

You must configure Azure Machine Learning Hyperdrive to optimize the hyperparameters for the classification model.

You need to define a primary metric to determine the hyperparameter values that result in the model with the best accuracy score.

Which three actions must you perform? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

* A.Set the primary_metric_goal of the estimator used to run the bird_classifier_train.py script to maximize.
* B.Add code to the bird_classifier_train.py script to calculate the validation loss of the model and log it as a float value with the key loss.
* C.Set the primary_metric_goal of the estimator used to run the bird_classifier_train.py script to minimize.
* D.Set the primary_metric_name of the estimator used to run the bird_classifier_train.py script to accuracy.
* E.Set the primary_metric_name of the estimator used to run the bird_classifier_train.py script to loss.
* F.Add code to the bird_classifier_train.py script to calculate the validation accuracy of the model and log it as a float value with the key accuracy.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>ADF</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Arend78</strong> <code>(Mon 12 Jun 2023 12:04)</code> - <em>Upvotes: 6</em></p><p>The primary_metric_goal=PrimaryMetricGoal.MAXIMIZE notation is depricated (v1):
https://learn.microsoft.com/nl-nl/azure/machine-learning/v1/how-to-tune-hyperparameters-v1 (DEPRICATED)

Please use 

```sweep_job = command_job_for_sweep.sweep(
    compute=&quot;cpu-cluster&quot;,
    sampling_algorithm = &quot;bayesian&quot;,
    primary_metric=&quot;accuracy&quot;,
    goal=&quot;Maximize&quot;,   # !!!
)

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 02 Dec 2024 12:58)</code> - <em>Upvotes: 2</em></p><p>given answers are correct</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Wed 27 Dec 2023 21:20)</code> - <em>Upvotes: 2</em></p><p>ADF - ChatGPT</p></blockquote>
<blockquote><p><strong>esimsek</strong> <code>(Mon 25 Sep 2023 10:23)</code> - <em>Upvotes: 3</em></p><p>ADF are correct</p></blockquote>
<blockquote><p><strong>Mirjalol</strong> <code>(Thu 03 Aug 2023 15:33)</code> - <em>Upvotes: 1</em></p><p>Why A and C answers are the same?</p></blockquote>
<blockquote><p><strong>Mirjalol</strong> <code>(Tue 08 Aug 2023 11:24)</code> - <em>Upvotes: 1</em></p><p>Sorry , one is maximize, the other one is minimize</p></blockquote>
<blockquote><p><strong>Thornehead</strong> <code>(Wed 28 Sep 2022 00:36)</code> - <em>Upvotes: 2</em></p><p>ADF are the correct answers.</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Fri 05 Nov 2021 16:54)</code> - <em>Upvotes: 1</em></p><p>Why not BCE ?</p></blockquote>
<blockquote><p><strong>skrangan</strong> <code>(Sat 06 Nov 2021 14:05)</code> - <em>Upvotes: 3</em></p><p>It is Classification model. Hence we depend it on Accuracy</p></blockquote>
<blockquote><p><strong>lakito</strong> <code>(Sat 18 Dec 2021 22:53)</code> - <em>Upvotes: 3</em></p><p>The question itself says &quot;accuracy&quot;, not &quot;loss&quot;.</p></blockquote>

</details>

---

[<< Previous Question](question_206.md) | [Home](/index.md) | [Next Question >>](question_208.md)
