# Question 224

You register a file dataset named csv_folder that references a folder. The folder includes multiple comma-separated values (CSV) files in an Azure storage blob container.

You plan to use the following code to run a script that loads data from the file dataset. You create and instantiate the following variables:

![Question Image](images/q224_q_0021500001.png)

You have the following code:

![Question Image](images/q224_q_0021500002.png)

You need to pass the dataset to ensure that the script can read the files it references.

Which code segment should you insert to replace the code comment?

* A.inputs=[file_dataset.as_named_input('training_files')],
* B.inputs=[file_dataset.as_named_input('training_files').as_mount()],
* C.inputs=[file_dataset.as_named_input('training_files').to_pandas_dataframe()],
* D.script_params={'--training_files': file_dataset},

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>
<p>Example:</p>
<p>from azureml.train.estimator import Estimator</p>
<p>script_params = {</p>
<p># to mount files referenced by mnist dataset</p>
<p>&#x27;--data-folder&#x27;: mnist_file_dataset.as_named_input(&#x27;mnist_opendataset&#x27;).as_mount(),</p>
<p>&#x27;--regularization&#x27;: 0.5</p>
<p>}</p>
<p>est = Estimator(source_directory=script_folder,</p>
<p>script_params=script_params,</p>
<p>compute_target=compute_target,</p>
<p>environment_definition=env,</p>
<p>entry_script=&#x27;train.py&#x27;)</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-train-models-with-aml</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>chaudha4</strong> <code>(Thu 05 May 2022 13:37)</code> - <em>Upvotes: 6</em></p><p>Estimator is deprecated. Can anyone confirm if they saw a question on this topic lately ?</p></blockquote>
<blockquote><p><strong>ralucabala</strong> <code>(Wed 20 Apr 2022 22:32)</code> - <em>Upvotes: 5</em></p><p>why is not A? is mount() required if we have already registered the dataset?</p></blockquote>
<blockquote><p><strong>azure1000</strong> <code>(Thu 04 Aug 2022 15:35)</code> - <em>Upvotes: 4</em></p><p>Because its a CSV.</p></blockquote>
<blockquote><p><strong>azure1000</strong> <code>(Thu 04 Aug 2022 15:36)</code> - <em>Upvotes: 1</em></p><p>My bad... I missed the option.</p></blockquote>
<blockquote><p><strong>HkIsCrazY</strong> <code>(Wed 22 Jun 2022 11:43)</code> - <em>Upvotes: 1</em></p><p>Same concern. Why not A?</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Thu 07 Jul 2022 09:48)</code> - <em>Upvotes: 2</em></p><p>Because to &quot;loads data&quot; needs to call &quot;as_mount()&quot; function.</p></blockquote>
<blockquote><p><strong>ahmeddataengineer</strong> <code>(Sat 17 Dec 2022 09:58)</code> - <em>Upvotes: 1</em></p><p>when to use &quot;as_dowload&quot; and &quot;as_mount&quot; please what is the difference</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Fri 28 Jun 2024 11:35)</code> - <em>Upvotes: 1</em></p><p>B - ChatGPT</p></blockquote>
<blockquote><p><strong>racnaoamo</strong> <code>(Fri 19 May 2023 07:54)</code> - <em>Upvotes: 2</em></p><p>on exam 18-5-22</p></blockquote>
<blockquote><p><strong>hargur</strong> <code>(Thu 20 Oct 2022 09:45)</code> - <em>Upvotes: 2</em></p><p>on 19Oct2021</p></blockquote>
<blockquote><p><strong>kisskeo</strong> <code>(Fri 07 Oct 2022 20:26)</code> - <em>Upvotes: 2</em></p><p>On Exam 01 Oct 2021</p></blockquote>
<blockquote><p><strong>snsnsnsn</strong> <code>(Sat 03 Sep 2022 07:32)</code> - <em>Upvotes: 4</em></p><p>on 2/9/21</p></blockquote>
<blockquote><p><strong>mayank25</strong> <code>(Fri 13 May 2022 11:49)</code> - <em>Upvotes: 2</em></p><p>Yes please tell if estimator questions still appear?</p></blockquote>
<blockquote><p><strong>NaishinMatiri</strong> <code>(Thu 21 Apr 2022 20:56)</code> - <em>Upvotes: 1</em></p><p>if the question specifies that we&#x27;re planing to use an script, shouldn&#x27;t we be using script_params?</p></blockquote>

</details>

---

[<< Previous Question](question_223.md) | [Home](/index.md) | [Next Question >>](question_225.md)
