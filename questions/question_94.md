# Question 94

HOTSPOT -

You are preparing to build a deep learning convolutional neural network model for image classification. You create a script to train the model using CUDA devices.

You must submit an experiment that runs this script in the Azure Machine Learning workspace.

The following compute resources are available:

✑ a Microsoft Surface device on which Microsoft Office has been installed. Corporate IT policies prevent the installation of additional software

✑ a Compute Instance named ds-workstation in the workspace with 2 CPUs and 8 GB of memory

✑ an Azure Machine Learning compute target named cpu-cluster with eight CPU-based nodes

✑ an Azure Machine Learning compute target named gpu-cluster with four CPU and GPU-based nodes

You need to specify the compute resources to be used for running the code to submit the experiment, and for running the script in order to minimize model training time.

Which resources should the data scientist use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q94_q_0011200001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q94_ans_0_0011300001.png" alt="Answer Image"><br>
<p>Box 1: the ds-workstation compute instance</p>
<p>A workstation notebook instance is good enough to run experiments.</p>
<p>Box 2: the gpu-cluster compute target</p>
<p>Just as GPUs revolutionized deep learning through unprecedented training and inferencing performance, RAPIDS enables traditional machine learning practitioners to unlock game-changing performance with GPUs. With RAPIDS on Azure Machine Learning service, users can accelerate the entire machine learning pipeline, including data processing, training and inferencing, with GPUs from the NC_v3,  NC_v2, ND or ND_v2 families. Users can unlock performance gains of more than 20X (with 4 GPUs), slashing training times from hours to minutes and dramatically reducing time-to-insight.</p>
<p>Reference:</p>
<p>https://azure.microsoft.com/sv-se/blog/azure-machine-learning-service-now-supports-nvidia-s-rapids/</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>dev2dev</strong> <code>(Sun 17 Sep 2023 05:29)</code> - <em>Upvotes: 32</em></p><p>answers are correct, for submitting job we can use surface book but due to restrictions we cant install sdk/python</p></blockquote>
<blockquote><p><strong>aoddy</strong> <code>(Thu 28 Sep 2023 03:16)</code> - <em>Upvotes: 3</em></p><p>Thanks for your sharing</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sat 16 Nov 2024 18:26)</code> - <em>Upvotes: 3</em></p><p>The answer should be correct ...
But the question is poorly written ...
I believe it means, you can write python codes on the ds computer instance to submit experiment with script steps against gpu computer instance as target</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Sat 20 Apr 2024 09:42)</code> - <em>Upvotes: 3</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Thu 04 Apr 2024 21:15)</code> - <em>Upvotes: 1</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Sun 03 Mar 2024 08:26)</code> - <em>Upvotes: 1</em></p><p>got similar question on 2/9/21</p></blockquote>
<blockquote><p><strong>VJPrakash</strong> <code>(Sun 11 Feb 2024 17:19)</code> - <em>Upvotes: 3</em></p><p>on exam in August 2021</p></blockquote>

</details>

---

[<< Previous Question](question_93.md) | [Home](/index.md) | [Next Question >>](question_95.md)
