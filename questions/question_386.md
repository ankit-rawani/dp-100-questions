# Question 386

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You train and register a machine learning model.

You plan to deploy the model as a real-time web service. Applications must use key-based authentication to use the model.

You need to deploy the web service.

Solution:

Create an AciWebservice instance.

Set the value of the ssl_enabled property to True.

Deploy the model to the service.

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>
<p>Instead use only auth_enabled = TRUE</p>
<p>Note: Key-based authentication.</p>
<p>Web services deployed on AKS have key-based auth enabled by default. ACI-deployed services have key-based auth disabled by default, but you can enable it by setting auth_enabled = TRUE when creating the ACI web service. The following is an example of creating an ACI deployment configuration with key-based auth enabled. deployment_config &lt;- aci_webservice_deployment_config(cpu_cores = 1, memory_gb = 1, auth_enabled = TRUE)</p>
<p>Reference:</p>
<p>https://azure.github.io/azureml-sdk-for-r/articles/deploying-models.html</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>santoshpandit</strong> <code>(Thu 23 Jun 2022 02:12)</code> - <em>Upvotes: 5</em></p><p>correct</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sun 20 Oct 2024 07:20)</code> - <em>Upvotes: 1</em></p><p>azureml.core.webservice.aci.AciWebservice(.. ssl_enable = true...)

https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice.aci.aciwebservice?view=azure-ml-py#variables

key-based and ssl_enable can work together.

Web services deployed on AKS have key-based auth enabled by default. ACI-deployed services have key-based auth disabled by default, but you can enable it by setting auth_enabled = TRUE when creating the ACI web service. The following is an example of creating an ACI deployment configuration with key-based auth enabled.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sun 20 Oct 2024 07:20)</code> - <em>Upvotes: 1</em></p><p>deployment_config &lt;- aci_webservice_deployment_config(cpu_cores = 1, 
                                                      memory_gb = 1,
                                                      auth_enabled = TRUE)
To fetch the auth keys, use get_webservice_keys(). To regenerate a key, use the generate_new_webservice_key() function:

# Generate the primary auth key
primary_key &lt;- generate_new_webservice_key(service, key_type = &quot;Primary&quot;)

# Generate the secondary auth key
secondary_key &lt;- generate_new_webservice_key(service, key_type = &quot;Secondary&quot;)

https://azure.github.io/azureml-sdk-for-r/articles/deploying-models.html#key-based-authentication</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sun 20 Oct 2024 07:21)</code> - <em>Upvotes: 1</em></p><p>I changed: missing step Generate auth_key. Choose B.</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Mon 27 Nov 2023 10:10)</code> - <em>Upvotes: 2</em></p><p>False - SSL is transport-layer only, not application-level authentication.</p></blockquote>
<blockquote><p><strong>claps92</strong> <code>(Thu 14 Sep 2023 10:59)</code> - <em>Upvotes: 1</em></p><p>answer is YES!!</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Sun 06 Nov 2022 23:08)</code> - <em>Upvotes: 3</em></p><p>on 6 Nov 2021</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Thu 20 Oct 2022 09:53)</code> - <em>Upvotes: 2</em></p><p>on 19Oct2021</p></blockquote>

</details>

---

[<< Previous Question](question_385.md) | [Home](/index.md) | [Next Question >>](question_387.md)
