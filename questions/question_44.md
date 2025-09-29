# Question 44

Your team is building a data engineering and data science development environment.

The environment must support the following requirements:

✑ support Python and Scala

✑ compose data storage, movement, and processing services into automated data pipelines

✑ the same tool should be used for the orchestration of both data engineering and data science

✑ support workload isolation and interactive workloads

✑ enable scaling across a cluster of machines

You need to create the environment.

What should you do?

* A.Build the environment in Apache Hive for HDInsight and use Azure Data Factory for orchestration.
* B.Build the environment in Azure Databricks and use Azure Data Factory for orchestration.
* C.Build the environment in Apache Spark for HDInsight and use Azure Container Instances for orchestration.
* D.Build the environment in Azure Databricks and use Azure Container Instances for orchestration.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Adi06</strong> <code>(Sat 13 Nov 2021 00:58)</code> - <em>Upvotes: 9</em></p><p>Is the answer not D?? They are trying to build a development environment (line 1). Nowhere it says its for production environment.</p></blockquote>
<blockquote><p><strong>allanm</strong> <code>(Tue 17 May 2022 14:26)</code> - <em>Upvotes: 1</em></p><p>Agreed. If it was production environment, it should be Kubernetes services. Since it&#x27;s development it should be container services. 

https://docs.microsoft.com/en-us/learn/modules/register-and-deploy-model-with-amls/2-deploy-model</p></blockquote>
<blockquote><p><strong>levm39</strong> <code>(Sat 18 Jun 2022 08:24)</code> - <em>Upvotes: 8</em></p><p>you cant do orchestration with ACI, only with data factory, answer is correct.</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Mon 30 May 2022 20:12)</code> - <em>Upvotes: 2</em></p><p>definitely d</p></blockquote>
<blockquote><p><strong>strikchao</strong> <code>(Fri 05 Aug 2022 12:57)</code> - <em>Upvotes: 1</em></p><p>Not D. There is no autoscaling with ACI</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 02 Feb 2024 02:35)</code> - <em>Upvotes: 8</em></p><p>B.
Azure Databricks is a fast, easy, and collaborative Apache Spark-based analytics platform that provides a complete environment for data engineering, machine learning, and data science. It supports Python and Scala, and allows you to compose data storage, movement, and processing services into automated data pipelines. Azure Data Factory, on the other hand, is a cloud-based data integration service that allows you to create, schedule, and orchestrate your data pipelines. By using both Databricks and Data Factory together, you can have a unified platform for both data engineering and data science that also supports workload isolation and interactive workloads, as well as enables scaling across a cluster of machines.</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Mon 15 Jul 2024 15:03)</code> - <em>Upvotes: 4</em></p><p>Azure Databricks is an obvious choice for the environment. To decide between Data Factory vs Container Instances for orchestration makes the difference here. ADF would be a more suitable choice compared to ACI for orchestration in this scenario due to

1. Native Orchestration Capabilities
2. Visual Workflow Designer
3. Integration with Diverse Data Sources and Services
4. Built-in Monitoring and Management

Therefore, for the purpose of orchestrating data pipelines in a data engineering and data science environment, ADF would be the recommended choice due to its dedicated orchestration features, data integration capabilities, visual workflow designer, and integration with diverse data sources and services.</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Wed 30 Nov 2022 18:29)</code> - <em>Upvotes: 3</em></p><p>B without doubts</p></blockquote>
<blockquote><p><strong>kolakone</strong> <code>(Sat 16 Jul 2022 00:16)</code> - <em>Upvotes: 6</em></p><p>B is the right answer.
C and D are out as there is need for data engineering 
Since there is need for &quot;both data engineering and data science&quot;, there is need for Data Factory, hence C and D are out.
Due to need for Scala and Python support, Databricks (B) is the correct answer.</p></blockquote>
<blockquote><p><strong>Navishmamta1111111111111</strong> <code>(Sat 02 Jul 2022 02:47)</code> - <em>Upvotes: 3</em></p><p>B is correct</p></blockquote>
<blockquote><p><strong>okeyken1</strong> <code>(Sat 25 Jun 2022 16:44)</code> - <em>Upvotes: 1</em></p><p>the correct answer is B</p></blockquote>
<blockquote><p><strong>MAGGCol</strong> <code>(Sun 29 May 2022 22:58)</code> - <em>Upvotes: 1</em></p><p>Previewed last year, Microsoft&#x27;s Azure Container Instances (ACI) is now ready for production usage, according to the company. ... Microsoft promises an uptime service level agreement of 99.9 percent for any container group. Each container is secured and isolated through a VM hypervisor.</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Fri 20 May 2022 18:07)</code> - <em>Upvotes: 5</em></p><p>azure databricks support clustering while azure data factory supports orchestration (https://docs.microsoft.com/en-us/azure/databricks/clusters/configure).  The orchestration here should be in the context of data processing (think SSIS, ETL, informatica etc.)  Answer should be B. Azure containers  instances provide some basic orchestration capabilities, but then again the context is different. https://docs.microsoft.com/en-us/azure/container-instances/container-instances-orchestrator-relationship</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Tue 03 May 2022 19:07)</code> - <em>Upvotes: 5</em></p><p>I think the best answer is B. ACI is used to deploy a model. ACI is just like docker - for orchestration you would need something like kubernetes not docker.</p></blockquote>
<blockquote><p><strong>LakeSky</strong> <code>(Sat 09 Apr 2022 09:43)</code> - <em>Upvotes: 2</em></p><p>Wow, so what&#x27;s the correct answer really? Why is Azure Container not an option?</p></blockquote>
<blockquote><p><strong>cab123</strong> <code>(Thu 14 Apr 2022 17:19)</code> - <em>Upvotes: 2</em></p><p>I think Azure Container instances cannot do orchestration</p></blockquote>

</details>

---

[<< Previous Question](question_43.md) | [Home](/index.md) | [Next Question >>](question_45.md)
