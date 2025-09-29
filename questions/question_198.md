# Question 198

HOTSPOT -

You create a script for training a machine learning model in Azure Machine Learning service.

You create an estimator by running the following code:

![Question Image](images/q198_q_0017000001.png)

For each of the following statements, select Yes if the statement is true. Otherwise, select No.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q198_q_0017100001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q198_ans_0_0017100002.png" alt="Answer Image"><br>
<p>Box 1: Yes -</p>
<p>Parameter source_directory is a local directory containing experiment configuration and code files needed for a training job.</p>
<p>Box 2: Yes -</p>
<p>script_params is a dictionary of command-line arguments to pass to the training script specified in entry_script.</p>
<p>Box 3: No -</p>
<p>Box 4: Yes -</p>
<p>The conda_packages parameter is a list of strings representing conda packages to be added to the Python environment for the experiment.</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>timosi</strong> <code>(Thu 31 Mar 2022 11:06)</code> - <em>Upvotes: 13</em></p><p>correct</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Wed 04 May 2022 18:22)</code> - <em>Upvotes: 10</em></p><p>estimator is deprecated. Can anyone confirm if they have seen a question on estimator lately ?</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 16 Jul 2024 17:10)</code> - <em>Upvotes: 1</em></p><p>yes, no, no, yes</p></blockquote>
<blockquote><p><strong>giusecozza</strong> <code>(Thu 07 Sep 2023 08:02)</code> - <em>Upvotes: 2</em></p><p>data_source is a Datastore object. I can&#x27;t see any reference to as_mount() method inside the doc. There&#x27;s something wrong here...

https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.datastore.datastore?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 19 May 2023 15:14)</code> - <em>Upvotes: 5</em></p><p>My vote Yes, No, No, Yes</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Sat 16 Dec 2023 11:55)</code> - <em>Upvotes: 2</em></p><p>Correct</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 19 May 2023 15:41)</code> - <em>Upvotes: 1</em></p><p>Not mount the local data-folder, but mount the data-storage as local data folder on the machine running the script</p></blockquote>
<blockquote><p><strong>Shiv948</strong> <code>(Thu 12 Jan 2023 18:17)</code> - <em>Upvotes: 4</em></p><p>I think the answer should be : NO,NO,NO,YES</p></blockquote>
<blockquote><p><strong>greengarden</strong> <code>(Thu 15 Dec 2022 01:20)</code> - <em>Upvotes: 1</em></p><p>estimator is deprecated.
https://docs.microsoft.com/zh-tw/python/api/azureml-train-core/azureml.train.estimator.estimator?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Wed 05 Oct 2022 20:24)</code> - <em>Upvotes: 4</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Sat 03 Sep 2022 07:30)</code> - <em>Upvotes: 2</em></p><p>not exactly but similar question on 2/9/21</p></blockquote>
<blockquote><p><strong>AkashV</strong> <code>(Fri 05 Aug 2022 20:15)</code> - <em>Upvotes: 2</em></p><p>Estimator will only run Scikit-learn experiments if the dependencies are added in the conda env, right ?
Shouldn&#x27;t it be No for the last option ?</p></blockquote>
<blockquote><p><strong>spaceykacey</strong> <code>(Thu 10 Nov 2022 06:17)</code> - <em>Upvotes: 1</em></p><p>look at the code carefully, they are added</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Wed 04 May 2022 18:21)</code> - <em>Upvotes: 5</em></p><p>estimator is deprecated. Can anyone confirm if they have seen a question on estimator lately ?</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Thu 24 Mar 2022 15:15)</code> - <em>Upvotes: 5</em></p><p>box2 is no. you need to upload the files that can be made available to mount the folder.

https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-1st-experiment-bring-data</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Mon 30 May 2022 22:38)</code> - <em>Upvotes: 3</em></p><p>no, you dont upload anything.</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Mon 30 May 2022 22:38)</code> - <em>Upvotes: 1</em></p><p>the source directory is for the training script</p></blockquote>

</details>

---

[<< Previous Question](question_197.md) | [Home](/index.md) | [Next Question >>](question_199.md)
