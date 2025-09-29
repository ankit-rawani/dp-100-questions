# Question 422

DRAG DROP

-

You create an Azure Machine Learning workspace. You are training a classification model with no-code AutoML in Azure Machine Learning studio.

The model must predict if a client of a financial institution will subscribe to a fixed-term deposit. You must preview the data profile in Azure Machine Learning studio once the dataset is created.

You need to train the model.

Which four actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

![Question Image](images/q422_q_image475.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q422_ans_0_image476.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>sl_mslconsulting</strong> <code>(Sat 30 Nov 2024 21:55)</code> - <em>Upvotes: 1</em></p><p>If you follow along closely with the steps detailed in the link provided by paperflying:
Create an Automated Machine Learning job 
Create and load a dataset as a data asset ( I would pick tabular as this is the default and only option supported by Auto ML. Also you can preview the data at this step)
create an experiment ( part of the configure job task)
create compute target ( part of the configure job task)
Again this is strictly following the steps outlined in the doc and you don&#x27;t need to agree.</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Sat 30 Nov 2024 22:08)</code> - <em>Upvotes: 1</em></p><p>In the newest UI, you specify the experiment name in the &quot;Basic settings&quot; step, which comes before the &quot;Task type &amp; data&quot;. So you just have to decide the orders yourself.</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Sun 25 Feb 2024 12:39)</code> - <em>Upvotes: 2</em></p><p>Create a tabular dataset.
Create a compute cluster.
Create an experiment.
Create an automated ML job.

First, you need to create a tabular dataset that contains the data you want to use to train the model. You can do this by uploading a file or connecting to an external data source in Azure Machine Learning studio. Once the dataset is created, you can preview the data profile in Azure Machine Learning studio.

Next, you need to create a compute cluster that will be used to run the automated ML job. 

After creating the compute cluster, you need to create an experiment to track the runs of your automated ML job. An experiment is a named container for a series of related runs.

Finally, you need to create an automated ML job 

SaM</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Wed 10 Jul 2024 10:36)</code> - <em>Upvotes: 1</em></p><p>I need to make corrections here. I went through it myself. The first thing you will do on Azure Ml is going to Azure Auto ML job, then it asks you for a name for the experiment (so create the experiment), then you can import data where you can see the data as well, indeed a preview of the dataset. Finally, you will create or choose the compute cluster and  then you will submit the experiment. So, I still don&#x27;t know what this question is asking specifically, but I would go with the order I mentioned in the updated comment. 

SaM</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Sat 24 Aug 2024 15:15)</code> - <em>Upvotes: 1</em></p><p>you are right but i think as you are creating automated ML job you need to select the dataset, environment, then select compute cluster. That means these objects should have already been created. Therefore, logically, your earlier answer seems to be correct  for me.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 27 Jan 2024 18:41)</code> - <em>Upvotes: 4</em></p><p>Create a tabular dataset
Create a compute cluster
Create an experiment
Create an automated ML job</p></blockquote>
<blockquote><p><strong>vish9</strong> <code>(Mon 13 Nov 2023 13:32)</code> - <em>Upvotes: 1</em></p><p>Automated ML only supports Tabular dataset
https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-create-register-datasets?view=azureml-api-1</p></blockquote>
<blockquote><p><strong>paperflying</strong> <code>(Fri 27 Oct 2023 23:33)</code> - <em>Upvotes: 1</em></p><p>Upload the file and preview.
https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-first-experiment-automated-ml?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>adamcodes716</strong> <code>(Thu 26 Oct 2023 11:48)</code> - <em>Upvotes: 1</em></p><p>Why not tabular dataset?</p></blockquote>

</details>

---

[<< Previous Question](question_421.md) | [Home](/index.md) | [Next Question >>](question_423.md)
