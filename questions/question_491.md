# Question 491

You plan to create a compute instance as part of an Azure Machine Learning development workspace.

You must interactively debug code running on the compute instance by using Visual Studio Code Remote.

You need to provision the compute instance.

What should you do?

* A.Enable Remote Desktop Protocol (RDP) access.
* B.Modify role-based access control (RBAC) settings at the workspace level.
* C.Enable Secure Shell Protocol (SSH) access.
* D.Modify role-based access control (RBAC) settings at the compute instance level.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>chevyli</strong> <code>(Thu 08 Sep 2022 08:58)</code> - <em>Upvotes: 11</em></p><p>Why not C? SSH is required to run and debug code in VSCode, right?</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Fri 10 Jan 2025 04:08)</code> - <em>Upvotes: 1</em></p><p>C. Enable Secure Shell Protocol (SSH) access.</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Fri 25 Oct 2024 11:45)</code> - <em>Upvotes: 2</em></p><p>It is C</p></blockquote>
<blockquote><p><strong>GHill1982</strong> <code>(Wed 17 Jan 2024 20:09)</code> - <em>Upvotes: 2</em></p><p>The correct answer is B. Modify role-based access control (RBAC) settings at the workspace level.
To use Visual Studio Code Remote with an Azure Machine Learning compute instance, you need to have the Contributor role at the workspace level. This role allows you to create, update, and delete compute instances, as well as launch Visual Studio Code remotely connected to them.
You do not need to enable RDP or SSH access, as Visual Studio Code Remote uses a secure WebSocket connection to communicate with the compute instance. You also do not need to modify the RBAC settings at the compute instance level, as the workspace-level role is sufficient for accessing the compute instance.</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Mon 11 Dec 2023 17:14)</code> - <em>Upvotes: 3</em></p><p>SSH is the correct answer</p></blockquote>
<blockquote><p><strong>SunilB</strong> <code>(Tue 14 Mar 2023 00:34)</code> - <em>Upvotes: 3</em></p><p>SSH

https://github.com/danielsc/azureml-debug-training/blob/master/Setting%20up%20VSCode%20Remote%20on%20an%20AzureML%20Compute%20Instance.md</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 24 Feb 2023 20:16)</code> - <em>Upvotes: 3</em></p><p>C. Enable Secure Shell Protocol (SSH) access.

To interactively debug code running on a compute instance by using Visual Studio Code Remote, you need to enable Secure Shell (SSH) access on the compute instance. This will allow you to connect to the compute instance remotely using Visual Studio Code and the Remote - SSH extension.

Enabling Remote Desktop Protocol (RDP) access (option A) is not necessary for debugging code using Visual Studio Code Remote. RDP is used for remote desktop access to a Windows machine.

Modifying role-based access control (RBAC) settings at the workspace level (option B) or the compute instance level (option D) is not required for enabling Visual Studio Code Remote. RBAC is used to manage permissions and access to resources in Azure, but it is not related to remote debugging with Visual Studio Code.</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Fri 16 Dec 2022 06:43)</code> - <em>Upvotes: 4</em></p><p>I agree it is B - the question is about access from VS Code, not SSH.</p></blockquote>
<blockquote><p><strong>silva_831</strong> <code>(Mon 21 Nov 2022 06:25)</code> - <em>Upvotes: 2</em></p><p>I think it should be D. Since it&#x27;s mentioned &quot;one checks are performed to make sure the user attempting to make a connection is authorized to use the compute instance.&quot;</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Wed 26 Oct 2022 00:36)</code> - <em>Upvotes: 3</em></p><p>Ref:https://learn.microsoft.com/en-us/azure/machine-learning/how-to-set-up-vs-code-remote?tabs=studio#configure-a-remote-compute-instance</p></blockquote>
<blockquote><p><strong>reddragondms</strong> <code>(Mon 03 Oct 2022 08:20)</code> - <em>Upvotes: 3</em></p><p>I agree it should be C</p></blockquote>

</details>

---

[<< Previous Question](question_490.md) | [Home](/index.md) | [Next Question >>](question_492.md)
