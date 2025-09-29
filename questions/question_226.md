# Question 226

You are creating a new Azure Machine Learning pipeline using the designer.

The pipeline must train a model using data in a comma-separated values (CSV) file that is published on a website. You have not created a dataset for this file.

You need to ingest the data from the CSV file into the designer pipeline using the minimal administrative effort.

Which module should you add to the pipeline in Designer?

- A.Convert to CSV
- B.Enter Data Manually
- C.Import Data
- D.Dataset

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>sachinrkp</strong> <code>(Sun 27 Jun 2021 14:12)</code> - <em>Upvotes: 43</em></p><p>Import data using the Import Data module
The Import Data module skips registering your dataset in Azure Machine Learning and imports data directly from a datastore or HTTP URL. So Answer is C</p></blockquote>
<blockquote><p><strong>amelia</strong> <code>(Tue 29 Jun 2021 12:03)</code> - <em>Upvotes: 14</em></p><p>Answer is D
By creating a dataset, you create a reference to the data source location, along with a copy of its metadata. Because the data remains in its existing location, you incur no extra storage cost, hence minimise administrative effort as required in the question. For the data to be accessible by Azure Machine Learning, datasets must be created from paths in Azure datastores or public web URLs.
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-register-datasets</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Thu 05 May 2022 13:41)</code> - <em>Upvotes: 16</em></p><p>The question is asking &quot;which module should you...&quot; Dataset is not a designer module so even though you could use it, the question is not about that. Ans is C.</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Fri 28 Jun 2024 11:37)</code> - <em>Upvotes: 3</em></p><p>C - ChatGPT
The &quot;Import Data&quot; module in the Azure Machine Learning designer allows you to import data from various sources, including web URLs. It provides a simple way to ingest data from a CSV file published on a website without the need to create a dataset beforehand.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 16 Feb 2024 01:46)</code> - <em>Upvotes: 2</em></p><p>C. Import Data
The Dataset module is used to create a dataset from existing data sources, such as Azure Blob Storage, Azure Data Lake Storage, or Azure SQL Database. Since the data is already in a CSV file, the Import Data module is the best option for ingesting the data into the pipeline with minimal administrative effort.</p></blockquote>
<blockquote><p><strong>mamau</strong> <code>(Tue 13 Feb 2024 05:49)</code> - <em>Upvotes: 1</em></p><p>C. Import Data for minimal admin effort
Using the Import Data component in Azure Machine Learning Studio requires minimal administrative effort compared to using Azure Machine Learning datasets. The Import Data component allows you to import data into your pipeline by specifying the URL of the file, so you can easily access and work with the data without the need to manually download and upload the file. This makes it a quick and efficient way to get your data into the pipeline with minimal administrative effort. On the other hand, creating an Azure Machine Learning dataset requires more steps, such as uploading the data to a storage account and creating the dataset in the Azure Machine Learning Studio, which can take more time and effort.
https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-designer-import-data</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Thu 07 Dec 2023 22:04)</code> - <em>Upvotes: 1</em></p><p>Import data is correct</p></blockquote>
<blockquote><p><strong>giusecozza</strong> <code>(Thu 07 Sep 2023 09:04)</code> - <em>Upvotes: 3</em></p><p>maybe this question is a bit outdated. Through a Dataset object is currently possible to read data from HTTP URL&#x27;s, so in my opinion D is the correct answer.

https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.core.dataset.dataset?view=azure-ml-py</p></blockquote>

<blockquote><p><strong>dija123</strong> <code>(Wed 07 Dec 2022 08:35)</code> - <em>Upvotes: 5</em></p><p>Answer is C</p></blockquote>
<blockquote><p><strong>prasad06</strong> <code>(Sat 17 Sep 2022 17:33)</code> - <em>Upvotes: 2</em></p><p>I see only this kind of comment by the user across many question. I suspect this is just spamming.. even the user display name is suspect</p></blockquote>
<blockquote><p><strong>Tejoo</strong> <code>(Mon 25 Jul 2022 16:03)</code> - <em>Upvotes: 5</em></p><p>C. Enter Data Manually (to minimize administrative cost)</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Mon 11 Jul 2022 14:06)</code> - <em>Upvotes: 4</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Thu 07 Jul 2022 10:00)</code> - <em>Upvotes: 6</em></p><p>Correct answer: C. 
Modules for data input and output on designer:
- Enter Data Manually
- Export Data
- Import Data
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/module-reference</p></blockquote>
<blockquote><p><strong>Kapil1803</strong> <code>(Tue 05 Jul 2022 16:41)</code> - <em>Upvotes: 2</em></p><p>Answer D is correct. Please refer the below link which states add dataset Module for import data. https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-designer-automobile-price-train-score</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Sun 07 Aug 2022 12:47)</code> - <em>Upvotes: 1</em></p><p>Wrong
Modules for data input and output on designer:
- Enter Data Manually
- Export Data
- Import Data
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/module-reference</p></blockquote>
<blockquote><p><strong>SnowCheetah</strong> <code>(Thu 16 Jun 2022 09:13)</code> - <em>Upvotes: 4</em></p><p>https://docs.microsoft.com/en-us/azure/machine-learning/how-to-designer-import-data
There are two possible ways to extract data
1. Register Data - to &quot;Dataset&quot; segment 
2. Using &quot;Import Data&quot;

Since question is already ask about extracting data via website and user didn&#x27;t register dataset beforehand
C is should be correct answer.</p></blockquote>

<blockquote><p><strong>rishi_ram</strong> <code>(Fri 03 Jun 2022 21:37)</code> - <em>Upvotes: 4</em></p><p>Answer is C:
Import Data module - Use the Import Data module to directly access data from online datasources.
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-designer-import-data
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/import-data</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Sun 27 Mar 2022 01:46)</code> - <em>Upvotes: 10</em></p><p>Dataset is not even a module that you can use in designer. Import Data is correct answer.</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Fri 18 Mar 2022 06:06)</code> - <em>Upvotes: 4</em></p><p>explication for the question is not even for the designer. 
the answer is &#x27;C&#x27;</p></blockquote>

</details>

---

[<< Previous Question](question_225.md) | [Home](../index.md) | [Next Question >>](question_227.md)
