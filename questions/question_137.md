# Question 137

You manage an Azure Machine Learning workspace. You have an environment for training jobs which uses an existing Docker image.

A new version of the Docker image is available.

You need to use the latest version of the Docker image for the environment configuration by using the Azure Machine Learning SDK v2.

What should you do?

- A.Modify the conda_file to specify the new version of the Docker image.
- B.Use the Environment class to create a new version of the environment.
- C.Use the create_or_update method to change the tag of the image.
- D.Change the description parameter of the environment configuration.

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 01 Dec 2024 13:42)</code> - <em>Upvotes: 2</em></p><p>B is the correct answer</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Fri 15 Nov 2024 03:06)</code> - <em>Upvotes: 2</em></p><p>Link: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-environments-v2?view=azureml-api-2&amp;tabs=python#create-an-environment-from-a-docker-image
Code:

env_docker_image = Environment(
image=&quot;pytorch/pytorch:latest&quot;,
name=&quot;docker-image-example&quot;,
description=&quot;Environment created from a Docker image.&quot;,
)
ml_client.environments.create_or_update(env_docker_image)</p></blockquote>

<blockquote><p><strong>deyoz</strong> <code>(Sun 01 Sep 2024 01:17)</code> - <em>Upvotes: 1</em></p><p>For environments, only description and tags can be updated. All other properties are immutable; if you need to change any of those properties you should create a new version of the environment.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-environments-v2?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>dporwal</strong> <code>(Thu 20 Jun 2024 18:28)</code> - <em>Upvotes: 1</em></p><p>B is the correct answer</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Sun 16 Jun 2024 09:19)</code> - <em>Upvotes: 1</em></p><p>Since the environment already uses a Docker image, the proper way to update to the latest image version is to call the create_or_update() method on that environment configuration object. This allows changing the image tag/version to point to the new Docker image.

Please change the answer to C it&#x27;s misleading.</p></blockquote>

<blockquote><p><strong>Sara_E</strong> <code>(Thu 08 Aug 2024 02:47)</code> - <em>Upvotes: 2</em></p><p>For environments, only description and tags can be updated. All other properties are immutable; if you need to change any of those properties you should create a new version of the environment =&gt;   https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-environments-v2?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>Mal42</strong> <code>(Wed 21 Feb 2024 08:34)</code> - <em>Upvotes: 3</em></p><p>On exam 18 Aug 2023</p></blockquote>
<blockquote><p><strong>Ahmed_Gehad</strong> <code>(Mon 29 Jan 2024 07:55)</code> - <em>Upvotes: 4</em></p><p>We set the image in the Environment class as follows

from azure.ai.ml.entities import Environment

env_docker_image = Environment(
image=&quot;mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04&quot;,
name=&quot;aml-docker-image-example&quot;,
description=&quot;Environment created from a Azure ML Docker image.&quot;,
)
ml_client.environments.create_or_update(env_docker_image)</p></blockquote>

<blockquote><p><strong>hiyoww</strong> <code>(Thu 20 Jun 2024 14:55)</code> - <em>Upvotes: 1</em></p><p>seem ans should be both B and C</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 12 Jan 2024 17:28)</code> - <em>Upvotes: 3</em></p><p>Correct.
You need to create a new version using the Environment class.
env_docker_image = Environment(
    image=&quot;pytorch/pytorch:latest&quot;,
    name=&quot;docker-image-example&quot;,
    description=&quot;Environment created from a Docker image.&quot;,
)
ml_client.environments.create_or_update(env_docker_image)</p></blockquote>
<blockquote><p><strong>pranav33</strong> <code>(Sun 24 Dec 2023 07:21)</code> - <em>Upvotes: 3</em></p><p>B looks correct</p></blockquote>
<blockquote><p><strong>Batman160591</strong> <code>(Wed 20 Dec 2023 22:18)</code> - <em>Upvotes: 4</em></p><p>B. Use the Environment class to create a new version of the environment.

To update the Docker image, you can create a new version of the environment by using the Environment class provided by the Azure Machine Learning SDK. You can update the Docker image reference in the environment&#x27;s Docker section to use the latest version.</p></blockquote>

</details>

---

[<< Previous Question](question_136.md) | [Home](../index.md) | [Next Question >>](question_138.md)
