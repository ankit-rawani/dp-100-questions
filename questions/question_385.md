# Question 385

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You train and register a machine learning model.

You plan to deploy the model as a real-time web service. Applications must use key-based authentication to use the model.

You need to deploy the web service.

Solution:

Create an AciWebservice instance.

Set the value of the auth_enabled property to False.

Set the value of the token_auth_enabled property to True.

Deploy the model to the service.

Does the solution meet the goal?

- A.Yes
- B.No

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

<blockquote><p><strong>james2033</strong> <code>(Sun 20 Oct 2024 07:24)</code> - <em>Upvotes: 1</em></p><p>Web services deployed on AKS have key-based auth enabled by default. ACI-deployed services have key-based auth disabled by default, but you can enable it by setting auth_enabled = TRUE when creating the ACI web service. The following is an example of creating an ACI deployment configuration with key-based auth enabled.

https://azure.github.io/azureml-sdk-for-r/articles/deploying-models.html#key-based-authentication

But missing step generate auth_key --&gt; no meet requirement --&gt; choose B. No.</p></blockquote>

<blockquote><p><strong>phdykd</strong> <code>(Thu 22 Feb 2024 21:11)</code> - <em>Upvotes: 1</em></p><p>B. No.

The solution does not meet the goal as it specifies setting the auth_enabled property to False, which means that there will be no authentication for accessing the web service. Additionally, the token_auth_enabled property is set to True, but it requires a token for authentication, which is contradictory to the previous property. To meet the goal of key-based authentication, the auth_enabled property should be set to True and the token_auth_enabled property should be set to False. Additionally, other configurations related to key-based authentication such as primary_key or secondary_key should be specified.</p></blockquote>

<blockquote><p><strong>michaelmorar</strong> <code>(Mon 27 Nov 2023 10:08)</code> - <em>Upvotes: 1</em></p><p>Falsch - token and key-based are different authentication methods.</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Thu 20 Oct 2022 09:53)</code> - <em>Upvotes: 3</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>Kapil1803</strong> <code>(Sun 03 Jul 2022 06:31)</code> - <em>Upvotes: 4</em></p><p>The answer is correct. Refer Key-Based vs Token-Based https://docs.microsoft.com/en-us/azure/machine-learning/how-to-authenticate-web-service</p></blockquote>
<blockquote><p><strong>SnowCheetah</strong> <code>(Mon 27 Jun 2022 08:10)</code> - <em>Upvotes: 4</em></p><p>The answer is FALSE

https://azure.github.io/azureml-sdk-for-r/articles/deploying-models.html

in aks there can be set authentication two way
key ==&gt; auth_enabled = TRUE
token ==&gt; token_auth_enabled = TRUE
problem specified with must authenticated by key-based</p></blockquote>

</details>

---

[<< Previous Question](question_384.md) | [Home](../index.md) | [Next Question >>](question_386.md)
