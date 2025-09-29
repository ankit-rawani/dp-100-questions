# Question 67

HOTSPOT -

You create an Azure Machine Learning compute target named ComputeOne by using the STANDARD_D1 virtual machine image.

ComputeOne is currently idle and has zero active nodes.

You define a Python variable named ws that references the Azure Machine Learning workspace. You run the following Python code:

![Question Image](images/q67_q_0008300001.png)

For each of the following statements, select Yes if the statement is true. Otherwise, select No.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q67_q_0008300002.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q67_ans_0_image598.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>dev2dev</strong> <code>(Mon 15 Mar 2021 08:57)</code> - <em>Upvotes: 103</em></p><p>Correct answers are No, Yes, Yes</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Tue 06 Jul 2021 05:39)</code> - <em>Upvotes: 3</em></p><p>I completely agree, because the exception will not be generated and the code inside this block (exception) will not be executed.</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Thu 24 Jun 2021 19:04)</code> - <em>Upvotes: 7</em></p><p>yes given answer is wrong and correct answer is NO Yes Yes</p></blockquote>
<blockquote><p><strong>Bridgerton</strong> <code>(Mon 18 Apr 2022 16:53)</code> - <em>Upvotes: 7</em></p><p>Agreed, the code given actually represents the compute creation, if there was no computeOne then the code will create one but as in this case there is already a computeOne, Exception block will not be executed</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Sat 30 Oct 2021 08:08)</code> - <em>Upvotes: 11</em></p><p>Tried the code and the answers &quot;No, Yes, Yes&quot; CONFIRMED</p></blockquote>
<blockquote><p><strong>f11c733</strong> <code>(Sun 16 Jun 2024 06:41)</code> - <em>Upvotes: 1</em></p><p>The answer is incorrect. No, yes, yes is correct because Compute 1 already exists</p></blockquote>
<blockquote><p><strong>Nadine_nm</strong> <code>(Wed 23 Aug 2023 23:20)</code> - <em>Upvotes: 1</em></p><p>In the first line of the code : 
try : 
      .......
       print(&#x27;Step1&#x27;)
We are checking if the compute already exists or not. Since it has been created the print will work, and so the &quot;exception&quot;  sequence won&#x27;t be executed. 
the fact that the cluster is not running, will not delete it. 

Answer should ben then, No, Yes, Yes.</p></blockquote>
<blockquote><p><strong>jpalaci22</strong> <code>(Mon 20 Feb 2023 21:10)</code> - <em>Upvotes: 4</em></p><p>Seen on the exam 20Feb2023</p></blockquote>
<blockquote><p><strong>MansoorDataScientist</strong> <code>(Thu 26 Jan 2023 16:44)</code> - <em>Upvotes: 2</em></p><p>NO,YES,YES</p></blockquote>
<blockquote><p><strong>Arend78</strong> <code>(Wed 07 Dec 2022 14:46)</code> - <em>Upvotes: 2</em></p><p>I agree with the majority saying &quot;Correct answer = No, Yes, Yes&quot;
I believe &quot;idle&quot; does not mean offline or non-existent, just &quot;not busy&quot;</p></blockquote>
<blockquote><p><strong>azurelearner666</strong> <code>(Sun 10 Apr 2022 14:30)</code> - <em>Upvotes: 1</em></p><p>Wrong,
Should be Yes Yes Yes.
My criteria for the first one is that the compute resource is created, that is the cluster, with a vm size of DS12_v2 and max 4 nodes.

This compute resource is the cluster definition, not the VM&#x27;s which are created while used.
But, the cluster definition, the Machine Learning Compute Resource IS CREATED.

So, Yes, Yes and Yes.</p></blockquote>
<blockquote><p><strong>DingDongSingSong</strong> <code>(Thu 31 Mar 2022 16:28)</code> - <em>Upvotes: 1</em></p><p>Why is the first answer No, and the second answer Yes?</p></blockquote>
<blockquote><p><strong>adamwar</strong> <code>(Mon 25 Oct 2021 12:41)</code> - <em>Upvotes: 3</em></p><p>Correct answer No, Yes, Yes

You can test this yourself by making a cluster (cpu-cluster) which can scale to zero nodes then running the code below:

from azureml.core.compute import ComputeTarget
from azureml.core.compute_target import ComputeTargetException

cluster_name = &quot;cpu-cluster&quot;

try:
    the_cluster = ComputeTarget(ws, name=cluster_name)
    print(&quot;Cluster with zero nodes ready to use&quot;)
except ComputeTargetException:
    print(&quot;Failed to reference cluster with zero nodes&quot;)</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Oct 2021 09:41)</code> - <em>Upvotes: 1</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Sun 03 Oct 2021 20:48)</code> - <em>Upvotes: 1</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Fri 03 Sep 2021 07:24)</code> - <em>Upvotes: 1</em></p><p>on exam 2/9/21</p></blockquote>
<blockquote><p><strong>datamijn</strong> <code>(Mon 02 Aug 2021 08:41)</code> - <em>Upvotes: 2</em></p><p>on 2/8/2021</p></blockquote>
<blockquote><p><strong>Rosh4yuh</strong> <code>(Sat 17 Jul 2021 12:51)</code> - <em>Upvotes: 5</em></p><p>on 17/7/2021

Answers are No, Yes, Yes</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Sun 11 Jul 2021 13:51)</code> - <em>Upvotes: 2</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>LVV1</strong> <code>(Fri 02 Jul 2021 00:06)</code> - <em>Upvotes: 1</em></p><p>Does the STANDARD_D1 virtual machine image even exist?
&quot;ComputeOne is currently idle and has zero active nodes&quot; - can it mean that it WAS created but has an issue with &quot;unsupported configuration values&quot;? Thanks</p></blockquote>

</details>

---

[<< Previous Question](question_66.md) | [Home](/index.md) | [Next Question >>](question_68.md)
