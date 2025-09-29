# Question 483

You have a dataset that includes confidential data. You use the dataset to train a model.

You must use a differential privacy parameter to keep the data of individuals safe and private.

You need to reduce the effect of user data on aggregated results.

What should you do?

- A.Decrease the value of the epsilon parameter to reduce the amount of noise added to the data
- B.Increase the value of the epsilon parameter to decrease privacy and increase accuracy
- C.Decrease the value of the epsilon parameter to increase privacy and reduce accuracy
- D.Set the value of the epsilon parameter to 1 to ensure maximum privacy

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>GHill1982</strong> <code>(Wed 17 Jul 2024 05:16)</code> - <em>Upvotes: 1</em></p><p>To reduce the effect of user data on aggregated results, you should use a smaller value of the differential privacy parameter, also known as epsilon or ε. This parameter controls the level of privacy and the amount of noise added to the data. A smaller epsilon means more noise and less influence of any individual record on the output of the analysis.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 24 Aug 2023 14:17)</code> - <em>Upvotes: 1</em></p><p>C. A lower epsilon reduces the impact of an individual&#x27;s data on aggregated results, increasing privacy and reducing accuracy</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 25 Apr 2023 06:45)</code> - <em>Upvotes: 3</em></p><p>A lower epsilon reduces the impact of an individual&#x27;s data on aggregated results, increasing privacy and reducing accuracy

https://learn.microsoft.com/zh-tw/training/modules/explore-differential-privacy/5-knowledge-check</p></blockquote>

<blockquote><p><strong>tgaos</strong> <code>(Sun 13 Aug 2023 03:34)</code> - <em>Upvotes: 1</em></p><p>Check this url: https://learn.microsoft.com/en-us/training/modules/explore-differential-privacy/5-knowledge-check
This guy is right, answer is C</p></blockquote>
<blockquote><p><strong>nahner</strong> <code>(Wed 08 Mar 2023 09:54)</code> - <em>Upvotes: 3</em></p><p>&quot;The lower the epsilon, the less impact an individual&#x27;s data has on aggregated results, and therefore the risk of exposure is reduced.&quot; See https://docs.microsoft.com/en-us/training/modules/explore-differential-privacy/5-knowledge-check</p></blockquote>
<blockquote><p><strong>Xubh13</strong> <code>(Fri 10 Mar 2023 13:41)</code> - <em>Upvotes: 1</em></p><p>Have you been given DP100 recently?</p></blockquote>
<blockquote><p><strong>bbigwolf</strong> <code>(Wed 01 Mar 2023 04:34)</code> - <em>Upvotes: 2</em></p><p>&quot;You need to reduce the effect of user data on aggregated results&quot; should be B</p></blockquote>
<blockquote><p><strong>dalinar_kholin</strong> <code>(Fri 30 Jun 2023 13:14)</code> - <em>Upvotes: 1</em></p><p>Wrong!
https://github.com/MicrosoftLearning/mslearn-dp100/blob/main/13%20-%20Explore%20Differential%20Privacy.ipynb</p></blockquote>

</details>

---

[<< Previous Question](question_482.md) | [Home](../index.md) | [Next Question >>](question_484.md)
