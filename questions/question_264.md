# Question 264

You use the Azure Machine Learning SDK in a notebook to run an experiment using a script file in an experiment folder.

The experiment fails.

You need to troubleshoot the failed experiment.

What are two possible ways to achieve this goal? Each correct answer presents a complete solution.

- A.Use the get_metrics() method of the run object to retrieve the experiment run logs.
- B.Use the get_details_with_logs() method of the run object to display the experiment run logs.
- C.View the log files for the experiment run in the experiment folder.
- D.View the logs for the experiment run in Azure Machine Learning studio.
- E.Use the get_output() method of the run object to retrieve the experiment run logs.

<details>
  <summary>Show Suggested Answer</summary>

<strong>BD</strong><br>

<p>Use get_details_with_logs() to fetch the run details and logs created by the run.</p>
<p>You can monitor Azure Machine Learning runs and view their logs with the Azure Machine Learning studio.</p>
<p>Incorrect Answers:</p>
<p>A: You can view the metrics of a trained model using run.get_metrics().</p>
<p>E: get_output() gets the output of the step as PipelineData.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.steprun https://docs.microsoft.com/en-us/azure/machine-learning/how-to-monitor-view-training-logs</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Mon 11 Jul 2022 14:12)</code> - <em>Upvotes: 5</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 20 Jul 2024 21:15)</code> - <em>Upvotes: 2</em></p><p>ChatGPT
B. Use the get_details_with_logs() method of the run object to display the experiment run logs.
D. View the logs for the experiment run in Azure Machine Learning studio.

These are two ways you could troubleshoot the failed experiment:

B. The get_details_with_logs() method of the run object in the Azure Machine Learning SDK can be used to retrieve the logs from a run of an experiment. These logs would contain details about the execution of the run, which may help in diagnosing the issue.

D. The Azure Machine Learning studio provides a user interface for managing your Azure Machine Learning resources. This includes viewing logs for experiment runs, which can be helpful in troubleshooting issues.</p></blockquote>

<blockquote><p><strong>phdykd</strong> <code>(Wed 21 Feb 2024 20:06)</code> - <em>Upvotes: 1</em></p><p>AB. The two most accurate options to troubleshoot a failed experiment in Azure Machine Learning SDK using a script file in an experiment folder are:

A. Use the get_metrics() method of the run object to retrieve the experiment run logs. B. Use the get_details_with_logs() method of the run object to display the experiment run logs.

Option A and B are both valid ways to access the experiment run logs and can provide valuable information to help diagnose the cause of the failed experiment. Option D is also a valid option, but it may not be as convenient as using the SDK methods within the notebook.</p></blockquote>

<blockquote><p><strong>kkkk_jjjj</strong> <code>(Sat 18 Mar 2023 09:45)</code> - <em>Upvotes: 4</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Sun 06 Nov 2022 23:03)</code> - <em>Upvotes: 4</em></p><p>on 6 Nov 2021</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Thu 20 Oct 2022 09:51)</code> - <em>Upvotes: 2</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>Abhinav_nasaiitkgp</strong> <code>(Sun 23 Jan 2022 23:05)</code> - <em>Upvotes: 3</em></p><p>Why not C? I think BCD all the three are correct. Or there is something which is missing in the question</p></blockquote>
<blockquote><p><strong>wjrmffldrhrl</strong> <code>(Thu 10 Mar 2022 00:23)</code> - <em>Upvotes: 12</em></p><p>It seems that the log files are not saved in the &quot;experiment folder&quot;. It will be saved in the logs folder (e.g. azureml-logs, logs/azureml).

https://docs.microsoft.com/en-us/azure/machine-learning/how-to-monitor-view-training-logs#azureml-logs-folder</p></blockquote>

</details>

---

[<< Previous Question](question_263.md) | [Home](../index.md) | [Next Question >>](question_265.md)
