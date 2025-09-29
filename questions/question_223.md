# Question 223

You use the Azure Machine Learning service to create a tabular dataset named training_data. You plan to use this dataset in a training script.

You create a variable that references the dataset using the following code: training_ds = workspace.datasets.get("training_data")

You define an estimator to run the script.

You need to set the correct property of the estimator to ensure that your script can access the training_data dataset.

Which property should you set?

* A.environment_definition = {"training_data":training_ds}
* B.inputs = [training_ds.as_named_input('training_ds')]
* C.script_params = {"--training_ds":training_ds}
* D.source_directory = training_ds

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>
<p>Example:</p>
<p># Get the training dataset</p>
<p>diabetes_ds = ws.datasets.get(&quot;Diabetes Dataset&quot;)</p>
<p># Create an estimator that uses the remote compute</p>
<p>hyper_estimator = SKLearn(source_directory=experiment_folder, inputs=[diabetes_ds.as_named_input(&#x27;diabetes&#x27;)], # Pass the dataset as an input compute_target = cpu_cluster, conda_packages=[&#x27;pandas&#x27;,&#x27;ipykernel&#x27;,&#x27;matplotlib&#x27;], pip_packages=[&#x27;azureml-sdk&#x27;,&#x27;argparse&#x27;,&#x27;pyarrow&#x27;], entry_script=&#x27;diabetes_training.py&#x27;)</p>
<p>Reference:</p>
<p>https://notebooks.azure.com/GraemeMalcolm/projects/azureml-primers/html/04%20-%20Optimizing%20Model%20Training.ipynb</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Wed 11 Jan 2023 15:05)</code> - <em>Upvotes: 8</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>DanielGP</strong> <code>(Tue 26 Jul 2022 17:43)</code> - <em>Upvotes: 7</em></p><p>Train a model from a tabular dataset:

Now that you have datasets, you&#x27;re ready to start training models from them. You can pass datasets to scripts as INPUTS in the estimator being used to run the script.</p></blockquote>
<blockquote><p><strong>treadst0ne</strong> <code>(Mon 22 Aug 2022 23:34)</code> - <em>Upvotes: 2</em></p><p>I concur.</p></blockquote>
<blockquote><p><strong>Peeking</strong> <code>(Thu 12 Sep 2024 00:04)</code> - <em>Upvotes: 1</em></p><p>B would seem the closest answer but it was not properly described in the answers:
from azureml.core import ScriptRunConfig

src = ScriptRunConfig(source_directory=script_folder,
                      script=&#x27;train_titanic.py&#x27;,
                      # pass dataset as an input with friendly name &#x27;titanic&#x27;
                      arguments=[&#x27;--input-data&#x27;, titanic_ds.as_named_input(&#x27;titanic&#x27;)],
                      compute_target=compute_target,
                      environment=myenv)
                             
# Submit the run configuration for your training run
run = experiment.submit(src)
run.wait_for_completion(show_output=True)

Reference: https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-train-with-datasets</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sun 26 Nov 2023 15:46)</code> - <em>Upvotes: 2</em></p><p>I guess if you want to pass the parameter into estimator it will be C; now the question is asking inside the estimator you are reading the input, it is B ... Still a bit confusion ...</p></blockquote>
<blockquote><p><strong>JJason</strong> <code>(Sun 21 May 2023 05:43)</code> - <em>Upvotes: 3</em></p><p>why should not inputs = [training_ds.as_named_input(&#x27;training_ds&#x27;).as_mount()]?</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Sat 05 Nov 2022 14:37)</code> - <em>Upvotes: 5</em></p><p>Estimator is deprecated. Can anyone confirm if they saw a question on this topic lately ?</p></blockquote>
<blockquote><p><strong>shivaborusu</strong> <code>(Tue 10 May 2022 14:45)</code> - <em>Upvotes: 1</em></p><p>Answer must be C</p></blockquote>
<blockquote><p><strong>shivaborusu</strong> <code>(Sun 15 May 2022 13:43)</code> - <em>Upvotes: 8</em></p><p>Taking back.. B is correct answer</p></blockquote>
<blockquote><p><strong>epgd</strong> <code>(Tue 28 Dec 2021 23:15)</code> - <em>Upvotes: 1</em></p><p>why the correct answer is not script_params ?</p></blockquote>
<blockquote><p><strong>amelia</strong> <code>(Wed 29 Dec 2021 12:51)</code> - <em>Upvotes: 3</em></p><p>The question does not specify using command-line arguments to pass to the training script, so I guess it is assumed the traiining data is specified as an input compute target in the estimator properties.</p></blockquote>

</details>

---

[<< Previous Question](question_222.md) | [Home](/index.md) | [Next Question >>](question_224.md)
