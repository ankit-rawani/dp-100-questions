# Question 71

A set of CSV files contains sales records. All the CSV files have the same data schema.

Each CSV file contains the sales record for a particular month and has the filename sales.csv. Each file is stored in a folder that indicates the month and year when the data was recorded. The folders are in an Azure blob container for which a datastore has been defined in an Azure Machine Learning workspace. The folders are organized in a parent folder named sales to create the following hierarchical structure:

![Question Image](images/q71_q_0007900001.png)

At the end of each month, a new folder with that month's sales file is added to the sales folder.

You plan to use the sales data to train a machine learning model based on the following requirements:

✑ You must define a dataset that loads all of the sales data to date into a structure that can be easily converted to a dataframe.

✑ You must be able to create experiments that use only data that was created before a specific previous month, ignoring any data that was added after that month.

✑ You must register the minimum number of datasets possible.

You need to register the sales data as a dataset in Azure Machine Learning service workspace.

What should you do?

* A.Create a tabular dataset that references the datastore and explicitly specifies each 'sales/mm-yyyy/sales.csv' file every month. Register the dataset with the name sales_dataset each month, replacing the existing dataset and specifying a tag named month indicating the month and year it was registered. Use this dataset for all experiments.
* B.Create a tabular dataset that references the datastore and specifies the path 'sales/*/sales.csv', register the dataset with the name sales_dataset and a tag named month indicating the month and year it was registered, and use this dataset for all experiments.
* C.Create a new tabular dataset that references the datastore and explicitly specifies each 'sales/mm-yyyy/sales.csv' file every month. Register the dataset with the name sales_dataset_MM-YYYY each month with appropriate MM and YYYY values for the month and year. Use the appropriate month-specific dataset for experiments.
* D.Create a tabular dataset that references the datastore and explicitly specifies each 'sales/mm-yyyy/sales.csv' file. Register the dataset with the name sales_dataset each month as a new version and with a tag named month indicating the month and year it was registered. Use this dataset for all experiments, identifying the version to be used based on the month tag as necessary.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>gamezone25</strong> <code>(Tue 19 Oct 2021 19:31)</code> - <em>Upvotes: 28</em></p><p>D seems to be the correct answer. B does not allow you to get the data from before a specific month. With D you create only one dataset with multiple versions (1 version per month).
Similar example in &#x27;Versioning best practice&#x27;:
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-version-track-datasets</p></blockquote>
<blockquote><p><strong>chevyli</strong> <code>(Sat 25 Feb 2023 06:38)</code> - <em>Upvotes: 3</em></p><p>I guess you can by using module like Split or Filter data? You can specify the condition to get data before a particular month</p></blockquote>
<blockquote><p><strong>Shailen</strong> <code>(Fri 17 Jun 2022 20:14)</code> - <em>Upvotes: 4</em></p><p>But D don&#x27;t satisfy the last requirement that register minimal data set possible since each specific sales file need to register in option D. Given answer B seems correct as it fulfils all conditions.</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Fri 29 Oct 2021 21:39)</code> - <em>Upvotes: 2</em></p><p>I agree. The example shown in the link below does exactly what is being asked in the question. 
https://docs.microsoft.com/en-us/azure/machine-learning/how-to-version-track-datasets#versioning-best-practice</p></blockquote>
<blockquote><p><strong>levm39</strong> <code>(Sat 04 Dec 2021 11:17)</code> - <em>Upvotes: 4</em></p><p>You must register the minimum number of datasets possible. D is not correct, because you will have to do this manually each month,?</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Wed 05 Jan 2022 07:13)</code> - <em>Upvotes: 1</em></p><p>But B you can&#x27;t select by (each) Month.</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Tue 12 Jul 2022 07:54)</code> - <em>Upvotes: 19</em></p><p>Quick update, verified, correct ans is D. Cross checked in coursera and validated there.</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Fri 28 Jun 2024 20:19)</code> - <em>Upvotes: 3</em></p><p>The Correct answer is: D

Option D is the most appropriate choice because it allows for both the inclusion of all data to date for general training and the ability to use specific versions for experiments that require data up to a particular month. The &quot;minimum number of datasets&quot; can be interpreted as the minimum number of distinct dataset entities registered in the workspace. With versioning (Option D), you&#x27;re still working with one dataset entity, but with multiple versions, which aligns with the requirement of minimal dataset registration.

