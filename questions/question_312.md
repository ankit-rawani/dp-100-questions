# Question 312

HOTSPOT -

You create an Azure Machine Learning workspace and a dataset. The dataset includes age values for a large group of diabetes patients. You use the dp_mean function from the SmartNoise library to calculate the mean of the age value. You store the value in a variable named age_mean.

You must output the value of the interval rage of released mean values that will be returned 95 percent of the time.

You need to complete the code.

Which code values should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q312_q_image431.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q312_ans_0_image613.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jl420</strong> <code>(Fri 08 Nov 2024 16:37)</code> - <em>Upvotes: 2</em></p><p>Correct: get_accuracy(): This function is typically used to obtain the accuracy level of the computed mean based on a given confidence level.

In this case, you want the 95% confidence interval, so you pass 0.95 to the function.
privacy_usage_to_accuracy() and compute_privacy_usage() are not typically used for confidence interval calculations; instead, they are related to privacy budget calculations.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 25 Jul 2023 20:53)</code> - <em>Upvotes: 3</em></p><p># Assuming you have the privacy usage stored in a variable called &#x27;usage&#x27;
alpha = 0.05  # 1 - 0.95 (to get 95% confidence interval)
https://github.com/opendp/smartnoise-samples/blob/master/analysis/accuracy_pitfalls.ipynb
accuracy = age_mean.get_accuracy(alpha, usage)

print(accuracy)</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Sat 03 Jun 2023 13:29)</code> - <em>Upvotes: 1</em></p><p>I think the ansver is get_accuracy(0.05)

        # get DP mean of age
        dp_D_tilde_mean_ages.append(sn.dp_mean(
            data = D_tilde,
            privacy_usage = {&#x27;epsilon&#x27;: 1}))

accuracy = dp_D_tilde_mean_ages[0].get_accuracy(0.05)

https://github.com/opendp/smartnoise-samples/blob/master/analysis/accuracy_pitfalls.ipynb</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Sat 03 Jun 2023 13:19)</code> - <em>Upvotes: 1</em></p><p>I think the ansver is wrong, I cant find any info about privacy_usage_to_accuracy in documentation.</p></blockquote>
<blockquote><p><strong>fqc</strong> <code>(Sat 20 May 2023 11:14)</code> - <em>Upvotes: 1</em></p><p>From Bard:

The compute_privacy_usage() method takes two parameters:

epsilon: The epsilon value for differential privacy
confidence: The confidence level
The compute_privacy_usage() method returns the privacy usage for the given epsilon and confidence level. The privacy usage is a measure of how much noise has been added to the data to protect privacy.

print(age_mean.compute_privacy_usage(0.05, 0.95)</p></blockquote>
<blockquote><p><strong>vish9</strong> <code>(Sat 13 May 2023 20:45)</code> - <em>Upvotes: 2</em></p><p>Not sure.</p></blockquote>

</details>

---

[<< Previous Question](question_311.md) | [Home](/index.md) | [Next Question >>](question_313.md)
