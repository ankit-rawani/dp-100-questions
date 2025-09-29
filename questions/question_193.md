# Question 193

HOTSPOT -

You have an Azure blob container that contains a set of TSV files. The Azure blob container is registered as a datastore for an Azure Machine Learning service workspace. Each TSV file uses the same data schema.

You plan to aggregate data for all of the TSV files together and then register the aggregated data as a dataset in an Azure Machine Learning workspace by using the Azure Machine Learning SDK for Python.

You run the following code.

![Question Image](../images/q193_q_0016500001.png)

For each of the following statements, select Yes if the statement is true. Otherwise, select No.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q193_q_0016500002.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q193_ans_0_0016600001.png" alt="Answer Image"><br>

<p>Box 1: No -</p>
<p>FileDataset references single or multiple files in datastores or from public URLs. The TSV files need to be parsed.</p>
<p>Box 2: Yes -</p>
<p>to_path() gets a list of file paths for each file stream defined by the dataset.</p>
<p>Box 3: Yes -</p>
<p>TabularDataset.to_pandas_dataframe loads all records from the dataset into a pandas DataFrame.</p>
<p>TabularDataset represents data in a tabular format created by parsing the provided file or list of files.</p>
<p>Note: TSV is a file extension for a tab-delimited file used with spreadsheet software. TSV stands for Tab Separated Values. TSV files are used for raw data and can be imported into and exported from spreadsheet software. TSV files are essentially text files, and the raw data can be viewed by text editors, though they are often used when moving raw data between spreadsheets.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/python/api/azureml-core/azureml.data.tabulardataset</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>SaulG</strong> <code>(Fri 09 Dec 2022 07:12)</code> - <em>Upvotes: 18</em></p><p>Answer No, Yes, Yes is correct!</p></blockquote>
<blockquote><p><strong>Dilesha</strong> <code>(Mon 19 Aug 2024 00:39)</code> - <em>Upvotes: 4</em></p><p>On Exam 17 Feb 2023</p></blockquote>
<blockquote><p><strong>majma</strong> <code>(Thu 30 Nov 2023 14:55)</code> - <em>Upvotes: 1</em></p><p>Should be 3 No</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Mon 18 Sep 2023 08:41)</code> - <em>Upvotes: 3</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Sun 10 Sep 2023 04:52)</code> - <em>Upvotes: 2</em></p><p>On march 2022</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Sat 06 May 2023 21:47)</code> - <em>Upvotes: 1</em></p><p>on exam 6 Nov 2021</p></blockquote>
<blockquote><p><strong>AI247</strong> <code>(Sat 06 May 2023 11:18)</code> - <em>Upvotes: 1</em></p><p>Was in exam 11/05/2021</p></blockquote>
<blockquote><p><strong>pkal</strong> <code>(Sat 25 Mar 2023 00:10)</code> - <em>Upvotes: 1</em></p><p>on exam 9/24/2021</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Wed 11 Jan 2023 15:00)</code> - <em>Upvotes: 4</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>slash_nyk</strong> <code>(Mon 16 Jan 2023 04:37)</code> - <em>Upvotes: 5</em></p><p>how many questions came from this dump ?</p></blockquote>

</details>

---

[<< Previous Question](question_192.md) | [Home](/index.md) | [Next Question >>](question_194.md)
