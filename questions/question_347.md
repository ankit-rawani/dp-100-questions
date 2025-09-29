# Question 347

You create a workspace by using Azure Machine Learning Studio.

You must run a Python SDK v2 notebook in the workspace by using Azure Machine Learning Studio.

You need to reset the state of the notebook.

Which three actions should you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

* A.Stop the current kernel.
* B.Change the compute.
* C.Reset the compute.
* D.Navigate to another section of the workspace.
* E.Change the current kernel.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>BCE</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>PI_Team</strong> <code>(Sat 24 Feb 2024 14:51)</code> - <em>Upvotes: 6</em></p><p>Stopping the current kernel will indeed interrupt the execution of the notebook, but it will not reset the state of the notebook. To reset the state of a Python SDK v2 notebook in an Azure Machine Learning Studio workspace, you can perform any of the following actions: B. Change the compute to switch to a different compute instance and reset the state of the notebook. C. Reset the compute to restart the compute instance running the notebook and reset its state. E. Change the current kernel to switch to a different kernel and reset the state of the notebook.

It&#x27;s easy, just try it in Azure notebook and you&#x27;ll see :) 

SaM</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Sun 24 Nov 2024 02:09)</code> - <em>Upvotes: 1</em></p><p>These actions will reset the notebook state and will reset all variables in the notebook.
Action	                 Result
Change the kernel	Notebook uses new kernel
Switch compute	Notebook automatically uses the new compute.
Reset compute	Starts again when you try to run a cell
Stop compute	No cells will run
Open notebook in Jupyter or JupyterLab	Notebook opened in a new tab.

reference:https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2#change-the-notebook-environment</p></blockquote>
<blockquote><p><strong>kay1101</strong> <code>(Sun 24 Nov 2024 02:11)</code> - <em>Upvotes: 1</em></p><p>seems like the format is a mess.
Actions:
Change the kernel
Switch compute
Reset compute
Stop compute	
Open notebook in Jupyter or JupyterLab</p></blockquote>
<blockquote><p><strong>abcd9999</strong> <code>(Fri 02 Feb 2024 07:09)</code> - <em>Upvotes: 1</em></p><p>A. Stop the current kernel: This action stops the current Python kernel that is running the notebook. Stopping the kernel will clear any variables or state that was previously defined during the notebook execution.

D. Navigate to another section of the workspace: Moving to another section of the workspace, such as opening a different notebook or going to the &quot;Experiments&quot; section, effectively resets the notebook&#x27;s execution state.

E. Change the current kernel: Changing the current Python kernel to a new one can effectively reset the notebook&#x27;s execution state, similar to stopping the current kernel.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 26 Jan 2024 20:02)</code> - <em>Upvotes: 3</em></p><p>A. Stop the current kernel.
C. Reset the compute.
E. Change the current kernel.</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Fri 05 Jan 2024 22:16)</code> - <em>Upvotes: 2</em></p><p>Correct.
These actions will reset the notebook state and will reset all variables in the notebook.
Action 	Result
Change the kernel 	Notebook uses new kernel
Switch compute 	Notebook automatically uses the new compute.
Reset compute 	Starts again when you try to run a cell
Stop compute 	No cells will run
Open notebook in Jupyter or JupyterLab 	Notebook opened in a new tab.</p></blockquote>

</details>

---

[<< Previous Question](question_346.md) | [Home](/index.md) | [Next Question >>](question_348.md)
