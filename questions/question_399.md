# Question 399

You develop and train a machine learning model to predict fraudulent transactions for a hotel booking website.

Traffic to the site varies considerably. The site experiences heavy traffic on Monday and Friday and much lower traffic on other days. Holidays are also high web traffic days.

You need to deploy the model as an Azure Machine Learning real-time web service endpoint on compute that can dynamically scale up and down to support demand.

Which deployment compute option should you use?

* A.attached Azure Databricks cluster
* B.Azure Container Instance (ACI)
* C.Azure Kubernetes Service (AKS) inference cluster
* D.Azure Machine Learning Compute Instance
* E.attached virtual machine in a different region

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>pddddd</strong> <code>(Sat 08 May 2021 08:23)</code> - <em>Upvotes: 64</em></p><p>C. AKS inference cluster</p></blockquote>
<blockquote><p><strong>Abhinav_nasaiitkgp</strong> <code>(Fri 23 Jul 2021 21:53)</code> - <em>Upvotes: 20</em></p><p>C as
AKS autoscales and support real time and can manage heavy traffic
Why not D - because it doesn&#x27;t support real time and doesn&#x27;t autoscale</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Tue 20 Aug 2024 02:28)</code> - <em>Upvotes: 1</em></p><p>had compute cluster as an option, then what would have been the answers? compute cluster or AKS?</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sat 20 Apr 2024 10:27)</code> - <em>Upvotes: 1</em></p><p>&#x27;scale up and scale down&#x27; --&gt; choose AKS. I choose C.</p></blockquote>
<blockquote><p><strong>Ran2025</strong> <code>(Thu 04 Apr 2024 05:40)</code> - <em>Upvotes: 1</em></p><p>I thinks the answer is C!</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Mon 07 Aug 2023 12:59)</code> - <em>Upvotes: 2</em></p><p>Another one to fix. Can we please fix it? This should be 100% AKS</p></blockquote>
<blockquote><p><strong>clark88</strong> <code>(Wed 05 Jul 2023 09:37)</code> - <em>Upvotes: 4</em></p><p>AKS - always for these kind of questions</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 13 Sep 2022 03:07)</code> - <em>Upvotes: 3</em></p><p>AKS inference cluster</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Apr 2022 09:53)</code> - <em>Upvotes: 1</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>slash_nyk</strong> <code>(Sun 16 Jan 2022 11:25)</code> - <em>Upvotes: 2</em></p><p>I agree with C</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 15:22)</code> - <em>Upvotes: 6</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>SnowCheetah</strong> <code>(Sun 26 Dec 2021 08:50)</code> - <em>Upvotes: 3</em></p><p>it should be C since AKS with inference cluster can autoscale and support realtime</p></blockquote>
<blockquote><p><strong>yobllip</strong> <code>(Wed 22 Dec 2021 04:17)</code> - <em>Upvotes: 3</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-instance
For production grade model training, use an Azure Machine Learning compute cluster with multi-node scaling capabilities. For production grade model deployment, use Azure Kubernetes Service cluster.
I will go for C for sure</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Sun 19 Sep 2021 06:10)</code> - <em>Upvotes: 3</em></p><p>the answer is &#x27;C&#x27; : 
Use for high-scale production deployments. Provides fast response time and autoscaling of the deployed service.
https://docs.microsoft.com/fr-fr/azure/machine-learning/how-to-deploy-and-where?tabs=azcli</p></blockquote>
<blockquote><p><strong>Oprawinkle1</strong> <code>(Thu 27 May 2021 07:25)</code> - <em>Upvotes: 2</em></p><p>The key word there is automatically scaling up and down, so its compute instance</p></blockquote>
<blockquote><p><strong>111ssy</strong> <code>(Thu 03 Jun 2021 21:51)</code> - <em>Upvotes: 7</em></p><p>A compute instance does not automatically scale down, so make sure to stop the resource to prevent ongoing charges. Therefore, compute instance is not the right answer</p></blockquote>
<blockquote><p><strong>111ssy</strong> <code>(Thu 03 Jun 2021 21:51)</code> - <em>Upvotes: 3</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-manage-compute-instance?tabs=python</p></blockquote>

</details>

---

[<< Previous Question](question_398.md) | [Home](/index.md) | [Next Question >>](question_400.md)
