# Question 496

You need to implement a scaling strategy for the local penalty detection data.

Which normalization type should you use?

- A.Streaming
- B.Weight
- C.Batch
- D.Cosine

<details>
  <summary>Show Suggested Answer</summary>

<strong>C</strong><br>

<p>Post batch normalization statistics (PBN) is the Microsoft Cognitive Toolkit (CNTK) version of how to evaluate the population mean and variance of Batch</p>
<p>Normalization which could be used in inference Original Paper.</p>
<p>In CNTK, custom networks are defined using the BrainScriptNetworkBuilder and described in the CNTK network description language &quot;BrainScript.&quot;</p>
<p>Scenario:</p>
<p>Local penalty detection models must be written by using BrainScript.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/cognitive-toolkit/post-batch-normalization-statistics</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>huyennguyen</strong> <code>(Thu 16 Jul 2020 04:24)</code> - <em>Upvotes: 78</em></p><p>Both the question and answer are difficult to follow.</p></blockquote>
<blockquote><p><strong>satishgunjal</strong> <code>(Wed 30 Jun 2021 05:45)</code> - <em>Upvotes: 9</em></p><p>In case study they have also mentioned 
- All penalty detection models show inference phases using a Stochastic Gradient Descent (SGD) are running too slow
- The images and videos will have varying sizes and formats

So Batch normalization is usefull to speedup the process where as Cosine normalization is usefull to handle varying sizes and formats of input data.</p></blockquote>

<blockquote><p><strong>prashantjoge</strong> <code>(Sun 28 Nov 2021 08:32)</code> - <em>Upvotes: 2</em></p><p>any reference for this?</p></blockquote>
<blockquote><p><strong>GHill1982</strong> <code>(Wed 17 Jul 2024 19:33)</code> - <em>Upvotes: 1</em></p><p>The best normalization type to use in this case is batch normalization. Batch normalization is a technique that reduces the internal covariate shift of the inputs to each layer of a neural network, making the training faster and more stable. Batch normalization also has the benefit of regularizing the model and reducing the need for dropout.</p></blockquote>
<blockquote><p><strong>snegnik</strong> <code>(Mon 04 Dec 2023 19:50)</code> - <em>Upvotes: 1</em></p><p>Terminology from Cognitive Toolkit and Synapse Analytics. It seems doesn&#x27;t relevant for DP-100 test</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sat 17 Dec 2022 12:40)</code> - <em>Upvotes: 2</em></p><p>DNN normalization?? I really do not expect this kind of questions ...
The most common one is batch, and weight is kind of a batch with some improvements ...
For other two, I do not know ...</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Tue 26 Jul 2022 12:11)</code> - <em>Upvotes: 2</em></p><p>any easy way to understand this ?</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sat 17 Dec 2022 21:02)</code> - <em>Upvotes: 1</em></p><p>The images and videos will have varying sizes and formats. Normalization mean put them into the same dimension and same format images / videos before further processing</p></blockquote>
<blockquote><p><strong>spaceykacey</strong> <code>(Thu 12 May 2022 06:40)</code> - <em>Upvotes: 3</em></p><p>&quot;Local penalty detection models must be written by using BrainScript.&quot; BrainScript is used in Microsoft Cognitive Toolkit (CNTK) and it&#x27;s network definition only supports batch normalization.  So C is correct.

https://docs.microsoft.com/en-us/cognitive-toolkit/batchnormalization</p></blockquote>

<blockquote><p><strong>gaint</strong> <code>(Wed 05 Jan 2022 14:52)</code> - <em>Upvotes: 5</em></p><p>Not able to follow question and answer. This question will take atleast 15 mins to read and summarize :-).</p></blockquote>
<blockquote><p><strong>satishgunjal</strong> <code>(Wed 30 Jun 2021 05:42)</code> - <em>Upvotes: 1</em></p><p>So Batch normalization is usefull to speedup the process where as normalization is use full to handle varying sizes and formats of input data.</p></blockquote>
<blockquote><p><strong>dmadhup</strong> <code>(Mon 19 Oct 2020 18:52)</code> - <em>Upvotes: 1</em></p><p>Answer: C</p></blockquote>

</details>

---

[<< Previous Question](question_495.md) | [Home](../index.md) | [Next Question >>](question_497.md)
