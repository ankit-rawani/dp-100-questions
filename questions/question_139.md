# Question 139

HOTSPOT

-

You create a new Azure Machine Learning workspace with a compute cluster.

You need to create the compute cluster asynchronously by using the Azure Machine Learning Python SDK v2.

How should you complete the code segment? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](../images/q139_q_image486.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q139_ans_0_image487.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>damaldon</strong> <code>(Fri 12 Jul 2024 17:58)</code> - <em>Upvotes: 3</em></p><p>Correct.
 begin_create_or_update(resource_group_name: str, domain_name: str, domain_info: ‘_models.Domain’, **kwargs: Any) → LROPoller[‘_models.Domain’][source]

    Create or update a domain.

    Asynchronously creates or updates a new domain with the specified parameters.</p></blockquote>

</details>

---

[<< Previous Question](question_138.md) | [Home](../index.md) | [Next Question >>](question_140.md)
