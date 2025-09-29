# Question 15

You need to consider the underlined segment to establish whether it is accurate.

To improve the amount of low incidence cases in a dataset, you should make use of the SMOTE module.

Select `No adjustment required` if the underlined segment is accurate. If the underlined segment is inaccurate, select the accurate option.

- A.No adjustment required.
- B.Remove Duplicate Rows
- C.Join Data
- D.Edit Metadata

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>PradhanManva</strong> <code>(Tue 24 Sep 2024 18:18)</code> - <em>Upvotes: 3</em></p><p>This is the answer.</p></blockquote>
<blockquote><p><strong>BakYac</strong> <code>(Sat 03 Feb 2024 17:54)</code> - <em>Upvotes: 2</em></p><p>SMOTE first selects a minority class instance a at random and finds its k nearest minority class neighbors. The synthetic instance is then created by choosing one of the k nearest neighbors b at random and connecting a and b to form a line segment in the feature space. The synthetic instances are generated as a convex combination of the two chosen instances a and b.</p></blockquote>
<blockquote><p><strong>exnaniantwort</strong> <code>(Sun 17 Sep 2023 04:48)</code> - <em>Upvotes: 4</em></p><p>This article describes how to use the SMOTE component in Azure Machine Learning designer to increase the number of underrepresented cases in a dataset that&#x27;s used for machine learning. SMOTE is a better way of increasing the number of rare cases than simply duplicating existing cases.

You connect the SMOTE component to a dataset that&#x27;s imbalanced. There are many reasons why a dataset might be imbalanced. For example, the category you&#x27;re targeting might be rare in the population, or the data might be difficult to collect. Typically, you use SMOTE when the class that you want to analyze is underrepresented.

The component returns a dataset that contains the original samples. It also returns a number of synthetic minority samples, depending on the percentage that you specify.

https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/smote</p></blockquote>

<blockquote><p><strong>pancman</strong> <code>(Thu 13 Apr 2023 18:32)</code> - <em>Upvotes: 1</em></p><p>Correct.</p></blockquote>

</details>

---

[<< Previous Question](question_14.md) | [Home](../index.md) | [Next Question >>](question_16.md)
