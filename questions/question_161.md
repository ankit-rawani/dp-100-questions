# Question 161

You manage an Azure Machine Learning workspace. You have a folder that contains a CSV file. The folder is registered as a folder data asset.

You plan to use the folder data asset for data wrangling during interactive development.

You need to access and load the folder data asset into a Pandas data frame.

Which method should you use to achieve this goal?

- A.mltable.from_parquet_files()
- B.mltable.from_delimited_files()
- C.mltable.from_data_lake()
- D.mltable.load()

<details>
  <summary>Show Suggested Answer</summary>

<strong>B</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>445f1bd</strong> <code>(Sun 22 Jun 2025 04:20)</code> - <em>Upvotes: 1</em></p><p>Is load() guys. Check this ...

# load mltable from azureml data asset short uri

from mltable import load
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
ml_client = MLClient(credential, &lt;subscription_id&gt;, &lt;resourcegroup-name&gt;, &lt;workspace-name&gt;)
tbl = load(&#x27;azureml:&lt;data-asset-name&gt;:&lt;version&gt;&#x27;, ml_client=ml_client)

in this link
https://learn.microsoft.com/en-us/python/api/mltable/mltable?view=azure-ml-py#mltable-from-delimited-files</p></blockquote>

<blockquote><p><strong>avinyc</strong> <code>(Fri 03 Jan 2025 23:45)</code> - <em>Upvotes: 1</em></p><p>mltable.from_delimited_files()</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Mon 02 Dec 2024 02:21)</code> - <em>Upvotes: 1</em></p><p>csv=&gt;delimited file</p></blockquote>
<blockquote><p><strong>sai384957324</strong> <code>(Thu 10 Oct 2024 22:00)</code> - <em>Upvotes: 1</em></p><p>B is correct</p></blockquote>
<blockquote><p><strong>401d299</strong> <code>(Sat 28 Sep 2024 10:34)</code> - <em>Upvotes: 1</em></p><p>correct</p></blockquote>
<blockquote><p><strong>3a0b61c</strong> <code>(Wed 18 Sep 2024 05:57)</code> - <em>Upvotes: 1</em></p><p>correct
https://learn.microsoft.com/en-us/python/api/mltable/mltable?view=azure-ml-py#mltable-from-delimited-files</p></blockquote>
<blockquote><p><strong>3a0b61c</strong> <code>(Fri 20 Sep 2024 06:51)</code> - <em>Upvotes: 1</em></p><p>sorry.
B is correct.</p></blockquote>
<blockquote><p><strong>nicorg5</strong> <code>(Thu 12 Sep 2024 08:49)</code> - <em>Upvotes: 1</em></p><p>answer is correct</p></blockquote>

</details>

---

[<< Previous Question](question_160.md) | [Home](../index.md) | [Next Question >>](question_162.md)
