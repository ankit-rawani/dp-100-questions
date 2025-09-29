# Question 326

You are implementing hyperparameter tuning for a model training from a notebook. The notebook is in an Azure Machine Learning workspace.

You must configure a grid sampling method over the search space for the num_hidden_layers and batch_size hyperparameters.

You need to identify the hyperparameters for the grid sampling.

Which hyperparameter sampling approach should you use?

- A.uniform
- B.qlognormal
- C.choice
- D.normal

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>avotofu</strong> <code>(Thu 19 Oct 2023 00:20)</code> - <em>Upvotes: 6</em></p><p>answer is c.choice</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Sat 23 Nov 2024 12:02)</code> - <em>Upvotes: 1</em></p><p>Grid sampling can only be used with choice hyperparameters.
Reference: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2#grid-sampling</p></blockquote>
<blockquote><p><strong>bobML</strong> <code>(Mon 11 Mar 2024 11:29)</code> - <em>Upvotes: 4</em></p><p>C
For configuring a grid sampling method over the search space for hyperparameters like num_hidden_layers and batch_size, you should use the &quot;choice&quot; hyperparameter sampling approach.

The &quot;choice&quot; sampling approach allows you to specify a list of discrete values from which the hyperparameter tuning process will select combinations. In your case, you would provide a list of possible values for num_hidden_layers and batch_size, and the grid search would consider all combinations of these values.

So, the correct option is:

C. choice</p></blockquote>

<blockquote><p><strong>BR_CS</strong> <code>(Sat 17 Feb 2024 11:49)</code> - <em>Upvotes: 1</em></p><p>Choice</p></blockquote>
<blockquote><p><strong>abcd9999</strong> <code>(Fri 02 Feb 2024 07:58)</code> - <em>Upvotes: 1</em></p><p>from azureml.train.hyperdrive import choice, GridParameterSampling

param_sampling = GridParameterSampling({
&#x27;num_hidden_layers&#x27;: choice([16, 32, 64]),
&#x27;batch_size&#x27;: choice([32, 64, 128])
})</p></blockquote>

<blockquote><p><strong>phdykd</strong> <code>(Fri 26 Jan 2024 14:52)</code> - <em>Upvotes: 1</em></p><p>c) 
Choice
https://learn.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.hyperdrive.gridparametersampling?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>mfcanseco</strong> <code>(Tue 05 Dec 2023 12:37)</code> - <em>Upvotes: 1</em></p><p>Grid sampling does a simple grid search over all possible values. Grid sampling can only be used with choice hyperparameters. For example, the following space has six samples:</p></blockquote>

</details>

---

[<< Previous Question](question_325.md) | [Home](../index.md) | [Next Question >>](question_327.md)
