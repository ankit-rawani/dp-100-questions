# Question 51

You are implementing a machine learning model to predict stock prices.

The model uses a PostgreSQL database and requires GPU processing.

You need to create a virtual machine that is pre-configured with the required tools.

What should you do?

* A.Create a Data Science Virtual Machine (DSVM) Windows edition.
* B.Create a Geo Al Data Science Virtual Machine (Geo-DSVM) Windows edition.
* C.Create a Deep Learning Virtual Machine (DLVM) Linux edition.
* D.Create a Deep Learning Virtual Machine (DLVM) Windows edition.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Avii123</strong> <code>(Mon 24 May 2021 16:06)</code> - <em>Upvotes: 27</em></p><p>Correct answer is DSVM on Linux as postgreSQL is only supported on Linux VMS.
https://docs.microsoft.com/en-us/azure/virtual-machines/linux/postgresql-install</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Wed 03 Nov 2021 20:53)</code> - <em>Upvotes: 13</em></p><p>I think that correct answer is A. I think this is a trick question. Option C and D are not even a valid option. Most people are reading it as &quot;DSVM linux edition&quot; while it is &quot;DLVM&quot; (not DSVM). There is almost no mention on DLVM anywhere in Azure docs. If there was an option called DSVM Linux edition, then that would have been the correct answer. The correct answer to this question is DVSM linux or windows edition.</p></blockquote>
<blockquote><p><strong>Rdninja</strong> <code>(Tue 01 Aug 2023 10:43)</code> - <em>Upvotes: 1</em></p><p>DLVM is a specialized version of DSVM optimized for Deep Learning. DSVM for Windows doesn&#x27;t come pre-configured with Postgres and I am unsure if it is supported.</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Sat 20 Nov 2021 21:12)</code> - <em>Upvotes: 2</em></p><p>pgsql is supported on windows and linux. https://www.postgresqltutorial.com/install-postgresql/</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Thu 10 Feb 2022 00:45)</code> - <em>Upvotes: 4</em></p><p>But isn&#x27;t DSVM Windows edition pre-configured.</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Sat 07 Dec 2024 23:10)</code> - <em>Upvotes: 2</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/tools-included?view=azureml-api-2#build-deep-learning-and-machine-learning-solutions</p></blockquote>
<blockquote><p><strong>Vikyyy</strong> <code>(Wed 22 May 2024 05:17)</code> - <em>Upvotes: 1</em></p><p>Some places it says DSVM windows doesn&#x27;t  support Postgres but Chat GPT says  &quot;PostgreSQL can run on any system, including both Windows and Linux, so it doesn’t affect the choice here.&quot;   I believe DLVM LInux or WInsdows DSVM are correct .</p></blockquote>
<blockquote><p><strong>ABosco</strong> <code>(Sat 17 Feb 2024 09:52)</code> - <em>Upvotes: 1</em></p><p>DSVM supports PostgreSQL. So the answer is A. Link below:
https://learn.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/linux-dsvm-walkthrough?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>BR_CS</strong> <code>(Sun 18 Feb 2024 14:18)</code> - <em>Upvotes: 2</em></p><p>PostgreSQL in your link is only mentioned for Linux</p></blockquote>
<blockquote><p><strong>daviduzo</strong> <code>(Thu 21 Dec 2023 10:20)</code> - <em>Upvotes: 1</em></p><p>The answer should be DSVM Linux edition. The Windows DSVM doesn&#x27;t come pre-configured with Postgres. Man these options should be updated, I doubt the exam would exclude the DSVM Linux edition. C and D are not even correct either and B isn&#x27;t useful here.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 02 Aug 2023 02:20)</code> - <em>Upvotes: 5</em></p><p>Moderator should provide correct answers! Answers are mess in this portal!
C. Create a Deep Learning Virtual Machine (DLVM) Linux edition. DLVM is pre-configured with tools such as CUDA and cuDNN for GPU processing, and it is optimized for deep learning workloads. Additionally, DLVM supports PostgreSQL, which is required for the stock price prediction model. The Linux edition of DLVM would provide a cost-effective and reliable environment for running the GPU-intensive machine learning workloads.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 11 Nov 2022 12:25)</code> - <em>Upvotes: 4</em></p><p>Only Windows and Linux Ubuntu two options when talking about machine / deep learning VMs; unless very specific MS / Windows products, e.g., SQL Server, otherwise always select Linux Ubuntu as your answer</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Sun 11 Jun 2023 17:22)</code> - <em>Upvotes: 1</em></p><p>Agree - C</p></blockquote>
<blockquote><p><strong>DingDongSingSong</strong> <code>(Fri 30 Sep 2022 02:21)</code> - <em>Upvotes: 2</em></p><p>According to this link: https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/linux-dsvm-walkthrough

