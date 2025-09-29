# Question 64

HOTSPOT -

A coworker registers a datastore in a Machine Learning services workspace by using the following code:

![Question Image](../images/q64_q_0007700001.png)

You need to write code to access the datastore from a notebook.

How should you complete the code segment? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q64_q_0007800001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q64_ans_0_0007800002.png" alt="Answer Image"><br>

<p>Box 1: DataStore -</p>
<p>To get a specific datastore registered in the current workspace, use the get() static method on the Datastore class:</p>
<p># Get a named datastore from the current workspace</p>
<p>datastore = Datastore.get(ws, datastore_name=&#x27;your datastore name&#x27;)</p>
<p>Box 2: ws -</p>
<p>Box 3: demo_datastore -</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-access-data</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Lucario95</strong> <code>(Sun 14 Nov 2021 16:08)</code> - <em>Upvotes: 14</em></p><p>Seems correct</p></blockquote>
<blockquote><p><strong>MattAnya</strong> <code>(Tue 04 Jul 2023 05:36)</code> - <em>Upvotes: 10</em></p><p>0n 03 Jan2023</p></blockquote>
<blockquote><p><strong>thisiston</strong> <code>(Sat 02 Nov 2024 22:25)</code> - <em>Upvotes: 1</em></p><p>Correct answer is: &#x27;Datastore&#x27;, &#x27;ws&#x27;, &#x27;blob_datastore_name&#x27;
Ex:blob_datastore = Datastore.get(ws, blob_datastore_name)
Link: https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.datastore.datastore?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>k1ngs1zed</strong> <code>(Mon 17 Oct 2022 11:33)</code> - <em>Upvotes: 1</em></p><p>answer is correct</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Sun 03 Apr 2022 20:24)</code> - <em>Upvotes: 2</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Thu 03 Mar 2022 08:23)</code> - <em>Upvotes: 1</em></p><p>on exam 2/9/21</p></blockquote>
<blockquote><p><strong>datamijn</strong> <code>(Wed 02 Feb 2022 09:40)</code> - <em>Upvotes: 2</em></p><p>on 2/8/2021</p></blockquote>
<blockquote><p><strong>Rosh4yuh</strong> <code>(Mon 17 Jan 2022 13:50)</code> - <em>Upvotes: 4</em></p><p>on 17/7/2021

Answer is correct</p></blockquote>

<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 14:50)</code> - <em>Upvotes: 2</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>okeyken1</strong> <code>(Sat 18 Dec 2021 15:27)</code> - <em>Upvotes: 4</em></p><p>yes correct</p></blockquote>

</details>

---

[<< Previous Question](question_63.md) | [Home](../index.md) | [Next Question >>](question_65.md)
