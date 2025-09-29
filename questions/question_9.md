# Question 9

This question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the recommendation satisfies the requirements.

You have been tasked with employing a machine learning model, which makes use of a PostgreSQL database and needs GPU processing, to forecast prices.

You are preparing to create a virtual machine that has the necessary tools built into it.

You need to make use of the correct virtual machine type.

Recommendation: You make use of a Deep Learning Virtual Machine (DLVM) Windows edition.

Will the requirements be satisfied?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Matt2000</strong> <code>(Tue 14 Nov 2023 10:53)</code> - <em>Upvotes: 9</em></p><p>I tend to say &#x27;no&#x27; since Windows DSVMs (the closest matching VM currently available) does not support PostGreSQL on the VM itself: https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/tools-included?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>windy610</strong> <code>(Sun 19 Nov 2023 08:02)</code> - <em>Upvotes: 1</em></p><p>That is the point, so Ubuntu version must be a correct solution?</p></blockquote>
<blockquote><p><strong>Shyam_kishor</strong> <code>(Tue 11 Oct 2022 19:01)</code> - <em>Upvotes: 7</em></p><p>Answer is correct</p></blockquote>
<blockquote><p><strong>KeiNek</strong> <code>(Tue 11 Feb 2025 07:15)</code> - <em>Upvotes: 2</em></p><p>B
PostgreSQL : Ubuntu
https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/tools-included?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>ManuelHenriques</strong> <code>(Wed 05 Feb 2025 14:22)</code> - <em>Upvotes: 1</em></p><p>No. Need Ubuntu for PostgreSQL</p></blockquote>
<blockquote><p><strong>sanctafrax</strong> <code>(Mon 03 Feb 2025 14:47)</code> - <em>Upvotes: 2</em></p><p>DLVM is discontinued. This question is therefore outdated. 
If you&#x27;d go back in time when it was still relevant. answer would still be NO.

This because the question states &quot;built into it&quot;. DLVM does have GPU support, no problem. it does NOT have PostgreSQL natively installed. Not even in the current version of DSVM (windows). ONLY the ubuntu version has it preinstalled.

https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/tools-included?view=azureml-api-2

Therefore PostgreSQL questions and DLVM/DSVM answers IF &quot;built into it&quot; is asked, are by definition. no. You can however install PostgreSQL anyways, it will work. BUT that is not the question.</p></blockquote>

<blockquote><p><strong>emmanuelodenyire</strong> <code>(Thu 26 Sep 2024 10:00)</code> - <em>Upvotes: 3</em></p><p>I will also stand with a Yes.
A Deep Learning Virtual Machine (DLVM) is a pre-configured virtual machine image on Microsoft Azure that is optimized for training deep learning models and includes popular tools such as TensorFlow, PyTorch, and Caffe2. The DLVM Windows edition includes support for GPU processing, making it suitable for the task of running a machine learning model that requires GPU processing to forecast prices. Additionally, the DLVM can be configured to use PostgreSQL as the database, satisfying the requirement for a PostgreSQL database. Therefore, the recommendation to use a DLVM Windows edition will satisfy the requirements.</p></blockquote>
<blockquote><p><strong>Truman</strong> <code>(Thu 26 Sep 2024 10:00)</code> - <em>Upvotes: 2</em></p><p>. The Deep Learning Virtual Machine (DLVM) Windows edition comes with NVIDIA GPU drivers pre-installed, which means that it can support GPU processing out of the box. Additionally, the DLVM comes with a variety of pre-installed tools and libraries that can be useful for machine learning workloads, including support for popular deep learning frameworks such as TensorFlow and PyTorch. Therefore, the DLVM Windows edition can be a good choice for a machine learning workload that requires both a PostgreSQL database and GPU processing.</p></blockquote>
<blockquote><p><strong>Sa_Msa</strong> <code>(Thu 26 Sep 2024 10:00)</code> - <em>Upvotes: 1</em></p><p>The DLVM is a specially configured variant of the Data Science Virtual Machine (DSVM) that comes with pre-configured environments for developing and deploying deep learning models on GPU instances.

