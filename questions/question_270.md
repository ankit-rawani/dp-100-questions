# Question 270

You create a script that trains a convolutional neural network model over multiple epochs and logs the validation loss after each epoch. The script includes arguments for batch size and learning rate.

You identify a set of batch size and learning rate values that you want to try.

You need to use Azure Machine Learning to find the combination of batch size and learning rate that results in the model with the lowest validation loss.

What should you do?

- A.Run the script in an experiment based on an AutoMLConfig object
- B.Create a PythonScriptStep object for the script and run it in a pipeline
- C.Use the Automated Machine Learning interface in Azure Machine Learning studio
- D.Run the script in an experiment based on a ScriptRunConfig object
- E.Run the script in an experiment based on a HyperDriveConfig object

<details>
  <summary>Show Suggested Answer</summary>

<strong>E</strong><br>

<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>hargur</strong> <code>(Thu 20 Oct 2022 09:52)</code> - <em>Upvotes: 6</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>Zhubajie</strong> <code>(Mon 10 Oct 2022 07:42)</code> - <em>Upvotes: 5</em></p><p>Correct！</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sun 20 Oct 2024 03:18)</code> - <em>Upvotes: 1</em></p><p>azureml.train.hyperdrive.HyperDriveConfig

https://learn.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.hyperdrive.hyperdriveconfig?view=azure-ml-py

&#x27;Finding the optimal model parameters with HyperDrive&#x27; https://subscription.packtpub.com/book/data/9781803232416/14/ch14lvl1sec63/finding-the-optimal-model-parameters-with-hyperdrive</p></blockquote>

</details>

---

[<< Previous Question](question_269.md) | [Home](../index.md) | [Next Question >>](question_271.md)
