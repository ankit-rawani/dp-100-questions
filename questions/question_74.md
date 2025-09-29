# Question 74

You are analyzing a dataset by using Azure Machine Learning Studio.

You need to generate a statistical summary that contains the p-value and the unique count for each feature column.

Which two modules can you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

* A.Computer Linear Correlation
* B.Export Count Table
* C.Execute Python Script
* D.Convert to Indicator Values
* E.Summarize Data

<details>
  <summary>Show Suggested Answer</summary>

  <strong>CE</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>lucazav</strong> <code>(Thu 14 Apr 2022 13:06)</code> - <em>Upvotes: 32</em></p><p>Summarize Data module output also has the following columns: P0.5, P1, P5, P95, P99, P99.5
Probably the person in charge of these tests was not very prepared and did not even check Microsoft&#x27;s docs, so he confused &quot;percentile&quot; values with &quot;p-&quot; values. By the way, &quot;p-values&quot; of what!?</p></blockquote>
<blockquote><p><strong>azurelearner666</strong> <code>(Tue 10 Oct 2023 15:32)</code> - <em>Upvotes: 2</em></p><p>Fully agree, sometimes the questions are a bit &quot;off&quot; (and that&#x27;s polite...)</p></blockquote>
<blockquote><p><strong>Arend78</strong> <code>(Sat 08 Jun 2024 08:28)</code> - <em>Upvotes: 2</em></p><p>Indeed, very confusing. Thanks for mentioning this!</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sat 03 Aug 2024 03:55)</code> - <em>Upvotes: 11</em></p><p>C. Execute Python Script
E. Summarize Data

In Azure Machine Learning Studio, you can use the &quot;Summarize Data&quot; module to generate a statistical summary that includes unique count and basic statistics such as mean, standard deviation, minimum, maximum, and quartiles for each feature column. To calculate p-value, you would need to use a &quot;Execute Python Script&quot; module and write a custom code to perform the hypothesis test and compute the p-value.
The &quot;Export Count Table&quot; module in Azure Machine Learning Studio only provides a count of the number of instances of each unique value in a single feature column, it doesn&#x27;t provide statistical summary information like the mean, standard deviation, minimum, maximum, quartiles, or p-value. To get the p-value and a more comprehensive statistical summary, you would need to use the &quot;Execute Python Script&quot; module and write custom code as described in my previous answer.</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Mon 11 Nov 2024 08:42)</code> - <em>Upvotes: 3</em></p><p>C. Execute Python Script
E. Summarize Data

The &quot;Execute Python Script&quot; module allows you to run your own Python script, which can be used to calculate any statistic, including unique counts and p-values.

The &quot;Summarize Data&quot; module in Azure Machine Learning Studio provides a statistical summary of the input dataset, including count, mean, mode, standard deviation, minimum, and maximum.

And like somebody mentioned, it should be percentile and not p-value.</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Thu 13 Jun 2024 17:39)</code> - <em>Upvotes: 1</em></p><p>Options AD</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Sat 17 Sep 2022 17:54)</code> - <em>Upvotes: 4</em></p><p>Answer is just &#x27;C&#x27;</p></blockquote>
<blockquote><p><strong>saurabhk1</strong> <code>(Sun 04 Sep 2022 13:53)</code> - <em>Upvotes: 4</em></p><p>Actually, the question is not clear about which type of p-value, it wants to calculate. 
Only module that can do it is &quot;Execute a python script&quot;</p></blockquote>
<blockquote><p><strong>Askme101</strong> <code>(Sun 26 Jun 2022 13:15)</code> - <em>Upvotes: 3</em></p><p>it should say percentile values</p></blockquote>
<blockquote><p><strong>modschegiebsch</strong> <code>(Mon 03 Jan 2022 08:33)</code> - <em>Upvotes: 7</em></p><p>Isn&#x27;t &quot;Execute a python script&quot; actually the only option to calculate the p-value?</p></blockquote>

</details>

---

[<< Previous Question](question_73.md) | [Home](/index.md) | [Next Question >>](question_75.md)
