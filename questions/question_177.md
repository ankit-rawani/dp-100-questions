# Question 177

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You manage an Azure Machine Learning workspace. The development environment for managing the workspace is configured to use Python SDK v2 in Azure Machine Learning Notebooks.

A Synapse Spark Compute is currently attached and uses system-assigned identity.

You need to use Python code to update the Synapse Spark Compute to use a user-assigned identity.

Solution: Pass the UserAssignedIdentity class object to the SynapseSparkCompute class.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>astone42</strong> <code>(Mon 13 Jan 2025 14:24)</code> - <em>Upvotes: 1</em></p><p>A Synapse Spark pool can also use a user-assigned identity. For a user-assigned identity, you can pass a managed identity definition, using the IdentityConfiguration class, as the identity parameter of the SynapseSparkCompute class. For the managed identity definition used in this way, set the type to UserAssigned. In addition, pass a user_assigned_identities parameter. The parameter user_assigned_identities is a list of objects of the UserAssignedIdentity class. The resource_idof the user-assigned identity populates each UserAssignedIdentity class object

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-synapse-spark-pool?view=azureml-api-2&amp;tabs=sdk#update-the-synapse-spark-pool</p></blockquote>

<blockquote><p><strong>colin1919</strong> <code>(Wed 11 Dec 2024 12:13)</code> - <em>Upvotes: 1</em></p><p>No. It is tricky, but no.

You don&#x27;t pass the UserAssignedIdentity() to SynapseSparkCompute() but to the user_assigned_identities INSIDE the ManagedIdentityConfiguration(), which in turn is passed to the SynapseSparkCompute() class.</p></blockquote>

<blockquote><p><strong>Sadhak</strong> <code>(Wed 27 Nov 2024 21:56)</code> - <em>Upvotes: 2</em></p><p>spark_compute = ml_client.compute.get(&quot;&lt;your-spark-compute-name&gt;&quot;)
spark_compute.identity = ManagedIdentityConfiguration(
type=&quot;UserAssigned&quot;,
user_assigned_identities=[
&quot;/subscriptions/&lt;your-subscription-id&gt;/resourcegroups/&lt;your-resource-group-name&gt;/providers/Microsoft.ManagedIdentity/userAssignedIdentities/&lt;your-identity-name&gt;&quot;
]
)</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Sun 17 Nov 2024 20:58)</code> - <em>Upvotes: 2</em></p><p>The answer is &quot;Yes&quot;</p></blockquote>
<blockquote><p><strong>Arvindu89</strong> <code>(Sun 27 Oct 2024 04:36)</code> - <em>Upvotes: 3</em></p><p>The answer is &quot;Yes&quot;

spark_compute = ml_client.compute.get(&quot;&lt;your-spark-compute-name&gt;&quot;)
spark_compute.identity = ManagedIdentityConfiguration(
type=&quot;UserAssigned&quot;,
user_assigned_identities=[
&quot;/subscriptions/&lt;your-subscription-id&gt;/resourcegroups/&lt;your-resource-group-name&gt;/providers/Microsoft.ManagedIdentity/userAssignedIdentities/&lt;your-identity-name&gt;&quot;
]
)</p></blockquote>

</details>

---

[<< Previous Question](question_176.md) | [Home](../index.md) | [Next Question >>](question_178.md)
