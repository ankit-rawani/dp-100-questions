# Question 202

You plan to run a script as an experiment using a Script Run Configuration. The script uses modules from the scipy library as well as several Python packages that are not typically installed in a default conda environment.

You plan to run the experiment on your local workstation for small datasets and scale out the experiment by running it on more powerful remote compute clusters for larger datasets.

You need to ensure that the experiment runs successfully on local and remote compute with the least administrative effort.

What should you do?

* A.Do not specify an environment in the run configuration for the experiment. Run the experiment by using the default environment.
* B.Create a virtual machine (VM) with the required Python configuration and attach the VM as a compute target. Use this compute target for all experiment runs.
* C.Create and register an Environment that includes the required packages. Use this Environment for all experiment runs.
* D.Create a config.yaml file defining the conda packages that are required and save the file in the experiment folder.
* E.Always run the experiment with an Estimator by using the default packages.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>scipio</strong> <code>(Tue 16 Nov 2021 17:10)</code> - <em>Upvotes: 21</em></p><p>C is correct. You may use a yml file to create the Environment and then register it to be used everywhere. If you put the file in the experiment folder you need to create the env every run, against the &quot;least administrative effort&quot; requirement</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Mon 06 Jun 2022 18:00)</code> - <em>Upvotes: 5</em></p><p>C is correct</p></blockquote>
<blockquote><p><strong>f82411e</strong> <code>(Wed 04 Jun 2025 11:21)</code> - <em>Upvotes: 1</em></p><p>C is correct</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 02 Dec 2024 13:12)</code> - <em>Upvotes: 1</em></p><p>C is the correct answer</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Sun 28 Jan 2024 10:09)</code> - <em>Upvotes: 1</em></p><p>C is correct</p></blockquote>
<blockquote><p><strong>esimsek</strong> <code>(Mon 25 Sep 2023 08:35)</code> - <em>Upvotes: 1</em></p><p>Registering environment is correct.</p></blockquote>
<blockquote><p><strong>esimsek</strong> <code>(Sat 23 Sep 2023 11:49)</code> - <em>Upvotes: 3</em></p><p>In exam 2023-03-23</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 15 Aug 2023 16:49)</code> - <em>Upvotes: 1</em></p><p>Creating a config.yaml file is not recommended in this scenario since the experiment is being run on both local and remote compute. It would require copying the file to every location where the experiment is run, which can be a time-consuming administrative task.

Using an Estimator with the default packages is not recommended in this scenario since the required packages are not typically installed in a default conda environment.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Tue 15 Aug 2023 16:48)</code> - <em>Upvotes: 2</em></p><p>C. The best solution for this scenario is to create and register an environment that includes the required packages, and use this environment for all experiment runs. This ensures that the experiment runs successfully on both local and remote compute with the least administrative effort.

Specifying an environment in the run configuration is necessary to ensure that the correct packages and dependencies are used. If no environment is specified, the default environment may not include the required packages, leading to errors.

Creating a virtual machine (VM) as a compute target is not necessary in this scenario since the experiment is being run on local and remote compute, not just remote compute. Also, creating and managing a VM can be a time-consuming administrative task.</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Fri 30 Jun 2023 12:24)</code> - <em>Upvotes: 2</em></p><p>C cannot be correct if we are creating an Environment using it for every run?</p></blockquote>
<blockquote><p><strong>BilJon</strong> <code>(Tue 28 Sep 2021 16:59)</code> - <em>Upvotes: 3</em></p><p>The case described is for a local Workstation, so the answer is correct.
For real-time inferencing service a .yml file is needed</p></blockquote>
<blockquote><p><strong>NaishinMatiri</strong> <code>(Thu 21 Oct 2021 18:29)</code> - <em>Upvotes: 4</em></p><p>the experiment also specify is should work remotely: &#x27;and scale out the experiment by running it on more powerful remote compute clusters for larger datasets.&#x27;
I think answer should be D since it would work in both cases</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Fri 17 Sep 2021 06:31)</code> - <em>Upvotes: 4</em></p><p>D is correct answer. It may not possible to have an environment with all necessary packages installed. yaml can ensure this.</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Sat 25 Dec 2021 16:43)</code> - <em>Upvotes: 1</em></p><p>Yes D look more correct.</p></blockquote>
<blockquote><p><strong>azure1000</strong> <code>(Fri 04 Feb 2022 15:14)</code> - <em>Upvotes: 4</em></p><p>I think when you create an environment you can give all necessary packages using conda dependencies.</p></blockquote>

</details>

---

[<< Previous Question](question_201.md) | [Home](/index.md) | [Next Question >>](question_203.md)
