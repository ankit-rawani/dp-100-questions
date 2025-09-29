# Question 40

This question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the recommendation satisfies the requirements.

You are planning to make use of Azure Machine Learning designer to train models.

You need choose a suitable compute type.

Recommendation: You choose Attached compute.

Will the requirements be satisfied?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>dushmantha</strong> <code>(Mon 30 Aug 2021 10:12)</code> - <em>Upvotes: 13</em></p><p>Should be True. Because we can use databricks or vm as attached compute for training purposes</p></blockquote>
<blockquote><p><strong>beny</strong> <code>(Mon 06 Sep 2021 19:12)</code> - <em>Upvotes: 5</em></p><p>Agree, Yes is the correct answer</p></blockquote>
<blockquote><p><strong>[Removed]</strong> <code>(Sun 01 May 2022 08:09)</code> - <em>Upvotes: 10</em></p><p>No, unforunately only AML Compute cluster or AML compute instance can be used in designer according to :

https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target</p></blockquote>

<blockquote><p><strong>Gabonia</strong> <code>(Fri 19 Aug 2022 14:30)</code> - <em>Upvotes: 3</em></p><p>I agree</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 17 Jun 2022 10:44)</code> - <em>Upvotes: 5</em></p><p>Designer!  Only computer instance or computer cluster</p></blockquote>
<blockquote><p><strong>azayra</strong> <code>(Thu 28 Oct 2021 14:03)</code> - <em>Upvotes: 8</em></p><p>Azure Machine Learning designer to train models. its the key so answer is compute cluster.</p></blockquote>
<blockquote><p><strong>testgm</strong> <code>(Thu 14 Nov 2024 16:09)</code> - <em>Upvotes: 1</em></p><p>Attached compute is already supported by Azure Machine Learning Designer</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Fri 07 Jun 2024 16:28)</code> - <em>Upvotes: 2</em></p><p>There are now 5 tabs in compute, and &quot;Attached computes&quot; is one of them. When you configure &amp; submit a pipeline job, you can choose attached compute.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 01 Aug 2023 02:25)</code> - <em>Upvotes: 1</em></p><p>A-Yes is answer</p></blockquote>
<blockquote><p><strong>SunilB</strong> <code>(Fri 10 Mar 2023 16:47)</code> - <em>Upvotes: 5</em></p><p>We can use attached compute. Just tried it</p></blockquote>
<blockquote><p><strong>SunilB</strong> <code>(Sun 05 Mar 2023 14:21)</code> - <em>Upvotes: 5</em></p><p>Correct Answer: B
See the blue box in the link below which says &#x27;Attached compute is not supported, use compute instances or clusters instead.&#x27;
https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-designer-automobile-price-train-score</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 01 Feb 2023 21:33)</code> - <em>Upvotes: 1</em></p><p>It is not possible to determine whether the requirements will be satisfied based on the information provided. The recommendation to choose Attached compute is a specific solution, but the requirements are not stated. It is important to have a clear understanding of the requirements and constraints before making a decision on which compute type to use in Azure Machine Learning Designer.</p></blockquote>
<blockquote><p><strong>Starlite</strong> <code>(Tue 24 Jan 2023 17:07)</code> - <em>Upvotes: 1</em></p><p>ChatGPT says A</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Sun 11 Dec 2022 15:54)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer#compute</p></blockquote>
<blockquote><p><strong>lookaaaa</strong> <code>(Thu 24 Nov 2022 00:38)</code> - <em>Upvotes: 4</em></p><p>As is shown in the links below, Designer only supports Azure Machine Learning Compute (AML Compute cluster or AML compute instance) for training.

1. https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer#compute
2. https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target#training-compute-targets</p></blockquote>
<blockquote><p><strong>fvil</strong> <code>(Mon 07 Nov 2022 15:31)</code> - <em>Upvotes: 2</em></p><p>Cannot use Attached Compute Cluster in designer:
https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target
Same context but slightly different question on exam 07/11/2022</p></blockquote>
<blockquote><p><strong>amokrane_mancer</strong> <code>(Wed 12 Oct 2022 20:27)</code> - <em>Upvotes: 1</em></p><p>Answer is A</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 11 Oct 2022 07:25)</code> - <em>Upvotes: 2</em></p><p>No is the correct answer.
https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target
ML Designer support 3 target:
1.Azure Machine Learning compute cluste
2.Azure Machine Learning compute instance
3.Azure Machine Learning Kubernetes</p></blockquote>
<blockquote><p><strong>hiyoww</strong> <code>(Sat 06 Apr 2024 13:50)</code> - <em>Upvotes: 1</em></p><p>plus 4. Azure Machine Learning serverless compute</p></blockquote>
<blockquote><p><strong>Steven2022</strong> <code>(Fri 02 Sep 2022 06:03)</code> - <em>Upvotes: 6</em></p><p>i just tried in AML designer, can choose attached compute now</p></blockquote>
<blockquote><p><strong>WeiD</strong> <code>(Thu 19 May 2022 15:48)</code> - <em>Upvotes: 1</em></p><p>can attach Kubernetes service for training and inferencing (preview)
Azure Machine Learning provides you with the following options to attach your own Kubernetes clusters for training and inferencing:

Azure Kubernetes Service. Azure Kubernetes Service provides a managed cluster in Azure.
Azure Arc Kubernetes. Use Azure Arc-enabled Kubernetes clusters if your cluster is hosted outside of Azure.
Those 2 also listed in the https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-target</p></blockquote>

<blockquote><p><strong>pancman</strong> <code>(Wed 13 Apr 2022 19:30)</code> - <em>Upvotes: 1</em></p><p>The correct answer should have been A</p></blockquote>

</details>

---

[<< Previous Question](question_39.md) | [Home](../index.md) | [Next Question >>](question_41.md)
