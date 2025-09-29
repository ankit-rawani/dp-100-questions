# Question 417

DRAG DROP

-

You have an Azure Machine Learning workspace that contains a training cluster and an inference cluster.

You plan to create a classification model by using the Azure Machine Learning designer.

You need to ensure that client applications can submit data as HTTP requests and receive predictions as responses.

Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

![Question Image](images/q417_q_image445.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q417_ans_0_image446.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>avotofu</strong> <code>(Fri 12 Apr 2024 03:05)</code> - <em>Upvotes: 18</em></p><p>Answer should be
1.create training pipeline
2.create inference pipeline
3.deploy to inference cluster</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 27 Jul 2024 16:30)</code> - <em>Upvotes: 4</em></p><p>The correct sequence of actions to ensure that client applications can submit data as HTTP requests and receive predictions as responses is:

b) Create a pipeline that trains a classification model and run the pipeline on the compute cluster. You first need to create and run a training pipeline in the Azure Machine Learning Designer. This pipeline should train a classification model on your data.
d) Create a real-time inference pipeline and run the pipeline on the compute cluster. After the model is trained, you can create a real-time inference pipeline. This type of pipeline will use your trained model to make predictions on new data in real time.
a) Deploy a service to the inference cluster. The last step is to deploy your real-time inference pipeline as a service to the inference cluster. This service will allow client applications to send data as HTTP requests and receive predictions as HTTP responses</p></blockquote>
<blockquote><p><strong>sap_dg</strong> <code>(Fri 29 Mar 2024 04:13)</code> - <em>Upvotes: 1</em></p><p>Create pipeline that trains classification model -&gt; deploy service to the inference cluster -&gt; create real time inference pipeline</p></blockquote>
<blockquote><p><strong>Piddi</strong> <code>(Fri 05 Apr 2024 04:03)</code> - <em>Upvotes: 3</em></p><p>Shouldn&#x27;t the third step be the second step in your answer?</p></blockquote>

</details>

---

[<< Previous Question](question_416.md) | [Home](/index.md) | [Next Question >>](question_418.md)
