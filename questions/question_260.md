# Question 260

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You create a model to forecast weather conditions based on historical data.

You need to create a pipeline that runs a processing script to load data from a datastore and pass the processed data to a machine learning model training script.

Solution: Run the following code:

![Question Image](images/q260_q_0027700001.png)

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Haet</strong> <code>(Tue 12 Oct 2021 17:59)</code> - <em>Upvotes: 12</em></p><p>The Answer should be No.</p></blockquote>
<blockquote><p><strong>SwaggyCD2</strong> <code>(Mon 13 Jun 2022 15:54)</code> - <em>Upvotes: 7</em></p><p>Deprecated as now we use FileOutputDatasetConfig</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Sat 03 Aug 2024 01:42)</code> - <em>Upvotes: 1</em></p><p>this is a correct code
precess_step = PythonScriptStep(name = &#x27;Data Processing&#x27;,
                                source_directory =&#x27;.&#x27;,
                                script_name =&quot;process.py&quot;,
                                inputs = [input_ds.as_named_input(&#x27;raw_data&#x27;)],
                                outputs = [dataFolder],
                                runconfig = run_config,
                                arguments = [&#x27;--datafolder&#x27;, dataFolder])

where, 

dataFolder = PipelineData(name = &#x27;datafolder&#x27;, datastore = ws.get_default_datastore())


so the answer is NO.</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Wed 29 Nov 2023 19:06)</code> - <em>Upvotes: 1</em></p><p>I think input argument were losted for proces_ step, and output argument for the train_step</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Mon 12 Sep 2022 00:29)</code> - <em>Upvotes: 2</em></p><p>The answer is correct (A). But no need to look into this. DataReference is deprecated</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Mon 12 Sep 2022 00:28)</code> - <em>Upvotes: 6</em></p><p>Skip this question. DataReference is deprecated</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 11 Oct 2022 02:15)</code> - <em>Upvotes: 1</em></p><p>I also checked and I confirm this information. Microsoft documentation says DataReference is no longer the recommended way.</p></blockquote>
<blockquote><p><strong>mis96</strong> <code>(Mon 08 Aug 2022 15:13)</code> - <em>Upvotes: 1</em></p><p>Deprecated</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Sun 09 Jan 2022 07:19)</code> - <em>Upvotes: 1</em></p><p>Why in training step we need &quot;data_output&quot; twice?</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Wed 29 Nov 2023 19:09)</code> - <em>Upvotes: 1</em></p><p>one for console input, and another input by default. and they lost output for the training step at all.</p></blockquote>
<blockquote><p><strong>Roszu</strong> <code>(Fri 05 Aug 2022 19:15)</code> - <em>Upvotes: 1</em></p><p>once as input and then as output</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Sat 27 Nov 2021 21:03)</code> - <em>Upvotes: 6</em></p><p>the answer is correct.</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Wed 02 Mar 2022 01:22)</code> - <em>Upvotes: 2</em></p><p>The answer should be yes.</p></blockquote>
<blockquote><p><strong>ac45863</strong> <code>(Thu 07 Oct 2021 23:49)</code> - <em>Upvotes: 5</em></p><p>I&#x27;m not sure if it&#x27;s correct. Maybe data_output should be passed as an argument also in the 1st step?</p></blockquote>
<blockquote><p><strong>scipio</strong> <code>(Wed 17 Nov 2021 13:11)</code> - <em>Upvotes: 5</em></p><p>I agree with that. The script &quot;process.py&quot; on the first step does not know the output folder data_output (-&gt; reference to datastore) if it is not passed by argument.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Wed 14 Aug 2024 02:23)</code> - <em>Upvotes: 1</em></p><p>this is what i exactly thought</p></blockquote>
<blockquote><p><strong>medsimus</strong> <code>(Sat 02 Oct 2021 15:19)</code> - <em>Upvotes: 2</em></p><p>https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.data_reference.datareference?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Sun 19 Sep 2021 05:20)</code> - <em>Upvotes: 2</em></p><p>DataReference() exist?</p></blockquote>
<blockquote><p><strong>treadst0ne</strong> <code>(Wed 22 Dec 2021 01:58)</code> - <em>Upvotes: 1</em></p><p>Yes.
https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.data_reference.datareference?view=azure-ml-py</p></blockquote>

</details>

---

[<< Previous Question](question_259.md) | [Home](/index.md) | [Next Question >>](question_261.md)
