# Question 250

You create a multi-class image classification deep learning model that uses a set of labeled images. You create a script file named train.py that uses the PyTorch

1.3 framework to train the model.

You must run the script by using an estimator. The code must not require any additional Python libraries to be installed in the environment for the estimator. The time required for model training must be minimized.

You need to define the estimator that will be used to run the script.

Which estimator type should you use?

- A.TensorFlow
- B.PyTorch
- C.SKLearn
- D.Estimator

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

<p>For PyTorch, TensorFlow and Chainer tasks, Azure Machine Learning provides respective PyTorch, TensorFlow, and Chainer estimators to simplify using these frameworks.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-train-ml-models</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ashii007</strong> <code>(Wed 26 Jun 2024 00:22)</code> - <em>Upvotes: 4</em></p><p>Estimator is deprecated as of dec&#x27;21. Shouldn&#x27;t see questions about estimator in the test.</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Wed 27 Sep 2023 03:47)</code> - <em>Upvotes: 2</em></p><p>Isnt it D? Esitmator is generic class and doesnt need additional libraries.</p></blockquote>
<blockquote><p><strong>ACSC</strong> <code>(Mon 09 Oct 2023 07:42)</code> - <em>Upvotes: 3</em></p><p>I agree. Anyway the question is outdated. https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.estimator.estimator?view=azure-ml-py</p></blockquote>

</details>

---

[<< Previous Question](question_249.md) | [Home](../index.md) | [Next Question >>](question_251.md)
