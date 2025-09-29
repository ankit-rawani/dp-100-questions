# Question 59

HOTSPOT -

You are retrieving data from a large datastore by using Azure Machine Learning Studio.

You must create a subset of the data for testing purposes using a random sampling seed based on the system clock.

You add the Partition and Sample module to your experiment.

You need to select the properties for the module.

Which values should you select? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q59_q_0007200001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q59_ans_0_0007300001.png" alt="Answer Image"><br>

<p>Box 1: Sampling -</p>
<p>Create a sample of data -</p>
<p>This option supports simple random sampling or stratified random sampling. This is useful if you want to create a smaller representative sample dataset for testing.</p>
<p>1. Add the Partition and Sample module to your experiment in Studio, and connect the dataset.</p>
<p>2. Partition or sample mode: Set this to Sampling.</p>
<p>3. Rate of sampling. See box 2 below.</p>
<p>Box 2: 0 -</p>
<p>3. Rate of sampling. Random seed for sampling: Optionally, type an integer to use as a seed value.</p>
<p>This option is important if you want the rows to be divided the same way every time. The default value is 0, meaning that a starting seed is generated based on the system clock. This can lead to slightly different results each time you run the experiment.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/partition-and-sample</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>BilJon</strong> <code>(Mon 28 Mar 2022 17:45)</code> - <em>Upvotes: 22</em></p><p>Random seed for sampling: Optionally, type an integer to use as a seed value.

This option is important if you want the rows to be divided the same way every time. The default value is 0, meaning that a starting seed is generated based on the system clock. This can lead to slightly different results each time you run the experiment.

https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/partition-and-sample</p></blockquote>

<blockquote><p><strong>David_Tadeu</strong> <code>(Wed 22 Mar 2023 14:42)</code> - <em>Upvotes: 10</em></p><p>So they just had the option time.clock() to trick us into failing?</p></blockquote>
<blockquote><p><strong>Hisayuki</strong> <code>(Sun 03 Nov 2024 09:22)</code> - <em>Upvotes: 1</em></p><p>time.clock() - Trick us. Microsoft learning says &quot;This option is important if you want the rows to be divided the same way every time. The default value is 0, meaning that a starting seed is generated based on the system clock.&quot;</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Thu 11 May 2023 11:45)</code> - <em>Upvotes: 2</em></p><p>correct! 0 --&gt; system clock, random sampling not stratified sampling</p></blockquote>
<blockquote><p><strong>dzzz</strong> <code>(Wed 15 Dec 2021 12:40)</code> - <em>Upvotes: 5</em></p><p>The question says &quot;a random sampling seed based on the system clock&quot;. 
I believe that implies the 2nd drop down is time.clock() - machine time.</p></blockquote>
<blockquote><p><strong>damirbek369</strong> <code>(Mon 20 Dec 2021 12:17)</code> - <em>Upvotes: 17</em></p><p>I think, &quot;0&quot; is a correct answer. Because the value to enter should be an integer. And look here as well: Random seed for sampling: Optionally, enter an integer to use as a seed value.

This option is important if you want the rows to be divided the same way every time. The default value is 0, meaning that a starting seed is generated based on the system clock. This value can lead to slightly different results each time you run the pipeline.

https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/partition-and-sample</p></blockquote>

<blockquote><p><strong>synapse</strong> <code>(Mon 13 Mar 2023 11:24)</code> - <em>Upvotes: 6</em></p><p>there&#x27;s no such option as time.clock(). 0 is the correct answer.</p></blockquote>

</details>

---

[<< Previous Question](question_58.md) | [Home](../index.md) | [Next Question >>](question_60.md)
