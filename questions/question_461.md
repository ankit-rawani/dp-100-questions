# Question 461

HOTSPOT -

You write code to retrieve an experiment that is run from your Azure Machine Learning workspace.

The run used the model interpretation support in Azure Machine Learning to generate and upload a model explanation.

Business managers in your organization want to see the importance of the features in the model.

You need to print out the model features and their relative importance in an output that looks similar to the following.

![Question Image](images/q461_q_0041500001.png)

How should you complete the code? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q461_q_0041600001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q461_ans_0_image619.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jiglesia22</strong> <code>(Mon 19 Sep 2022 09:47)</code> - <em>Upvotes: 50</em></p><p>The correct answer is: 
1. client = ExplanationClient.from_run_id() (from_run requires just one parameter and three are being passed here)
2. explanation = client.download_model_explanation()
3. explanation.get_feature_importance_dict()

As dev2dev pointed out: https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/machine-learning/how-to-machine-learning-interpretability-automl.md

Check out in addition: https://docs.microsoft.com/es-es/python/api/azureml-interpret/azureml.interpret.explanationclient?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Sun 04 Dec 2022 10:27)</code> - <em>Upvotes: 8</em></p><p>client = ExplanationClient.from_run_id()# as run_id is passed as parmaeter
explanation = client.download_model_explanation()# as it is mentioned in question it has #been uploaded
feature_importances = explanation .get_feature_importance_dict()</p></blockquote>
<blockquote><p><strong>SnowCheetah</strong> <code>(Sun 25 Dec 2022 09:39)</code> - <em>Upvotes: 1</em></p><p>https://docs.microsoft.com/en-us/python/api/azureml-interpret/azureml.interpret.explanationclient?view=azure-ml-py#from-run-id-workspace--experiment-name--run-id-
for more detail how to use explaination module</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 24 Aug 2024 00:31)</code> - <em>Upvotes: 1</em></p><p>client = ExplanationClient.from_run_id(workspace=ws,
                                       experiment_name=experiment.experiment_name, 
                                       run_id=run.id)
explanation = client.download_model_explanation()
feature_importances = explanation.get_feature_importance_dict()</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Mon 18 Dec 2023 02:51)</code> - <em>Upvotes: 1</em></p><p>On exam 18-06-22</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Mon 18 Sep 2023 08:48)</code> - <em>Upvotes: 3</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Sat 06 May 2023 22:13)</code> - <em>Upvotes: 2</em></p><p>on Exam 6 Nov 2021, the variable should be &quot;client&quot; in the first statement. However, the exam gives exactly the same typo.</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Mon 26 Dec 2022 19:16)</code> - <em>Upvotes: 5</em></p><p>after reading all the comments there is confusion in from_run and froun_run_id (correct answer)so if you follow the below link  ExplanationClient.from_run(run) , it is expecting only 1 parameter and it is used to get an Explanation Client and upload the explanation whereas 
from_run_id is expecting 3 parameter and used to download the explanation
from azureml.contrib.interpret.explanation.explanation_client import ExplanationClient

client = ExplanationClient.from_run_id(workspace=ws,
                                       experiment_name=experiment.experiment_name, 
                                       run_id=run.id)
explanation = client.download_model_explanation()
feature_importances = explanation.get_feature_importance_dict()</p></blockquote>
<blockquote><p><strong>Q95</strong> <code>(Tue 15 Nov 2022 04:27)</code> - <em>Upvotes: 2</em></p><p>Agree with other posters&#x27; answers. Link for reference: https://docs.microsoft.com/en-us/learn/modules/explain-machine-learning-models-with-azure-machine-learning/4-create-explanations (Viewing the explanation section)</p></blockquote>
<blockquote><p><strong>htiwari</strong> <code>(Thu 03 Nov 2022 23:12)</code> - <em>Upvotes: 1</em></p><p>from azureml.interpret import ExplanationClient

# Get the feature explanations
client = ExplanationClient.from_run(run)
engineered_explanations = client.download_model_explanation()
feature_importances = engineered_explanations.get_feature_importance_dict()

