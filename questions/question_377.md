# Question 377

You create a multi-class image classification deep learning model.

You train the model by using PyTorch version 1.2.

You need to ensure that the correct version of PyTorch can be identified for the inferencing environment when the model is deployed.

What should you do?

- A.Save the model locally as a.pt file, and deploy the model as a local web service.
- B.Deploy the model on computer that is configured to use the default Azure Machine Learning conda environment.
- C.Register the model with a .pt file extension and the default version property.
- D.Register the model, specifying the model_framework and model_framework_version properties.

<details>
  <summary>Show Suggested Answer</summary>

<strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>rishi_ram</strong> <code>(Tue 07 Dec 2021 13:38)</code> - <em>Upvotes: 10</em></p><p>Question was there in June 2021 Exam</p></blockquote>
<blockquote><p><strong>shuvovertigo</strong> <code>(Sat 18 Dec 2021 23:19)</code> - <em>Upvotes: 8</em></p><p>You can view these two properties in the Model.register() section here, which takes model framework and framework version
https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py#register-workspace--model-path--model-name--tags-none--properties-none--description-none--datasets-none--model-framework-none--model-framework-version-none--child-paths-none--sample-input-dataset-none--sample-output-dataset-none--resource-configuration-none-</p></blockquote>
<blockquote><p><strong>treadst0ne</strong> <code>(Mon 20 Dec 2021 19:41)</code> - <em>Upvotes: 1</em></p><p>I agree.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 11:03)</code> - <em>Upvotes: 1</em></p><p>D is correct:
pecifying the model_framework and model_framework_version properties when registering the model, you provide metadata that informs Azure Machine Learning about the specific framework and version used to train the model.</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Sun 19 Jun 2022 11:42)</code> - <em>Upvotes: 3</em></p><p>I agree with D</p></blockquote>
<blockquote><p><strong>Tehseen</strong> <code>(Thu 23 Dec 2021 12:52)</code> - <em>Upvotes: 2</em></p><p>The answer is correct.

Check API for model registering.
https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.run.run?view=azure-ml-py#register-model-model-name--model-path-none--tags-none--properties-none--model-framework-none--model-framework-version-none--description-none--datasets-none--sample-input-dataset-none--sample-output-dataset-none--resource-configuration-none----kwargs-</p></blockquote>

<blockquote><p><strong>ACSC</strong> <code>(Tue 02 Nov 2021 11:14)</code> - <em>Upvotes: 4</em></p><p>Answer is C. https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.dnn.pytorch?view=azure-ml-py#default-version----1-4-</p></blockquote>
<blockquote><p><strong>Haisheng_Zhang</strong> <code>(Wed 13 Oct 2021 05:36)</code> - <em>Upvotes: 1</em></p><p>https://docs.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.dnn.pytorch?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Fri 17 Sep 2021 03:33)</code> - <em>Upvotes: 1</em></p><p>model_framework is Model&#x27;s property
https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Fri 17 Sep 2021 03:26)</code> - <em>Upvotes: 1</em></p><p>https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.webservice(class)?view=azure-ml-py#run-input-</p></blockquote>

</details>

---

[<< Previous Question](question_376.md) | [Home](../index.md) | [Next Question >>](question_378.md)
