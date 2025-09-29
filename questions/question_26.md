# Question 26

You have recently concluded the construction of a binary classification machine learning model.

You are currently assessing the model. You want to make use of a visualization that allows for precision to be used as the measurement for the assessment.

Which of the following actions should you take?

- A.You should consider using Venn diagram visualization.
- B.You should consider using Receiver Operating Characteristic (ROC) curve visualization.
- C.You should consider using Box plot visualization.
- D.You should consider using the Binary classification confusion matrix visualization.

<details>
  <summary>Show Suggested Answer</summary>

<strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>spaceykacey</strong> <code>(Wed 11 May 2022 18:42)</code> - <em>Upvotes: 16</em></p><p>you cannot visualize precision with ROC. True Positive Rate(on ROC&#x27;s y axis) = Recall. Not precision. PR curve is used to visualize precision.

I think I would go with Confusion matrix even though it requires further computations</p></blockquote>

<blockquote><p><strong>evangelist</strong> <code>(Wed 21 Aug 2024 11:38)</code> - <em>Upvotes: 2</em></p><p>it&#x27;s important to note that while ROC is immensely useful for evaluating and comparing models, it doesn&#x27;t directly display precision.</p></blockquote>
<blockquote><p><strong>jdada</strong> <code>(Fri 10 May 2024 14:56)</code> - <em>Upvotes: 1</em></p><p>D. You should consider using the Binary classification confusion matrix visualization.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 19 Apr 2024 07:56)</code> - <em>Upvotes: 1</em></p><p>Based on https://learn.microsoft.com/en-us/azure/machine-learning/how-to-understand-automated-ml?view=azureml-api-2#binary-vs-multiclass-classification-metrics . Visualization for Classification: Not has Venn diagram; box plot diagram. Consider ROC (Receiver Operating Characteristic) and Binary classification confusion matrix.

&#x27;The receiver operating characteristic (ROC) curve plots the relationship between true positive rate (TPR) and false positive rate (FPR) as the decision threshold changes.&#x27;

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-understand-automated-ml?view=azureml-api-2#confusion-matrix

Confusion matrix has &#x27;precision to be used as the measurement&#x27;, but Receiver operating characteristic has not.</p></blockquote>

<blockquote><p><strong>PradhanManva</strong> <code>(Sun 24 Mar 2024 19:21)</code> - <em>Upvotes: 1</em></p><p>This is the answer.</p></blockquote>
<blockquote><p><strong>SoftAI</strong> <code>(Thu 12 Oct 2023 16:59)</code> - <em>Upvotes: 2</em></p><p>classification confusion matrix is the best accuracy measure</p></blockquote>
<blockquote><p><strong>ZIMARAKI</strong> <code>(Sat 02 Sep 2023 11:27)</code> - <em>Upvotes: 2</em></p><p>D for precision</p></blockquote>
<blockquote><p><strong>KarthikKumarK</strong> <code>(Tue 15 Aug 2023 03:34)</code> - <em>Upvotes: 2</em></p><p>Correct.
https://builtin.com/data-science/precision-and-recall</p></blockquote>
<blockquote><p><strong>clark88</strong> <code>(Wed 05 Jul 2023 13:29)</code> - <em>Upvotes: 3</em></p><p>precision, recall, f1-score. Are part of the confusion matrix, I agree that this answer is correct.</p></blockquote>
<blockquote><p><strong>VJPrakash</strong> <code>(Thu 10 Feb 2022 16:52)</code> - <em>Upvotes: 4</em></p><p>Shouldnt the answer be &quot;B&quot;. ROC is a graph against TPR and FPR.. precision could be clearly visualized.</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Thu 13 Oct 2022 18:52)</code> - <em>Upvotes: 4</em></p><p>You can get the precision number without any further calculations in a confusion matrix. ROC curve shows True Positive vs. False Positive. But it doesn&#x27;t show precision.</p></blockquote>
<blockquote><p><strong>dijaa</strong> <code>(Mon 28 Feb 2022 06:46)</code> - <em>Upvotes: 5</em></p><p>we can plot confusion matrix as grid</p></blockquote>

</details>

---

[<< Previous Question](question_25.md) | [Home](../index.md) | [Next Question >>](question_27.md)
