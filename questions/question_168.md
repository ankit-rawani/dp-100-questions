# Question 168

You manage an Azure Machine Learning workspace.

You must create and configure a compute cluster for a training job by using Python SDK v2.

You need to create a persistent Azure Machine Learning compute resource, specifying the fewest possible properties.

Which two properties should you define? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

* A.size
* B.win_instances
* C.type
* D.name
* E.max_instances

<details>
  <summary>Show Suggested Answer</summary>

  <strong>AE</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>f82411e</strong> <code>(Thu 29 May 2025 12:06)</code> - <em>Upvotes: 1</em></p><p>B. win_instances: Not a valid property.
C. type: Not directly specified; the type is implied by the class AmlCompute.
E. max_instances: Optional — useful to auto-scale, but not required.
cpu_cluster = AmlCompute(
    name=&quot;cpu-cluster&quot;,
    size=&quot;Standard_DS11_v2&quot;
)</p></blockquote>
<blockquote><p><strong>avinyc</strong> <code>(Sat 04 Jan 2025 00:08)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/AZURE/machine-learning/how-to-create-attach-compute-cluster?view=azureml-api-1&amp;tabs=python</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Sat 23 Nov 2024 18:38)</code> - <em>Upvotes: 1</em></p><p>Sorry, my last answer was wrong, the correct answer would be A and E</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Sat 23 Nov 2024 18:36)</code> - <em>Upvotes: 1</em></p><p>from azure.ai.ml.entities import AmlCompute
from azure.ai.ml import MLClient

ml_client = MLClient(
    credential=DefaultAzureCredential(),
    subscription_id=&quot;your-subscription-id&quot;,
    resource_group_name=&quot;your-resource-group&quot;,
    workspace_name=&quot;your-workspace-name&quot;
)

compute_cluster = AmlCompute(
    name=&quot;my-compute-cluster&quot;,
    size=&quot;Standard_DS3_v2&quot;
)

ml_client.compute.begin_create_or_update(compute_cluster)

A and D</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Sun 17 Nov 2024 19:57)</code> - <em>Upvotes: 1</em></p><p>To create a persistent Azure Machine Learning Compute resource in Python, specify the size and max_instances properties. Azure Machine Learning then uses smart defaults for the other properties.

size: The VM family of the nodes created by Azure Machine Learning Compute.
max_instances: The maximum number of nodes to autoscale up to when you run a job on Azure Machine Learning Compute.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-attach-compute-cluster?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Tue 05 Nov 2024 16:32)</code> - <em>Upvotes: 2</em></p><p>To create a persistent Azure Machine Learning Compute resource in Python, specify the size and max_instances properties. Azure Machine Learning then uses smart defaults for the other properties. size: The VM family of the nodes created by Azure Machine Learning Compute.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-attach-compute-cluster?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>onurag</strong> <code>(Thu 24 Oct 2024 02:14)</code> - <em>Upvotes: 1</em></p><p>should be size and name, type is not essential property</p></blockquote>
<blockquote><p><strong>PrenCarr</strong> <code>(Sun 06 Oct 2024 20:04)</code> - <em>Upvotes: 1</em></p><p>To create a persistent Azure Machine Learning compute resource with the fewest possible properties using the Python SDK v2, you should define:

type ©
name (D)
These two properties are essential for creating the compute resource. The type specifies the kind of compute resource, and the name gives it a unique identifier within your workspace.</p></blockquote>

</details>

---

[<< Previous Question](question_167.md) | [Home](/index.md) | [Next Question >>](question_169.md)
