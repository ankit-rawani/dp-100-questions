# Question 256

You create a machine learning model by using the Azure Machine Learning designer. You publish the model as a real-time service on an Azure Kubernetes

Service (AKS) inference compute cluster. You make no changes to the deployed endpoint configuration.

You need to provide application developers with the information they need to consume the endpoint.

Which two values should you provide to application developers? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

- A.The name of the AKS cluster where the endpoint is hosted.
- B.The name of the inference pipeline for the endpoint.
- C.The URL of the endpoint.
- D.The run ID of the inference pipeline experiment for the endpoint.
- E.The key for the endpoint.

<details>
  <summary>Show Suggested Answer</summary>

<strong>CE</strong><br>

<p>Deploying an Azure Machine Learning model as a web service creates a REST API endpoint. You can send data to this endpoint and receive the prediction returned by the model.</p>
<p>You create a web service when you deploy a model to your local environment, Azure Container Instances, Azure Kubernetes Service, or field-programmable gate arrays (FPGA). You retrieve the URI used to access the web service by using the Azure Machine Learning SDK. If authentication is enabled, you can also use the</p>
<p>SDK to get the authentication keys or tokens.</p>
<p>Example:</p>
<p># URL for the web service</p>
<p>scoring_uri = &#x27;&#x27;</p>
<p># If the service is authenticated, set the key or token</p>
<p>key = &#x27;&#x27;</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-consume-web-service</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ac45863</strong> <code>(Fri 07 Oct 2022 23:27)</code> - <em>Upvotes: 19</em></p><p>It&#x27;s correct, url and key.</p></blockquote>
<blockquote><p><strong>MattAnya</strong> <code>(Thu 04 Jul 2024 05:50)</code> - <em>Upvotes: 4</em></p><p>on 03 Jan 2023</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Mon 18 Dec 2023 02:46)</code> - <em>Upvotes: 2</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Sun 22 Oct 2023 10:50)</code> - <em>Upvotes: 1</em></p><p>on exam 04/22/2022</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Mon 18 Sep 2023 08:44)</code> - <em>Upvotes: 2</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Sat 06 May 2023 22:00)</code> - <em>Upvotes: 1</em></p><p>on Exam 7 Nov 2021, answer is correct</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Sun 09 Apr 2023 21:00)</code> - <em>Upvotes: 1</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Wed 11 Jan 2023 15:10)</code> - <em>Upvotes: 3</em></p><p>On exam 2021/7/10</p></blockquote>

</details>

---

[<< Previous Question](question_255.md) | [Home](../index.md) | [Next Question >>](question_257.md)
