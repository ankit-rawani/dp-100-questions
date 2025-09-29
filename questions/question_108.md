# Question 108

You are authoring a notebook in Azure Machine Learning studio.

You must install packages from the notebook into the currently running kernel. The installation must be limited to the currently running kernel only.

You need to install the packages.

Which magic function should you use?

* A.!pip
* B.%pip
* C.!conda
* D.%load

<details>
  <summary>Show Suggested Answer</summary>

  <strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>ajay0011</strong> <code>(Wed 04 Oct 2023 01:00)</code> - <em>Upvotes: 12</em></p><p>The %pip magic function is used to install Python packages directly from the notebook environment, and it installs packages only in the currently running kernel. This means that any packages you install with %pip will be available only in the notebook session where you install them.

The !pip command is used to install Python packages in a system-wide installation of Python. It does not restrict the installation to the currently running kernel, and packages installed with !pip will be available to all Python processes on the system.

The !conda command is used to install packages using the Conda package manager. While Conda is a popular package manager, it does not integrate well with the notebook environment and can cause conflicts with the Anaconda distribution of Python that is used in Azure Machine Learning.

The %load magic function is used to load the contents of a file into a cell. It is not used for installing packages.

Therefore, the correct answer is option B: %pip.</p></blockquote>
<blockquote><p><strong>TA_</strong> <code>(Wed 25 Sep 2024 10:22)</code> - <em>Upvotes: 1</em></p><p>On exam 15-03-2024. Plus, there were a few other questions related to kernels</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Mon 12 Aug 2024 13:35)</code> - <em>Upvotes: 2</em></p><p>On exam 12-02-2024.</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Sat 20 Jan 2024 14:23)</code> - <em>Upvotes: 4</em></p><p>On exam 20 July 2023.</p></blockquote>
<blockquote><p><strong>Jin_22</strong> <code>(Fri 22 Sep 2023 12:06)</code> - <em>Upvotes: 3</em></p><p>The !pip command installs packages from the notebook into the currently running kernel but does not limit the installation to the currently running kernel only.

This means that if you have multiple kernels running in your notebook, !pip will install the package in all of them.</p></blockquote>
<blockquote><p><strong>Retko</strong> <code>(Wed 20 Sep 2023 08:12)</code> - <em>Upvotes: 1</em></p><p>Why not !pip?? Can it also be used? Thx</p></blockquote>
<blockquote><p><strong>ajay0011</strong> <code>(Wed 04 Oct 2023 01:05)</code> - <em>Upvotes: 1</em></p><p>The %pip magic function is used to install Python packages directly from the notebook environment, and it installs packages only in the currently running kernel. This means that any packages you install with %pip will be available only in the notebook session where you install them.

The !pip command is used to install Python packages in a system-wide installation of Python. It does not restrict the installation to the currently running kernel, and packages installed with !pip will be available to all Python processes on the system.</p></blockquote>

</details>

---

[<< Previous Question](question_107.md) | [Home](/index.md) | [Next Question >>](question_109.md)
