# Question 91

You create an Azure Machine Learning compute resource to train models. The compute resource is configured as follows:

✑ Minimum nodes: 2

✑ Maximum nodes: 4

You must decrease the minimum number of nodes and increase the maximum number of nodes to the following values:

✑ Minimum nodes: 0

✑ Maximum nodes: 8

You need to reconfigure the compute resource.

What are three possible ways to achieve this goal? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

- A.Use the Azure Machine Learning studio.
- B.Run the update method of the AmlCompute class in the Python SDK.
- C.Use the Azure portal.
- D.Use the Azure Machine Learning designer.
- E.Run the refresh_state() method of the BatchCompute class in the Python SDK.

<details>
  <summary>Show Suggested Answer</summary>

<strong>ABC</strong><br>

<p>A: You can manage assets and resources in the Azure Machine Learning studio.</p>
<p>B: The update(min_nodes=None, max_nodes=None, idle_seconds_before_scaledown=None) of the AmlCompute class updates the ScaleSettings for this</p>
<p>AmlCompute target.</p>
<p>C: To change the nodes in the cluster, use the UI for your cluster in the Azure portal.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.amlcompute(class)</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Haet</strong> <code>(Mon 25 Oct 2021 06:07)</code> - <em>Upvotes: 23</em></p><p>Answer is correct A,B,C. I have verified it</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Wed 27 Oct 2021 16:03)</code> - <em>Upvotes: 3</em></p><p>Can you elaborate on &quot;C&quot;. There is no access to the cluster from Azure portal. Where do you see it ?</p></blockquote>
<blockquote><p><strong>SaudMeethal</strong> <code>(Tue 09 Nov 2021 13:12)</code> - <em>Upvotes: 4</em></p><p>Azure portal is unlikely to do this and refresh_state() method of the BatchCompute also seems to be incorrect. In designer there is an option to create a new CC with the specifications we require, but not sure if it can be considered as reconfiguration as we&#x27;re simply creating another resource.</p></blockquote>
<blockquote><p><strong>levm39</strong> <code>(Wed 15 Dec 2021 10:54)</code> - <em>Upvotes: 17</em></p><p>Answer is A,B
C was possible in the past, they removed the option to manage compute instance for ML from the portal.

E is incorrect</p></blockquote>

<blockquote><p><strong>NullVoider_0</strong> <code>(Mon 12 Aug 2024 13:33)</code> - <em>Upvotes: 1</em></p><p>On exam 12-02-2024.</p></blockquote>
<blockquote><p><strong>Awooga</strong> <code>(Tue 06 Aug 2024 14:16)</code> - <em>Upvotes: 1</em></p><p>On exam 2024-02-06</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 05 Aug 2023 00:34)</code> - <em>Upvotes: 2</em></p><p>A. Use the Azure Machine Learning studio.
C. Use the Azure portal.
D. Use the Azure Machine Learning designer.</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sun 18 Dec 2022 02:39)</code> - <em>Upvotes: 1</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Wed 16 Nov 2022 18:31)</code> - <em>Upvotes: 2</em></p><p>Only know A and B ...</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Sat 22 Oct 2022 10:44)</code> - <em>Upvotes: 2</em></p><p>on exam 04/22/2022</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 13 Sep 2022 13:46)</code> - <em>Upvotes: 1</em></p><p>A  B  C. Given answer is correct</p></blockquote>
<blockquote><p><strong>piyu18</strong> <code>(Tue 05 Jul 2022 18:07)</code> - <em>Upvotes: 2</em></p><p>I think its correct, as we can access ml compute from cli and we can connect with cli from azure portal</p></blockquote>
<blockquote><p><strong>VJPrakash</strong> <code>(Fri 11 Feb 2022 17:20)</code> - <em>Upvotes: 1</em></p><p>on exam in August 2021</p></blockquote>
<blockquote><p><strong>slash_nyk</strong> <code>(Sat 25 Dec 2021 03:38)</code> - <em>Upvotes: 2</em></p><p>How you can do if from Machine Learning Studio ?</p></blockquote>
<blockquote><p><strong>scipio</strong> <code>(Tue 16 Nov 2021 16:37)</code> - <em>Upvotes: 4</em></p><p>Cannot be E. BatchCompute is an attach resource, and refresh_state() is &quot;This method updates the properties based on the current state of the corresponding cloud object. This is primarily used for manual polling of compute state.&quot; Just a refresh. 
I agree though that C is strange, except to use the portal to access the ML Studio.
https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.compute.batchcompute?view=azure-ml-py#refresh-state--</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Sat 23 Oct 2021 00:13)</code> - <em>Upvotes: 7</em></p><p>The correct answer is A, B and E. You cannot do it from portal.</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Fri 17 Sep 2021 05:38)</code> - <em>Upvotes: 5</em></p><p>I dont see from where we can resize the culuster size from portal except that from the ml workspace we click on studio link and change from there</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Fri 17 Sep 2021 05:36)</code> - <em>Upvotes: 2</em></p><p>I dont see from where we can resize the culuster size from portal except that from the workspace we click on studio link</p></blockquote>

</details>

---

[<< Previous Question](question_90.md) | [Home](../index.md) | [Next Question >>](question_92.md)
