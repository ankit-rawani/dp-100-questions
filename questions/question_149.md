# Question 149

You manage an Azure Machine Learning workspace.

You need to define an environment from a Docker image by using the Azure Machine Learning Python SDK v2.

Which parameter should you use?

* A.properties
* B.image
* C.build
* D.conda_file

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>PI_Team</strong> <code>(Wed 26 Jul 2023 16:17)</code> - <em>Upvotes: 17</em></p><p>Correct. 
The main difference between using the build and image parameters when defining an environment using the Azure Machine Learning Python SDK v2 is whether you want to define the environment from a Dockerfile or a Docker image.

If you want to define an environment from a Dockerfile, you should use the build parameter and set it to a dictionary that specifies the contents of the Dockerfile using the dockerfile key.
If you want to define an environment from a Docker image, you should use the image parameter and set it to the name of the Docker image you want to use.

SaM</p></blockquote>
<blockquote><p><strong>dreamlimit666</strong> <code>(Sat 16 Nov 2024 08:45)</code> - <em>Upvotes: 1</em></p><p>The correct answer is:

B. image

When defining an environment from a Docker image using the Azure Machine Learning Python SDK v2, the image parameter should be used. This parameter specifies the Docker image that will be used as the base environment for running the experiment.</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Tue 21 May 2024 04:14)</code> - <em>Upvotes: 1</em></p><p>The answer is correct. define from docker image using image parameter.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-environments-v2?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Wed 24 Jan 2024 08:40)</code> - <em>Upvotes: 1</em></p><p>image is correct. Reference: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-environments-v2?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Tue 26 Dec 2023 20:51)</code> - <em>Upvotes: 1</em></p><p>The Correct answer is: C. build
Justification:
When defining an environment from a Docker image using the Azure Machine Learning Python SDK v2, the appropriate parameter to use is build. This is because in the context of the Azure Machine Learning environment, the build parameter is used to specify the configuration for building the environment, including specifying the Docker image to be used.
C. build: This is the correct parameter. Within the Environment class in SDK v2, the build parameter is used to define the build context, which includes specifying the Docker image. When creating an environment from a Docker image, you typically use the BuildContext class within build to specify the Docker image.</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Wed 12 Jul 2023 19:18)</code> - <em>Upvotes: 2</em></p><p>Correct.
env_docker_image = Environment(
    image=&quot;pytorch/pytorch:latest&quot;,
    name=&quot;docker-image-example&quot;,
    description=&quot;Environment created from a Docker image.&quot;,
)
ml_client.environments.create_or_update(env_docker_image)</p></blockquote>

</details>

---

[<< Previous Question](question_148.md) | [Home](/index.md) | [Next Question >>](question_150.md)
