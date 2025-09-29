# Question 221

You are performing feature engineering on a dataset.

You must add a feature named CityName and populate the column value with the text London.

You need to add the new feature to the dataset.

Which Azure Machine Learning Studio module should you use?

- A.Edit Metadata
- B.Filter Based Feature Selection
- C.Execute Python Script
- D.Latent Dirichlet Allocation

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>RSMCT2011</strong> <code>(Wed 01 Jul 2020 10:04)</code> - <em>Upvotes: 58</em></p><p>Answer C
to add a new column you can run Execute Python Script</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Sat 25 Sep 2021 08:03)</code> - <em>Upvotes: 2</em></p><p>I agree</p></blockquote>
<blockquote><p><strong>Indranee</strong> <code>(Mon 19 Jul 2021 11:58)</code> - <em>Upvotes: 2</em></p><p>Agree with @RSMCT2011 and @vraviranjan that option C &quot;Execute Python Script&quot; to &quot;add a feature&quot; seems to be the most appropriate response.</p></blockquote>
<blockquote><p><strong>juandante</strong> <code>(Thu 10 Sep 2020 11:21)</code> - <em>Upvotes: 2</em></p><p>A new column is a new &quot;feature&quot; ?</p></blockquote>
<blockquote><p><strong>FU_User</strong> <code>(Sat 19 Nov 2022 12:23)</code> - <em>Upvotes: 1</em></p><p>Everything you use as an input for you model is a feature. So if you add a column in your pipeline it will be used as a feature unless you filter it out somewhere or specify not to use it.</p></blockquote>
<blockquote><p><strong>VickyM</strong> <code>(Tue 17 Nov 2020 20:59)</code> - <em>Upvotes: 13</em></p><p>C seems to be the apt answer among the answer choices. Change Metadata module cannot be used to add new feature\column.</p></blockquote>
<blockquote><p><strong>sar77</strong> <code>(Sat 19 Jul 2025 03:00)</code> - <em>Upvotes: 1</em></p><p>Why the Others Are Incorrect:

A. Edit Metadata Changes column types, names, or roles—but does not add or populate columns
B. Filter Based Feature Selection Used to rank and select existing features based on statistical metrics—not for adding new features
D. Latent Dirichlet Allocation Used for topic modeling with text data—not relevant for manually adding features</p></blockquote>

<blockquote><p><strong>f82411e</strong> <code>(Thu 05 Jun 2025 12:00)</code> - <em>Upvotes: 1</em></p><p>Changes data types or names, does not add new columns with values.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Sun 01 Sep 2024 22:40)</code> - <em>Upvotes: 2</em></p><p>after careful reading of all the threads below, I am going with C. As with edit metadata, you can mark a variable as a feature but can&#x27;t create a new feature or column that has text as values. You need code for that, which in execute python script.</p></blockquote>
<blockquote><p><strong>InversaRadice</strong> <code>(Mon 03 Jun 2024 14:59)</code> - <em>Upvotes: 1</em></p><p>Well Guys, I do not agree :
answer is correct

By ML studio drag the module , a couple of click and the work is done...
You can achieve it by the script, you can do anything by script, sure, but you&#x27;re getting lost in a glass of water....</p></blockquote>

<blockquote><p><strong>PI_Team</strong> <code>(Sun 28 Jan 2024 11:47)</code> - <em>Upvotes: 2</em></p><p>To add a new feature named CityName to a dataset and populate the column value with the text London in Azure Machine Learning Studio, you should use the Execute Python Script module (Option C). Option A (Edit Metadata) is used to modify the metadata of a dataset, such as changing column names or data types, but it cannot be used to add new columns or modify the data itself.

SaM</p></blockquote>

<blockquote><p><strong>bobML</strong> <code>(Fri 19 Jan 2024 04:23)</code> - <em>Upvotes: 2</em></p><p>The correct Azure Machine Learning Studio module to add a new feature named CityName and populate it with the text &quot;London&quot; is:

A. Edit Metadata

The Edit Metadata module in Azure Machine Learning Studio allows you to modify the metadata of your dataset, including adding or renaming columns. In this case, you can use the Edit Metadata module to add a new column named &quot;CityName&quot; and set its value as &quot;London&quot; for every row in the dataset.</p></blockquote>

<blockquote><p><strong>vv_bb</strong> <code>(Tue 14 May 2024 18:21)</code> - <em>Upvotes: 1</em></p><p>Edit Metadata module doesn&#x27;t allow you to add new column, neither set its values

RTFM
https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/edit-metadata?view=azureml-api-2</p></blockquote>

<blockquote><p><strong>phdykd</strong> <code>(Thu 18 Jan 2024 04:04)</code> - <em>Upvotes: 1</em></p><p>C, Execute Python Script</p></blockquote>
<blockquote><p><strong>umair_hanu</strong> <code>(Thu 11 Jan 2024 11:06)</code> - <em>Upvotes: 2</em></p><p>A should be the ans.</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Thu 28 Dec 2023 12:17)</code> - <em>Upvotes: 2</em></p><p>A - ChatGPT</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 15 Aug 2023 22:39)</code> - <em>Upvotes: 1</em></p><p>C.  The Edit Metadata module is used to edit the metadata of existing columns, not to add new columns.</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 18 Apr 2023 06:46)</code> - <em>Upvotes: 2</em></p><p>C is correct</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 25 Nov 2022 12:32)</code> - <em>Upvotes: 1</em></p><p>If you need set up a value for a column, regardless of whether the column existing, you need python script</p></blockquote>
<blockquote><p><strong>Thornehead</strong> <code>(Fri 23 Sep 2022 19:34)</code> - <em>Upvotes: 1</em></p><p>As far as filling the data in a column. It can&#x27;t be done through Edit MetaData. So the answer is C.</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Sun 21 Aug 2022 17:46)</code> - <em>Upvotes: 2</em></p><p>The question requires that we populate (alter) the column value but Edit Metadata module does not alter the values and the data types.

From this link: https://docs.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/edit-metadata

This article describes how to use the Edit Metadata module in Machine Learning Studio (classic) to change metadata that is associated with columns in a dataset. The values and the data types in the dataset are not actually altered; what changes is the metadata inside Machine Learning that tells downstream components how to use the column.</p></blockquote>

<blockquote><p><strong>eskilos</strong> <code>(Mon 01 Aug 2022 18:11)</code> - <em>Upvotes: 3</em></p><p>can&#x27;t add new columns in edit metadata</p></blockquote>

</details>

---

[<< Previous Question](question_220.md) | [Home](../index.md) | [Next Question >>](question_222.md)
