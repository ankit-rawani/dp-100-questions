# Question 286

You have a Jupyter Notebook that contains Python code that is used to train a model.

You must create a Python script for the production deployment. The solution must minimize code maintenance.

Which two actions should you perform? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

- A.Refactor the Jupyter Notebook code into functions
- B.Save each function to a separate Python file
- C.Define a main() function in the Python script
- D.Remove all comments and functions from the Python script

<details>
  <summary>Show Suggested Answer</summary>

<strong>AC</strong><br>

<p>C: Python main function is a starting point of any program. When the program is run, the python interpreter runs the code sequentially. Main function is executed only when it is run as a Python program.</p>
<p>A: Refactoring, code style and testing</p>
<p>The first step is to modularise the notebook into a reasonable folder structure, this effectively means to convert files from .ipynb format to .py format, ensure each script has a clear distinct purpose and organise these files in a coherent way.</p>
<img src="../images/q286_ref_6_0031200001.jpg" alt="Reference Image"><br>
<p>Once the project is nicely structured we can tidy up or refactor the code.</p>
<p>Reference:</p>
<p>https://www.guru99.com/learn-python-main-function-with-examples-understand-main.html https://towardsdatascience.com/from-jupyter-notebook-to-deployment-a-straightforward-example-1838c203a437</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>evangelist</strong> <code>(Sun 08 Dec 2024 08:00)</code> - <em>Upvotes: 1</em></p><p>given answers are correct</p></blockquote>
<blockquote><p><strong>Kakusaif</strong> <code>(Sat 08 Apr 2023 17:04)</code> - <em>Upvotes: 2</em></p><p>correct - official MS reference  is here - https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-convert-ml-experiment-to-production</p></blockquote>
<blockquote><p><strong>chevyli</strong> <code>(Thu 02 Mar 2023 04:29)</code> - <em>Upvotes: 1</em></p><p>Seems correct</p></blockquote>

</details>

---

[<< Previous Question](question_285.md) | [Home](../index.md) | [Next Question >>](question_287.md)
