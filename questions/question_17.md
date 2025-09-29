# Question 17

You have been tasked with creating a new Azure pipeline via the Machine Learning designer.

You have to makes sure that the pipeline trains a model using data in a comma-separated values (CSV) file that is published on a website. A dataset for the file for this file does not exist.

Data from the CSV file must be ingested into the designer pipeline with the least amount of administrative effort as possible.

Which of the following actions should you take?

- A.You should make use of the Convert to TXT module.
- B.You should add the Copy Data object to the pipeline.
- C.You should add the Import Data object to the pipeline.
- D.You should add the Dataset object to the pipeline.

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>JTWang</strong> <code>(Thu 21 Apr 2022 00:55)</code> - <em>Upvotes: 14</em></p><p>The Import Data component support read data from following sources:

URL via HTTP
Azure cloud storages through Datastores)
Azure Blob Container
Azure File Share
Azure Data Lake
Azure Data Lake Gen2
Azure SQL Database
Azure PostgreSQL</p></blockquote>

<blockquote><p><strong>lianaliam</strong> <code>(Fri 06 Jun 2025 10:05)</code> - <em>Upvotes: 1</em></p><p>import</p></blockquote>
<blockquote><p><strong>shahid.azad</strong> <code>(Wed 24 Jul 2024 16:00)</code> - <em>Upvotes: 1</em></p><p>why the revealed tell wrong answer</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 17 Feb 2024 11:15)</code> - <em>Upvotes: 1</em></p><p>C. You should add the Import Data object to the pipeline.

Adding the Import Data object to the pipeline in Azure Machine Learning designer is the most efficient way to ingest data from a CSV file published on a website. This action allows you to directly access and import the data into the pipeline with minimal administrative effort, eliminating the need for manual data conversion or copying. The Import Data object supports various data sources, including web URLs, making it ideal for this task.</p></blockquote>

<blockquote><p><strong>Matt2000</strong> <code>(Tue 06 Feb 2024 16:27)</code> - <em>Upvotes: 1</em></p><p>The instruction explicitly says that there is no dataset registered for the csv file. D (add dataset object) presupposes that such a dataset exists and thus is False. C  (import data module) remains as the only viable option.</p></blockquote>
<blockquote><p><strong>Charoon</strong> <code>(Thu 21 Dec 2023 02:04)</code> - <em>Upvotes: 1</em></p><p>According to MS in reference to the Import Data component:

&quot;All functionality provided by this component can be done by datastore and datasets in the workspace landing page. We recommend you use datastore and dataset which includes additional features like data monitoring&quot;

https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/import-data?view=azureml-api-2

Hence DataSet is the preferred method, i.e. answer D.</p></blockquote>

<blockquote><p><strong>james2033</strong> <code>(Fri 20 Oct 2023 13:15)</code> - <em>Upvotes: 1</em></p><p>Let&#x27;s see screenshot, it is CSV https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/media/module/import-data-path.png?view=azureml-api-2

https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/import-data?view=azureml-api-2#how-to-configure-import-data

C is the correct answer: &#x27;Import Data&#x27; in pipeline.</p></blockquote>

<blockquote><p><strong>PopeyeDS</strong> <code>(Fri 14 Jul 2023 07:50)</code> - <em>Upvotes: 1</em></p><p>the correct answer is C. You should add the Import Data object to the pipeline. However, if you prefer to create the dataset manually, then you could use the Dataset object.</p></blockquote>
<blockquote><p><strong>Sa_Msa</strong> <code>(Fri 30 Jun 2023 11:28)</code> - <em>Upvotes: 2</em></p><p>The Import Data module in Azure Machine Learning designer allows you to read data from various data sources, including web URLs, and import it directly into your pipeline. By configuring the Import Data object with the URL of the CSV file, you can easily bring the data into the pipeline for further processing.</p></blockquote>
<blockquote><p><strong>Mirjalol</strong> <code>(Fri 10 Feb 2023 08:38)</code> - <em>Upvotes: 2</em></p><p>Dataset for this file does not exist.... and proceeded with answer D? My question is how you add dataset object to pipeline if it does not exist? Like literally how? Answer is C obviously</p></blockquote>
<blockquote><p><strong>KingTN</strong> <code>(Wed 08 Feb 2023 14:44)</code> - <em>Upvotes: 2</em></p><p>There is a note in the link, regarding import-data &quot;https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/import-data&quot;, which recommends to use dataset... I am not sure when this note was added.. 
This is the note: &quot;All functionality provided by this component can be done by datastore and datasets in the workspace landing page. We recommend you use datastore and dataset which includes additional features like data monitoring. To learn more, see How to Access Data and How to Register Datasets article. After you register a dataset, you can find it in the Datasets -&gt; My Datasets category in designer interface. This component is reserved for Studio(classic) users to for a familiar experience.&quot;

