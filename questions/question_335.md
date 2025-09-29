# Question 335

You create an Azure Machine learning workspace.

You must use the Azure Machine Learning Python SDK v2 to define the search space for discrete hyperparameters. The hyperparameters must consist of a list of predetermined, comma-separated integer values.

You need to import the class from the azure.ai.ml.sweep package used to create the list of values.

Which class should you import?

* A.Choice
* B.Randint
* C.Uniform
* D.Normal

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>orionduo</strong> <code>(Fri 01 Mar 2024 09:16)</code> - <em>Upvotes: 5</em></p><p>Correct
Choice</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Sun 24 Nov 2024 01:29)</code> - <em>Upvotes: 2</em></p><p>Discrete hyperparameters.
Consist of a list of predetermined, comma-separated integer value.
&gt;&gt;&gt;A. Choice

Discrete hyperparameters are specified as a Choice among discrete values. Choice can be:
one or more comma-separated values
a range object
any arbitrary list object
reference:
https://learn.microsoft.com/en-us/AZURE/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2#discrete-hyperparameters</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 23 Feb 2024 15:10)</code> - <em>Upvotes: 4</em></p><p>To define the search space for discrete hyperparameters using the Azure Machine Learning Python SDK v2, you should import the Choice class from the azure.ai.ml.sweep package. The Choice class allows you to specify a list of predetermined, comma-separated values for a discrete hyperparameter.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2

SaM</p></blockquote>
<blockquote><p><strong>BR_CS</strong> <code>(Sat 17 Feb 2024 12:24)</code> - <em>Upvotes: 1</em></p><p>AS this is about &quot;creation&quot; of the list, Randint is correct</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 05 Jan 2024 20:32)</code> - <em>Upvotes: 1</em></p><p>Only Randint supports integers values.
https://learn.microsoft.com/en-us/python/api/azure-ai-ml/azure.ai.ml.sweep.randint?view=azure-python</p></blockquote>
<blockquote><p><strong>Panda_man</strong> <code>(Tue 30 Jul 2024 22:31)</code> - <em>Upvotes: 1</em></p><p>you&#x27;re reference link is not showing anything about the correct answer;</p></blockquote>

</details>

---

[<< Previous Question](question_334.md) | [Home](/index.md) | [Next Question >>](question_336.md)
