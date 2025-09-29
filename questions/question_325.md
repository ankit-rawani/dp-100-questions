# Question 325

HOTSPOT

-

You manage an Azure Machine Learning workspace named workspace1 by using the Python SDK v2.

The default datastore of workspace1 contains a folder named sample_data. The folder structure contains the following content:

|— sample_data

|— MLTable

|— file1.txt

|— file2.txt

|— file3.txt

You write Python SDK v2 code to materialize the data from the files in the sample_data folder into a Pandas data frame.

You need to complete the Python SDK v2 code to use the MLTable folder as the materialization blueprint.

How should you complete the code? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

![Question Image](images/q325_q_image502.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q325_ans_0_image503.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jojashi</strong> <code>(Sat 30 Nov 2024 12:04)</code> - <em>Upvotes: 1</em></p><p>CORRECT. 

from Chat GPT, 
- The mltable.load function is used to load the data from the folder. It returns an MLTable object.

-In Azure Machine Learning, when you have a folder containing an MLTable file along with data files (like file1.txt, file2.txt), the MLTable file serves as a configuration file that describes how to load and parse the data. You should load the directory containing the MLTable file, not the MLTable file itself.</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Mon 25 Nov 2024 21:34)</code> - <em>Upvotes: 1</em></p><p>Correct. MLTable is a yaml file not a directory. Check the link here: https://learn.microsoft.com/en-us/python/api/mltable/mltable?view=azure-ml-py#mltable-load</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 10:29)</code> - <em>Upvotes: 4</em></p><p>WRONG. The Correct answer is: load, ./sample_data/MLTable

The Python SDK v2 code is for the purpose of materializing data into a Pandas data frame using an MLTable folder as a blueprint. 
Materialization in this context refers to the process of loading data from various sources and formats into a Pandas data frame which can be used for data analysis and model training within Python.

Given the context and the folder structure in the default datastore of workspace1, the MLTable folder should contain the blueprint for materialization, which includes information about how to read the data and convert it into a format suitable for machine learning tasks.

Therefore, to complete the Python SDK v2 code to use the MLTable folder as the materialization blueprint, you would use the load method on the mltable object, and specify the path to the MLTable folder, which is ./sample_data/MLTable. This path points to the MLTable folder in the sample_data directory, which is expected to contain the MLTable file that defines the data to be materialized into a Pandas data frame.</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 10:31)</code> - <em>Upvotes: 1</em></p><p>import mltable
tbl = mltable.load(&quot;./sample_data/MLTable&quot;)
df = tbl.to_pandas_dataframe()</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 26 Jan 2024 15:48)</code> - <em>Upvotes: 4</em></p><p>load and . sample data MLTable</p></blockquote>
<blockquote><p><strong>damaldon</strong> <code>(Sun 14 Jan 2024 21:20)</code> - <em>Upvotes: 2</em></p><p>Correct.
import mltable

# load the previously saved MLTable file
tbl = mltable.load(&quot;./titanic/&quot;)
https://learn.microsoft.com/en-us/azure/machine-learning/how-to-mltable?view=azureml-api-2&amp;tabs=cli</p></blockquote>

</details>

---

[<< Previous Question](question_324.md) | [Home](/index.md) | [Next Question >>](question_326.md)
