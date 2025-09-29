# Question 391

You use Azure Machine Learning designer to create a training pipeline for a regression model.

You need to prepare the pipeline for deployment as an endpoint that generates predictions asynchronously for a dataset of input data values.

What should you do?

* A.Clone the training pipeline.
* B.Create a batch inference pipeline from the training pipeline.
* C.Create a real-time inference pipeline from the training pipeline.
* D.Replace the dataset in the training pipeline with an Enter Data Manually module.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>dsyouness</strong> <code>(Tue 04 May 2021 01:00)</code> - <em>Upvotes: 54</em></p><p>The answer should be B :
async : Create a batch inference pipeline from the training pipeline</p></blockquote>
<blockquote><p><strong>DickyC</strong> <code>(Mon 10 May 2021 02:45)</code> - <em>Upvotes: 19</em></p><p>Should be B. 
 .... batch inferencing is used to apply a predictive model to multiple cases asynchronously - usually writing the results to a file or database.
https://docs.microsoft.com/en-us/learn/modules/deploy-batch-inference-pipelines-with-azure-machine-learning/1-introduction</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 14:09)</code> - <em>Upvotes: 1</em></p><p>asynchronously ==&gt;batch</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Fri 29 Nov 2024 20:36)</code> - <em>Upvotes: 1</em></p><p>use this link to help you answer this question: https://learn.microsoft.com/en-us/azure/machine-learning/concept-endpoints-batch?view=azureml-api-2#pipeline-component-deployment</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Tue 20 Aug 2024 02:08)</code> - <em>Upvotes: 1</em></p><p>Real time inference??? it is Batch inference.</p></blockquote>
<blockquote><p><strong>Ran2025</strong> <code>(Thu 04 Apr 2024 05:09)</code> - <em>Upvotes: 1</em></p><p>I think that the answer is B</p></blockquote>
<blockquote><p><strong>BR_CS</strong> <code>(Sat 17 Feb 2024 13:28)</code> - <em>Upvotes: 1</em></p><p>Async= B</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 27 Jan 2024 02:54)</code> - <em>Upvotes: 1</em></p><p>B.B. Create a batch inference pipeline from the training pipeline.

Asynchronous predictions are typically done with batch inferencing. Azure Machine Learning provides the batch inference pipeline, which is suited for large volumes of data where the results aren&#x27;t needed in real-time. This differs from a real-time inference pipeline, which provides synchronous, real-time predictions. So, to generate predictions asynchronously for a dataset of input data values, you should create a batch inference pipeline from the training pipeline.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 23 Aug 2023 14:56)</code> - <em>Upvotes: 1</em></p><p>B and C.</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Mon 07 Aug 2023 12:40)</code> - <em>Upvotes: 1</em></p><p>we are talking to get Asynch response so it should be Batch Inference</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Sun 23 Jul 2023 13:42)</code> - <em>Upvotes: 5</em></p><p>Another one wrong this should be B, please correct this answer I have paid for it to be sure the answers are correct.</p></blockquote>
<blockquote><p><strong>Mckay_</strong> <code>(Thu 13 Apr 2023 18:23)</code> - <em>Upvotes: 2</em></p><p>Examtopic should try to review all these wrong answer choices. It is obvious that the word to focus on in this question is &quot;&quot;asynchronous&quot;. The answer is B - batch inferencing</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sat 10 Dec 2022 17:42)</code> - <em>Upvotes: 4</em></p><p>Async = batch
Sync = realtime</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Wed 12 Oct 2022 01:44)</code> - <em>Upvotes: 4</em></p><p>&quot;asynchronously&quot; is the key word here. Asynchronous predictions means batch inferencing</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Tue 13 Sep 2022 02:56)</code> - <em>Upvotes: 4</em></p><p>B. Asynchronous predictions = Batch inferencing</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Sat 03 Sep 2022 06:57)</code> - <em>Upvotes: 2</em></p><p>Similar question On Exam: 03 March 2022</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 15:20)</code> - <em>Upvotes: 3</em></p><p>On exam 2021/7/10</p></blockquote>

</details>

---

[<< Previous Question](question_390.md) | [Home](/index.md) | [Next Question >>](question_392.md)
