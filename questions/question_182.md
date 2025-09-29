# Question 182

Note: This question is part of a series of questions that present the same scenario. Each question in the series contains a unique solution that might meet the stated goals. Some question sets might have more than one correct solution, while others might not have a correct solution.

After you answer a question in this section, you will NOT be able to return to it. As a result, these questions will not appear in the review screen.

You are using Azure Machine Learning to run an experiment that trains a classification model.

You want to use Hyperdrive to find parameters that optimize the AUC metric for the model. You configure a HyperDriveConfig for the experiment by running the following code:

![Question Image](images/q182_q_0014400001.png)

You plan to use this configuration to run a script that trains a random forest model and then tests it with validation data. The label values for the validation data are stored in a variable named y_test variable, and the predicted probabilities from the model are stored in a variable named y_predicted.

You need to add logging to the script to allow Hyperdrive to optimize hyperparameters for the AUC metric.

Solution: Run the following code:

![Question Image](images/q182_q_0014400002.png)

Does the solution meet the goal?

* A.Yes
* B.No

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>DennisWitjes</strong> <code>(Mon 14 Feb 2022 17:16)</code> - <em>Upvotes: 20</em></p><p>To allow optimize hyperdrive you require to use Azure ML run context to log and use it in the hyperdrive config.

logging.info() logs it but does not allow for optimizing hyperdrive

See: https://docs.microsoft.com/en-us/learn/modules/tune-hyperparameters-with-azure-machine-learning/6a-knowledge-check</p></blockquote>
<blockquote><p><strong>JohnDup</strong> <code>(Wed 08 Jun 2022 14:23)</code> - <em>Upvotes: 1</em></p><p>The question is &quot;You need to add logging to the script to allow Hyperdrive to optimize hyperparameters for the AUC metric.&quot; so it should be correct, since it only ask for log. 
Answer: A. Yes</p></blockquote>
<blockquote><p><strong>spaceykacey</strong> <code>(Tue 26 Apr 2022 13:14)</code> - <em>Upvotes: 2</em></p><p>agreed. correct answer is B.</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Wed 14 Sep 2022 02:54)</code> - <em>Upvotes: 6</em></p><p>Copying a good explanation: The question is not about just logging AUC but logging to allow Hyperdrive to optimize hyperparameters for the AUC metric. So you must log using run instance. That way the Hyperdrive has access to that metric to compare with other runs. SO the correct answer is &quot;No&quot;</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 02 Dec 2024 06:37)</code> - <em>Upvotes: 1</em></p><p># Get the current run context
run = Run.get_context()

# Log the AUC score
run.log(&quot;AUC&quot;, auc)</p></blockquote>
<blockquote><p><strong>PradhanManva</strong> <code>(Mon 25 Mar 2024 07:20)</code> - <em>Upvotes: 1</em></p><p>B is the answer</p></blockquote>
<blockquote><p><strong>abhishekm94</strong> <code>(Sat 16 Dec 2023 04:01)</code> - <em>Upvotes: 1</em></p><p>&quot;The training script for your model must log the primary metric during model training using the same corresponding metric name so that the SweepJob can access it for hyperparameter tuning.&quot; - link :: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-tune-hyperparameters?view=azureml-api-2  clearly says mlflow logging is  required. Any other logging will not work.</p></blockquote>
<blockquote><p><strong>Tommo565</strong> <code>(Sat 23 Sep 2023 08:54)</code> - <em>Upvotes: 1</em></p><p>B is correct</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Mon 07 Aug 2023 19:26)</code> - <em>Upvotes: 6</em></p><p>B. Logging the AUC metric alone is not enough to allow Hyperdrive to optimize hyperparameters for that metric. The HyperDriveConfig object needs to be used to initiate the Hyperdrive run, and the script needs to pass the HyperDriveConfig object as an argument to the Azure Machine Learning experiment run function. This will enable Hyperdrive to monitor the logged AUC metric and adjust the hyperparameters during the run to optimize the AUC metric.</p></blockquote>
<blockquote><p><strong>klowqw</strong> <code>(Wed 01 Mar 2023 15:43)</code> - <em>Upvotes: 6</em></p><p>run.log</p></blockquote>
<blockquote><p><strong>prasad06</strong> <code>(Wed 16 Mar 2022 14:01)</code> - <em>Upvotes: 5</em></p><p>The answer should be B</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Mon 13 Sep 2021 04:50)</code> - <em>Upvotes: 1</em></p><p>technically this might work if filemode was w+ instead of w but logger module is simple</p></blockquote>
<blockquote><p><strong>chaudha4</strong> <code>(Fri 29 Oct 2021 20:57)</code> - <em>Upvotes: 7</em></p><p>It still won&#x27;t work. The logging should be done on run instance so that the hyperdrive experiment can actually get that value. Writing it to a file or printing it to stdout will not help.</p></blockquote>

</details>

---

[<< Previous Question](question_181.md) | [Home](/index.md) | [Next Question >>](question_183.md)
