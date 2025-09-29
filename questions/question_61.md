# Question 61

You are developing a data science workspace that uses an Azure Machine Learning service.

You need to select a compute target to deploy the workspace.

What should you use?

- A.Azure Data Lake Analytics
- B.Azure Databricks
- C.Azure Container Service
- D.Apache Spark for HDInsight

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>cenkersoy</strong> <code>(Tue 16 Jun 2020 19:17)</code> - <em>Upvotes: 18</em></p><p>Should it not say &quot;deploying the trained model&quot; instead of &quot;workspace&quot; ?</p></blockquote>
<blockquote><p><strong>modschegiebsch</strong> <code>(Fri 03 Jul 2020 06:09)</code> - <em>Upvotes: 14</em></p><p>Before reading this question, I never heard of &quot;Azure Container Service&quot;. Here is why:
https://azure.microsoft.com/de-de/updates/azure-container-service-will-retire-on-january-31-2020/

One can choose Azure Kubernetes Service (AKS) or Azure Container Instances as a &quot;compute target&quot; as well as Databricks clusters or Spark on HDInsight clusters.

https://docs.microsoft.com/de-de/azure/machine-learning/concept-compute-target

But the question is probably about deploying the model as a web service. Then there is actually no correct answer, because the Azure Container Service retired.</p></blockquote>

<blockquote><p><strong>prashantjoge</strong> <code>(Sun 30 May 2021 20:46)</code> - <em>Upvotes: 3</em></p><p>no, its not retired. its still used fir development</p></blockquote>
<blockquote><p><strong>Laredo</strong> <code>(Wed 18 Nov 2020 19:53)</code> - <em>Upvotes: 4</em></p><p>You are right. Answer is Azure Container Instance. C looks like it was corrected in the solution.</p></blockquote>
<blockquote><p><strong>sar77</strong> <code>(Wed 16 Jul 2025 03:32)</code> - <em>Upvotes: 1</em></p><p>To deploy an Azure Machine Learning workspace, the most appropriate compute target would be:

B. Azure Databricks</p></blockquote>

<blockquote><p><strong>f82411e</strong> <code>(Thu 15 May 2025 01:13)</code> - <em>Upvotes: 1</em></p><p>porque todas las preguntas hablan de databricks nunca se menciona contenedores</p></blockquote>
<blockquote><p><strong>84b1989</strong> <code>(Fri 17 Jan 2025 11:33)</code> - <em>Upvotes: 1</em></p><p>Azure Databricks is the most suitable compute target for deploying a data science workspace that uses Azure Machine Learning service. Here&#x27;s why:

Integration with Azure Machine Learning:
Azure Databricks integrates seamlessly with Azure Machine Learning, allowing you to train and deploy machine learning models at scale. It supports collaborative data science workflows and provides a unified platform for data engineering and machine learning.

Scalability:
Azure Databricks is built on Apache Spark and provides a highly scalable environment for processing large datasets and running complex machine learning algorithms.

Support for diverse workloads:
Azure Databricks supports both batch and real-time data processing, making it ideal for data science tasks like data preparation, model training, and deployment.

Collaboration:
Azure Databricks provides a collaborative workspace for data scientists, data engineers, and machine learning engineers, enabling teams to work together efficiently.</p></blockquote>

<blockquote><p><strong>84b1989</strong> <code>(Wed 15 Jan 2025 14:11)</code> - <em>Upvotes: 1</em></p><p>Azure Databricks is the most suitable compute target for deploying a data science workspace that uses Azure Machine Learning service. Here&#x27;s why:

Integration with Azure Machine Learning:
Azure Databricks integrates seamlessly with Azure Machine Learning, allowing you to train and deploy machine learning models at scale. It supports collaborative data science workflows and provides a unified platform for data engineering and machine learning.

Scalability:
Azure Databricks is built on Apache Spark and provides a highly scalable environment for processing large datasets and running complex machine learning algorithms.

Support for diverse workloads:
Azure Databricks supports both batch and real-time data processing, making it ideal for data science tasks like data preparation, model training, and deployment.

Collaboration:
Azure Databricks provides a collaborative workspace for data scientists, data engineers, and machine learning engineers, enabling teams to work together efficientl</p></blockquote>

