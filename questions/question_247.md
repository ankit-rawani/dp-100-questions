# Question 247

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You have a Python script named train.py in a local folder named scripts. The script trains a regression model by using scikit-learn. The script includes code to load a training data file which is also located in the scripts folder.

You must run the script as an Azure ML experiment on a compute cluster named aml-compute.

You need to configure the run to ensure that the environment includes the required packages for model training. You have instantiated a variable named aml- compute that references the target compute cluster.

Solution: Run the following code:

![Question Image](images/q247_q_0025800001.png)

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

<blockquote><p><strong>folkmusic99</strong> <code>(Sat 24 Aug 2024 01:49)</code> - <em>Upvotes: 3</em></p><p>from azureml.core import ScriptRunConfig, Experiment

   # create or load an experiment
   experiment = Experiment(workspace, &#x27;MyExperiment&#x27;)
   # create or retrieve a compute target
   cluster = workspace.compute_targets[&#x27;MyCluster&#x27;]
   # create or retrieve an environment
   env = Environment.get(ws, name=&#x27;MyEnvironment&#x27;)
   # configure and submit your training run
   config = ScriptRunConfig(source_directory=&#x27;.&#x27;,
                            script=&#x27;train.py&#x27;,
                            arguments=[&#x27;--arg1&#x27;, arg1_val, &#x27;--arg2&#x27;, arg2_val],
                            compute_target=cluster,
                            environment=env)
   script_run = experiment.submit(config)

ScriptRunConfig and Experiment are two imp keys</p></blockquote>
<blockquote><p><strong>medsimus</strong> <code>(Tue 02 Apr 2024 14:32)</code> - <em>Upvotes: 3</em></p><p>Question is outdated:
https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.sklearn.sklearn?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Wed 20 Mar 2024 08:47)</code> - <em>Upvotes: 3</em></p><p>how is this correct answer? we need to use experiment class to run experiments.</p></blockquote>

</details>

---

[<< Previous Question](question_246.md) | [Home](/index.md) | [Next Question >>](question_248.md)
