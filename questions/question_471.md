# Question 471

You are creating a binary classification by using a two-class logistic regression model.

You need to evaluate the model results for imbalance.

Which evaluation metric should you use?

- A.Relative Absolute Error
- B.AUC Curve
- C.Mean Absolute Error
- D.Relative Squared Error
- E.Accuracy
- F.Root Mean Square Error

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>akgarg00</strong> <code>(Fri 26 Feb 2021 17:07)</code> - <em>Upvotes: 15</em></p><p>99% class 1 data and 1% class 2 data. If all prediction is class 1, we will attain 99% accuracy. So accuracy is incorrect answer</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 12 Apr 2022 21:48)</code> - <em>Upvotes: 1</em></p><p>Absolutely not. Funny thing is, you proved yourself wrong on why it shouldn&#x27;t be accuracy in the answer you gave.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 11:46)</code> - <em>Upvotes: 1</em></p><p>For evaluating a binary classification model, especially with imbalanced datasets, the Area Under the Receiver Operating Characteristic (AUC-ROC) Curve is an excellent metric. It&#x27;s insensitive to class imbalance and provides a good summary of the model&#x27;s performance across different classification thresholds.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 18 May 2024 06:20)</code> - <em>Upvotes: 1</em></p><p>AUC Curve (Area Under the Curve): The AUC-ROC (Receiver Operating Characteristic) curve is a performance measurement for classification problems at various threshold settings. AUC represents the degree or measure of separability, indicating how much the model is capable of distinguishing between classes. An AUC value of 0.5 suggests no discrimination (i.e., random guessing), whereas a value of 1.0 indicates perfect discrimination.

The AUC-ROC curve is particularly useful for evaluating models on imbalanced datasets because it is insensitive to changes in the class distribution. It provides a single metric that captures the trade-off between sensitivity (true positive rate) and specificity (true negative rate).</p></blockquote>

<blockquote><p><strong>phdykd</strong> <code>(Fri 24 Feb 2023 04:06)</code> - <em>Upvotes: 1</em></p><p>The appropriate evaluation metric to use for assessing imbalance in a binary classification model is the AUC Curve (B). AUC (Area Under the Curve) is a measure of the model&#x27;s ability to distinguish between positive and negative classes. AUC ranges from 0 to 1, where an AUC of 1 indicates perfect separation between the positive and negative classes, and an AUC of 0.5 indicates random chance. A high AUC value indicates that the model has a strong ability to correctly classify positive and negative instances, which is especially important in imbalanced datasets where one class may have significantly fewer instances than the other. Therefore, the AUC curve is a commonly used metric to evaluate the performance of binary classification models in the presence of class imbalance.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sun 12 Jun 2022 13:54)</code> - <em>Upvotes: 4</em></p><p>I guess weighted AUC is the best answer ...</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sun 12 Jun 2022 13:56)</code> - <em>Upvotes: 1</em></p><p>Or weighted accuracy</p></blockquote>
<blockquote><p><strong>[Removed]</strong> <code>(Thu 21 Apr 2022 05:11)</code> - <em>Upvotes: 1</em></p><p>What does it mean by &quot;evaluate the model results for imbalance&quot;? Does it mean evaluate the extent/degree of imbalance in the dataset? Or does it simply mean to evaluate the model when the underyling data is imbalanced?</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 12 Apr 2022 21:48)</code> - <em>Upvotes: 4</em></p><p>AUC is the correct answer.</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sat 12 Mar 2022 06:19)</code> - <em>Upvotes: 2</em></p><p>AUC seems to be the right answer as per this..  https://stats.stackexchange.com/questions/260164/auc-and-class-imbalance-in-training-test-dataset</p></blockquote>
<blockquote><p><strong>anonymjason</strong> <code>(Fri 09 Jul 2021 08:49)</code> - <em>Upvotes: 2</em></p><p>I would assume AUC Curve is a typo, because AUC is Area Under Curve. Seems it would be the right answer though.</p></blockquote>
<blockquote><p><strong>OmarF</strong> <code>(Tue 16 Mar 2021 10:12)</code> - <em>Upvotes: 1</em></p><p>It should be E (Accuracy) The AUC is the area under ROC curve so it&#x27;s a number not a curve. 
So there is no curve called AUC curve.</p></blockquote>
<blockquote><p><strong>sim39</strong> <code>(Tue 07 Sep 2021 09:09)</code> - <em>Upvotes: 1</em></p><p>No, can&#x27;t be accuracy. I agree that there is nothing called &quot;AUC curve&quot;, but I assume it&#x27;s supposed to say just AUC</p></blockquote>
<blockquote><p><strong>Askme101</strong> <code>(Sun 27 Dec 2020 05:31)</code> - <em>Upvotes: 2</em></p><p>Should Accuracy not be included along with AUC?</p></blockquote>
<blockquote><p><strong>Neuron</strong> <code>(Tue 02 Feb 2021 19:59)</code> - <em>Upvotes: 10</em></p><p>no, accuracy can be misleading when the dataset is skewed (not balanced). AUC provides better insight overall.</p></blockquote>
<blockquote><p><strong>dijaa</strong> <code>(Sat 28 Aug 2021 10:52)</code> - <em>Upvotes: 3</em></p><p>accuracy fails when imbalance exists.</p></blockquote>

</details>

---

[<< Previous Question](question_470.md) | [Home](../index.md) | [Next Question >>](question_472.md)
