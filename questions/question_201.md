# Question 201

You write a Python script that processes data in a comma-separated values (CSV) file.

You plan to run this script as an Azure Machine Learning experiment.

The script loads the data and determines the number of rows it contains using the following code:

![Question Image](images/q201_q_0018200001.png)

You need to record the row count as a metric named row_count that can be returned using the get_metrics method of the Run object after the experiment run completes.

Which code should you use?

* A.run.upload_file(T3 row_count', './data.csv')
* B.run.log('row_count', rows)
* C.run.tag('row_count', rows)
* D.run.log_table('row_count', rows)
* E.run.log_row('row_count', rows)

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ahson0124</strong> <code>(Tue 15 Aug 2023 12:43)</code> - <em>Upvotes: 6</em></p><p>In exam on 2023-02-15</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 02 Dec 2024 13:09)</code> - <em>Upvotes: 1</em></p><p>run.log(&#x27;row_count&#x27;, rows)</p></blockquote>
<blockquote><p><strong>orionduo</strong> <code>(Thu 29 Feb 2024 13:20)</code> - <em>Upvotes: 1</em></p><p>correct.
Log a numerical or string value to the run with the given name using log. Logging a metric to a run causes that metric to be stored in the run record in the experiment. You can log the same metric multiple times within a run, the result being considered a vector of that metric.</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Sun 06 Aug 2023 16:07)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Sat 15 Jul 2023 19:19)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#remarks</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sun 18 Dec 2022 02:40)</code> - <em>Upvotes: 4</em></p><p>on exam 18-06-22</p></blockquote>
<blockquote><p><strong>racnaoamo</strong> <code>(Sat 19 Nov 2022 08:52)</code> - <em>Upvotes: 3</em></p><p>on exam 18-5-22</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Sat 22 Oct 2022 10:47)</code> - <em>Upvotes: 4</em></p><p>on exam 04/22/2022</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Wed 14 Sep 2022 04:28)</code> - <em>Upvotes: 3</em></p><p>correct</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Sun 14 Aug 2022 09:08)</code> - <em>Upvotes: 1</em></p><p>Correct</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Sun 17 Jul 2022 11:11)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Tue 05 Apr 2022 21:02)</code> - <em>Upvotes: 2</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Thu 03 Mar 2022 08:30)</code> - <em>Upvotes: 2</em></p><p>on 2/9/21</p></blockquote>
<blockquote><p><strong>datamijn</strong> <code>(Wed 02 Feb 2022 09:47)</code> - <em>Upvotes: 3</em></p><p>on 2/8/2021</p></blockquote>

</details>

---

[<< Previous Question](question_200.md) | [Home](/index.md) | [Next Question >>](question_202.md)
