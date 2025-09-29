# Question 371

You manage an Azure Machine Learning Workspace named Workspase1 and an Azure Files share named Share1.

You plan to create an Azure Files datastore in Workspace1 to target Share1.

You need to configure permanent access to Share1 from the Azure Files datastore.

Which authorization method should you use?

* A.Primary access key
* B.Anonymous access
* C.Account SAS key
* D.User delegation SAS key

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>7bbe541</strong> <code>(Thu 08 May 2025 23:48)</code> - <em>Upvotes: 2</em></p><p>A. Primary access key
Why?

    Primary access key provides persistent, full access to the Azure Storage account (including the Azure Files share).

    It does not expire (unlike SAS keys), making it ideal for long-term access in ML workloads.

    Azure ML datastores require stable credentials for reliable data access during training and inference.</p></blockquote>

</details>

---

[<< Previous Question](question_370.md) | [Home](/index.md) | [Next Question >>](question_372.md)
