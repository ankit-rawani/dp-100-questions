# Question 307

You create a multi-class image classification model with automated machine learning in Azure Machine Learning.

You need to prepare labeled image data as input for model training in the form of an Azure Machine Learning tabular dataset.

Which data format should you use?

- A.COCO
- B.JSONL
- C.JSON
- D.Pascal VOC

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>GHill1982</strong> <code>(Fri 12 Jul 2024 19:07)</code> - <em>Upvotes: 3</em></p><p>To prepare labeled image data as input for model training in the form of an Azure Machine Learning tabular dataset, you should use the JSONL format. https://learn.microsoft.com/en-us/azure/machine-learning/how-to-prepare-datasets-for-automl-images?view=azureml-api-2&amp;ssp=1</p></blockquote>
<blockquote><p><strong>ferren</strong> <code>(Mon 11 Mar 2024 05:12)</code> - <em>Upvotes: 1</em></p><p>bard says B is correct and give some example</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Sun 03 Dec 2023 13:45)</code> - <em>Upvotes: 1</em></p><p>To use labeled image data for a tabular dataset, you need to prepare the data in the accepted format. According to the Microsoft Learn website, labeled data should be in JSONL format. JSONL is a format where each line of the file is a valid JSON object, which makes it easy to read and parse[1]. Once you have your labeled data in JSONL format, you can use it to create an MLTable, which packages your data into a consumable object for training. https://learn.microsoft.com/en-us/azure/machine-learning/how-to-prepare-datasets-for-automl-images?view=azureml-api-2&amp;tabs=cli</p></blockquote>
<blockquote><p><strong>sap_dg</strong> <code>(Wed 27 Sep 2023 17:35)</code> - <em>Upvotes: 1</em></p><p>A. COCO
To prepare labeled image data as input for model training in the form of an Azure Machine Learning tabular dataset, you should use the COCO (Common Objects in Context) data format.</p></blockquote>
<blockquote><p><strong>sap_dg</strong> <code>(Wed 27 Sep 2023 17:42)</code> - <em>Upvotes: 5</em></p><p>Take it back. JSONL is correct</p></blockquote>
<blockquote><p><strong>oakmm</strong> <code>(Fri 22 Sep 2023 22:31)</code> - <em>Upvotes: 3</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/how-to-prepare-datasets-for-automl-images?tabs=cli</p></blockquote>

</details>

---

[<< Previous Question](question_306.md) | [Home](../index.md) | [Next Question >>](question_308.md)
