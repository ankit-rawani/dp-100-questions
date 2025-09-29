# Question 383

An organization creates and deploys a multi-class image classification deep learning model that uses a set of labeled photographs.

The software engineering team reports there is a heavy inferencing load for the prediction web services during the summer. The production web service for the model fails to meet demand despite having a fully-utilized compute cluster where the web service is deployed.

You need to improve performance of the image classification web service with minimal downtime and minimal administrative effort.

What should you advise the IT Operations team to do?

* A.Create a new compute cluster by using larger VM sizes for the nodes, redeploy the web service to that cluster, and update the DNS registration for the service endpoint to point to the new cluster.
* B.Increase the node count of the compute cluster where the web service is deployed.
* C.Increase the minimum node count of the compute cluster where the web service is deployed.
* D.Increase the VM size of nodes in the compute cluster where the web service is deployed.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>santoshpandit</strong> <code>(Thu 23 Dec 2021 02:00)</code> - <em>Upvotes: 10</em></p><p>looks correct</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 13:32)</code> - <em>Upvotes: 1</em></p><p>anything that touches VM specs caused downtime, only increasing node count does not cause downtime. B is correct</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sat 20 Apr 2024 07:05)</code> - <em>Upvotes: 1</em></p><p>&#x27;Increase the minimum node count of the compute cluster&#x27; . I choose C.</p></blockquote>
<blockquote><p><strong>ahmednani015</strong> <code>(Tue 26 Nov 2024 11:32)</code> - <em>Upvotes: 1</em></p><p>The answer is incorrect because the heavy inferencing occurs only during the summer. The problem remains since we haven&#x27;t upgraded the cluster&#x27;s capabilities, leading to higher costs outside of summer due to always active nodes, even with no inferencing requests.</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Sat 27 May 2023 09:06)</code> - <em>Upvotes: 2</em></p><p>Increasing the node count has the least administrative effort compared to option A which describes a heavier solution.</p></blockquote>
<blockquote><p><strong>tchip</strong> <code>(Wed 24 Aug 2022 23:59)</code> - <em>Upvotes: 1</em></p><p>this is correct as it requires lesser downtime and minimal administrative effort</p></blockquote>
<blockquote><p><strong>tchip</strong> <code>(Sat 20 Aug 2022 04:53)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>
<blockquote><p><strong>nick234987</strong> <code>(Fri 15 Apr 2022 18:33)</code> - <em>Upvotes: 1</em></p><p>It is correct</p></blockquote>

</details>

---

[<< Previous Question](question_382.md) | [Home](/index.md) | [Next Question >>](question_384.md)
