# Question 151

You create an Azure Machine Learning managed compute resource. The compute resource is configured as follows:

• Minimum nodes: 2

• Maximum nodes: 4

You must decrease the minimum number of nodes and increase the maximum number of nodes to the following values:

• Minimum nodes: 0

• Maximum nodes: 8

You need to reconfigure the compute resource.

Which three methods can you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- A.Azure Machine Learning designer
- B.MLClient class in Python SDK v2
- C.Azure Machine Learning studio
- D.Azure CLI ml extension v2
- E.BuildContext class in Python SDK v2

<details>
  <summary>Show Suggested Answer</summary>

<strong>BCD</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>umair_hanu</strong> <code>(Wed 10 Jan 2024 07:25)</code> - <em>Upvotes: 7</em></p><p>BCD should be the answer.</p></blockquote>
<blockquote><p><strong>Techlover74</strong> <code>(Sun 18 Aug 2024 03:57)</code> - <em>Upvotes: 1</em></p><p>BCD is the answer.</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Sun 16 Jun 2024 11:09)</code> - <em>Upvotes: 2</em></p><p>You cannot scale the instances from the AML Designer.</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Tue 28 May 2024 11:07)</code> - <em>Upvotes: 1</em></p><p>BCD should be the answer.</p></blockquote>
<blockquote><p><strong>Hisayuki</strong> <code>(Sun 05 May 2024 01:53)</code> - <em>Upvotes: 2</em></p><p>The compute autoscales down to zero nodes when it isn&#x27;t used. Dedicated VMs are created to run your jobs as needed. Use the following examples to create a compute cluster:
- Python SDK
- Azure CLI
- Studio

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-attach-compute-cluster?view=azureml-api-2&amp;tabs=python#create</p></blockquote>

<blockquote><p><strong>cyberfriends</strong> <code>(Sat 20 Apr 2024 20:22)</code> - <em>Upvotes: 1</em></p><p>ABD is the answer</p></blockquote>
<blockquote><p><strong>ABosco</strong> <code>(Sun 18 Feb 2024 12:40)</code> - <em>Upvotes: 2</em></p><p>BCD is correct</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 26 Jan 2024 17:25)</code> - <em>Upvotes: 1</em></p><p>I presume Azure ML studio is correct as well, however, since we have only 3 choices, maybe we need to choose the closet ones! :)</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Tue 28 May 2024 11:08)</code> - <em>Upvotes: 2</em></p><p>wrong answer... BCD is correct sorry...

I tested it, you can&#x27;t change it with designer</p></blockquote>

<blockquote><p><strong>damaldon</strong> <code>(Fri 12 Jan 2024 20:23)</code> - <em>Upvotes: 1</em></p><p>ACD is correct</p></blockquote>

</details>

---

[<< Previous Question](question_150.md) | [Home](../index.md) | [Next Question >>](question_152.md)
