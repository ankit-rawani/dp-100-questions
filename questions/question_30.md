# Question 30

This question is included in a number of questions that depicts the identical set-up. However, every question has a distinctive result. Establish if the recommendation satisfies the requirements.

You are in the process of carrying out feature engineering on a dataset.

You want to add a feature to the dataset and fill the column value.

Recommendation: You must make use of the Edit Metadata Azure Machine Learning Studio module.

Will the requirements be satisfied?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>gaint</strong> <code>(Wed 05 Jan 2022 07:12)</code> - <em>Upvotes: 30</em></p><p>Edit meta data cannot add a new column, it can change properties of existing columns</p></blockquote>
<blockquote><p><strong>Gabonia</strong> <code>(Sun 19 Feb 2023 15:03)</code> - <em>Upvotes: 1</em></p><p>question says fill column, not add</p></blockquote>
<blockquote><p><strong>lcgcastro96</strong> <code>(Wed 13 Dec 2023 10:29)</code> - <em>Upvotes: 1</em></p><p>&quot;You want to add a feature to the dataset and fill the column value.&quot;</p></blockquote>
<blockquote><p><strong>azure1000</strong> <code>(Wed 02 Feb 2022 09:31)</code> - <em>Upvotes: 4</em></p><p>Agree. New column can be added through SQL transformation or python script</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Thu 13 Oct 2022 19:00)</code> - <em>Upvotes: 1</em></p><p>Exactly!</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Wed 21 Aug 2024 11:47)</code> - <em>Upvotes: 1</em></p><p>filling value has nothing to do with Edit metadata</p></blockquote>
<blockquote><p><strong>PopeyeDS</strong> <code>(Mon 15 Jan 2024 05:11)</code> - <em>Upvotes: 1</em></p><p>Edit metadata helps to change column type to categorical or any other.. not necessary to add a feature</p></blockquote>
<blockquote><p><strong>Sa_Msa</strong> <code>(Mon 01 Jan 2024 16:43)</code> - <em>Upvotes: 1</em></p><p>&quot;Edit Meta Data&quot; as the name is saying, is for editing the meta data, you can select the columns that you want to change, you can change their type e.g. numerical to categorial, then you can choose if they are features or labels etc.. you can also change the column name here too. 
Below is the options you have: 
Column
Edit column
[Column names: test2]
Data type
[Categorical]
Fields
[Label]
New column names
-</p></blockquote>
<blockquote><p><strong>Nadine_nm</strong> <code>(Wed 06 Dec 2023 13:21)</code> - <em>Upvotes: 1</em></p><p>The answer is correct, the module allows you to : Mark columns as features.
https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/edit-metadata?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>eloyinaay</strong> <code>(Sun 03 Sep 2023 17:20)</code> - <em>Upvotes: 1</em></p><p>To add a column the only way is with python scripts.</p></blockquote>
<blockquote><p><strong>mamau</strong> <code>(Sat 12 Aug 2023 06:50)</code> - <em>Upvotes: 2</em></p><p>YES. The recommendation to use the Edit Metadata Azure Machine Learning Studio module would satisfy the requirements of adding a feature to the dataset and filling the column value. The Edit Metadata module allows for editing of the metadata of the dataset, including adding columns, modifying column names, and changing data types. It would be an appropriate tool for adding a new feature to the dataset and filling its values.</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Wed 06 Sep 2023 15:03)</code> - <em>Upvotes: 2</em></p><p>mamau, could you bring a proof please? a link...</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Sat 10 Jun 2023 17:11)</code> - <em>Upvotes: 1</em></p><p>Keyword =&gt; Add</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Mon 12 Sep 2022 09:56)</code> - <em>Upvotes: 2</em></p><p>Can&#x27;t add new columns. Change existing ones</p></blockquote>
<blockquote><p><strong>Tsardoz</strong> <code>(Sat 16 Jul 2022 09:19)</code> - <em>Upvotes: 3</em></p><p>Edit metadata can change existing column names not add new ones</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Wed 15 Jun 2022 07:23)</code> - <em>Upvotes: 1</em></p><p>Agree with Edit metadata</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Thu 13 Oct 2022 19:00)</code> - <em>Upvotes: 2</em></p><p>Try it in Azure ML Studio and you will see that you can&#x27;t add a new column using &quot;Edit Metadata&quot;</p></blockquote>
<blockquote><p><strong>gnsu</strong> <code>(Thu 19 May 2022 04:31)</code> - <em>Upvotes: 1</em></p><p>Given answer is wrong: Should be No.  Add Columns must be right answer.
https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/add-columns</p></blockquote>
<blockquote><p><strong>bdsrca</strong> <code>(Mon 28 Feb 2022 19:38)</code> - <em>Upvotes: 4</em></p><p>The answer is correct, you can ADD a new column by editing metadata.
ref:
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/edit-metadata</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Thu 13 Oct 2022 19:01)</code> - <em>Upvotes: 3</em></p><p>Try it in Azure ML Studio yourself and you will see that you can&#x27;t add a new column using &quot;Edit Metadata&quot;. Please don&#x27;t spread false information unless you&#x27;re sure!</p></blockquote>
<blockquote><p><strong>sapna_tare</strong> <code>(Fri 06 Oct 2023 05:18)</code> - <em>Upvotes: 1</em></p><p>Thanks for this link.</p></blockquote>
<blockquote><p><strong>dushmantha</strong> <code>(Mon 28 Feb 2022 11:01)</code> - <em>Upvotes: 2</em></p><p>I can only find to give a new name to the existing columns. But not adding a completely new column</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Mon 28 Feb 2022 12:25)</code> - <em>Upvotes: 2</em></p><p>No, For New column names, enter the new name of the selected column or columns. Not for adding new column..</p></blockquote>

</details>

---

[<< Previous Question](question_29.md) | [Home](/index.md) | [Next Question >>](question_31.md)
