# Question 279

You plan to run a Python script as an Azure Machine Learning experiment.

The script must read files from a hierarchy of folders. The files will be passed to the script as a dataset argument.

You must specify an appropriate mode for the dataset argument.

Which two modes can you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

* A.to_pandas_dataframe()
* B.as_download()
* C.as_upload()
* D.as_mount()

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>exam_monkey1234</strong> <code>(Fri 02 Jul 2021 11:08)</code> - <em>Upvotes: 33</em></p><p>Should have 2 answers right? I thought B and D.</p></blockquote>
<blockquote><p><strong>ML_Novice</strong> <code>(Thu 18 Nov 2021 16:43)</code> - <em>Upvotes: 1</em></p><p>Could you explain why please?</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Sat 10 Jul 2021 15:12)</code> - <em>Upvotes: 8</em></p><p>yes correct answer should B and D</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Sun 11 Jul 2021 14:15)</code> - <em>Upvotes: 6</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>ferdcoz</strong> <code>(Tue 17 Dec 2024 15:17)</code> - <em>Upvotes: 1</em></p><p>B and D since it&#x27;s asking for two modes</p></blockquote>
<blockquote><p><strong>D0ktor</strong> <code>(Tue 19 Nov 2024 17:54)</code> - <em>Upvotes: 1</em></p><p>B and D</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 08 Jun 2024 06:37)</code> - <em>Upvotes: 1</em></p><p>B and D</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 20 Oct 2023 04:14)</code> - <em>Upvotes: 1</em></p><p>Correct answer: B, D

azureml.data.FileDataSet.as_mount() --&gt; https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.data.filedataset?view=azure-ml-py#azureml-data-filedataset-as-mount

azureml.data.FileDataSet.as_download() --&gt; https://learn.microsoft.com/en-us/python/api/azureml-core/azureml.data.filedataset?view=azure-ml-py#azureml-data-filedataset-as-download

to_pandas_dataframe() and as_upload() are fiction, they are not existing.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 22 Feb 2023 01:36)</code> - <em>Upvotes: 1</em></p><p>C. as_upload() and D. as_mount()</p></blockquote>
<blockquote><p><strong>RamundiGR</strong> <code>(Fri 20 Jan 2023 17:20)</code> - <em>Upvotes: 1</em></p><p>You should highlight 2 Answers not just one</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sat 18 Jun 2022 01:48)</code> - <em>Upvotes: 1</em></p><p>On exam 18-06-22
----------
B &amp; D</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Wed 08 Jun 2022 11:05)</code> - <em>Upvotes: 1</em></p><p>B&amp;D, mount only for linux, and download is for all</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Wed 20 Oct 2021 09:52)</code> - <em>Upvotes: 3</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>TomFinch</strong> <code>(Fri 20 Aug 2021 18:52)</code> - <em>Upvotes: 3</em></p><p>Answer - B &amp; D</p></blockquote>
<blockquote><p><strong>NickData90</strong> <code>(Sun 08 Aug 2021 07:27)</code> - <em>Upvotes: 2</em></p><p>B &amp; D
as_download: downloads the dataset
as_mount: provides a reference to the dataset</p></blockquote>
<blockquote><p><strong>slash_nyk</strong> <code>(Fri 16 Jul 2021 10:05)</code> - <em>Upvotes: 2</em></p><p>B &amp; D are the answers</p></blockquote>
<blockquote><p><strong>slash_nyk</strong> <code>(Sat 10 Jul 2021 09:21)</code> - <em>Upvotes: 2</em></p><p>I agree that B and D should be the correct answe</p></blockquote>

</details>

---

[<< Previous Question](question_278.md) | [Home](/index.md) | [Next Question >>](question_280.md)
