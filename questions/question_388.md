# Question 388

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You train and register a machine learning model.

You plan to deploy the model as a real-time web service. Applications must use key-based authentication to use the model.

You need to deploy the web service.

Solution:

Create an AciWebservice instance.

Set the value of the auth_enabled property to True.

Deploy the model to the service.

Does the solution meet the goal?

- A.Yes
- B.No

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>desmondfernando</strong> <code>(Fri 24 Dec 2021 04:43)</code> - <em>Upvotes: 7</em></p><p>Yes, the correct answer is Option A. Because AKS is based on Key-value auth as default.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 13:40)</code> - <em>Upvotes: 1</em></p><p>It meets the requirements</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Mon 05 Aug 2024 07:45)</code> - <em>Upvotes: 1</em></p><p>The answer is No. The question is about AciWebservice. This option is not recommended for real-time inferencing: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/innovate/best-practices/ml-deployment-inference</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 22 Aug 2023 20:08)</code> - <em>Upvotes: 2</em></p><p>B. No
The solution provided does not fully meet the goal. While creating an AciWebservice instance and deploying the model to the service are necessary steps, simply setting the value of the auth_enabled property to True does not provide a key-based authentication mechanism for the web service. Additional steps are required to generate and manage the authentication keys, such as creating an Azure Key Vault to store the keys and implementing code in the client applications to retrieve and use the keys for authentication.</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Sat 27 May 2023 09:09)</code> - <em>Upvotes: 3</em></p><p>True - key-based authentication is exactly the solution here.</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Fri 06 May 2022 22:08)</code> - <em>Upvotes: 1</em></p><p>on 6 Nov 2021</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Apr 2022 09:53)</code> - <em>Upvotes: 3</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Sat 25 Dec 2021 17:03)</code> - <em>Upvotes: 4</em></p><p>given answer is correct auth_enabled=True is used for Key-based authentication and token_auth_enabled =True is used for Token-based authentication
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-authenticate-web-service</p></blockquote>
<blockquote><p><strong>nmuenter</strong> <code>(Sat 27 Nov 2021 12:26)</code> - <em>Upvotes: 3</em></p><p>I think A is correct. The requirements say : Applications must use key-based authentication to use the model. auth_enabled parameter is for key-based authentication (By default it&#x27;s True for AKS) and token_auth_enabled is for token based authentication (not for key-based).</p></blockquote>
<blockquote><p><strong>birbyne</strong> <code>(Tue 23 Nov 2021 18:52)</code> - <em>Upvotes: 3</em></p><p>B: No
token_auth_enabled=True
https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice.akswebservice?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>treadst0ne</strong> <code>(Wed 15 Dec 2021 02:34)</code> - <em>Upvotes: 4</em></p><p>The question says &quot;key-based&quot;, not token_auth, so the correct answer is A.</p></blockquote>

</details>

---

[<< Previous Question](question_387.md) | [Home](../index.md) | [Next Question >>](question_389.md)
