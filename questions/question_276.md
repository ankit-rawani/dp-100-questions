# Question 276

You use the Azure Machine Learning Python SDK to define a pipeline to train a model.

The data used to train the model is read from a folder in a datastore.

You need to ensure the pipeline runs automatically whenever the data in the folder changes.

What should you do?

* A.Set the regenerate_outputs property of the pipeline to True
* B.Create a ScheduleRecurrance object with a Frequency of auto. Use the object to create a Schedule for the pipeline
* C.Create a PipelineParameter with a default value that references the location where the training data is stored
* D.Create a Schedule for the pipeline. Specify the datastore in the datastore property, and the folder containing the training data in the path_on_datastore property

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-trigger-published-pipeline</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>azurecert2021</strong> <code>(Mon 10 Jan 2022 16:12)</code> - <em>Upvotes: 12</em></p><p>given answer is correct.
To create a file-reactive Schedule, you must set the datastore parameter in the call to Schedule.create. To monitor a folder, set the path_on_datastore argument.

The polling_interval argument allows you to specify, in minutes, the frequency at which the datastore is checked for changes.

If the pipeline was constructed with a DataPath PipelineParameter, you can set that variable to the name of the changed file by setting the data_path_parameter_name argument.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 07:35)</code> - <em>Upvotes: 1</em></p><p>Nothing but D triggers automatically training when data changed</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sat 20 Apr 2024 03:27)</code> - <em>Upvotes: 1</em></p><p>Quote &#x27;To monitor a folder, set the path_on_datastore argument.&#x27; 

at https://learn.microsoft.com/en-us/azure/machine-learning/how-to-trigger-published-pipeline?view=azureml-api-1#create-a-change-based-schedule 

--&gt; Choose D, where has path_on_datastore</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Thu 20 Apr 2023 09:14)</code> - <em>Upvotes: 3</em></p><p>Correct.
https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-trigger-published-pipeline</p></blockquote>
<blockquote><p><strong>AzureJobsTillRetire</strong> <code>(Wed 23 Aug 2023 19:44)</code> - <em>Upvotes: 1</em></p><p>To run a pipeline on a recurring basis, you&#x27;ll create a schedule. A Schedule associates a pipeline, an experiment, and a trigger. The trigger can either be aScheduleRecurrence that describes the wait between jobs or a Datastore path that specifies a directory to watch for changes.</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Sun 18 Sep 2022 08:45)</code> - <em>Upvotes: 3</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Sat 03 Sep 2022 05:35)</code> - <em>Upvotes: 2</em></p><p>On 03 March 2022</p></blockquote>
<blockquote><p><strong>jed_elhak</strong> <code>(Thu 17 Mar 2022 00:09)</code> - <em>Upvotes: 3</em></p><p>D ..given answer is correct.</p></blockquote>

</details>

---

[<< Previous Question](question_275.md) | [Home](/index.md) | [Next Question >>](question_277.md)
