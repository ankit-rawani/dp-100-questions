# Question 387

You use the following Python code in a notebook to deploy a model as a web service: from azureml.core.webservice import AciWebservice from azureml.core.model import InferenceConfig inference_config = InferenceConfig(runtime='python', source_directory='model_files', entry_script='score.py', conda_file='env.yml') deployment_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1) service = Model.deploy(ws, 'my-service', [model], inference_config, deployment_config) service.wait_for_deployment(True)

The deployment fails.

You need to use the Python SDK in the notebook to determine the events that occurred during service deployment an initialization.

Which code segment should you use?

* A.service.state
* B.service.get_logs()
* C.service.serialize()
* D.service.environment

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>
<p>The first step in debugging errors is to get your deployment logs. In Python: service.get_logs()</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-troubleshoot-deployment</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>james2033</strong> <code>(Sun 20 Oct 2024 10:16)</code> - <em>Upvotes: 1</em></p><p>from azureml.core.webservice import AciWebservice
from azureml.core.model import InferenceConfig 

inference_config = InferenceConfig(runtime = &#x27;python&#x27;, source_directory = &#x27;model_files&#x27;, entry_script = &#x27;score.py&#x27;, conda_file = &#x27;env.yml&#x27;)
deployment_config = AciWebservice.deploy_configuration(cpu_cores = 1, memory_gb = 1)
service = Model.deploy(ws, &#x27;my-service&#x27;, [model], inference_config, deployment_config) service.wait_for_deployment(True)

logging like this

ml_client.online_deployments.get_logs(name = &quot;&lt;deployment-name&gt;&quot;, endpoint_name = &quot;&lt;endpoint-name&gt;&quot;, lines=100)

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-troubleshoot-online-endpoints?view=azureml-api-2&amp;tabs=python#get-container-logs</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sun 18 Jun 2023 01:50)</code> - <em>Upvotes: 1</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Wed 12 Apr 2023 01:39)</code> - <em>Upvotes: 1</em></p><p>Duplicate question</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Fri 03 Mar 2023 07:56)</code> - <em>Upvotes: 3</em></p><p>On Exam: 03 March 2022</p></blockquote>
<blockquote><p><strong>nick234987</strong> <code>(Sat 15 Oct 2022 18:42)</code> - <em>Upvotes: 2</em></p><p>Correct answer B</p></blockquote>

</details>

---

[<< Previous Question](question_386.md) | [Home](/index.md) | [Next Question >>](question_388.md)
