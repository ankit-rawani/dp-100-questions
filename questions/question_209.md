# Question 209

HOTSPOT -

You create a binary classification model to predict whether a person has a disease.

You need to detect possible classification errors.

Which error type should you choose for each description? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q209_q_0019300001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q209_ans_0_0019400001.png" alt="Answer Image"><br>
<p>Box 1: True Positive -</p>
<p>A true positive is an outcome where the model correctly predicts the positive class</p>
<p>Box 2: True Negative -</p>
<p>A true negative is an outcome where the model correctly predicts the negative class.</p>
<p>Box 3: False Positive -</p>
<p>A false positive is an outcome where the model incorrectly predicts the positive class.</p>
<p>Box 4: False Negative -</p>
<p>A false negative is an outcome where the model incorrectly predicts the negative class.</p>
<p>Note: Let&#x27;s make the following definitions:</p>
<p>&quot;Wolf&quot; is a positive class.</p>
<p>&quot;No wolf&quot; is a negative class.</p>
<p>We can summarize our &quot;wolf-prediction&quot; model using a 2x2 confusion matrix that depicts all four possible outcomes:</p>
<p>Reference:</p>
<p>https://developers.google.com/machine-learning/crash-course/classification/true-false-positive-negative</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>lucazav</strong> <code>(Mon 18 Apr 2022 21:29)</code> - <em>Upvotes: 19</em></p><p>A mnemonic rule could be:
  - &quot;Positive&quot; and &quot;Negative&quot; are related to the output of the model, once the positive result is associated to an outcome by convention.
  - &quot;True&quot; and &quot;False&quot; are the result comparing the model output to the reality 

That said, given that is positive a person that has a disease by convention, &quot;the model predict that a person has a disease (Positive), and the person doesn&#x27;t have a disease (False with respect to the prediction): it&#x27;s a False Positive</p></blockquote>
<blockquote><p><strong>Nugi</strong> <code>(Mon 14 Feb 2022 10:20)</code> - <em>Upvotes: 13</em></p><p>True Positive, True Negative, False Positive, False Negative.</p></blockquote>
<blockquote><p><strong>nokcha1006</strong> <code>(Sun 17 Nov 2024 07:51)</code> - <em>Upvotes: 1</em></p><p>True Positive, True Negative, False Negative, False Positive.
&quot;Wolf&quot; is a [P (Positives)] : Reality: A wolf threatened [T (True)]
                          Reality: No wolf threatened. [F (False)]
&quot;No wolf&quot; is a [N (Negatives)] : Reality: No wolf threatened. [T (True)]
                               Reality: A wolf threatened [F (False)]</p></blockquote>
<blockquote><p><strong>Mirjalol</strong> <code>(Sat 03 Aug 2024 15:45)</code> - <em>Upvotes: 1</em></p><p>tp
tn
fp
fn</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Mon 14 Aug 2023 09:42)</code> - <em>Upvotes: 2</em></p><p>Correct</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Sun 25 Dec 2022 21:58)</code> - <em>Upvotes: 5</em></p><p>given answers are correct.</p></blockquote>

</details>

---

[<< Previous Question](question_208.md) | [Home](/index.md) | [Next Question >>](question_210.md)
