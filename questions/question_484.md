# Question 484

HOTSPOT -

You create an Azure Machine Learning workspace and load a Python training script named train.py in the src subfolder. The dataset used to train your model is available locally.

You run the following script to train the model:

![Question Image](../images/q484_q_0045500001.jpg)

Instructions: For each of the following statements, select Yes if the statement is true. Otherwise, select No.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q484_q_0045600001.jpg)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q484_ans_0_0045600002.jpg" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>JTWang</strong> <code>(Thu 25 Apr 2024 07:28)</code> - <em>Upvotes: 7</em></p><p>My answer:  
1.N 
2.N 
3.N  (use build_local function to create local env)

https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.environment(class)?view=azure-ml-p</p></blockquote>

<blockquote><p><strong>BTAB</strong> <code>(Sun 14 Jul 2024 11:48)</code> - <em>Upvotes: 1</em></p><p>Yes, that&#x27;s correct.</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Sat 10 Aug 2024 18:56)</code> - <em>Upvotes: 2</em></p><p>The first box is No because when you use your local computer for training, there is no need to create a compute target.

https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-attach-compute-targets#local-computer</p></blockquote>

<blockquote><p><strong>Tommo565</strong> <code>(Sat 28 Sep 2024 11:49)</code> - <em>Upvotes: 1</em></p><p>N, N, N is correct</p></blockquote>
<blockquote><p><strong>claps92</strong> <code>(Sun 10 Mar 2024 14:10)</code> - <em>Upvotes: 3</em></p><p>isn&#x27;t 1)N 2)N 3)Y?</p></blockquote>

</details>

---

[<< Previous Question](question_483.md) | [Home](/index.md) | [Next Question >>](question_485.md)
