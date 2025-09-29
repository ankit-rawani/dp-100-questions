# Question 323

HOTSPOT

-

You use Azure Machine Learning and SmartNoise Python libraries to implement a differential privacy solution to protect a dataset containing citizen demographics for the city of Seattle in the United States.

The solution has the following requirements:

•	Allow for multiple queries targeting the mean and variance of the citizen’s age.

•	Ensure full plausible deniability.

You need to define the query rate limit to minimize the risk of re-identification.

What should you configure? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q323_q_image467.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q323_ans_0_image468.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>KeiNek</strong> <code>(Sun 09 Feb 2025 12:43)</code> - <em>Upvotes: 1</em></p><p>Box1 : privacy budget
Box2 : Set the epsilon value to the sum of epsilon values assigned to the mean and variance queries.</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 23 Aug 2024 11:24)</code> - <em>Upvotes: 1</em></p><p>correct answer.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 26 Jul 2024 13:46)</code> - <em>Upvotes: 3</em></p><p>Configuration option: C) Privacy Budget
Action: D) Set the epsilon value to the sum of epsilon values assigned to the mean and variance queries
When dealing with differential privacy, the &quot;privacy budget&quot; is often represented by the value of epsilon (ε). The value of epsilon is used to control the amount of noise added to the data to maintain privacy.

When you perform multiple queries against the dataset, each one &quot;uses&quot; a part of this privacy budget. In order to maintain an appropriate level of overall privacy, you should consider that each separate query could potentially leak some information. Therefore, the cumulative privacy loss or total epsilon should be the sum of the epsilons for each query, not the smallest or largest single value.
If you were to set the total epsilon to the smallest of the two values, you would be assuming that only one of the queries contributes to privacy loss, which is not the case.</p></blockquote>
<blockquote><p><strong>barb4ever2002</strong> <code>(Thu 27 Jun 2024 07:05)</code> - <em>Upvotes: 3</em></p><p>from chat gtp: 
To minimize the risk of re-identification and ensure full plausible deniability when implementing a differential privacy solution using Azure Machine Learning and the SmartNoise Python libraries, you should configure the privacy budget.

In this scenario, the appropriate action to take is:

Action:
3) Set the epsilon value to the smaller of the epsilon values assigned to the mean and variance queries.</p></blockquote>

</details>

---

[<< Previous Question](question_322.md) | [Home](/index.md) | [Next Question >>](question_324.md)