# Overall feature importance
print(&#x27;Feature\tImportance&#x27;)
for key, value in feature_importances.items():
    print(key, &#x27;\t&#x27;, value)</p></blockquote>
<blockquote><p><strong>BilJon</strong> <code>(Thu 29 Sep 2022 07:51)</code> - <em>Upvotes: 3</em></p><p>from_run_id(workspace, experiment_name, run_id)</p></blockquote>
<blockquote><p><strong>BilJon</strong> <code>(Thu 29 Sep 2022 07:38)</code> - <em>Upvotes: 4</em></p><p>Correct answer:
from azureml.interpret import ExplanationClient

# Get the feature explanations
client = ExplanationClient.from_run(run)
engineered_explanations = client.download_model_explanation()
feature_importances = engineered_explanations.get_feature_importance_dict()</p></blockquote>
<blockquote><p><strong>anjurad</strong> <code>(Wed 26 Oct 2022 06:26)</code> - <em>Upvotes: 2</em></p><p>I upvoted incorrectly - the code is correct, but it look at the arguments in the associated question brackets - https://docs.microsoft.com/en-us/python/api/azureml-interpret/azureml.interpret.explanationclient?view=azure-ml-py#from-run-id-workspace--experiment-name--run-id-</p></blockquote>
<blockquote><p><strong>stonefl</strong> <code>(Mon 19 Sep 2022 11:00)</code> - <em>Upvotes: 4</em></p><p>client = ExplanationClient.from_run_id(workspace=ws,
                                       experiment_name=experiment.experiment_name, 
                                       run_id=run.id)
explanation = client.download_model_explanation()
feature_importances = explanation.get_feature_importance_dict()</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Sun 18 Sep 2022 07:37)</code> - <em>Upvotes: 1</em></p><p>The correct answer is : 

client = ExplanationClient.from_run(run)
explanation = client.download_model_explanation()
feature_importances = explanation .get_feature_importance_dict()</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Sat 24 Sep 2022 09:07)</code> - <em>Upvotes: 6</em></p><p>sorry, it is from_run_id()

client = ExplanationClient.from_run_id()
explanation = client.download_model_explanation()
feature_importances = explanation .get_feature_importance_dict()</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Sat 17 Sep 2022 15:22)</code> - <em>Upvotes: 3</em></p><p>1 and 2 should be corrected
Full example here: https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/machine-learning/how-to-machine-learning-interpretability-automl.md

from azureml.interpret import ExplanationClient

client = ExplanationClient.from_run(best_run)
raw_explanations = client.download_model_explanation(raw=True)
print(raw_explanations.get_feature_importance_dict())</p></blockquote>
<blockquote><p><strong>bruce</strong> <code>(Sat 08 Oct 2022 10:06)</code> - <em>Upvotes: 1</em></p><p>It should be Run_id since the arguments for the first line has run_id instead of run.</p></blockquote>
<blockquote><p><strong>Anty85</strong> <code>(Sat 17 Sep 2022 11:44)</code> - <em>Upvotes: 2</em></p><p>1. from_run()
2. client.download_model_explanation()
3. explanation.get_feature_importance_dict()</p></blockquote>
<blockquote><p><strong>OmarF</strong> <code>(Thu 15 Sep 2022 18:26)</code> - <em>Upvotes: 1</em></p><p>I think this solution is not correct the correct  one is: 
1. client = ExplanationClient.from_run_id()
2. explanation = client.download_model_explanation()
3. explanation.get_feature_importance_dict()</p></blockquote>
<blockquote><p><strong>ImogenW</strong> <code>(Sun 11 Sep 2022 16:11)</code> - <em>Upvotes: 2</em></p><p>I think this is incorrect, 
1 should be client = Explanation.from_run_id()
2. explanation = client.download_model_explanation()
3. explanation.get_feature_importance_dict()</p></blockquote>

</details>

---

[<< Previous Question](question_460.md) | [Home](/index.md) | [Next Question >>](question_462.md)
