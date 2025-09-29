# Question 285

You plan to run a Python script as an Azure Machine Learning experiment.

The script contains the following code:

![Question Image](images/q285_q_0031000001.png)

You must specify a file dataset as an input to the script. The dataset consists of multiple large image files and must be streamed directly from its source.

You need to write code to define a ScriptRunConfig object for the experiment and pass the ds dataset as an argument.

Which code segment should you use?

* A.arguments = ['--input-data', ds.to_pandas_dataframe()]
* B.arguments = ['--input-data', ds.as_mount()]
* C.arguments = ['--data-data', ds]
* D.arguments = ['--input-data', ds.as_download()]

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Xsytt419</strong> <code>(Thu 30 Jun 2022 17:28)</code> - <em>Upvotes: 24</em></p><p>should be B?</p></blockquote>
<blockquote><p><strong>J_AR</strong> <code>(Fri 01 Jul 2022 14:39)</code> - <em>Upvotes: 15</em></p><p>Yes. Because 1) the data are images, not tabular, 2) the data are large and so should be mounted not downloaded.</p></blockquote>
<blockquote><p><strong>rgdk</strong> <code>(Sun 03 Jul 2022 14:16)</code> - <em>Upvotes: 9</em></p><p>Yes - also because it says &quot;must be streamed directly from its source&quot;</p></blockquote>
<blockquote><p><strong>dp100uber</strong> <code>(Wed 29 Jun 2022 21:28)</code> - <em>Upvotes: 8</em></p><p>Incorrect, it&#x27;s B</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 07:58)</code> - <em>Upvotes: 1</em></p><p>The main reasons cited include:
The data are large image files.
The requirement to stream data directly from the source.
The as_mount() method is suitable for streaming large datasets without downloading them.</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Fri 16 Aug 2024 09:13)</code> - <em>Upvotes: 1</em></p><p>A is only defined for instances of the TabularDataset class.</p></blockquote>
<blockquote><p><strong>Ran2025</strong> <code>(Thu 04 Apr 2024 05:56)</code> - <em>Upvotes: 1</em></p><p>B is correct!</p></blockquote>
<blockquote><p><strong>BR_CS</strong> <code>(Fri 16 Feb 2024 15:26)</code> - <em>Upvotes: 1</em></p><p>Clearly B</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Fri 21 Apr 2023 02:43)</code> - <em>Upvotes: 2</em></p><p>Answer is B</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Wed 12 Oct 2022 01:18)</code> - <em>Upvotes: 5</em></p><p>The correct answer is B. Because the question states &quot;for streaming data&quot;. To stream data, you mount the dataset.</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Sun 18 Sep 2022 08:46)</code> - <em>Upvotes: 4</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>danku</strong> <code>(Fri 02 Sep 2022 17:14)</code> - <em>Upvotes: 5</em></p><p>Must be &quot;B&quot;, as_mount() is for streaming data from data sources</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Mon 25 Jul 2022 07:34)</code> - <em>Upvotes: 5</em></p><p>streaming is the key</p></blockquote>

</details>

---

[<< Previous Question](question_284.md) | [Home](/index.md) | [Next Question >>](question_286.md)
