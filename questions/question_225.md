# Question 225

You define a datastore named ml-data for an Azure Storage blob container. In the container, you have a folder named train that contains a file named data.csv.

You plan to use the file to train a model by using the Azure Machine Learning SDK.

You plan to train the model by using the Azure Machine Learning SDK to run an experiment on local compute.

You define a DataReference object by running the following code:

![Question Image](images/q225_q_0021700001.png)

You need to load the training data.

Which code segment should you use?

A.

![Question Image](images/q225_q_0021800001.png)

B.

![Question Image](images/q225_q_0021800002.png)

C.

![Question Image](images/q225_q_0021800003.png)

D.

![Question Image](images/q225_q_0021800004.png)

E.

![Question Image](images/q225_q_0021800005.png)

<details>
  <summary>Show Suggested Answer</summary>

  <strong>E</strong><br>
<p>Example:</p>
<p>data_folder = args.data_folder</p>
<p># Load Train and Test data</p>
<p>train_data = pd.read_csv(os.path.join(data_folder, &#x27;data.csv&#x27;))</p>
<p>Reference:</p>
<p>https://www.element61.be/en/resource/azure-machine-learning-services-complete-toolbox-ai</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>trickerk</strong> <code>(Mon 07 Feb 2022 13:55)</code> - <em>Upvotes: 14</em></p><p>Given answer is correct cause &quot;data_folder&quot; already has &#x27;train&#x27; path.
Take a look at:
data_ref = ml_data.path(&#x27;train&#x27;).as_download(path_on_compute=&#x27;train_data&#x27;)</p></blockquote>
<blockquote><p><strong>rishi_ram</strong> <code>(Wed 01 Dec 2021 08:43)</code> - <em>Upvotes: 6</em></p><p>How about answer B as question says data is in &#x27;train&#x27; folder ?</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Fri 07 Jan 2022 11:39)</code> - <em>Upvotes: 1</em></p><p>I think the script will run inside the folder, so the absolute path will be returned, so doesn&#x27;t  need to describe the folder&#x27;s name.</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Thu 20 Jun 2024 13:12)</code> - <em>Upvotes: 1</em></p><p>The correct code segment to load the training data is B. This is because you have defined the data reference as data_ref = ml_data.path(&#x27;train&#x27;).as_download(path_on_compute=&#x27;train_data&#x27;), which means that the data will be downloaded to the train_data folder on the compute target. Therefore, you need to use os.path.join(data_folder, &#x27;train&#x27;, &#x27;data.csv&#x27;) to read the CSV file from the train folder in the ml-data datastore.</p></blockquote>
<blockquote><p><strong>fhlos</strong> <code>(Thu 28 Dec 2023 12:41)</code> - <em>Upvotes: 2</em></p><p>B - ChatGPT
The correct code segment to load the training data in this scenario is:

B.
import os
import argparse
import pandas as pd
parser = argparse.ArgumentParser()
parser.add_argument(&#x27;--data-folder&#x27;, type=str, dest=&#x27;data_folder&#x27;)
args = parser.parse_args()
data_folder = args.data_folder
data = pd.read_csv(os.path.join(data_folder, &#x27;train&#x27;, &#x27;data.csv&#x27;))

Explanation:
The code segment B properly handles the command-line argument parsing using the argparse module and retrieves the data_folder argument. It then uses os.path.join to construct the correct path to the training data file data.csv within the specified data_folder.

The other code segments (A, C, D, E) either have syntax errors, incorrect path references, or incorrect argument parsing, which would lead to issues when trying to load the training data.

Therefore, the correct code segment is B.</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 11:59)</code> - <em>Upvotes: 2</em></p><p>The Correct answer is as given: E
We just need to join the data_folder with the CSV file data.csv
data = pd.read_csv(os.path.join(data_folder, &#x27;data.csv&#x27;))

Let me explain why B is WRONG:
The DataReference is configured to download the data from a datastore to a local directory named &#x27;train_data&#x27; on the compute target:
data_ref = ml_data.path(&#x27;train&#x27;).as_download(path_on_compute=&#x27;train_data&#x27;) 

In this context, the data_ref object will download the contents of the &#x27;train&#x27; folder from the Azure Blob Storage to a local directory called &#x27;train_data&#x27; on the compute target. The script_params in the Estimator object then passes this data_ref as an argument for --data-folder:
script_params={&#x27;--data-folder&#x27;: data_ref}, 

Given this setup, the training script (optin E) expects the --data-folder argument to specify the path to the directory where the data.csv file is located. It then reads this CSV file into a pandas DataFrame.</p></blockquote>
<blockquote><p><strong>Lion007</strong> <code>(Sun 30 Jun 2024 11:59)</code> - <em>Upvotes: 2</em></p><p>Option B assumes that the data.csv file is still inside the directory &#x27;train&#x27; within the data_folder. This is WRONG since the path is already constructed in the data_ref without the need to repeat the &#x27;train&#x27; directory, as the data_ref is already pointing to the correct location of the data.csv file.</p></blockquote>
<blockquote><p><strong>Andrea2</strong> <code>(Fri 09 Dec 2022 09:04)</code> - <em>Upvotes: 4</em></p><p>I think answer E is correct. Data_ref contains the reference to data, that has been downloaded on the compute at the path train_data. For this reason you can simply add data.csv to load data.</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Tue 25 Jan 2022 15:15)</code> - <em>Upvotes: 1</em></p><p>Seems different from #43 above (using input)</p></blockquote>
<blockquote><p><strong>MohsenSic</strong> <code>(Tue 28 Dec 2021 01:57)</code> - <em>Upvotes: 2</em></p><p>@rishi_ram, I guess it is wrong as we will end up with  two &#x27;&#x27;train&quot;s in the path, one from data_folder and one from &quot;train&quot;</p></blockquote>

</details>

---

[<< Previous Question](question_224.md) | [Home](/index.md) | [Next Question >>](question_226.md)
