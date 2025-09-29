# Question 55

You plan to use a Data Science Virtual Machine (DSVM) with the open source deep learning frameworks Caffe2 and PyTorch.

You need to select a pre-configured DSVM to support the frameworks.

What should you create?

- A.Data Science Virtual Machine for Windows 2012
- B.Data Science Virtual Machine for Linux (CentOS)
- C.Geo AI Data Science Virtual Machine with ArcGIS
- D.Data Science Virtual Machine for Windows 2016
- E.Data Science Virtual Machine for Linux (Ubuntu)

<details>
  <summary>Show Suggested Answer</summary>

<strong>E</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>James_James</strong> <code>(Thu 19 Nov 2020 22:14)</code> - <em>Upvotes: 13</em></p><p>They are on the list https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-tools-deep-learning-frameworks</p></blockquote>
<blockquote><p><strong>HkIsCrazY</strong> <code>(Fri 06 Aug 2021 06:59)</code> - <em>Upvotes: 7</em></p><p>Thus, answer &quot;E&quot; is correct</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Wed 21 Aug 2024 05:48)</code> - <em>Upvotes: 2</em></p><p>Deep Learning must be performed on Linux system and Ubuntu is natural choice.</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Sat 19 Aug 2023 20:09)</code> - <em>Upvotes: 4</em></p><p>Ubuntu is legendary for everything</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 02 Aug 2023 03:09)</code> - <em>Upvotes: 1</em></p><p>E. Data Science Virtual Machine for Linux (Ubuntu) is the most accurate choice.

Justification: Both Caffe2 and PyTorch are widely used deep learning frameworks and are well supported on Linux platforms, particularly Ubuntu. The Data Science Virtual Machine for Linux (Ubuntu) is pre-configured with the necessary libraries, tools, and deep learning frameworks to help you get started quickly with your deep learning projects.

CentOS is a stable and reliable Linux distribution, but it may not have the latest version of Caffe2 or PyTorch, or the necessary dependencies to run them. Windows Server operating systems such as Windows 2012 and Windows 2016 are not as commonly used for deep learning and may not have the necessary support for these frameworks. The Geo AI Data Science Virtual Machine with ArcGIS is a specialized DSVM specifically designed for geospatial data and may not include support for Caffe2 and PyTorch.</p></blockquote>

<blockquote><p><strong>MansoorDataScientist</strong> <code>(Wed 26 Jul 2023 14:14)</code> - <em>Upvotes: 1</em></p><p>The DSVM is available on:

Windows Server 2019
Ubuntu 20.04 LTS</p></blockquote>

<blockquote><p><strong>racnaoamo</strong> <code>(Sat 19 Nov 2022 08:42)</code> - <em>Upvotes: 1</em></p><p>similar question on 18-5-22</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Fri 09 Sep 2022 20:49)</code> - <em>Upvotes: 2</em></p><p>On march-9-2022</p></blockquote>
<blockquote><p><strong>ashii007</strong> <code>(Sat 25 Jun 2022 20:40)</code> - <em>Upvotes: 1</em></p><p>A-D are wrong. None of the OS mentioned in options A-D are supported.</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Fri 29 Oct 2021 20:38)</code> - <em>Upvotes: 3</em></p><p>Has anyone seen this question asked recently. It seems like out of scope based on https://query.prod.cms.rt.microsoft.com/cms/api/am/binary/RE3VUjA</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Tue 30 Nov 2021 21:41)</code> - <em>Upvotes: 4</em></p><p>caffe is outdated and is replaced by pytorch which is available on windows and linux. if the question was about horovod, then ubuntu would make sense</p></blockquote>
<blockquote><p><strong>sambis</strong> <code>(Sun 18 Jul 2021 04:38)</code> - <em>Upvotes: 2</em></p><p>Correct ans: D
Ref: https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/dsvm-tools-deep-learning-frameworks</p></blockquote>
<blockquote><p><strong>Srivathsan</strong> <code>(Fri 30 Jul 2021 05:18)</code> - <em>Upvotes: 14</em></p><p>From the same link, I am providing you the necessary proofs:
Caffe2 - Supported DSVM editions	Ubuntu 16.04
PyTorch - Supported DSVM editions	Windows Server 2019
Ubuntu 18.04
Ubuntu 16.04

And, DSVMs are available only in Windows Server 2019 and Linux(Ubuntu).
https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/overview

So, the answer is clearly E. Because DSVM don&#x27;t work in Windows Server 2012/2016 and CentOS is not supported, as per the documentation.</p></blockquote>

<blockquote><p><strong>ipindado2020</strong> <code>(Sat 08 May 2021 18:43)</code> - <em>Upvotes: 2</em></p><p>Agree with D
https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/tools-included</p></blockquote>
<blockquote><p><strong>111ssy</strong> <code>(Sat 05 Jun 2021 14:50)</code> - <em>Upvotes: 1</em></p><p>Your link specifically say that Caffe2 is not supported by Window...!!!! The answer is E</p></blockquote>
<blockquote><p><strong>Kamalraj</strong> <code>(Sun 14 Mar 2021 10:53)</code> - <em>Upvotes: 1</em></p><p>Caffe2 in Ubuntu 16.04 and PyTorch in Ubuntu 16.04 &amp; Ubuntu 18.04.</p></blockquote>
<blockquote><p><strong>Rajuuu</strong> <code>(Sun 07 Feb 2021 17:05)</code> - <em>Upvotes: 1</em></p><p>Correct answer should be Linux which is not in the option.
Link below points Cafffe2 to Linux and not UBUNTU.
https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/tools-included</p></blockquote>
<blockquote><p><strong>jkuz</strong> <code>(Sun 31 Jan 2021 11:19)</code> - <em>Upvotes: 3</em></p><p>List of supported configuration:
https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/tools-included</p></blockquote>
<blockquote><p><strong>Zhuo</strong> <code>(Sun 15 Nov 2020 13:20)</code> - <em>Upvotes: 1</em></p><p>The inccorecct answer &quot;D: Caffe2 and PytOCH are only supported in the Data Science Virtual Machine for Linux.&quot; is not in the list. Besides I thought if it is in the list, it should be the correct answer. Not E.</p></blockquote>

</details>

---

[<< Previous Question](question_54.md) | [Home](../index.md) | [Next Question >>](question_56.md)
