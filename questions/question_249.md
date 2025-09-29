# Question 249

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have a Python script named train.py in a local folder named scripts. The script trains a regression model by using scikit-learn. The script includes code to load a training data file which is also located in the scripts folder.

You must run the script as an Azure ML experiment on a compute cluster named aml-compute.

You need to configure the run to ensure that the environment includes the required packages for model training. You have instantiated a variable named aml- compute that references the target compute cluster.

Solution: Run the following code:

![Question Image](images/q249_q_0025900001.png)

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>
<p>The scikit-learn estimator provides a simple way of launching a scikit-learn training job on a compute target. It is implemented through the SKLearn class, which can be used to support single-node CPU training.</p>
<p>Example:</p>
<p>from azureml.train.sklearn import SKLearn</p>
<p>}</p>
<p>estimator = SKLearn(source_directory=project_folder,</p>
<p>compute_target=compute_target,</p>
<p>entry_script=&#x27;train_iris.py&#x27;</p>
<p>)</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-train-scikit-learn</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>hendriktytgatpwc</strong> <code>(Tue 14 Mar 2023 16:03)</code> - <em>Upvotes: 11</em></p><p>Question is outdated: Estimator is being replaced by ScriptRunConfig
https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.sklearn.sklearn?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>medsimus</strong> <code>(Sun 02 Apr 2023 14:30)</code> - <em>Upvotes: 1</em></p><p>Indeed</p></blockquote>
<blockquote><p><strong>Lucario95</strong> <code>(Sat 03 Jun 2023 15:56)</code> - <em>Upvotes: 5</em></p><p>Doesn&#x27;t the solution still meet requirements? (Even if not using SKLearn object)</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Sun 08 Dec 2024 21:53)</code> - <em>Upvotes: 2</em></p><p>This one is correct as opposed to 67 which does not specify scikit learn in the conda_environment packages.</p></blockquote>
<blockquote><p><strong>AkashV</strong> <code>(Sun 06 Aug 2023 15:12)</code> - <em>Upvotes: 1</em></p><p>Don&#x27;t we have to copy the scripts folders for them to be accessible in the computer cluster ?</p></blockquote>

</details>

---

[<< Previous Question](question_248.md) | [Home](/index.md) | [Next Question >>](question_250.md)
