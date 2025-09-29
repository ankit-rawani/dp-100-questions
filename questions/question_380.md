# Question 380

You register a model that you plan to use in a batch inference pipeline.

The batch inference pipeline must use a ParallelRunStep step to process files in a file dataset. The script has the ParallelRunStep step runs must process six input files each time the inferencing function is called.

You need to configure the pipeline.

Which configuration setting should you specify in the ParallelRunConfig object for the PrallelRunStep step?

* A.process_count_per_node= "6"
* B.node_count= "6"
* C.mini_batch_size= "6"
* D.error_threshold= "6"

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Jolin130</strong> <code>(Fri 14 May 2021 14:51)</code> - <em>Upvotes: 40</em></p><p>The answer should be C. For FileDataset input, this field is the number of files user script can process in one run() call.</p></blockquote>
<blockquote><p><strong>shivaborusu</strong> <code>(Sat 15 May 2021 13:54)</code> - <em>Upvotes: 19</em></p><p>Answer is C, https://docs.microsoft.com/en-us/python/api/azureml-pipeline-steps/azureml.pipeline.steps.parallel_run_config.parallelrunconfig?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>MonayiYC</strong> <code>(Thu 20 Jun 2024 02:35)</code> - <em>Upvotes: 1</em></p><p>mini_batch_size:  Number of files passed per scoring script run.
https://learn.microsoft.com/en-us/training/modules/deploy-model-batch-endpoint/3-deploy-your-mlflow-model-batch-endpoint</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 12 Apr 2024 09:26)</code> - <em>Upvotes: 1</em></p><p>ParallelRunStep means run parallel in single one node.

Question keyword &#x27;six input files each time the inferencing function is called&#x27;.

Answer keyword: mini_batch_size=&quot;6&quot; .</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 22 Aug 2023 18:36)</code> - <em>Upvotes: 2</em></p><p>The ParallelRunStep step runs must process six input files each time the inferencing function is called, so the correct configuration setting to specify in the ParallelRunConfig object for the ParallelRunStep step is the mini_batch_size, which should be set to 6.

Therefore, the correct answer is:

C. mini_batch_size= &quot;6&quot;</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Mon 07 Aug 2023 12:28)</code> - <em>Upvotes: 1</em></p><p>as stated in Microsoft Documentation this should be mini_batch_size: https://docs.microsoft.com/en-us/python/api/azureml-contrib-pipeline-steps/azureml.contrib.pipeline.steps.parallelrunconfig?view=azure-ml-py. @ExamTopic Can we please fix the answer.</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Sun 23 Jul 2023 13:12)</code> - <em>Upvotes: 1</em></p><p>I believe the answer is C can we please fix the mistake? We are referring on the number of files here so why should be A?</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Sun 11 Jun 2023 09:49)</code> - <em>Upvotes: 3</em></p><p>Node count is about number of compute instances, servers etc.,</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 09 Dec 2022 22:36)</code> - <em>Upvotes: 2</em></p><p>I am sure C is the answer, number of nodes = how many computer inst, number of processes = how many parallel running processes on a node, min_batch_size = min number of files processed</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 11 Oct 2022 20:51)</code> - <em>Upvotes: 2</em></p><p>Correct answer is C. Question notes that the type of dateset to be used is a file dataset. Microsoft documentation says mini_batch_size: For FileDataset input, this field is the number of files a user script can process in one run() call
https://docs.microsoft.com/en-us/python/api/azureml-pipeline-steps/azureml.pipeline.steps.parallel_run_config.parallelrunconfig?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Tue 14 Jun 2022 13:02)</code> - <em>Upvotes: 5</em></p><p>Answer is C</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Apr 2022 09:53)</code> - <em>Upvotes: 2</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>1q2w3e4r5t</strong> <code>(Sun 27 Feb 2022 04:59)</code> - <em>Upvotes: 1</em></p><p>the answer should be mini_batch_size


mini_batch_size
Union[str, int]
For FileDataset input, this field is the number of files a user script can process in one run() call. For TabularDataset input, this field is the approximate size of data the user script can process in one run() call. Example values are 1024, 1024KB, 10MB, and 1GB. (optional, default value is 10 files for FileDataset and 1MB for TabularDataset.)</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Tue 11 Jan 2022 15:17)</code> - <em>Upvotes: 4</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>anwar1</strong> <code>(Sun 28 Nov 2021 14:48)</code> - <em>Upvotes: 4</em></p><p>This Q&amp;A model set has quite a few wrong answers... #Examtopics, kindly fix the wrong answers.</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Sat 27 Nov 2021 09:42)</code> - <em>Upvotes: 1</em></p><p>Answer is C:
Refer below code:
def run(mini_batch):
    # This runs for each batch
    resultList = []

    # process each file in the batch
    for f in mini_batch:
        # Read comma-delimited data into an array
        data = np.genfromtxt(f, delimiter=&#x27;,&#x27;)
        # Reshape into a 2-dimensional array for model input
        prediction = model.predict(data.reshape(1, -1))
        # Append prediction to results
        resultList.append(&quot;{}: {}&quot;.format(os.path.basename(f), prediction[0]))
    return resultList</p></blockquote>
<blockquote><p><strong>BilJon</strong> <code>(Tue 28 Sep 2021 15:14)</code> - <em>Upvotes: 5</em></p><p>mini_batch_size is correct</p></blockquote>

</details>

---

[<< Previous Question](question_379.md) | [Home](/index.md) | [Next Question >>](question_381.md)
