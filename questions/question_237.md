# Question 237

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You plan to use a Python script to run an Azure Machine Learning experiment. The script creates a reference to the experiment run context, loads data from a file, identifies the set of unique values for the label column, and completes the experiment run:

![Question Image](images/q237_q_0023600001.png)

The experiment must record the unique labels in the data as metrics for the run that can be reviewed later.

You must add code to the script to record the unique label values as run metrics at the point indicated by the comment.

Solution: Replace the comment with the following code:

for label_val in label_vals:

run.log('Label Values', label_val)

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>giusecozza</strong> <code>(Wed 07 Sep 2022 09:29)</code> - <em>Upvotes: 10</em></p><p>answer A is correct, no doubt.
&quot;Logging a metric to a run causes that metric to be stored in the run record in the experiment. You can log the same metric multiple times within a run, the result being considered a vector of that metric. If step is specified for a metric it must be specified for all values.&quot;

https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml-core-run-log</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Tue 18 Jan 2022 10:42)</code> - <em>Upvotes: 9</em></p><p>why not run.log_list

Log a list of values to the run with the given name using log_list.

Example: run.log_list(&quot;accuracies&quot;, [0.6, 0.7, 0.87])

https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>f82411e</strong> <code>(Fri 06 Jun 2025 12:08)</code> - <em>Upvotes: 1</em></p><p>for is the answer, A</p></blockquote>
<blockquote><p><strong>KeiNek</strong> <code>(Mon 10 Feb 2025 14:58)</code> - <em>Upvotes: 1</em></p><p>A. 
for label_val in label_vals:
      run.log(&#x27;Label Values&#x27;, label_val)</p></blockquote>
<blockquote><p><strong>testgm</strong> <code>(Sat 30 Nov 2024 15:43)</code> - <em>Upvotes: 1</em></p><p>correct answer is A</p></blockquote>
<blockquote><p><strong>Stemix</strong> <code>(Mon 18 Mar 2024 14:16)</code> - <em>Upvotes: 1</em></p><p>Answer A is correct since we are looping all the elements of the array. So log is fine(and not log_list) because every time we are logging a scalar</p></blockquote>
<blockquote><p><strong>Karthikat</strong> <code>(Tue 05 Mar 2024 20:47)</code> - <em>Upvotes: 1</em></p><p>answer A is correct, here performance is not consideration. It does the job</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Tue 13 Feb 2024 04:51)</code> - <em>Upvotes: 1</em></p><p>Why A is not the correct. it logs all the values one at a time. For sure log_list is better solution, but for loop here also works in my opinion</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Thu 21 Dec 2023 05:33)</code> - <em>Upvotes: 2</em></p><p>The best solution is to use the run.log_list method, which can log a list of values as a metric</p></blockquote>
<blockquote><p><strong>Hisayuki</strong> <code>(Mon 06 Nov 2023 07:34)</code> - <em>Upvotes: 1</em></p><p>unique() creates the array. So run.log_list should be used.
-----
u = df[&#x27;state&#x27;].unique()
print(u)
print(type(u))
# [&#x27;NY&#x27; nan &#x27;CA&#x27; &#x27;TX&#x27;]
# &lt;class &#x27;numpy.ndarray&#x27;&gt;</p></blockquote>
<blockquote><p><strong>colin1919</strong> <code>(Wed 25 Oct 2023 15:07)</code> - <em>Upvotes: 1</em></p><p>(1) Should be log_list()
(2) Should be a list not np.array</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Wed 28 Jun 2023 12:07)</code> - <em>Upvotes: 1</em></p><p>YES - ChatGPT
Yes, the solution meets the goal. The provided code snippet correctly loads the data from a CSV file, identifies the unique values in the label column, and logs each unique label value as a run metric using the run.log() function. Finally, the run.complete() function is called to indicate the completion of the experiment run.

The unique label values will be recorded as run metrics and can be reviewed later.</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Wed 28 Jun 2023 12:07)</code> - <em>Upvotes: 1</em></p><p>YES - ChatGPT
Yes, the solution meets the goal. The provided code snippet correctly loads the data from a CSV file, identifies the unique values in the label column, and logs each unique label value as a run metric using the run.log() function. Finally, the run.complete() function is called to indicate the completion of the experiment run.

The unique label values will be recorded as run metrics and can be reviewed later.</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Mon 06 Feb 2023 20:34)</code> - <em>Upvotes: 5</em></p><p>the answer is correct because we are looping on label_vals array</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Thu 08 Dec 2022 08:00)</code> - <em>Upvotes: 1</em></p><p>Correct (A) - run.log(‘Label Values’, label_val)</p></blockquote>
<blockquote><p><strong>casiopa</strong> <code>(Fri 09 Dec 2022 12:55)</code> - <em>Upvotes: 1</em></p><p>Why not run.log_list() ?

run.log_list(&#x27;Label Values, label_val) or
run.log_list(&#x27;Label Values&#x27;, list((label_val))</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Thu 08 Dec 2022 08:01)</code> - <em>Upvotes: 1</em></p><p>SORRY! Accidentally clicked on B, but meant to vote for A</p></blockquote>
<blockquote><p><strong>zb99</strong> <code>(Wed 08 Jun 2022 15:32)</code> - <em>Upvotes: 3</em></p><p>Read the sample code carefully.  It is actually a loop logging each value individually, not the list all at once.</p></blockquote>
<blockquote><p><strong>chevyli</strong> <code>(Wed 31 Aug 2022 05:16)</code> - <em>Upvotes: 1</em></p><p>So the code will log the same metric named &#x27;label values&#x27; multiple times. This seems not the expected result.</p></blockquote>
<blockquote><p><strong>racnaoamo</strong> <code>(Thu 19 May 2022 07:56)</code> - <em>Upvotes: 1</em></p><p>similar question on 18-5-22</p></blockquote>

</details>

---

[<< Previous Question](question_236.md) | [Home](/index.md) | [Next Question >>](question_238.md)
