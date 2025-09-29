# Question 189

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

An IT department creates the following Azure resource groups and resources:

![Question Image](../images/q189_q_0015600001.png)

The IT department creates an Azure Kubernetes Service (AKS)-based inference compute target named aks-cluster in the Azure Machine Learning workspace.

You have a Microsoft Surface Book computer with a GPU. Python 3.6 and Visual Studio Code are installed.

You need to run a script that trains a deep neural network (DNN) model and logs the loss and accuracy metrics.

Solution: Attach the mlvm virtual machine as a compute target in the Azure Machine Learning workspace. Install the Azure ML SDK on the Surface Book and run

Python code to connect to the workspace. Run the training script as an experiment on the mlvm remote compute resource.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>bkuchi</strong> <code>(Wed 15 Dec 2021 15:04)</code> - <em>Upvotes: 9</em></p><p>Question was there in June 2021 Exam</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Fri 08 Sep 2023 11:15)</code> - <em>Upvotes: 5</em></p><p>Exactly this question was on exam 07/March/2023</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Sun 17 Nov 2024 02:55)</code> - <em>Upvotes: 1</em></p><p>Remote VMs are considered as a unmanaged and can require extra steps for you to maintain or to improve performance for machine learning workloads. I interpret this as you won&#x27;t be able to log the metrics out-of-the box. Link: require extra steps for you to maintain or to improve performance for machine learning workloads. https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2#unmanaged-compute</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Wed 13 Dec 2023 16:04)</code> - <em>Upvotes: 2</em></p><p>Isn&#x27;t inference cluster used for deployment and not for training?</p></blockquote>
<blockquote><p><strong>Deathking15</strong> <code>(Mon 13 May 2024 20:42)</code> - <em>Upvotes: 3</em></p><p>I believe what&#x27;s currently recommended as the compute resource for deployment is a Kubernetes compute, but the question is simply asking if the given compute can work, not whether it&#x27;s the most optimal.</p></blockquote>
<blockquote><p><strong>krishna1818</strong> <code>(Wed 29 Nov 2023 11:02)</code> - <em>Upvotes: 1</em></p><p>existing VM has to be attached</p></blockquote>
<blockquote><p><strong>ahson0124</strong> <code>(Tue 15 Aug 2023 12:42)</code> - <em>Upvotes: 3</em></p><p>In exam on 2023-02-15</p></blockquote>
<blockquote><p><strong>robotcop</strong> <code>(Sun 28 May 2023 14:50)</code> - <em>Upvotes: 1</em></p><p>no objection</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 18 Nov 2022 13:42)</code> - <em>Upvotes: 1</em></p><p>Attach existing VM as a target, sounds correct</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Wed 14 Sep 2022 03:33)</code> - <em>Upvotes: 1</em></p><p>Given answer is correct</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Sun 17 Jul 2022 03:37)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Tue 21 Jun 2022 07:26)</code> - <em>Upvotes: 2</em></p><p>Is the given answer correct?</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Apr 2022 09:43)</code> - <em>Upvotes: 2</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Thu 03 Mar 2022 08:28)</code> - <em>Upvotes: 3</em></p><p>on exam 2/9/21</p></blockquote>
<blockquote><p><strong>dushmantha</strong> <code>(Mon 28 Feb 2022 14:15)</code> - <em>Upvotes: 3</em></p><p>On exam 2021/08/31</p></blockquote>

</details>

---

[<< Previous Question](question_188.md) | [Home](/index.md) | [Next Question >>](question_190.md)
