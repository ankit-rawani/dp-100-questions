# Question 96

HOTSPOT -

You create an Azure Machine Learning workspace and set up a development environment. You plan to train a deep neural network (DNN) by using the

Tensorflow framework and by using estimators to submit training scripts.

You must optimize computation speed for training runs.

You need to choose the appropriate estimator to use as well as the appropriate training compute target configuration.

Which values should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q96_q_0012400001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q96_ans_0_0012500001.png" alt="Answer Image"><br>

<p>Box 1: Tensorflow -</p>
<p>TensorFlow represents an estimator for training in TensorFlow experiments.</p>
<p>Box 2: 12 vCPU, 112 GB memory..,2 GPU,..</p>
<p>Use GPUs for the deep neural network.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.dnn</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>MarinaMijailovic</strong> <code>(Fri 31 May 2024 12:37)</code> - <em>Upvotes: 1</em></p><p>How do you know which training compute to choose? There are so many details. How to know in general what are the best options?</p></blockquote>
<blockquote><p><strong>lcgcastro96</strong> <code>(Thu 13 Jun 2024 14:09)</code> - <em>Upvotes: 5</em></p><p>TensorFlow will normally require GPU for faster computation times, the only machine there with GPU is the solution chosen one</p></blockquote>
<blockquote><p><strong>PremPatrick</strong> <code>(Sun 12 Nov 2023 06:43)</code> - <em>Upvotes: 1</em></p><p>Why not Pytorch as option?</p></blockquote>
<blockquote><p><strong>RicSpd</strong> <code>(Thu 23 Nov 2023 13:53)</code> - <em>Upvotes: 6</em></p><p>Because it is written &quot;by using the Tensorflow framework&quot;</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Sun 19 Feb 2023 12:45)</code> - <em>Upvotes: 4</em></p><p>Correct! DNN frameworks include TensorFlow and Pytorch, and works best with GPU!</p></blockquote>
<blockquote><p><strong>renuka1234</strong> <code>(Fri 09 Dec 2022 08:50)</code> - <em>Upvotes: 4</em></p><p>Correct</p></blockquote>

</details>

---

[<< Previous Question](question_95.md) | [Home](../index.md) | [Next Question >>](question_97.md)
