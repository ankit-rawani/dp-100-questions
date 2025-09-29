# Question 186

DRAG DROP -

You create a multi-class image classification deep learning experiment by using the PyTorch framework. You plan to run the experiment on an Azure Compute cluster that has nodes with GPU's.

You need to define an Azure Machine Learning service pipeline to perform the monthly retraining of the image classification model. The pipeline must run with minimal cost and minimize the time required to train the model.

Which three pipeline steps should you run in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Select and Place:

![Question Image](images/q186_q_0015400001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q186_ans_0_0015500001.png" alt="Answer Image"><br>
<p>Step 1: Configure a DataTransferStep() to fetch new image dataג€¦</p>
<p>Step 2: Configure a PythonScriptStep() to run image_resize.y on the cpu-compute compute target.</p>
<p>Step 3: Configure the EstimatorStep() to run training script on the gpu_compute computer target.</p>
<p>The PyTorch estimator provides a simple way of launching a PyTorch training job on a compute target.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-train-pytorch</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>chaudha4</strong> <code>(Thu 04 Nov 2021 16:29)</code> - <em>Upvotes: 17</em></p><p>Hope we don&#x27;t see this question in exam since it is covering topics that are all deprecated.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 18 Nov 2022 13:38)</code> - <em>Upvotes: 6</em></p><p>I think the answer is correct, though it might not in the scope of test any more

1. Fetch whole / big image
2. Break into small / tile images
3. Run training models</p></blockquote>
<blockquote><p><strong>haby</strong> <code>(Wed 26 Jun 2024 19:55)</code> - <em>Upvotes: 4</em></p><p>EstimatorStep is deprecated, it&#x27;s recommended to use PythonSriptStep or CommandStep. 

For now(2023-12), I will take :
1. Configure a PythonScriptStep() to run image_fetcher.py on the cpu-compute compute target.
2. Configure a PythonScriptStep() to run image_resize.py on the cpu-compute compute target.
3. Configure an PythonScriptStep() to run an estimator that runs the bird_classifier_train.py model training script on the gpu_compute compute target.</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Wed 19 Jun 2024 11:03)</code> - <em>Upvotes: 1</em></p><p>Based on the requirements to minimize cost and training time for the image classification retraining pipeline, the three steps that should be configured are:

1. Configure a PythonScriptStep() to run image_fetcher.py on the cpu-compute compute target.
2. Configure a PythonScriptStep() to run image_resize.py on the cpu-compute compute target.
3. Configure an EstimatorStep() to run an estimator that runs the bird_classifier_train.py model training script on the gpu_compute compute target.</p></blockquote>
<blockquote><p><strong>giusecozza</strong> <code>(Tue 07 Mar 2023 07:48)</code> - <em>Upvotes: 3</em></p><p>I&#x27;m afraid the first step is wrong, since DataTransferStep is used only to move data between datastores, not fetching data from the web. 

https://docs.microsoft.com/en-us/python/api/azureml-pipeline-steps/azureml.pipeline.steps.data_transfer_step.datatransferstep?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>chevyli</strong> <code>(Tue 28 Feb 2023 06:50)</code> - <em>Upvotes: 3</em></p><p>Look correct</p></blockquote>
<blockquote><p><strong>luisbenitez_14</strong> <code>(Tue 13 Dec 2022 04:10)</code> - <em>Upvotes: 1</em></p><p>Estimator is deprecated. PythonScript is the correct 3rd step</p></blockquote>

</details>

---

[<< Previous Question](question_185.md) | [Home](/index.md) | [Next Question >>](question_187.md)
