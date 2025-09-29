# Question 394

You are a data scientist working for a hotel booking website company. You use the Azure Machine Learning service to train a model that identifies fraudulent transactions.

You must deploy the model as an Azure Machine Learning real-time web service using the Model.deploy method in the Azure Machine Learning SDK. The deployed web service must return real-time predictions of fraud based on transaction data input.

You need to create the script that is specified as the entry_script parameter for the InferenceConfig class used to deploy the model.

What should the entry script do?

- A.Register the model with appropriate tags and properties.
- B.Create a Conda environment for the web service compute and install the necessary Python packages.
- C.Load the model and use it to predict labels from input data.
- D.Start a node on the inference cluster where the web service is deployed.
- E.Specify the number of cores and the amount of memory required for the inference compute.

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ljljljlj</strong> <code>(Sun 11 Jul 2021 14:21)</code> - <em>Upvotes: 11</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Fri 06 May 2022 09:46)</code> - <em>Upvotes: 8</em></p><p>Following the given link, the workflow to deploy a model is:

1. Register the model.
2. Prepare an entry script.
3. Prepare an inference configuration.
4. Deploy the model locally to ensure everything works.
5. Choose a compute target.
6. Deploy the model to the cloud.
7. Test the resulting web service.

We are in interested in step 2., and this step can be divided in:
2.1. LOADING YOUR MODEL (using a function called init())
2.2. Running your model on input data (using a function called run())</p></blockquote>

<blockquote><p><strong>Fefnut</strong> <code>(Wed 13 Nov 2024 12:57)</code> - <em>Upvotes: 1</em></p><p>Response C is correct: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-deploy-and-where?view=azureml-api-1&amp;tabs=azcli</p></blockquote>
<blockquote><p><strong>bbe8966</strong> <code>(Sat 22 Jun 2024 10:20)</code> - <em>Upvotes: 1</em></p><p>The answer is correct</p></blockquote>
<blockquote><p><strong>esimsek</strong> <code>(Mon 27 Mar 2023 19:52)</code> - <em>Upvotes: 2</em></p><p>on exam 2023-03-27</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sun 13 Mar 2022 04:03)</code> - <em>Upvotes: 3</em></p><p>Given answer C is correct</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Sat 06 Nov 2021 23:11)</code> - <em>Upvotes: 3</em></p><p>on 6 Nov 2021</p></blockquote>
<blockquote><p><strong>VJPrakash</strong> <code>(Wed 28 Jul 2021 14:29)</code> - <em>Upvotes: 4</em></p><p>This answer is correct.</p></blockquote>

</details>

---

[<< Previous Question](question_393.md) | [Home](../index.md) | [Next Question >>](question_395.md)
