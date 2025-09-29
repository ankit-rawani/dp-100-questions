# Question 398

HOTSPOT -

You create an Azure Machine Learning workspace.

You need to detect data drift between a baseline dataset and a subsequent target dataset by using the DataDriftDetector class.

How should you complete the code segment? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q398_q_0040300001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q398_ans_0_0040400001.png" alt="Answer Image"><br>
<p>Box 1: create_from_datasets -</p>
<p>The create_from_datasets method creates a new DataDriftDetector object from a baseline tabular dataset and a target time series dataset.</p>
<p>Box 2: backfill -</p>
<p>The backfill method runs a backfill job over a given specified start and end date.</p>
<p>Syntax: backfill(start_date, end_date, compute_target=None, create_compute_target=False)</p>
<p>Incorrect Answers:</p>
<p>List and update do not have datetime parameters.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-datadrift/azureml.datadrift.datadriftdetector(class)</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>AjoseO</strong> <code>(Sat 03 Sep 2022 06:58)</code> - <em>Upvotes: 5</em></p><p>On Exam: 03 March 2022</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 20:25)</code> - <em>Upvotes: 1</em></p><p>Given answer is correct: create_from_datasets  and   backfill

# Instantiate a DataDriftDetector object with the necessary parameters for data drift detection
monitor = DataDriftDetector.create_from_datasets(ws, &#x27;drift-monitor&#x27;, baseline, 
                                                 target, compute_target=&#x27;cpu-cluster&#x27;, 
                                                 frequency=&#x27;Week&#x27;, feature_list=None, 
                                                 drift_threshold=6, latency=24)

# Run the data drift analysis over the specified time period from the start date to today
complete = monitor.backfill(datetime(2021, 1, 1), datetime.today())</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sat 20 Apr 2024 10:36)</code> - <em>Upvotes: 1</em></p><p>azureml.datadrift.DataDriftDetector.backfill() --&gt; Run a backfill job over a given specified start and end date.

azureml.datadrift.DataDriftDetector.create_from_dataset() --&gt; Create a new DataDriftDectector object from baseline tabular dataset and set a target time series dataset.

https://learn.microsoft.com/en-us/python/api/azureml-datadrift/azureml.datadrift.datadriftdetector.datadriftdetector?view=azure-ml-py#methods

choose 1) create_from_datasets(...) 2) backfill(...) . Very clear.</p></blockquote>
<blockquote><p><strong>Tsardoz</strong> <code>(Fri 15 Jul 2022 10:54)</code> - <em>Upvotes: 4</em></p><p>Agree with answer.</p></blockquote>

</details>

---

[<< Previous Question](question_397.md) | [Home](/index.md) | [Next Question >>](question_399.md)
