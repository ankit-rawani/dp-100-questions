# Question 332

You plan to run a script as an experiment. The script uses modules from the SciPy library and several Python packages that are not typically installed in a default conda environment.

You plan to run the experiment on your local workstation for small datasets and scale out the experiment by running it on more powerful remote compute dusters for larger datasets.

You need to ensure that the experiment runs successfully on local and remote compute with the least administrative effort.

What should you do?

- A.Leave the environment unspecified for the experiment. Run the expenment by using the default environment.
- B.Create a config.yaml file that defines the required conda packages and save the file in the experiment folder.
- C.Create and register an environment that includes the required packages. Use this environment for all experiment jobs.
- D.Create a virtual machine (VM) by using the required Python configuration and attach the VM as a compute target. Use this compute target for all experiment runs.

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>BR_CS</strong> <code>(Sat 17 Aug 2024 11:13)</code> - <em>Upvotes: 2</em></p><p>Correct</p></blockquote>
<blockquote><p><strong>Mikku123</strong> <code>(Tue 06 Aug 2024 20:59)</code> - <em>Upvotes: 1</em></p><p>C is correct answer</p></blockquote>

</details>

---

[<< Previous Question](question_331.md) | [Home](../index.md) | [Next Question >>](question_333.md)