<blockquote><p><strong>maguido</strong> <code>(Thu 22 Aug 2024 09:02)</code> - <em>Upvotes: 1</em></p><p>Azure Databricks is more suited for the development and training phases of machine learning, while Azure Kubernetes Service (AKS) is the preferred choice for deploying machine learning models as it offers the necessary infrastructure for production-level serving of these models</p></blockquote>
<blockquote><p><strong>Hisayuki</strong> <code>(Fri 03 Nov 2023 09:08)</code> - <em>Upvotes: 1</em></p><p>Once we have the Databricks workspace, we can link it to the Azure ML workspace so that they can talk to each other.</p></blockquote>
<blockquote><p><strong>Ran2025</strong> <code>(Sat 30 Sep 2023 14:57)</code> - <em>Upvotes: 4</em></p><p>C is correct!  Azure Container Services include AKS and ACI.
https://learn.microsoft.com/en-us/azure/containers/</p></blockquote>
<blockquote><p><strong>Ahmed_Gehad</strong> <code>(Sun 23 Jul 2023 07:35)</code> - <em>Upvotes: 3</em></p><p>I think it&#x27;s C as per https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2#compute-targets-for-inference</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Tue 11 Jul 2023 20:07)</code> - <em>Upvotes: 2</em></p><p>Containers only for small deployments, otherwise Databricks</p></blockquote>
<blockquote><p><strong>prabhjot</strong> <code>(Mon 29 Jan 2024 13:31)</code> - <em>Upvotes: 1</em></p><p>100% agree with you</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Sat 27 May 2023 20:32)</code> - <em>Upvotes: 1</em></p><p>While Azure Container Service (ACS) can be used to deploy and manage containers for various applications, including machine learning workloads, it is not the recommended compute target for deploying a data science workspace using Azure Machine Learning service.

Azure Databricks is a more suitable choice for deploying the workspace in this scenario. It provides a collaborative and scalable environment specifically designed for data engineering and data science tasks. With Azure Databricks, you can leverage the power of Apache Spark for distributed data processing and machine learning tasks, making it an ideal compute target for data science workloads.

Azure Container Service, on the other hand, is a container orchestration service that supports various container runtimes, such as Docker and Kubernetes. While it can be used to deploy machine learning models encapsulated in containers, it is not optimized for the specific requirements of a data science workspace and may not provide the same level of integration and ease of use as Azure Databricks.

Therefore, in this context, the recommended choice for deploying the data science workspace using Azure Machine Learning service is B. Azure Databricks.</p></blockquote>

<blockquote><p><strong>sahithi2004</strong> <code>(Mon 20 Mar 2023 13:05)</code> - <em>Upvotes: 3</em></p><p>it is databricks</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 02 Feb 2023 04:35)</code> - <em>Upvotes: 4</em></p><p>B. Azure Databricks is the most accurate answer if you&#x27;re looking to deploy a data science workspace using Azure Machine Learning service as a compute target. Azure Databricks is a fast, easy, and collaborative Apache Spark-based analytics platform that helps you build and deploy machine learning models. It provides a seamless integration with the Azure Machine Learning service and offers features such as auto-scaling, collaboration and management of the machine learning workflow, and a secure and scalable infrastructure for running your data science projects.
While you can run machine learning models inside containers in Azure Container Service, it doesn&#x27;t provide the seamless integration and specific features for managing and deploying machine learning models that Azure Databricks does. For example, you wouldn&#x27;t have access to the auto-scaling, collaboration, and management features for the machine learning workflow that Azure Databricks provides.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Wed 11 May 2022 11:36)</code> - <em>Upvotes: 4</em></p><p>Deployment target, only two options: Container Instance, Azure Kubernetes Cluster</p></blockquote>
<blockquote><p><strong>Rosh4yuh</strong> <code>(Sat 17 Jul 2021 12:49)</code> - <em>Upvotes: 5</em></p><p>on 17/7/2021</p></blockquote>
<blockquote><p><strong>Narendra05</strong> <code>(Sun 27 Jun 2021 15:06)</code> - <em>Upvotes: 3</em></p><p>The service is discontinued from 31Jan 2020 the Question is not relavent anymore</p></blockquote>

</details>

---

[<< Previous Question](question_60.md) | [Home](../index.md) | [Next Question >>](question_62.md)
