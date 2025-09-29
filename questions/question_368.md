# Question 368

HOTSPOT

-

You manage an Azure Machine Learning workspace.

You plan to train a natural language processing (NLP) model that will assign labels for designated tokens in unstructured text.

You need to configure the NLP task by using automated machine learning.

Which configuration values should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q368_q_image572.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q368_ans_0_image573.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Secure_Defense</strong> <code>(Wed 05 Feb 2025 18:50)</code> - <em>Upvotes: 1</em></p><p>Answers are correct:
- Named Entity Recognition (NER)
&quot;There are multiple possible tags for tokens in sequences. The task is to predict the tags for all the tokens for each sequence.

For example, extracting domain-specific entities from unstructured text, such as contracts or financial documents.&quot;

Ref: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-auto-train-nlp-models?view=azureml-api-2&amp;tabs=python#select-your-nlp-task

- CoNLL
&quot;Unlike multi-class or multi-label, which takes .csv format datasets, named entity recognition requires CoNLL format. The file must contain exactly two columns and in each row, the token and the label is separated by a single space.&quot;

Ref: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-auto-train-nlp-models?view=azureml-api-2&amp;tabs=python#named-entity-recognition-ner</p></blockquote>
<blockquote><p><strong>Fefnut</strong> <code>(Wed 20 Nov 2024 10:13)</code> - <em>Upvotes: 1</em></p><p>- Multi-label text classification because &quot; model that will assign labels for designated tokens in unstructured text&quot; implying there can be multiple labels for tokens.
- CSV because it&#x27;s the format for NLP multi-label task.
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-auto-train-nlp-models?view=azureml-api-2&amp;tabs=python</p></blockquote>
<blockquote><p><strong>jefimija</strong> <code>(Wed 23 Oct 2024 13:23)</code> - <em>Upvotes: 1</em></p><p>JSONL would be the best option</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Thu 28 Nov 2024 23:19)</code> - <em>Upvotes: 1</em></p><p>It is CSV</p></blockquote>
<blockquote><p><strong>Sadhak</strong> <code>(Thu 28 Nov 2024 23:19)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/azure/machine-learning/how-to-auto-train-nlp-models?view=azureml-api-2&amp;tabs=python#preparing-data</p></blockquote>
<blockquote><p><strong>ulg</strong> <code>(Fri 24 Jan 2025 12:11)</code> - <em>Upvotes: 1</em></p><p>Above website says: &quot;Unlike multi-class or multi-label, which takes .csv format datasets, named entity recognition requires CoNLL format.&quot;</p></blockquote>
<blockquote><p><strong>ulg</strong> <code>(Fri 24 Jan 2025 12:12)</code> - <em>Upvotes: 1</em></p><p>Hence, selected options are correct.</p></blockquote>

</details>

---

[<< Previous Question](question_367.md) | [Home](/index.md) | [Next Question >>](question_369.md)
