# Question 190

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

An IT department creates the following Azure resource groups and resources:

![Question Image](images/q190_q_0015800001.png)

The IT department creates an Azure Kubernetes Service (AKS)-based inference compute target named aks-cluster in the Azure Machine Learning workspace.

You have a Microsoft Surface Book computer with a GPU. Python 3.6 and Visual Studio Code are installed.

You need to run a script that trains a deep neural network (DNN) model and logs the loss and accuracy metrics.

Solution: Install the Azure ML SDK on the Surface Book. Run Python code to connect to the workspace. Run the training script as an experiment on the aks- cluster compute target.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>chaudha4</strong> <code>(Fri 22 Oct 2021 21:50)</code> - <em>Upvotes: 19</em></p><p>A very long question trying to ask if you can use an inference cluster for training purpose !!</p></blockquote>
<blockquote><p><strong>gamezone25</strong> <code>(Wed 20 Oct 2021 19:12)</code> - <em>Upvotes: 13</em></p><p>B is indeed the correct answer. AKS is for inference, not for training</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 02 Dec 2024 11:15)</code> - <em>Upvotes: 1</em></p><p>answer is A, yes, AKS is used as inference compute target, inference means hosting and deploying the model not training the model</p></blockquote>
<blockquote><p><strong>a6cb3b0</strong> <code>(Fri 27 Sep 2024 16:47)</code> - <em>Upvotes: 1</em></p><p>read this:
Azure Machine Learning Kubernetes compute supports two kinds of Kubernetes cluster:

AKS cluster in Azure. With your self-managed AKS cluster in Azure, you can gain security and controls to meet compliance requirement and flexibility to manage teams&#x27; ML workload.
Arc Kubernetes cluster outside of Azure. With Arc Kubernetes cluster, you can train or deploy models in any infrastructure on-premises, across multicloud, or the edge.

Since this question menthioned we have AKS Cluster in Azure, so it is not possible to train the model. the correct answer is B.</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Mon 12 Aug 2024 16:40)</code> - <em>Upvotes: 1</em></p><p>AKS clusters can process training and allow for gpu usage. So it seems feasible. Reference: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-attach-kubernetes-anywhere?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>esimsek</strong> <code>(Sat 23 Sep 2023 11:46)</code> - <em>Upvotes: 5</em></p><p>In exam 2023-03-23</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Fri 08 Sep 2023 11:15)</code> - <em>Upvotes: 4</em></p><p>Exactly this question was on exam 07/March/2023</p></blockquote>
<blockquote><p><strong>ahson0124</strong> <code>(Tue 15 Aug 2023 12:42)</code> - <em>Upvotes: 3</em></p><p>In exam on 2023-02-15</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 18 Nov 2022 13:50)</code> - <em>Upvotes: 1</em></p><p>No need to over thinking ...
AKS for deploying large scale applications ...
No where in documentation mentioned as training target ...
In practically, you can certainly train data on AKS, LOL ...</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Wed 14 Sep 2022 03:36)</code> - <em>Upvotes: 1</em></p><p>aks is for inferencing not for training</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Apr 2022 09:43)</code> - <em>Upvotes: 1</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>lander_c</strong> <code>(Sun 20 Mar 2022 06:12)</code> - <em>Upvotes: 3</em></p><p>The answer should be No. But note the AKS has a preview feature that allows it to train models as well. Check whether it has been moved out of the preview feature set.</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Thu 03 Mar 2022 08:28)</code> - <em>Upvotes: 1</em></p><p>on exam 2/9/21</p></blockquote>

</details>

---

[<< Previous Question](question_189.md) | [Home](/index.md) | [Next Question >>](question_191.md)
