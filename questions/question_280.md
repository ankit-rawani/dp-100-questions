# Question 280

You run a script as an experiment in Azure Machine Learning.

You have a Run object named run that references the experiment run. You must review the log files that were generated during the experiment run.

You need to download the log files to a local folder for review.

Which two code segments can you run to achieve this goal? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

* A.run.get_details()
* B.run.get_file_names()
* C.run.get_metrics()
* D.run.download_files(output_directory='./runfiles')
* E.run.get_all_logs(destination='./runlogs')

<details>
  <summary>Show Suggested Answer</summary>

  <strong>DE</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Oliverto</strong> <code>(Thu 07 Jul 2022 13:20)</code> - <em>Upvotes: 9</em></p><p>D &amp; E
&quot;You need to download the log files to a local folder for review.&quot;  
Only D&amp;E downloads data.</p></blockquote>
<blockquote><p><strong>zehraoneexam</strong> <code>(Mon 19 Sep 2022 07:40)</code> - <em>Upvotes: 1</em></p><p>No, you re downloading with the E.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 07:40)</code> - <em>Upvotes: 2</em></p><p># Assuming &#x27;run&#x27; is your Run object

# Download all files associated with the run to a local directory
run.download_files(output_directory=&#x27;./runfiles&#x27;)

# Download all logs associated with the run to a local directory
run.get_all_logs(destination=&#x27;./runlogs&#x27;)</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Sat 03 Aug 2024 05:14)</code> - <em>Upvotes: 1</em></p><p>get details also gives current log files, so why it is incorrect?

https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 22 Aug 2023 02:11)</code> - <em>Upvotes: 2</em></p><p>D. run.download_files(output_directory=&#x27;./runfiles&#x27;)
E. run.get_all_logs(destination=&#x27;./runlogs&#x27;)

Explanation:

Option D (run.download_files(output_directory=&#x27;./runfiles&#x27;)) downloads all the files generated during the experiment run to a local folder named &quot;runfiles&quot; in the current working directory. This includes the log files and any other files generated during the experiment.

Option E (run.get_all_logs(destination=&#x27;./runlogs&#x27;)) downloads all the logs generated during the experiment run to a local folder named &quot;runlogs&quot; in the current working directory. This includes any stdout and stderr output generated during the experiment run.

Option A (run.get_details()) returns the details of the experiment run, such as the start time, end time, and run ID, but it does not download any files.

Option B (run.get_file_names()) returns the names of all the files generated during the experiment run, but it does not download any files.

Option C (run.get_metrics()) returns any metrics collected during the experiment run, but it does not download any files.</p></blockquote>
<blockquote><p><strong>PremPatrick</strong> <code>(Mon 15 May 2023 01:59)</code> - <em>Upvotes: 1</em></p><p>For Downloads D,E</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Thu 08 Dec 2022 12:08)</code> - <em>Upvotes: 1</em></p><p>A is not correct, get_details_with_log will download the log file content, otherwise, just show log file name</p></blockquote>
<blockquote><p><strong>WeiD</strong> <code>(Tue 15 Nov 2022 15:25)</code> - <em>Upvotes: 2</em></p><p>D &amp; E
download_files	
Download files from a given storage prefix (folder name) or the entire container if prefix is unspecified.
get_all_logs	
Download all logs for the run to a directory.</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 11 Oct 2022 18:54)</code> - <em>Upvotes: 2</em></p><p>D and E
Reference: https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml-core-run-get-all-logs</p></blockquote>
<blockquote><p><strong>Thornehead</strong> <code>(Thu 29 Sep 2022 01:34)</code> - <em>Upvotes: 1</em></p><p>It is absolutely D and E.

https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run(class)?view=azure-ml-py#azureml-core-run-get-all-logs</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Sun 18 Sep 2022 08:46)</code> - <em>Upvotes: 4</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Tue 19 Jul 2022 15:23)</code> - <em>Upvotes: 2</em></p><p>download log files to local folder.</p></blockquote>

</details>

---

[<< Previous Question](question_279.md) | [Home](/index.md) | [Next Question >>](question_281.md)
