# Question 215

DRAG DROP -

You create a training pipeline using the Azure Machine Learning designer. You upload a CSV file that contains the data from which you want to train your model.

You need to use the designer to create a pipeline that includes steps to perform the following tasks:

✑ Select the training features using the pandas filter method.

✑ Train a model based on the naive_bayes.GaussianNB algorithm.

✑ Return only the Scored Labels column by using the query

✑ SELECT [Scored Labels] FROM t1;

Which modules should you use? To answer, drag the appropriate modules to the appropriate locations. Each module name may be used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

Select and Place:

![Question Image](images/q215_q_0020000001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q215_ans_0_image608.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>JB246</strong> <code>(Tue 27 Apr 2021 16:23)</code> - <em>Upvotes: 74</em></p><p>1. Execute python script
2. Create Python mode (for using naive_bayes.GausianNB)
3. Apply SQL Transform
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/create-python-model
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/apply-sql-transformation</p></blockquote>
<blockquote><p><strong>gunn_m</strong> <code>(Sun 24 Nov 2024 21:33)</code> - <em>Upvotes: 1</em></p><p>Totally agree with this answer</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Mon 13 Dec 2021 17:57)</code> - <em>Upvotes: 1</em></p><p>Totally agree with this answer</p></blockquote>
<blockquote><p><strong>Thornehead</strong> <code>(Wed 23 Mar 2022 19:37)</code> - <em>Upvotes: 1</em></p><p>I couldn&#x27;t find anything called naive_bayes.GaussianNB algorithm in the documentation link provided. So your answer is correct</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Thu 08 Jul 2021 08:45)</code> - <em>Upvotes: 5</em></p><p>Create Python model (typo). But you are right!</p></blockquote>
<blockquote><p><strong>hendriktytgatpwc</strong> <code>(Sun 14 Mar 2021 17:02)</code> - <em>Upvotes: 13</em></p><p>I rebuild this network in Designer and the answer is totally wrong:
It should be from top to bottom = Execute Python script (after dataset), before train model the 2 Class NN module, after scoring it should be SQL Transformation</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Thu 18 Mar 2021 09:30)</code> - <em>Upvotes: 2</em></p><p>I agree</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Thu 18 Mar 2021 09:32)</code> - <em>Upvotes: 1</em></p><p>and the question asks :
Train a model based on the naive_bayes.GaussianNB algorithm.
But there is not an option for this</p></blockquote>
<blockquote><p><strong>brendal89</strong> <code>(Tue 06 Apr 2021 07:13)</code> - <em>Upvotes: 12</em></p><p>That can&#x27;t be correct since they are asking for Naive Bayes
* box 1: execute Python script (the only way to use the pandas filter method)
* box 2: exectue python script (see: https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/create-python-model)
* box 3: apply SQL transformation (the SELECT statement indicates we should use SQL here)</p></blockquote>
<blockquote><p><strong>bruce</strong> <code>(Wed 07 Apr 2021 08:03)</code> - <em>Upvotes: 8</em></p><p>Should it be Create python model for the 2nd?</p></blockquote>
<blockquote><p><strong>gtyeap87</strong> <code>(Wed 16 Oct 2024 13:20)</code> - <em>Upvotes: 3</em></p><p>It should be 
1. Select columns in dataset
2. Create Phython model
3.Execute Phython script
https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/create-python-model?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>LM12</strong> <code>(Tue 09 Jul 2024 07:07)</code> - <em>Upvotes: 2</em></p><p>1.	select cols
2.	Create model
3.	execute python script. 
The exact example here :
https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/create-python-model?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 18 Jul 2023 02:59)</code> - <em>Upvotes: 1</em></p><p>SLECT COLUMNS, CREATE PYTHON MODEL, APPLY SQL TRANSFORMATION</p></blockquote>
<blockquote><p><strong>umair_hanu</strong> <code>(Tue 11 Jul 2023 09:42)</code> - <em>Upvotes: 1</em></p><p>a)select column in dataset  
b)python model
c)python script</p></blockquote>
<blockquote><p><strong>MattAnya</strong> <code>(Wed 04 Jan 2023 06:46)</code> - <em>Upvotes: 5</em></p><p>on 03 Jan 2023</p></blockquote>
<blockquote><p><strong>therealola</strong> <code>(Sat 18 Jun 2022 01:42)</code> - <em>Upvotes: 6</em></p><p>on exam 18-06-22
------
1. Execute python script
2. Create Python model
3. Apply SQL Transform</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sun 22 May 2022 13:50)</code> - <em>Upvotes: 2</em></p><p>1. select columns
2. NB model
3. SQL Transform

My answer will be that ...</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Thu 26 May 2022 16:15)</code> - <em>Upvotes: 1</em></p><p>Read question again ...
1. If have to use pandas filter, then script
2. If Bayes is the algorithm, then python model</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Fri 22 Apr 2022 10:48)</code> - <em>Upvotes: 2</em></p><p>on exam 04/22/2022</p></blockquote>
<blockquote><p><strong>kkkk_jjjj</strong> <code>(Fri 18 Mar 2022 09:42)</code> - <em>Upvotes: 3</em></p><p>on exam 18/03/2022</p></blockquote>
<blockquote><p><strong>TheYazan</strong> <code>(Thu 10 Mar 2022 05:54)</code> - <em>Upvotes: 1</em></p><p>On march 2022</p></blockquote>
<blockquote><p><strong>Tushazz</strong> <code>(Tue 04 Jan 2022 16:43)</code> - <em>Upvotes: 1</em></p><p>1.left side box:execute python script.
2.Select columns in dataset
3.apply SQL transformation</p></blockquote>
<blockquote><p><strong>JoshuaXu</strong> <code>(Sat 06 Nov 2021 22:52)</code> - <em>Upvotes: 1</em></p><p>On 6 Nov 2021, agree with the highest voted answer (by JB246).</p></blockquote>
<blockquote><p><strong>farahpeebs</strong> <code>(Sun 24 Oct 2021 02:21)</code> - <em>Upvotes: 8</em></p><p>It should be:
Box 1: Select columns in dataset
Box 2: Create python model
Box 3: Execute python script

Based on this link: https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/create-python-model</p></blockquote>
<blockquote><p><strong>AjoseO</strong> <code>(Sun 20 Feb 2022 07:40)</code> - <em>Upvotes: 1</em></p><p>Correct!</p></blockquote>
<blockquote><p><strong>skrjha20</strong> <code>(Sun 17 Oct 2021 07:31)</code> - <em>Upvotes: 1</em></p><p>Select columns ftom dataset
create model
Apply SQL Transformations</p></blockquote>
<blockquote><p><strong>skrjha20</strong> <code>(Mon 27 Sep 2021 16:27)</code> - <em>Upvotes: 4</em></p><p>1.Select columns in dataset
2.Create Python Model
3.Execute Python Script
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/create-python-model</p></blockquote>

</details>

---

[<< Previous Question](question_214.md) | [Home](/index.md) | [Next Question >>](question_216.md)
