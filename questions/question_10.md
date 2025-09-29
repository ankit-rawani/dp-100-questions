# Question 10

This question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the recommendation satisfies the requirements.

You have been tasked with employing a machine learning model, which makes use of a PostgreSQL database and needs GPU processing, to forecast prices.

You are preparing to create a virtual machine that has the necessary tools built into it.

You need to make use of the correct virtual machine type.

Recommendation: You make use of a Data Science Virtual Machine (DSVM) Windows edition.

Will the requirements be satisfied?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Tin_Tin</strong> <code>(Thu 25 Jan 2024 06:45)</code> - <em>Upvotes: 7</em></p><p>DSVM Windows does not support PostgreSQL.</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Sat 27 May 2023 18:28)</code> - <em>Upvotes: 6</em></p><p>Deep Learning Virtual Machine (DLVM) and Data Science Virtual Machine (DSVM) can be used for machine learning workloads and come with pre-installed tools and frameworks.

In this case, you can choose either the DLVM or DSVM based on your preference and specific requirements. Both virtual machine types can support the use of a PostgreSQL database and GPU processing for your machine learning model.

To summarize, both DLVM and DSVM can satisfy the requirements of using a PostgreSQL database and GPU processing for your machine learning model. You can choose the one that best suits your needs and preferences. 
Answer should be A I am updating the answer</p></blockquote>
<blockquote><p><strong>sar77</strong> <code>(Fri 25 Jul 2025 20:32)</code> - <em>Upvotes: 1</em></p><p>The Data Science Virtual Machine (DSVM) Windows edition is a solid choice for this scenario. It supports GPU-based processing when deployed on an appropriate N-series VM SKU, and while PostgreSQL is not preinstalled, it can be easily added manually — which is acceptable in this context since the recommendation implies extensibility.

Why this recommendation satisfies the requirements:

DSVM includes deep learning frameworks (e.g., TensorFlow, PyTorch) and GPU drivers.

It can be deployed on GPU-enabled hardware for high-performance training.

PostgreSQL can be installed on Windows Server 2019, which is the base OS for DSVM.

DSVM is designed for flexible data science workloads, including custom setups.

So yes — this VM type meets both the GPU and PostgreSQL requirements when configured properly.</p></blockquote>
<blockquote><p><strong>sanctafrax</strong> <code>(Mon 03 Feb 2025 14:49)</code> - <em>Upvotes: 2</em></p><p>Question states &quot;built into it&quot;. 

DSVM windows does support PostgreSQL, but its not natively installed. therefore an out of the box DSVM windows install will not &quot;run&quot; PostgreSQL. Only DSVM ubuntu has it preinstalled. 

You can however install PostgreSQL, and it will work. But that is NOT what the question states.

