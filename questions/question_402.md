# Question 402

You have a Python script that executes a pipeline. The script includes the following code: from azureml.core import Experiment pipeline_run = Experiment(ws, 'pipeline_test').submit(pipeline)

You want to test the pipeline before deploying the script.

You need to display the pipeline run details written to the STDOUT output when the pipeline completes.

Which code segment should you add to the test script?

* A.pipeline_run.get.metrics()
* B.pipeline_run.wait_for_completion(show_output=True)
* C.pipeline_param = PipelineParameter(name="stdout", default_value="console")
* D.pipeline_run.get_status()

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>trysec</strong> <code>(Sat 10 Aug 2024 18:26)</code> - <em>Upvotes: 1</em></p><p>The correct answer is B</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Thu 12 Oct 2023 20:21)</code> - <em>Upvotes: 3</em></p><p>Confirmed, given answer is correct.</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Mon 18 Sep 2023 08:48)</code> - <em>Upvotes: 4</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Wed 13 Sep 2023 04:42)</code> - <em>Upvotes: 1</em></p><p>Given answer B is correct</p></blockquote>
<blockquote><p><strong>Tsardoz</strong> <code>(Sat 15 Jul 2023 10:58)</code> - <em>Upvotes: 2</em></p><p>agree with answer &quot;when the pipeline completes&quot; is key</p></blockquote>

</details>

---

[<< Previous Question](question_401.md) | [Home](/index.md) | [Next Question >>](question_403.md)
