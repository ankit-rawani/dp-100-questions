# Question 142

HOTSPOT

-

You manage an Azure Machine Learning workspace.

You must define the execution environments for your jobs and encapsulate the dependencies for your code.

You need to configure the environment from a Docker build context.

How should you complete the code segment? To answer, select the appropriate option in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q142_q_image490.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q142_ans_0_image491.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Kanwal001</strong> <code>(Wed 28 Feb 2024 20:38)</code> - <em>Upvotes: 6</em></p><p>On exam 28 Aug 2023</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 26 Jan 2024 14:23)</code> - <em>Upvotes: 5</em></p><p>Correct. 

from azureml.core import Environment
from azureml.core.environment import BuildContext

env_docker_context = Environment(
    build=BuildContext(path=&quot;docker-contexts/python-and-pip&quot;),
    name=&quot;docker-context-example&quot;,
    description=&quot;Environment created from a Docker context.&quot;,
)

SaM</p></blockquote>
<blockquote><p><strong>TA_</strong> <code>(Wed 25 Sep 2024 10:38)</code> - <em>Upvotes: 1</em></p><p>On exam 15-03-2024</p></blockquote>
<blockquote><p><strong>Batman160591</strong> <code>(Wed 20 Dec 2023 23:32)</code> - <em>Upvotes: 1</em></p><p>seems correct</p></blockquote>

</details>

---

[<< Previous Question](question_141.md) | [Home](/index.md) | [Next Question >>](question_143.md)
