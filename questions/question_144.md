# Question 144

You create a workspace to include a compute instance by using Azure Machine Learning Studio. You are developing a Python SDK v2 notebook in the workspace.

You need to use Intellisense in the notebook.

What should you do?

* A.Stop the compute instance.
* B.Start the compute instance.
* C.Run a %pip magic function on the compute instance.
* D.Run a !pip magic function on the compute instance.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Ahmed_Gehad</strong> <code>(Mon 29 Jan 2024 09:01)</code> - <em>Upvotes: 5</em></p><p>- Option A (Stop the compute instance) will not enable Intellisense. Stopping the compute instance will shut it down, and you won&#x27;t be able to access its resources until you start it again.
- Option C (Run a %pip magic function on the compute instance) and Option D (Run a !pip magic function on the compute instance) are not related to enabling Intellisense. These magic functions are used to install Python packages in the notebook&#x27;s environment. While installing packages may be necessary for code execution, it won&#x27;t impact the availability of Intellisense.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 01 Dec 2024 14:38)</code> - <em>Upvotes: 1</em></p><p>Correct is B, intellisense needs a running compute instance to support this feature</p></blockquote>
<blockquote><p><strong>jojashi</strong> <code>(Fri 29 Nov 2024 11:24)</code> - <em>Upvotes: 1</em></p><p>Correct. C

Chat GPT says it is C. To enable Intellisense in a Python SDK v2 notebook within an Azure Machine Learning Studio workspace, you don&#x27;t need to perform any actions related to starting or stopping the compute instance. Instead, you need to ensure that the required Python packages are installed in your environment to support Intellisense.</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Wed 24 Jul 2024 07:06)</code> - <em>Upvotes: 2</em></p><p>B seems to be correct. See https://learn.microsoft.com/en-us/azure/machine-learning/how-to-run-jupyter-notebooks?view=azureml-api-2</p></blockquote>
<blockquote><p><strong>ferren</strong> <code>(Fri 10 May 2024 19:55)</code> - <em>Upvotes: 1</em></p><p>claude says it is B</p></blockquote>
<blockquote><p><strong>cyberfriends</strong> <code>(Wed 17 Apr 2024 14:16)</code> - <em>Upvotes: 1</em></p><p>You can use %pip install to install packages and enable Intellisense. For example, if you want to install a package like numpy, you can run the following command in your Jupyter notebook cell:
%p ip install numpy</p></blockquote>
<blockquote><p><strong>PradhanManva</strong> <code>(Mon 25 Mar 2024 07:46)</code> - <em>Upvotes: 2</em></p><p>B is correct</p></blockquote>
<blockquote><p><strong>ABosco</strong> <code>(Sun 18 Feb 2024 12:10)</code> - <em>Upvotes: 2</em></p><p>B is correct
When a compute instance is running, you can also use code completion, powered by Intellisense, in any Python notebook.</p></blockquote>
<blockquote><p><strong>PI_Team</strong> <code>(Fri 26 Jan 2024 14:27)</code> - <em>Upvotes: 2</em></p><p>To use Intellisense in a Python SDK v2 notebook in Azure Machine Learning Studio, you should start the compute instance. This will enable you to use advanced features like full IntelliSense and inline error highlighting directly in your Jupyter notebooks1. So the correct answer is B. Start the compute instance.

SaM</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 27 Dec 2023 18:41)</code> - <em>Upvotes: 1</em></p><p>To use it, you must ensure that your compute instance is running and connected to your notebook.

 the correct answer is:

B. Start the compute instance.</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Wed 27 Dec 2023 15:51)</code> - <em>Upvotes: 1</em></p><p>C - is correct answer</p></blockquote>
<blockquote><p><strong>Batman160591</strong> <code>(Wed 20 Dec 2023 23:37)</code> - <em>Upvotes: 2</em></p><p>B seems the correct</p></blockquote>

</details>

---

[<< Previous Question](question_143.md) | [Home](/index.md) | [Next Question >>](question_145.md)
