# Question 400

You are planning to register a trained model in an Azure Machine Learning workspace.

You must store additional metadata about the model in a key-value format. You must be able to add new metadata and modify or delete metadata after creation.

You need to register the model.

Which parameter should you use?

- A.description
- B.model_framework
- C.tags
- D.properties

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>J_AR</strong> <code>(Mon 02 Jan 2023 21:33)</code> - <em>Upvotes: 10</em></p><p>Tags can be deleted but properties cannot.</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Wed 12 Apr 2023 20:10)</code> - <em>Upvotes: 7</em></p><p>The correct answer is C. To clarify things for everybody: tags and properties are both key value pairs . But here is the important difference: tags can be changed later; but properties can&#x27;t be changed after the model is registered.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sun 20 Oct 2024 10:42)</code> - <em>Upvotes: 1</em></p><p>Tag key-value pairs for model

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-models?view=azureml-api-2&amp;tabs=python%2Cuse-local#update

https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.core.model.model?view=azure-ml-py#parameters</p></blockquote>

<blockquote><p><strong>phdykd</strong> <code>(Fri 23 Feb 2024 20:39)</code> - <em>Upvotes: 1</em></p><p>Seems C.</p></blockquote>
<blockquote><p><strong>Thornehead</strong> <code>(Tue 28 Mar 2023 03:13)</code> - <em>Upvotes: 1</em></p><p>Tags can be deleted or changed.

https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json</p></blockquote>

<blockquote><p><strong>dp100uber</strong> <code>(Thu 29 Dec 2022 23:31)</code> - <em>Upvotes: 4</em></p><p>Should be tags because those can be deleted.</p></blockquote>

</details>

---

[<< Previous Question](question_399.md) | [Home](../index.md) | [Next Question >>](question_401.md)
