# Question 27

This question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the recommendation satisfies the requirements.

You are in the process of carrying out feature engineering on a dataset.

You want to add a feature to the dataset and fill the column value.

Recommendation: You must make use of the Join Data Azure Machine Learning Studio module.

Will the requirements be satisfied?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>gnsu</strong> <code>(Thu 19 May 2022 04:29)</code> - <em>Upvotes: 14</em></p><p>No is Correct answer. Add Columns need to be used. Join data is needed only for database style joins
https://docs.microsoft.com/bs-cyrl-ba/azure/machine-learning/component-reference/add-columns
https://docs.microsoft.com/bs-cyrl-ba/azure/machine-learning/component-reference/join-data</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Wed 21 Aug 2024 11:46)</code> - <em>Upvotes: 2</em></p><p>The &quot;Join Data&quot; module in Azure Machine Learning Studio allows you to merge two datasets based on a common key or keys. This is particularly useful when you want to augment your existing dataset with additional information from another source. For example, if you have a dataset of sales transactions and another dataset with product information, you could use the &quot;Join Data&quot; module to add product details (a new feature) to the sales transactions dataset by joining on a product ID column present in both datasets.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 19 Apr 2024 08:09)</code> - <em>Upvotes: 1</em></p><p>The &#x27;Join Data&#x27; module in Microsoft Azure Machine Learning Studio (classic) is used to merge two datasets using a database-style join operation.

If you want to add a feature to the dataset and FILL COLUMN VALUE --&gt; No.

Join dataset https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/join-data?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>PradhanManva</strong> <code>(Sun 24 Mar 2024 19:23)</code> - <em>Upvotes: 1</em></p><p>This is the answer.</p></blockquote>
<blockquote><p><strong>Sa_Msa</strong> <code>(Mon 01 Jan 2024 16:40)</code> - <em>Upvotes: 2</em></p><p>Answer is correct. I tested it multiple times and got error regarding the size. You need to use &quot;add columns&quot; if you want to add two dataset together.</p></blockquote>
<blockquote><p><strong>SoftAI</strong> <code>(Thu 12 Oct 2023 17:00)</code> - <em>Upvotes: 1</em></p><p>Join Data Azure Machine Learning Studio is a data transformation tool</p></blockquote>
<blockquote><p><strong>mhmichiel</strong> <code>(Wed 06 Sep 2023 14:04)</code> - <em>Upvotes: 2</em></p><p>If you want to add a colom with a new feature you will need data. This data could be in a secondery dataset which needs to be joined to the original dataset via a join. A could be correct. Concidering that it would be B, how would I fill the column? Manualy? That sounds like a unlogical option concidering that the datasets are usualy pretty big and not made up.</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Sun 23 Jul 2023 17:37)</code> - <em>Upvotes: 3</em></p><p>JOIN implies a query, not inserting a column to a database.</p></blockquote>
<blockquote><p><strong>Sibajene</strong> <code>(Tue 04 Jul 2023 13:17)</code> - <em>Upvotes: 2</em></p><p>B. No

The Join Data module in Azure Machine Learning Studio is used to combine two datasets by matching values in key columns. It is not a general-purpose tool for adding features or filling column values in a single dataset.</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Fri 09 Jun 2023 15:55)</code> - <em>Upvotes: 1</em></p><p>Option B</p></blockquote>
<blockquote><p><strong>KIshor1212</strong> <code>(Mon 29 May 2023 13:12)</code> - <em>Upvotes: 1</em></p><p>To perform a join on two datasets, they should be related by a key column. Composite keys using multiple columns are also supported. Add the datasets you want to combine, and then drag the Join Data component into your pipeline.</p></blockquote>
<blockquote><p><strong>Mirjalol</strong> <code>(Tue 01 Aug 2023 10:33)</code> - <em>Upvotes: 5</em></p><p>The question says &#x27;add a feature to the dataset &#x27; ... there are no 2 datasets here. You are not joining them... You are adding a damn single feature to the dataset. Why you guys like to mislead people?</p></blockquote>
<blockquote><p><strong>mhmichiel</strong> <code>(Wed 06 Sep 2023 14:11)</code> - <em>Upvotes: 1</em></p><p>You are right, however, how do you want to add the feature to the dataset withoud data? Concidering that you want to add a feature to a dataset and that you dont want to make it up you need to ad a coulomn representing the new feature. To add this colomn you need a secondary dataset which you join to the main dataset. This means that A is not incorect. The question is incorrect and the answer is not nesseserely b.</p></blockquote>
<blockquote><p><strong>dynamic_person91</strong> <code>(Sat 18 Mar 2023 17:51)</code> - <em>Upvotes: 1</em></p><p>join is used for datasets not for columns b is correct</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 16 Dec 2022 14:37)</code> - <em>Upvotes: 1</em></p><p>This is possible</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 16 Dec 2022 15:27)</code> - <em>Upvotes: 1</em></p><p>There is an assumption that column is in another dataset with a key to map to the base dataset</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Mon 12 Sep 2022 09:52)</code> - <em>Upvotes: 2</em></p><p>Don&#x27;t use Join  Data Use Add Columns</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 16 Dec 2022 14:37)</code> - <em>Upvotes: 2</em></p><p>Add columns is definitely incorrect!
1. it is cross join, not link data with key column
2. it will add all columns from both data set
Join is the correct answer, you can control which key column to join and which columns are from left dataset and which columns are from right data set</p></blockquote>
<blockquote><p><strong>Tsardoz</strong> <code>(Sat 16 Jul 2022 09:13)</code> - <em>Upvotes: 4</em></p><p>I think Yes is correct. The second dataset might be a key which is joined with a second column being the extra column to add to the dataset.</p></blockquote>

</details>

---

[<< Previous Question](question_26.md) | [Home](/index.md) | [Next Question >>](question_28.md)