DSVM on Linux has PostgreSQL preinstalled. Windows does not. So the answer is C even though it says DLVM (which is nothing but a variation of DSVM with GPU, which is also the requirement per the question)</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Sun 06 Feb 2022 19:48)</code> - <em>Upvotes: 2</em></p><p>Question #10 in next page is about DLVM. So the correct answer is C, because DSVM for Windows doesn&#x27;t have pre-configured PostgreSQL. DLVM (DSVM framework) for Linux have pre-configured PostgreSQL.</p></blockquote>
<blockquote><p><strong>thhvancouver</strong> <code>(Mon 31 Jan 2022 11:21)</code> - <em>Upvotes: 2</em></p><p>Windows DSVM appears to be correct: https://medium.com/@Hackyroot/azure-deep-learning-a7c1953e2542</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Fri 07 Jan 2022 04:45)</code> - <em>Upvotes: 1</em></p><p>I believe the correct answer is C. Because the Microsoft documents don&#x27;t mention PostgreSQL for DSVM for Windows. Just compare: 
https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/vm-do-ten-things
https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/linux-dsvm-walkthrough</p></blockquote>
<blockquote><p><strong>Akki0120</strong> <code>(Tue 04 Jan 2022 17:03)</code> - <em>Upvotes: 3</em></p><p>If anyone wants all questions ping me 9403778084</p></blockquote>
<blockquote><p><strong>Frank90T</strong> <code>(Wed 27 Apr 2022 17:47)</code> - <em>Upvotes: 1</em></p><p>Please</p></blockquote>
<blockquote><p><strong>cccwahtever</strong> <code>(Fri 15 Jul 2022 06:34)</code> - <em>Upvotes: 1</em></p><p>Thanks a lot!</p></blockquote>
<blockquote><p><strong>luisdanielse</strong> <code>(Wed 04 Aug 2021 19:42)</code> - <em>Upvotes: 4</em></p><p>Postgress is not available on DSVM windows.
I&#x27;d go for C.
Actually, another question on this set is related to postgress-Windows. The explanation on this other question is that Postgress cannot be used with windows vm</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Thu 09 Sep 2021 08:08)</code> - <em>Upvotes: 1</em></p><p>postgress cant be used with windows is a joke.</p></blockquote>
<blockquote><p><strong>treadst0ne</strong> <code>(Mon 23 Aug 2021 16:03)</code> - <em>Upvotes: 4</em></p><p>I think a Deep Learning Virtual Machine is not available anymore. Only option is DSVM.</p></blockquote>
<blockquote><p><strong>vippi66</strong> <code>(Sat 14 Aug 2021 08:47)</code> - <em>Upvotes: 2</em></p><p>totally agree!</p></blockquote>
<blockquote><p><strong>Srivathsan</strong> <code>(Fri 30 Jul 2021 03:54)</code> - <em>Upvotes: 7</em></p><p>To all who feel confused, refer the below docs:
https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview

It clearly states the DSVM windows edition means Windows Server 2019. Hence we shall say Option A is correct here. 
DSVM has GPU enabled [Refer &quot;Deep learning with GPUs&quot; section in the docs link] 

As per the Docs:
&quot;The Windows editions of the DSVM come pre-installed with GPU drivers, frameworks, and GPU versions of deep learning frameworks. On the Linux editions, deep learning on GPUs is enabled on the Ubuntu DSVMs.&quot;</p></blockquote>
<blockquote><p><strong>DingDongSingSong</strong> <code>(Fri 30 Sep 2022 02:22)</code> - <em>Upvotes: 1</em></p><p>Sorry, not correct. The requirement is for GPU + PostgreSQL. Both of those are available on DSVM on Linux, not on Windows. Answer is C</p></blockquote>
<blockquote><p><strong>nepketo</strong> <code>(Mon 07 Jun 2021 05:30)</code> - <em>Upvotes: 6</em></p><p>The answer is C since we need Deep Learning VM for GPU capability and Linux to support PostgreSQL.</p></blockquote>
<blockquote><p><strong>ipindado2020</strong> <code>(Sat 08 May 2021 18:29)</code> - <em>Upvotes: 1</em></p><p>Agree with A:
B-&gt;  Customized for Geospatial Analytics
C &amp; D-&gt; Customized for Deep Learning (DLVM)</p></blockquote>

</details>

---

[<< Previous Question](question_50.md) | [Home](/index.md) | [Next Question >>](question_52.md)
