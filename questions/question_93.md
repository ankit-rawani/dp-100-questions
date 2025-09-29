# Question 93

HOTSPOT -

You have a dataset that contains 2,000 rows. You are building a machine learning classification model by using Azure Learning Studio. You add a Partition and

Sample module to the experiment.

You need to configure the module. You must meet the following requirements:

✑ Divide the data into subsets

✑ Assign the rows into folds using a round-robin method

✑ Allow rows in the dataset to be reused

How should you configure the module? To answer, select the appropriate options in the dialog box in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q93_q_0012000001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q93_ans_0_0012000002.png" alt="Answer Image"><br>

<p>Use the Split data into partitions option when you want to divide the dataset into subsets of the data. This option is also useful when you want to create a custom number of folds for cross-validation, or to split rows into several groups.</p>
<p>1. Add the Partition and Sample module to your experiment in Studio (classic), and connect the dataset.</p>
<p>2. For Partition or sample mode, select Assign to Folds.</p>
<p>3. Use replacement in the partitioning: Select this option if you want the sampled row to be put back into the pool of rows for potential reuse. As a result, the same row might be assigned to several folds.</p>
<p>4. If you do not use replacement (the default option), the sampled row is not put back into the pool of rows for potential reuse. As a result, each row can be assigned to only one fold.</p>
<p>5. Randomized split: Select this option if you want rows to be randomly assigned to folds.</p>
<p>If you do not select this option, rows are assigned to folds using the round-robin method.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/partition-and-sample</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>phdykd</strong> <code>(Mon 05 Aug 2024 00:42)</code> - <em>Upvotes: 3</em></p><p>A. Assign to Folds: To divide the data into subsets and assign the rows into folds using a round-robin method.
E. Use replacement in the partitioning: To allow the same row to be assigned to multiple folds.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Mon 05 Aug 2024 00:40)</code> - <em>Upvotes: 3</em></p><p>A. Assign to Folds: To divide the data into subsets and assign the rows into folds using a round-robin method.
C. Sampling: To allow rows in the dataset to be reused.
E. Use replacement in the partitioning: To allow the same row to be assigned to multiple folds.</p></blockquote>
<blockquote><p><strong>ajay0011</strong> <code>(Thu 03 Oct 2024 00:32)</code> - <em>Upvotes: 2</em></p><p>you are wrong given answer is correct, i have checked the module in designer</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Wed 13 Sep 2023 09:32)</code> - <em>Upvotes: 4</em></p><p>The given answer is correct.</p></blockquote>
<blockquote><p><strong>MohammadKhubeb</strong> <code>(Thu 03 Aug 2023 00:08)</code> - <em>Upvotes: 1</em></p><p>It is Randomized split because of Round Robin.</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Tue 26 Sep 2023 07:40)</code> - <em>Upvotes: 6</em></p><p>You mean Randomized_split is unchecked because of Round Robin</p></blockquote>
<blockquote><p><strong>Narendra05</strong> <code>(Mon 26 Dec 2022 14:31)</code> - <em>Upvotes: 2</em></p><p>The Data to divide into fold is already mentioned that option is correct .</p></blockquote>
<blockquote><p><strong>parwa</strong> <code>(Tue 03 Jan 2023 01:52)</code> - <em>Upvotes: 9</em></p><p>1. Assign to Folds
2.  use Replacement in the partition - Checked
3. Randomized split- unchecked</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Wed 25 Jan 2023 14:50)</code> - <em>Upvotes: 10</em></p><p>Randomized split: Select this option if you want rows to be randomly assigned to folds.

If you do not select this option, rows are assigned to folds using the round-robin method.</p></blockquote>

</details>

---

[<< Previous Question](question_92.md) | [Home](/index.md) | [Next Question >>](question_94.md)
