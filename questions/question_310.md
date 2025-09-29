# Question 310

HOTSPOT

-

You are implementing hyperparameter tuning for a model training from a notebook. The notebook is in an Azure Machine Learning workspace. You add code that imports all relevant Python libraries.

You must configure Bayesian sampling over the search space for the num_hidden_layers and batch_size hyperparameters.

You need to complete the following Python code to configure Bayesian sampling.

Which code segments should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q310_q_image427.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q310_ans_0_image428.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>haby</strong> <code>(Mon 18 Dec 2023 20:08)</code> - <em>Upvotes: 6</em></p><p>correct for me. 
range(16,128,16) means select all numbers from 16 to 128 with 16 intervals. 
for i in range(16,128,16) :
    print(i)
output : 
16
32
...

Not uniform since uniform should only have 2 parameters:(min_num, max_num)
ref : https://learn.microsoft.com/en-us/python/api/azureml-train-core/azureml.train.hyperdrive.parameter_expressions?view=azure-ml-py</p></blockquote>
<blockquote><p><strong>jl420</strong> <code>(Fri 08 Nov 2024 16:28)</code> - <em>Upvotes: 1</em></p><p>this question is broken</p></blockquote>
<blockquote><p><strong>Nghia1</strong> <code>(Tue 06 Jun 2023 20:01)</code> - <em>Upvotes: 3</em></p><p>correct
https://learn.microsoft.com/en-us/training/modules/tune-hyperparameters-with-azure-machine-learning/3-sampling</p></blockquote>
<blockquote><p><strong>orionduo</strong> <code>(Fri 01 Sep 2023 03:53)</code> - <em>Upvotes: 1</em></p><p>your link gives the answer
choice &amp; uniform
but you said the anwser is correct
weird</p></blockquote>
<blockquote><p><strong>Gosku666</strong> <code>(Sun 25 Jun 2023 16:26)</code> - <em>Upvotes: 1</em></p><p>Regarding link that you&#x27;ve added should be: choice and uniform for Bayesian sampling:

&quot;You can only use Bayesian sampling with choice, uniform, and quniform parameter expressions, and you can&#x27;t combine it with an early-termination policy.&quot;</p></blockquote>

</details>

---

[<< Previous Question](question_309.md) | [Home](/index.md) | [Next Question >>](question_311.md)
