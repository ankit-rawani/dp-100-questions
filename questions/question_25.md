# Question 25

You are preparing to train a regression model via automated machine learning. The data available to you has features with missing values, as well as categorical features with little discrete values.

You want to make sure that automated machine learning is configured as follows:

✑ missing values must be automatically imputed.

✑ categorical features must be encoded as part of the training task.

Which of the following actions should you take?

- A.You should make use of the featurization parameter with the 'auto' value pair.
- B.You should make use of the featurization parameter with the 'off' value pair.
- C.You should make use of the featurization parameter with the 'on' value pair.
- D.You should make use of the featurization parameter with the 'FeaturizationConfig' value pair.

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>tushy</strong> <code>(Mon 15 Jul 2024 09:25)</code> - <em>Upvotes: 2</em></p><p>In exam 14-01-2023</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 12 Apr 2024 08:35)</code> - <em>Upvotes: 3</em></p><p>The anwser is clear. Question keyword &#x27;automatically imputed&#x27; . Answer keyword &#x27;_auto_ value pair&#x27; .

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-features?view=azureml-api-1#configure-featurization</p></blockquote>

<blockquote><p><strong>endeesa</strong> <code>(Fri 08 Dec 2023 22:15)</code> - <em>Upvotes: 4</em></p><p>Answer is A, if you set featurization to &quot;auto&quot;, azure ml will do this for you

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-features?view=azureml-api-1#configure-featurization</p></blockquote>

<blockquote><p><strong>MarinaMijailovic</strong> <code>(Wed 25 Oct 2023 10:23)</code> - <em>Upvotes: 2</em></p><p>A) AUTO ML will handle the necessary preprocessing steps, such as imputing missing values and encoding categorical features, before training the regression model.</p></blockquote>
<blockquote><p><strong>lookaaaa</strong> <code>(Tue 23 May 2023 20:17)</code> - <em>Upvotes: 2</em></p><p>&quot;on&quot; is not an option, &quot;auto&quot; is</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 11 Apr 2023 06:24)</code> - <em>Upvotes: 2</em></p><p>A is correct.
https://learn.microsoft.com/zh-tw/azure/machine-learning/how-to-configure-auto-features#automatic-featurization</p></blockquote>
<blockquote><p><strong>exnaniantwort</strong> <code>(Fri 17 Mar 2023 06:10)</code> - <em>Upvotes: 1</em></p><p>The following table shows the accepted settings for featurization in the AutoMLConfig class:

Featurization configuration Description
&quot;featurization&quot;: &#x27;auto&#x27; Specifies that, as part of preprocessing, data guardrails and featurization steps are to be done automatically. This setting is the default.
&quot;featurization&quot;: &#x27;off&#x27; Specifies that featurization steps are not to be done automatically.
&quot;featurization&quot;: &#x27;FeaturizationConfig&#x27; Specifies that customized featurization steps are to be used. Learn how to customize featurization.</p></blockquote>

<blockquote><p><strong>ning</strong> <code>(Fri 16 Dec 2022 15:26)</code> - <em>Upvotes: 2</em></p><p>On is not an option</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Thu 13 Oct 2022 19:16)</code> - <em>Upvotes: 3</em></p><p>I change my answer, ON is not an option under featurization. Auto is correct.</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Thu 13 Oct 2022 19:15)</code> - <em>Upvotes: 1</em></p><p>They key word here is that you want to &quot;ensure&quot;. Therefore,  you need to turn the featurization option ON. Auto is not the correct answer. If you set it to auto, it is at the discretion of Auto ML to do the required actions stated in the question.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Fri 16 Dec 2022 15:25)</code> - <em>Upvotes: 2</em></p><p>I do not think &quot;on&quot; is an option
1. auto --&gt; correct answer here
2. off --&gt; nothing happens
3. an object of FeaturizationConfig class type --&gt; use the special setting</p></blockquote>

</details>

---

[<< Previous Question](question_24.md) | [Home](../index.md) | [Next Question >>](question_26.md)