So I think as of Jan 2023, the answer should be registering a dataset (similar to D, but may need to be rephrased).</p></blockquote>

<blockquote><p><strong>Vinit9</strong> <code>(Mon 06 Feb 2023 05:44)</code> - <em>Upvotes: 2</em></p><p>B. You should add the Copy Data object to the pipeline.

To ingest data from a CSV file published on a website into the Azure Machine Learning designer pipeline with the least amount of administrative effort possible, you should add the Copy Data object to the pipeline. The Copy Data object is used to copy data from a source to a destination, and it supports a variety of sources, including web URLs. By using the Copy Data object, you can quickly and easily ingest the data from the CSV file into the pipeline, without having to create a dataset or perform any additional preprocessing. This will minimize administrative effort and allow you to quickly get started with training a model using the data.</p></blockquote>

<blockquote><p><strong>Mirjalol</strong> <code>(Wed 01 Feb 2023 08:58)</code> - <em>Upvotes: 3</em></p><p>I have a question for yall fellas: The question mentions that there is no dataset for this file... 
Can we import data object if there is no dataset of this file?</p></blockquote>
<blockquote><p><strong>KIshor1212</strong> <code>(Tue 29 Nov 2022 13:57)</code> - <em>Upvotes: 1</em></p><p>There are two ways you can import data into the designer: Azure Machine Learning datasets - Register datasets in Azure Machine Learning to enable advanced features that help you manage your data. Import Data component - Use the Import Data component to directly access data from online data sources</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Wed 13 Apr 2022 03:55)</code> - <em>Upvotes: 3</em></p><p>The correct answer is C. Import data component is used to import data from data sources such as web URLs with minimum effort. Reference: https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/import-data</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Thu 21 Apr 2022 00:55)</code> - <em>Upvotes: 1</em></p><p>The Import Data component support read data from following sources:

URL via HTTP
Azure cloud storages through Datastores)
Azure Blob Container
Azure File Share
Azure Data Lake
Azure Data Lake Gen2
Azure SQL Database
Azure PostgreSQL</p></blockquote>

<blockquote><p><strong>Thornehead</strong> <code>(Sat 26 Mar 2022 01:17)</code> - <em>Upvotes: 3</em></p><p>In Azure Designer, there is no such object as &quot;IMPORT DATA&quot;. So the answer is &quot;insert Dataset&quot;.</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Wed 13 Apr 2022 03:56)</code> - <em>Upvotes: 4</em></p><p>No, there is a component called import data and it is in fact the correct answer to this question. Check here: https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/import-data</p></blockquote>
<blockquote><p><strong>windy610</strong> <code>(Sun 19 Nov 2023 08:51)</code> - <em>Upvotes: 1</em></p><p>God it is tricky</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Mon 17 Jan 2022 16:52)</code> - <em>Upvotes: 2</em></p><p>shouldn&#x27;t the answer be C ?</p></blockquote>
<blockquote><p><strong>RAHULsingla</strong> <code>(Wed 19 Jan 2022 04:53)</code> - <em>Upvotes: 2</em></p><p>I think so too, it should be C, as it mentions less administrative effort</p></blockquote>

</details>

---

[<< Previous Question](question_16.md) | [Home](../index.md) | [Next Question >>](question_18.md)