Justification:
- Versioning in Azure Machine Learning allows you to handle the evolving data by creating new versions of the dataset each month, without increasing the number of dataset entities in the workspace.
- By using version tags, you can manage and reference the appropriate data snapshot for experiments as needed.
- This approach offers a balance between efficient data management and the ability to run experiments on specific subsets of the data as of a given date, thus meeting all the stated requirements.</p></blockquote>
<blockquote><p><strong>Kanwal001</strong> <code>(Wed 28 Feb 2024 20:25)</code> - <em>Upvotes: 4</em></p><p>On exam 28/08/2023..</p></blockquote>
<blockquote><p><strong>Depayser</strong> <code>(Sat 18 Nov 2023 17:32)</code> - <em>Upvotes: 1</em></p><p>Option D</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Sat 20 Jan 2024 09:10)</code> - <em>Upvotes: 1</em></p><p>ChatGPT agrees.</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Fri 27 Oct 2023 09:36)</code> - <em>Upvotes: 1</em></p><p>A: *replaces* the the existing dataset -&gt; can&#x27;t directly filter data before the specific month
B: captures all the sales data from different folders in *one dataset* -&gt; can&#x27;t can&#x27;t directly filter data before the specific month
C: requires registering multiple datasets

D: satisfies all the requirements</p></blockquote>
<blockquote><p><strong>Yuriy_Ch</strong> <code>(Fri 08 Sep 2023 11:07)</code> - <em>Upvotes: 2</em></p><p>Exactly this question was on exam 07/03/2023</p></blockquote>
<blockquote><p><strong>Jit1981</strong> <code>(Wed 27 Sep 2023 06:59)</code> - <em>Upvotes: 2</em></p><p>Is Answer B or D?</p></blockquote>
<blockquote><p><strong>mamau</strong> <code>(Sat 12 Aug 2023 19:32)</code> - <em>Upvotes: 2</em></p><p>B. Create a tabular dataset that references the datastore and specifies the path &#x27;sales/*/sales.csv&#x27;, register the dataset with the name sales_dataset and a tag named month indicating the month and year it was registered, and use this dataset for all experiments.

This option meets all the requirements of the problem statement:
✑ The dataset loads all of the sales data to date into a structure that can be easily converted to a dataframe.
✑ You can create experiments that use only data that was created before a specific previous month, ignoring any data that was added after that month by filtering the dataset based on the &quot;month&quot; tag.
✑ The minimum number of datasets possible is registered (only one).</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 02 Aug 2023 16:39)</code> - <em>Upvotes: 2</em></p><p>Option D satisfies the last requirement of registering the minimum number of datasets possible.
While option B uses a single dataset that references the entire path &#x27;sales/*/sales.csv&#x27;, it still requires registering the dataset every month with a new tag indicating the month and year. In comparison, option D registers each month&#x27;s sales data as a new version of the same dataset with a tag indicating the month and year. This allows you to only have to register one dataset instead of multiple datasets, minimizing the number of registered datasets.

Option B does not satisfy the requirement of being able to create experiments that use only data that was created before a specific previous month as it only references the entire path and not individual files for each month</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Tue 13 Jun 2023 08:59)</code> - <em>Upvotes: 2</em></p><p>Option C</p></blockquote>
<blockquote><p><strong>Arend78</strong> <code>(Wed 07 Jun 2023 13:22)</code> - <em>Upvotes: 1</em></p><p>If I look at the explanation for the &quot;correct&quot; (?) answer B, it seems that they mean to ask &quot;How to load CSVs form the appropriate folders using the least amount of lines?&quot; In the explanation they use an asterix. Not a very clear question i.m.o.</p></blockquote>
<blockquote><p><strong>fvil</strong> <code>(Sun 07 May 2023 14:33)</code> - <em>Upvotes: 1</em></p><p>On exam 07/11/2022</p></blockquote>
<blockquote><p><strong>victorafb</strong> <code>(Sun 23 Apr 2023 14:37)</code> - <em>Upvotes: 3</em></p><p>on exam 16/10/2022 I&#x27;ve answer D</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 11 Nov 2022 12:52)</code> - <em>Upvotes: 2</em></p><p>Absolutely correct, one dataset with different versions.  Versions are NOT the same as different dataset!</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Sat 22 Oct 2022 10:42)</code> - <em>Upvotes: 1</em></p><p>on exam 04/22/2022</p></blockquote>
<blockquote><p><strong>azurelearner666</strong> <code>(Mon 10 Oct 2022 14:19)</code> - <em>Upvotes: 3</em></p><p>Correct answer is D,
Even this question is really very badly written to promote misunderstanding and confusion.</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Sun 18 Sep 2022 08:39)</code> - <em>Upvotes: 2</em></p><p>on exam 18/03/2022</p></blockquote>

</details>

---

[<< Previous Question](question_70.md) | [Home](/index.md) | [Next Question >>](question_72.md)