https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/tools-included?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>astone42</strong> <code>(Mon 13 Jan 2025 10:50)</code> - <em>Upvotes: 1</em></p><p>The question specifically mentions &quot;necessary tools built into it&quot;, DSVM windows edition does not have PostgreSQL.</p></blockquote>
<blockquote><p><strong>Xsesi</strong> <code>(Mon 29 Jul 2024 11:31)</code> - <em>Upvotes: 1</em></p><p>I would stand for A since: firstly, DSVM Windows has pre-configured GPU Option; secondly, PostgreSQL can be installed and run on various operating systems, including Windows. And it&#x27;s possible to connect to a PostgreSQL server from the DSVM Windows edition.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 20 Oct 2023 09:24)</code> - <em>Upvotes: 2</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/tools-included?view=azureml-api-2#build-deep-learning-and-machine-learning-solutions</p></blockquote>
<blockquote><p><strong>eternaleclipse</strong> <code>(Tue 17 Oct 2023 12:30)</code> - <em>Upvotes: 3</em></p><p>This wasn&#x27;t in the exam study material</p></blockquote>
<blockquote><p><strong>daviduzo</strong> <code>(Tue 20 Jun 2023 16:12)</code> - <em>Upvotes: 1</em></p><p>Option A is correct/ DSVM windows edition certifies the requirements</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Sat 27 May 2023 18:12)</code> - <em>Upvotes: 4</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/tools-included?view=azureml-api-2
Postgress is not available for windows edition, Please check the link . Answer should be B</p></blockquote>
<blockquote><p><strong>Truman</strong> <code>(Tue 04 Apr 2023 09:59)</code> - <em>Upvotes: 1</em></p><p>The Windows edition of the Data Science Virtual Machine (DSVM) does not come with GPU support by default. If you need GPU processing for your machine learning workload, you should choose the Linux edition of the DSVM, which comes with NVIDIA GPU drivers pre-installed. The Linux edition of the DSVM is designed for data science workloads that require GPU processing and includes a variety of pre-installed tools and libraries that can be useful for machine learning workloads.</p></blockquote>
<blockquote><p><strong>rashjan</strong> <code>(Fri 19 May 2023 14:50)</code> - <em>Upvotes: 1</em></p><p>&quot;The Windows editions of the DSVM come preinstalled with GPU drivers, frameworks, and GPU versions of deep learning frameworks. On the Linux editions, deep learning on GPUs is enabled on the Ubuntu DSVMs.&quot;
https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>emmanuelodenyire</strong> <code>(Tue 31 Jan 2023 07:54)</code> - <em>Upvotes: 4</em></p><p>I know most of the people will choose B, but for me I will stand with a Yes.
My choice: A
A Data Science Virtual Machine (DSVM) is a pre-configured virtual machine image on Microsoft Azure that is equipped with a comprehensive set of tools that are commonly used in data science and deep learning, including a GPU-enabled version. The Windows edition of the DSVM includes PostgreSQL, making it a suitable choice for the task of running a machine learning model that requires a PostgreSQL database and GPU processing to forecast prices. Therefore, the recommendation to use a DSVM Windows edition will satisfy the requirements.</p></blockquote>
<blockquote><p><strong>victorafb</strong> <code>(Thu 06 Oct 2022 02:12)</code> - <em>Upvotes: 3</em></p><p>I&#x27;ts corret guys, if as our colleague said that PostgreeSQL is avaliable in linux, this schema shows that is also avaliable in Windows DSVM.
https://azure.microsoft.com/en-us/products/virtual-machines/data-science-virtual-machines/#product-overview</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Tue 14 Jun 2022 17:34)</code> - <em>Upvotes: 4</em></p><p>PostgreSQL only mentioned in Linux VM, at least per documentation ...
It should be B</p></blockquote>
<blockquote><p><strong>exnaniantwort</strong> <code>(Sat 17 Sep 2022 04:05)</code> - <em>Upvotes: 3</em></p><p>nope

The Data Science Virtual Machine (DSVM) is a customized VM image on the Azure cloud platform built specifically for doing data science. It has many popular data science tools preinstalled and pre-configured to jump-start building intelligent applications for advanced analytics.

The DSVM is available on:

Windows Server 2019
Ubuntu 18.04 LTS
Ubuntu 20.04 LTS

https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview</p></blockquote>
<blockquote><p><strong>SweetChilliPhilly</strong> <code>(Thu 10 Nov 2022 22:29)</code> - <em>Upvotes: 3</em></p><p>Sure it has many popular data science tools but does it have anything that can access a PostgreSQL database preinstalled? The linux one does.</p></blockquote>
<blockquote><p><strong>peppertool</strong> <code>(Sun 22 May 2022 21:57)</code> - <em>Upvotes: 3</em></p><p>Should be deep learning virtual machine linux edition</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Wed 13 Apr 2022 03:38)</code> - <em>Upvotes: 1</em></p><p>Answer is correct. Refer to:
https://azuremarketplace.microsoft.com/en-ca/marketplace/apps/microsoft-dsvm.dsvm-win-2019?tab=Overview</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Sun 30 Jan 2022 15:26)</code> - <em>Upvotes: 4</em></p><p>B. It should be DSVM Linux edition</p></blockquote>

</details>

---

[<< Previous Question](question_9.md) | [Home](/index.md) | [Next Question >>](question_11.md)
