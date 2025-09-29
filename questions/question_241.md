# Question 241

HOTSPOT -

You publish a batch inferencing pipeline that will be used by a business application.

The application developers need to know which information should be submitted to and returned by the REST interface for the published pipeline.

You need to identify the information required in the REST request and returned as a response from the published pipeline.

Which values should you use in the REST request and to expect in the response? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q241_q_0023800001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q241_ans_0_0023900001.png" alt="Answer Image"><br>
<p>Box 1: JSON containing an OAuth bearer token</p>
<p>Specify your authentication header in the request.</p>
<p>To run the pipeline from the REST endpoint, you need an OAuth2 Bearer-type authentication header.</p>
<p>Box 2: JSON containing the experiment name</p>
<p>Add a JSON payload object that has the experiment name.</p>
<p>Example:</p>
<p>rest_endpoint = published_pipeline.endpoint</p>
<p>response = requests.post(rest_endpoint,</p>
<p>headers=auth_header,</p>
<p>json={&quot;ExperimentName&quot;: &quot;batch_scoring&quot;,</p>
<p>&quot;ParameterAssignments&quot;: {&quot;process_count_per_node&quot;: 6}})</p>
<p>run_id = response.json()[&quot;Id&quot;]</p>
<p>Box 3: JSON containing the run ID</p>
<p>Make the request to trigger the run. Include code to access the Id key from the response dictionary to get the value of the run ID.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-pipeline-batch-scoring-classification</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>datamijn</strong> <code>(Mon 02 Aug 2021 09:00)</code> - <em>Upvotes: 9</em></p><p>on exam 2/8/2021</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Sun 25 Jul 2021 02:53)</code> - <em>Upvotes: 8</em></p><p>response = requests.post(rest_endpoint, 
                         headers=auth_header, 
                         json={&quot;ExperimentName&quot;: &quot;Tutorial-Batch-Scoring&quot;,
                               &quot;ParameterAssignments&quot;: {&quot;process_count_per_node&quot;: 6}})
run_id = response.json()[&quot;Id&quot;]

https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-pipeline-batch-scoring-classification</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Sun 24 Nov 2024 20:30)</code> - <em>Upvotes: 1</em></p><p>I didn&#x27;t find this in the V2 documentation, can you help me by sending the updated link?</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Tue 05 Dec 2023 10:42)</code> - <em>Upvotes: 4</em></p><p>In the Request Header, you should select &quot;JSON containing an OAuth bearer token&quot;.

In the Request Body, you should select &quot;JSON containing the pipeline ID&quot; ---&gt; The run ID would not be included here because it is generated after the pipeline is initiated, and the experiment name is typically not required in the request body for a pipeline execution.

The Response will contain the &quot;JSON containing the run ID&quot; because it is generated after the pipeline runs. It should also contain &quot;JSON containing a list of predictions&quot; since this is the output of a batch inference pipeline. And if the pipeline is configured to save outputs to a file, &quot;JSON containing a path to the parallel_run_step.txt output file&quot; would also be included.

SaM</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Sun 24 Nov 2024 20:30)</code> - <em>Upvotes: 1</em></p><p>I didn&#x27;t find this in the V2 documentation, can you help me by sending the updated link?</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Thu 19 Oct 2023 03:36)</code> - <em>Upvotes: 1</em></p><p>The answer is correct.

- Request header: OAuth bear token
- Request body: Experiment name
- Response: run_id

Request https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-pipelines?view=azureml-api-1#run-a-published-pipeline

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-pipelines?view=azureml-api-1#run-a-published-pipeline-using-c

[DataContract]
public class SubmitPipelineRunRequest
{
    [DataMember]
    public string ExperimentName { get; set; }
...

Return run_id: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-pipelines?view=azureml-api-1#submit-a-job-to-a-pipeline-endpoint</p></blockquote>
<blockquote><p><strong>orionduo</strong> <code>(Thu 31 Aug 2023 06:36)</code> - <em>Upvotes: 1</em></p><p>correct
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-pipelines?view=azureml-api-1</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 20 Jul 2023 02:01)</code> - <em>Upvotes: 2</em></p><p>Request Header:
JSON containing an OAuth bearer token

Request Body:
JSON containing the pipeline ID

Response:
JSON containing the run ID
JSON containing a list of predictions</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Wed 28 Jun 2023 12:12)</code> - <em>Upvotes: 2</em></p><p>Not correct answer. Correct from ChatGPT is:
The values required in the REST request and expected in the response for the published pipeline are as follows:

Request Header: JSON containing an Auth bearer token
Request Body: JSON containing the run ID
Response: JSON containing the run ID and JSON containing a list of predictions</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Wed 08 Mar 2023 12:19)</code> - <em>Upvotes: 2</em></p><p>on exam 07/March/2023</p></blockquote>
<blockquote><p><strong>Manjari_002</strong> <code>(Sun 06 Aug 2023 05:09)</code> - <em>Upvotes: 1</em></p><p>Ans&gt;&gt;???</p></blockquote>
<blockquote><p><strong>racnaoamo</strong> <code>(Thu 19 May 2022 07:56)</code> - <em>Upvotes: 6</em></p><p>on exam 18-5-22</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Mon 21 Feb 2022 09:50)</code> - <em>Upvotes: 1</em></p><p>request_headers = { &quot;Content-Type&quot;:&quot;application/json&quot;,
                    &quot;Authorization&quot;:&quot;Bearer &quot; + key_or_token }

# Call the service
response = requests.post(url = endpoint,
                         data = json_data,
                         headers = request_headers)
https://docs.microsoft.com/en-us/learn/modules/register-and-deploy-model-with-amls/3-consume-model</p></blockquote>
<blockquote><p><strong>Crusader2k13</strong> <code>(Mon 19 Dec 2022 23:40)</code> - <em>Upvotes: 1</em></p><p>We are talking about batch inference, your link is the documentation for realtime inference!</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Fri 03 Sep 2021 07:33)</code> - <em>Upvotes: 2</em></p><p>on 2/9/21</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Sun 11 Jul 2021 14:08)</code> - <em>Upvotes: 3</em></p><p>On exam 2021/7/10</p></blockquote>

</details>

---

[<< Previous Question](question_240.md) | [Home](/index.md) | [Next Question >>](question_242.md)
