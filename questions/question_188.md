# Question 188

You create a datastore named training_data that references a blob container in an Azure Storage account. The blob container contains a folder named csv_files in which multiple comma-separated values (CSV) files are stored.

You have a script named train.py in a local folder named ./script that you plan to run as an experiment using an estimator. The script includes the following code to read data from the csv_files folder:

![Question Image](images/q188_q_0015100001.png)

You have the following script.

![Question Image](images/q188_q_0015100002.png)

You need to configure the estimator for the experiment so that the script can read the data from a data reference named data_ref that references the csv_files folder in the training_data datastore.

Which code should you use to configure the estimator?

A.

![Question Image](images/q188_q_0015200001.png)

B.

![Question Image](images/q188_q_0015200002.png)

C.

![Question Image](images/q188_q_0015200003.png)

D.

![Question Image](images/q188_q_0015200004.png)

E.

![Question Image](images/q188_q_0015200005.png)

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>
<p>Besides passing the dataset through the input parameters in the estimator, you can also pass the dataset through script_params and get the data path (mounting point) in your training script via arguments. This way, you can keep your training script independent of azureml-sdk. In other words, you will be able use the same training script for local debugging and remote training on any cloud platform.</p>
<p>Example:</p>
<p>from azureml.train.sklearn import SKLearn</p>
<p>script_params = {</p>
<p># mount the dataset on the remote compute and pass the mounted path as an argument to the training script</p>
<p>&#x27;--data-folder&#x27;: mnist_ds.as_named_input(&#x27;mnist&#x27;).as_mount(),</p>
<p>&#x27;--regularization&#x27;: 0.5</p>
<p>}</p>
<p>est = SKLearn(source_directory=script_folder,</p>
<p>script_params=script_params,</p>
<p>compute_target=compute_target,</p>
<p>environment_definition=env,</p>
<p>entry_script=&#x27;train_mnist.py&#x27;)</p>
<p># Run the experiment</p>
<p>run = experiment.submit(est)</p>
<p>run.wait_for_completion(show_output=True)</p>
<p>Incorrect Answers:</p>
<p>A: Pandas DataFrame not used.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/es-es/azure/machine-learning/how-to-train-with-datasets</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>chaudha4</strong> <code>(Wed 04 May 2022 15:09)</code> - <em>Upvotes: 13</em></p><p>The use of estimator is deprecated.  Use the ScriptRunConfig object with your own defined environment. Hope we don&#x27;t see this question going forward !!

https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.estimator.estimator?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>scipio</strong> <code>(Mon 16 May 2022 11:47)</code> - <em>Upvotes: 5</em></p><p>You&#x27;re right, but if you replace the estimator with the ScriptRunConfig this question still holds, as the method to pass Dataset, mount vs. download, by argument, etc.. are relevant</p></blockquote>
<blockquote><p><strong>vv_bb</strong> <code>(Tue 12 Nov 2024 21:58)</code> - <em>Upvotes: 3</em></p><p>Even though the Estimator is deprecated in favor for ScriptRunConfig (google - &quot;Migrating from Estimators to ScriptRunConfig&quot;) , I tried to understand the correct answer for the question as it is defined here.

1) For Estimator class both &quot;script_params&quot; and &quot;arguments&quot; parameters are acceptable
check here -  https://learn.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.estimator.estimator?view=azure-ml-py

2) So how to define which of them is valid in our case?
The answer is here: 
(be aware for PythonScriptStep &quot;arguments&quot; is the same as &quot;script_params&quot; for Estimator)
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-move-data-in-out-of-pipelines?view=azureml-api-1#access-datasets-within-your-script

Meaning because in our script we use the ArgParser we have to pass the dataset using the  &quot;script_params&quot;</p></blockquote>
<blockquote><p><strong>iai</strong> <code>(Tue 28 May 2024 14:01)</code> - <em>Upvotes: 2</em></p><p>Shouldn&#x27;t it be D.? for local compute_target not sure if as_mount will work. better as_download</p></blockquote>
<blockquote><p><strong>danishanis</strong> <code>(Tue 27 Feb 2024 00:04)</code> - <em>Upvotes: 2</em></p><p>Answer is B.
I typed the question as it is in ChatGPT and it gave the answer where the &#x27;script_params&#x27; argument is configured to read data from &#x27;data_ref&#x27; (and data_ref.as_mount() is being used to specify the file path in datastore) that references a &#x27;csv_files&#x27; folder.</p></blockquote>
<blockquote><p><strong>jpalaci22</strong> <code>(Tue 20 Feb 2024 21:14)</code> - <em>Upvotes: 3</em></p><p>Seen on the exam 20Feb2023</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Sat 16 Dec 2023 09:50)</code> - <em>Upvotes: 1</em></p><p>can be A,C,E - what do you thing?</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Thu 18 May 2023 12:29)</code> - <em>Upvotes: 3</em></p><p>B should be correct!</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Fri 10 Mar 2023 05:51)</code> - <em>Upvotes: 4</em></p><p>on march 2022</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Tue 04 Oct 2022 22:24)</code> - <em>Upvotes: 3</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Mon 11 Jul 2022 13:59)</code> - <em>Upvotes: 3</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>sarahmoin</strong> <code>(Thu 09 Jun 2022 10:07)</code> - <em>Upvotes: 1</em></p><p>what is the correct answer? Why its not D.</p></blockquote>
<blockquote><p><strong>vhx</strong> <code>(Mon 13 Jun 2022 16:43)</code> - <em>Upvotes: 3</em></p><p>as_download, which copies the files to a temporary location on the compute where the script is being run. as_mount to stream the files directly from their source.</p></blockquote>
<blockquote><p><strong>iai</strong> <code>(Tue 28 May 2024 14:02)</code> - <em>Upvotes: 1</em></p><p>Notice however, that compute target is local, will mounting work?</p></blockquote>
<blockquote><p><strong>iuolu</strong> <code>(Sun 01 May 2022 14:36)</code> - <em>Upvotes: 2</em></p><p>Nobody checked this question? The answer should be A, using to_pandas_dataframe() for tabular files instead</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Wed 04 May 2022 15:02)</code> - <em>Upvotes: 10</em></p><p>No, you are wrong. Several problems in A. 
1) Parameter is being passed as named input. That is wrong since it is not being accessed using named input in t he script.
2) You convert to dataframe in the script not when you pass it.
So A is definitely not the correct answer.</p></blockquote>

</details>

---

[<< Previous Question](question_187.md) | [Home](/index.md) | [Next Question >>](question_189.md)
