# Question 104

HOTSPOT -

You create an Azure Machine Learning workspace named workspace1. You assign a custom role to a user of workspace1.

The custom role has the following JSON definition:

![Question Image](../images/q104_q_0013700001.png)

Instructions: For each of the following statements, select Yes if the statement is true. Otherwise, select No.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q104_q_0013800001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q104_ans_0_0013800002.png" alt="Answer Image"><br>

<p>Box 1: No -</p>
<p>The actions listed in NotActions are prohibited.</p>
<p>If the roles include Actions that have a wildcard (*), the effective permissions are computed by subtracting the NotActions from the allowed Actions.</p>
<p>Box 2: No -</p>
<p>Deleting compute resources in the workspace is in the NotActions list.</p>
<p>Box 3: Yes -</p>
<p>Writing metrics is not listed in NotActions.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/role-based-access-control/overview#how-azure-rbac-determines-if-a-user-has-access-to-a-resource</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ABosco</strong> <code>(Sun 18 Feb 2024 06:17)</code> - <em>Upvotes: 5</em></p><p>No, No, Yes is correct. The last one is concerning the Roles not related to WS.</p></blockquote>
<blockquote><p><strong>PremPatrick</strong> <code>(Thu 18 May 2023 07:52)</code> - <em>Upvotes: 5</em></p><p>Correct. No, No, Yes</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Sat 13 Jan 2024 10:51)</code> - <em>Upvotes: 3</em></p><p>No,No,NO

Writing metrics specifically is not listed in the NotActions property of the provided role definition. However, the NotActions property does include &quot;Microsoft.MachineLearningServices/workspaces/write&quot;, which would likely prevent the user from writing metrics to the workspace, as writing metrics would likely require write permissions on the workspace

SaM</p></blockquote>

<blockquote><p><strong>Nadine_nm</strong> <code>(Sun 25 Feb 2024 14:47)</code> - <em>Upvotes: 2</em></p><p>&quot;Microsoft.MachineLearningServices/workspaces/write&quot;, this line only means that It can&#x27;t create or update the workspace
i don&#x27;t think that writing metrics is part of the &quot;updating workspace&quot;</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Wed 03 Jul 2024 17:36)</code> - <em>Upvotes: 4</em></p><p>Yes, you are correct! My bad!</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Thu 18 Jan 2024 22:01)</code> - <em>Upvotes: 1</em></p><p>You used &quot;likely&quot; twice. So does it or does it not?</p></blockquote>

</details>

---

[<< Previous Question](question_103.md) | [Home](../index.md) | [Next Question >>](question_105.md)
