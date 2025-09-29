# Question 222

DRAG DROP -

You plan to explore demographic data for home ownership in various cities. The data is in a CSV file with the following format: age,city,income,home_owner

21,Chicago,50000,0

35,Seattle,120000,1

23,Seattle,65000,0

45,Seattle,130000,1

18,Chicago,48000,0

You need to run an experiment in your Azure Machine Learning workspace to explore the data and log the results. The experiment must log the following information:

✑ the number of observations in the dataset

✑ a box plot of income by home_owner

✑ a dictionary containing the city names and the average income for each city

You need to use the appropriate logging methods of the experiment's run object to log the required information.

How should you complete the code? To answer, drag the appropriate code segments to the correct locations. Each code segment may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

Select and Place:

![Question Image](images/q222_q_0021200001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q222_ans_0_0021300001.png" alt="Answer Image"><br>
<p>Box 1: log -</p>
<p>The number of observations in the dataset.</p>
<p>run.log(name, value, description=&#x27;&#x27;)</p>
<p>Scalar values: Log a numerical or string value to the run with the given name. Logging a metric to a run causes that metric to be stored in the run record in the experiment. You can log the same metric multiple times within a run, the result being considered a vector of that metric.</p>
<p>Example: run.log(&quot;accuracy&quot;, 0.95)</p>
<p>Box 2: log_image -</p>
<p>A box plot of income by home_owner.</p>
<p>log_image Log an image to the run record. Use log_image to log a .PNG image file or a matplotlib plot to the run. These images will be visible and comparable in the run record.</p>
<p>Example: run.log_image(&quot;ROC&quot;, plot=plt)</p>
<p>Box 3: log_table -</p>
<p>A dictionary containing the city names and the average income for each city. log_table: Log a dictionary object to the run with the given name.</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>SnowCheetah</strong> <code>(Thu 29 Dec 2022 02:57)</code> - <em>Upvotes: 26</em></p><p>The Answer is correct

First is straightforward to store a single value is using log()

Second since code try to save pyplot graph = image 
the second answer is log_image()

On Last question Based on to_dict function https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html

to save log with that format The last answer should use log_table()

https://stackoverflow.com/questions/65156959/what-are-the-various-run-metrics-that-can-be-added-in-run-in-azureml</p></blockquote>
<blockquote><p><strong>Dilesha</strong> <code>(Mon 19 Aug 2024 00:41)</code> - <em>Upvotes: 9</em></p><p>On Exam 17 Feb 2023</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Thu 18 Apr 2024 07:56)</code> - <em>Upvotes: 4</em></p><p>Correct.

https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>racnaoamo</strong> <code>(Sun 19 Nov 2023 08:53)</code> - <em>Upvotes: 3</em></p><p>similar question on 18-5-22</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Thu 20 Apr 2023 09:45)</code> - <em>Upvotes: 3</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Fri 07 Apr 2023 20:14)</code> - <em>Upvotes: 2</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>mthombenindhl84</strong> <code>(Sat 11 Mar 2023 23:01)</code> - <em>Upvotes: 2</em></p><p>on exam 11/9/2021</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Fri 03 Mar 2023 08:31)</code> - <em>Upvotes: 3</em></p><p>on 2/9/21</p></blockquote>
<blockquote><p><strong>dushmantha</strong> <code>(Tue 28 Feb 2023 14:18)</code> - <em>Upvotes: 3</em></p><p>On exam 2021/08/31</p></blockquote>
<blockquote><p><strong>datamijn</strong> <code>(Thu 02 Feb 2023 09:49)</code> - <em>Upvotes: 3</em></p><p>on 2/8/2021</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Mon 26 Dec 2022 10:12)</code> - <em>Upvotes: 4</em></p><p>yes given answer is correct
https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Sat 26 Nov 2022 17:09)</code> - <em>Upvotes: 2</em></p><p>i think the last one is list</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Tue 07 Feb 2023 13:38)</code> - <em>Upvotes: 1</em></p><p>For log a dictionary you need to use the log_table() function</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Sat 26 Nov 2022 17:10)</code> - <em>Upvotes: 3</em></p><p>wrong, the answer is correct.https://stackoverflow.com/questions/65156959/what-are-the-various-run-metrics-that-can-be-added-in-run-in-azureml</p></blockquote>

</details>

---

[<< Previous Question](question_221.md) | [Home](/index.md) | [Next Question >>](question_223.md)