Regarding PostgreSQL, the DLVM (Deep Learning Virtual Machine) is a specially configured variant of the DSVM (Data Science Virtual Machine) that is custom made to help users jump-start deep learning on Azure GPU VMs2. The DLVM uses the same underlying VM images of the DSVM and hence comes with the same set of data science tools and deep learning frameworks as the base VM. So, you can have access to PostgreSQL .</p></blockquote>

<blockquote><p><strong>prabhjot</strong> <code>(Sat 27 Jan 2024 02:55)</code> - <em>Upvotes: 1</em></p><p>NO is Ans - as per chat GPT-
No, the recommendation to use a Deep Learning Virtual Machine (DLVM) Windows edition may not fully satisfy the requirements mentioned.

PostgreSQL is typically used on Linux-based systems, and GPU processing for machine learning is often better supported on Linux. The DLVM Windows edition may not be the most suitable choice for this scenario. Instead, you might want to consider a virtual machine with a Linux operating system that supports GPU acceleration and provides compatibility with PostgreSQL for your machine learning model.</p></blockquote>

<blockquote><p><strong>Vikyyy</strong> <code>(Sat 11 Nov 2023 04:53)</code> - <em>Upvotes: 1</em></p><p>The Windows editions of the DSVM come preinstalled with GPU drivers, frameworks, and GPU versions of deep learning frameworks. On the Linux editions, deep learning on GPUs is enabled on the Ubuntu DSVMs.

You can also deploy the Ubuntu or Windows editions of the DSVM to an Azure virtual machine that isn&#x27;t based on GPUs. In this case, all the deep learning frameworks falls back to the CPU mode.</p></blockquote>

<blockquote><p><strong>james2033</strong> <code>(Fri 20 Oct 2023 09:22)</code> - <em>Upvotes: 1</em></p><p>Question is obsoleted

https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview?view=azureml-api-2#whats-included-in-the-data-science-vm

DSVM https://azure.microsoft.com/en-us/products/virtual-machines/data-science-virtual-machines</p></blockquote>

<blockquote><p><strong>eternaleclipse</strong> <code>(Tue 17 Oct 2023 12:30)</code> - <em>Upvotes: 2</em></p><p>This wasn&#x27;t in the exam study material</p></blockquote>
<blockquote><p><strong>PradhanManva</strong> <code>(Sun 24 Sep 2023 18:10)</code> - <em>Upvotes: 1</em></p><p>This is the answer.</p></blockquote>
<blockquote><p><strong>chen7777</strong> <code>(Sun 17 Sep 2023 19:50)</code> - <em>Upvotes: 1</em></p><p>B. No.  Not all configurations of the Deep Learning Virtual Machine (DLVM) come with GPU hardware as a default or built-in feature. DLVMs are designed to cater to a wide range of machine learning and deep learning workloads, and some configurations may be GPU-enabled, while others may not.

If you require GPU acceleration for tasks like deep learning models or other GPU-intensive computations, you would need to choose a specific DLVM configuration that includes GPU resources or add GPU hardware to the virtual machine separately. This ensures that your virtual machine has the necessary GPU processing power to handle such workloads efficiently.</p></blockquote>

<blockquote><p><strong>phydev</strong> <code>(Thu 20 Jul 2023 07:26)</code> - <em>Upvotes: 2</em></p><p>Yes, because DLVM is a modified DSVM.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sun 26 Feb 2023 04:00)</code> - <em>Upvotes: 2</em></p><p>B. No.

The recommendation to use a Deep Learning Virtual Machine (DLVM) Windows edition is not suitable for the given requirements because it is designed for Windows-based deep learning tasks and does not support GPU processing for PostgreSQL databases.

Instead, a suitable virtual machine for this task would be one that supports GPU processing and has the necessary tools and libraries for machine learning and PostgreSQL database management. One such option is the Data Science Virtual Machine (DSVM), which is available for both Windows and Linux operating systems and has support for GPU processing and machine learning tools, including TensorFlow, PyTorch, and scikit-learn.</p></blockquote>

<blockquote><p><strong>mamau</strong> <code>(Sun 12 Feb 2023 07:11)</code> - <em>Upvotes: 1</em></p><p>No is the answer ,it would be DSVM</p></blockquote>

</details>

---

[<< Previous Question](question_8.md) | [Home](../index.md) | [Next Question >>](question_10.md)
