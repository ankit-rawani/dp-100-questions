# Question 45

You plan to build a team data science environment. Data for training models in machine learning pipelines will be over 20 GB in size.

You have the following requirements:

✑ Models must be built using Caffe2 or Chainer frameworks.

✑ Data scientists must be able to use a data science environment to build the machine learning pipelines and train models on their personal devices in both connected and disconnected network environments.

Personal devices must support updating machine learning pipelines when connected to a network.

You need to select a data science environment.

Which environment should you use?

- A.Azure Machine Learning Service
- B.Azure Machine Learning Studio
- C.Azure Databricks
- D.Azure Kubernetes Service (AKS)

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>chaudha4</strong> <code>(Fri 29 Apr 2022 20:04)</code> - <em>Upvotes: 14</em></p><p>It seems like the answer explanation is mixing Azure Machine Learning Studio with Azure Machine Learning Designer since the description is for designer not studio. Studio includes designer, notebook and autoML. I think the correct answer is actually B since Azure Machine Learning Service can only be used from within Azure Machine Learning Studio.</p></blockquote>
<blockquote><p><strong>Wayland</strong> <code>(Tue 29 Aug 2023 20:45)</code> - <em>Upvotes: 10</em></p><p>I just did some digging and here is what I find: https://docs.microsoft.com/en-us/azure/machine-learning/overview-what-is-machine-learning-studio. The &quot;Machine Learning Studio&quot; in this question is actually referring to &quot;Machine Learning Studio Classic&quot;, which is an outdated platform that only offering web service (no offline), and the &quot;Machine Learning Service&quot; is actually the &quot;Azure Machine Learning&quot; you can find in Azure Portal. What&#x27;s the more the new Studio is now part of the &quot;Azure Machine Learning&quot; as we speak. So for this question, A is the correct answer at the time when it was firstly created, but it no long applies right now. Now, A and B are pretty much the same thing.</p></blockquote>
<blockquote><p><strong>sar77</strong> <code>(Tue 15 Jul 2025 19:36)</code> - <em>Upvotes: 1</em></p><p>A. Azure Machine Learning Service
Supports large datasets and custom frameworks (like Caffe2, Chainer via Docker).
Allows local development and offline work using Azure ML SDK and local compute.
Pipelines can be updated when reconnected. ✅ Best fit for all requirements.</p></blockquote>
<blockquote><p><strong>SaraGG28</strong> <code>(Tue 14 Jan 2025 11:11)</code> - <em>Upvotes: 1</em></p><p>Azure Machine Learning Service is the most appropriate choice based on the requirements:
Supports Caffe2 and Chainer frameworks:

Azure Machine Learning Service allows flexibility in choosing machine learning frameworks, including Caffe2 and Chainer, through custom environments.
Supports both connected and disconnected environments:

With Azure Machine Learning Service, data scientists can work locally on their personal devices using the Azure ML SDK or CLI, even offline.
Pipelines and models can be updated and synced when reconnected to the network.
Large dataset support:

The service can handle datasets larger than 20 GB by enabling integration with cloud storage (e.g., Azure Blob Storage) and local caching mechanisms for disconnected environments.
Personal device flexibility:

Azure Machine Learning Service supports local development and allows deploying models on personal devices with proper synchronization capabilities.

Chat GPT</p></blockquote>

<blockquote><p><strong>uncleeeesam</strong> <code>(Wed 27 Nov 2024 19:32)</code> - <em>Upvotes: 1</em></p><p>ChatGPT says D.</p></blockquote>
<blockquote><p><strong>Ran2025</strong> <code>(Mon 30 Sep 2024 13:57)</code> - <em>Upvotes: 1</em></p><p>A is correct! Azure Machine Learning Service supports local machine compute!</p></blockquote>
<blockquote><p><strong>Yoshizn</strong> <code>(Wed 07 Feb 2024 16:26)</code> - <em>Upvotes: 3</em></p><p>https://www.codit.eu/blog/azure-machine-learning-studio-vs-services/</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 02 Feb 2024 03:14)</code> - <em>Upvotes: 3</em></p><p>A. Azure Machine Learning Service would be the best option for building a team data science environment with the given requirements. It allows building machine learning pipelines using Caffe2 or Chainer frameworks, supports training models on personal devices in both connected and disconnected network environments, and provides a mechanism for updating machine learning pipelines when connected to a network.</p></blockquote>
<blockquote><p><strong>shubhangi2612</strong> <code>(Fri 19 Jan 2024 15:16)</code> - <em>Upvotes: 1</em></p><p>on this link, I found the difference between  azure ML service and studio
and the conclusion is azure Ml service is hybrid(on cloud or premise)
https://www.codit.eu/blog/azure-machine-learning-studio-vs-services/?country_sel=uk</p></blockquote>
<blockquote><p><strong>Sibajene</strong> <code>(Fri 05 Jan 2024 10:22)</code> - <em>Upvotes: 1</em></p><p>C is correct</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Tue 12 Dec 2023 17:11)</code> - <em>Upvotes: 1</em></p><p>Option A</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Mon 11 Dec 2023 18:27)</code> - <em>Upvotes: 1</em></p><p>option A</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Mon 11 Dec 2023 18:30)</code> - <em>Upvotes: 1</em></p><p>https://www.codit.eu/blog/azure-machine-learning-studio-vs-services/?country_sel=be</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Thu 12 Oct 2023 06:28)</code> - <em>Upvotes: 4</em></p><p>Answer is  A.
Because Azure Machine Learning Studio need network!
Azure Machine Learning Service can support local compute.

https://www.codit.eu/blog/azure-machine-learning-studio-vs-services/?country_sel=be</p></blockquote>

<blockquote><p><strong>Nav727</strong> <code>(Sun 04 Jun 2023 12:24)</code> - <em>Upvotes: 2</em></p><p>Why is B incorrect??</p></blockquote>
<blockquote><p><strong>chevyli</strong> <code>(Fri 25 Aug 2023 02:45)</code> - <em>Upvotes: 2</em></p><p>The ML studio seems to refer to the Web UI ml.azure.com, which is unavailable in an offline setting.</p></blockquote>
<blockquote><p><strong>turtle666</strong> <code>(Fri 21 Apr 2023 14:33)</code> - <em>Upvotes: 1</em></p><p>answer should be A, but already out-dated ?
https://www.codit.eu/blog/azure-machine-learning-studio-vs-services/?country_sel=be</p></blockquote>
<blockquote><p><strong>DingDongSingSong</strong> <code>(Thu 30 Mar 2023 22:13)</code> - <em>Upvotes: 2</em></p><p>What&#x27;s the consensus on the answer? Is it A or B? I cannot find any learning document that provides clarity on compatibility with caffe2 or chainer, and any information on off network local machine usage.</p></blockquote>
<blockquote><p><strong>spaceykacey</strong> <code>(Tue 25 Oct 2022 08:26)</code> - <em>Upvotes: 2</em></p><p>I think the answer is A, Azure ML service is hybrid (can be run both on cloud and on premise)
https://www.codit.eu/blog/azure-machine-learning-studio-vs-services/</p></blockquote>

</details>

---

[<< Previous Question](question_44.md) | [Home](../index.md) | [Next Question >>](question_46.md)
