# Question 101

HOTSPOT -

You are the owner of an Azure Machine Learning workspace.

You must prevent the creation or deletion of compute resources by using a custom role. You must allow all other operations inside the workspace.

You need to configure the custom role.

How should you complete the configuration? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q101_q_0013500001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q101_ans_0_0013600001.png" alt="Answer Image"><br>

<p>Box 1: Microsoft.MachineLearningServices/workspaces/*/read</p>
<p>Reader    role: Read-only actions in the workspace. Readers can list and view assets, including datastore credentials, in a workspace. Readers can&#x27;t create or update these assets.</p>
<p>Box 2: Microsoft.MachineLearningServices/workspaces/*/write</p>
<p>If the roles include Actions that have a wildcard (*), the effective permissions are computed by subtracting the NotActions from the allowed Actions.</p>
<p>Box 3: Box 2: Microsoft.MachineLearningServices/workspaces/computes/*/delete</p>
<p>Box 4: Microsoft.MachineLearningServices/workspaces/computes/*/write</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/role-based-access-control/overview#how-azure-rbac-determines-if-a-user-has-access-to-a-resource</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>danishanis</strong> <code>(Sat 24 Aug 2024 03:20)</code> - <em>Upvotes: 6</em></p><p>correct af</p></blockquote>
<blockquote><p><strong>klowqw</strong> <code>(Sat 02 Mar 2024 20:41)</code> - <em>Upvotes: 4</em></p><p>correct</p></blockquote>

</details>

---

[<< Previous Question](question_100.md) | [Home](../index.md) | [Next Question >>](question_102.md)
