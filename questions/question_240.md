# Question 240

HOTSPOT -

You are running Python code interactively in a Conda environment. The environment includes all required Azure Machine Learning SDK and MLflow packages.

You must use MLflow to log metrics in an Azure Machine Learning experiment named mlflow-experiment.

How should you complete the code? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q240_q_0024500001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q240_ans_0_0024600001.png" alt="Answer Image"><br>
<p>Box 1: mlflow.set_tracking_uri(ws.get_mlflow_tracking_uri())</p>
<p>In the following code, the get_mlflow_tracking_uri() method assigns a unique tracking URI address to the workspace, ws, and set_tracking_uri() points the MLflow tracking URI to that address. mlflow.set_tracking_uri(ws.get_mlflow_tracking_uri())</p>
<p>Box 2: mlflow.set_experiment(experiment_name)</p>
<p>Set the MLflow experiment name with set_experiment() and start your training run with start_run().</p>
<p>Box 3: mlflow.start_run()</p>
<p>Box 4: mlflow.log_metric -</p>
<p>Then use log_metric() to activate the MLflow logging API and begin logging your training run metrics.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Wed 11 Jan 2023 15:08)</code> - <em>Upvotes: 6</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>MattAnya</strong> <code>(Thu 04 Jul 2024 05:48)</code> - <em>Upvotes: 4</em></p><p>on 03 Jan2023</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Thu 20 Apr 2023 09:47)</code> - <em>Upvotes: 2</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Fri 03 Mar 2023 08:34)</code> - <em>Upvotes: 2</em></p><p>Not exactly but similar question on 2/9/21</p></blockquote>
<blockquote><p><strong>VJPrakash</strong> <code>(Sat 11 Feb 2023 17:25)</code> - <em>Upvotes: 4</em></p><p>on exam in August 2021</p></blockquote>
<blockquote><p><strong>datamijn</strong> <code>(Thu 02 Feb 2023 10:01)</code> - <em>Upvotes: 3</em></p><p>on exam 2/8/2021</p></blockquote>
<blockquote><p><strong>MohsenSic</strong> <code>(Fri 30 Dec 2022 04:34)</code> - <em>Upvotes: 1</em></p><p>Anybody knows why run.log is wrong in the last box, we have this example from MS run.log(&#x27;n_estimators&#x27;,  np.int(args.n_estimators)), so , run.log () is fine as well</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Sat 07 Jan 2023 12:46)</code> - <em>Upvotes: 2</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-mlflow
import mlflow
with mlflow.start_run():
    mlflow.log_metric(&#x27;example&#x27;, 1.23)</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Thu 01 Dec 2022 13:27)</code> - <em>Upvotes: 3</em></p><p>Answer is correct though there is some syntax error in the question itself anyway answer would be same as mentioned.</p></blockquote>
<blockquote><p><strong>joysail</strong> <code>(Sun 06 Nov 2022 02:32)</code> - <em>Upvotes: 1</em></p><p>box 2 - set with experiment name</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Sun 18 Sep 2022 05:42)</code> - <em>Upvotes: 3</em></p><p>syntax error in box 2. correct systax ends with colon
with mlflow.start_run():</p></blockquote>

</details>

---

[<< Previous Question](question_239.md) | [Home](/index.md) | [Next Question >>](question_241.md)
