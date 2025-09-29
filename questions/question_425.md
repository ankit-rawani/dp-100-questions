# Question 425

You create an Azure Machine Learning workspace. You use Azure Machine Learning designer to create a pipeline within the workspace.

You need to submit a pipeline run from the designer.

What should you do first?

- A.Create an experiment.
- B.Create an attached compute resource.
- C.Create a compute cluster.
- D.Select a model.

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>445f1bd</strong> <code>(Mon 28 Jul 2025 01:54)</code> - <em>Upvotes: 1</em></p><p>it is A.

https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-component-pipelines-ui?view=azureml-api-2#submit-pipeline

Check the image &quot;Submit pipeline&quot;

First we need to select experiment then we can select runtime.

People that says it is C your information is outdated ...answer should be C. Create a compute cluster.
&quot;To run a pipeline, you first have to set default compute target to run the pipeline on.&quot;
https://learn.microsoft.com/en-us/azure/machine-learning/samples-designer..... this is V1 and V2 is the updated information, so A is correct</p></blockquote>

<blockquote><p><strong>kay1101</strong> <code>(Tue 26 Nov 2024 03:54)</code> - <em>Upvotes: 4</em></p><p>I think answer is A.
reference:https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-component-pipelines-ui?view=azureml-api-2#submit-pipeline</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Sat 30 Nov 2024 22:34)</code> - <em>Upvotes: 2</em></p><p>agreed. You won&#x27;t be able to get to the next step without selecting existing or Create new experiment.</p></blockquote>
<blockquote><p><strong>haby</strong> <code>(Sat 22 Jun 2024 16:50)</code> - <em>Upvotes: 1</em></p><p>After click &quot;Designer&quot;, you must set &quot;Default compute target&quot; or there will be a red warning showing on the panel. After fixing this, you will be able to access Designer Experiment. So I will take C.</p></blockquote>
<blockquote><p><strong>robdale</strong> <code>(Thu 02 May 2024 18:12)</code> - <em>Upvotes: 1</em></p><p>ChatGPT sounds reasonable:  To submit a pipeline run from Azure Machine Learning designer, you should first:

C. Create a compute cluster.

In Azure Machine Learning, you need a compute cluster to run the pipeline. Compute clusters provide the necessary compute resources for training and running machine learning models as part of your pipeline. Once you have a compute cluster set up, you can then create an experiment within the workspace (Option A) and design your pipeline using the Azure Machine Learning designer. After the pipeline is designed, you can submit a pipeline run using the compute cluster you&#x27;ve created.

Options B and D are not the first steps for submitting a pipeline run; they come into play after you&#x27;ve created the compute cluster and designed the pipeline.</p></blockquote>

<blockquote><p><strong>Fercho5813</strong> <code>(Sun 28 Apr 2024 02:17)</code> - <em>Upvotes: 1</em></p><p>Answer is A</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Thu 29 Feb 2024 14:29)</code> - <em>Upvotes: 1</em></p><p>Could it aslo be B?</p></blockquote>
<blockquote><p><strong>Pyguy</strong> <code>(Wed 01 Nov 2023 12:59)</code> - <em>Upvotes: 3</em></p><p>of course it is C - compute cluster</p></blockquote>
<blockquote><p><strong>19c1ee5</strong> <code>(Fri 20 Oct 2023 15:21)</code> - <em>Upvotes: 1</em></p><p>Answer should be A</p></blockquote>
<blockquote><p><strong>avotofu</strong> <code>(Fri 20 Oct 2023 07:37)</code> - <em>Upvotes: 2</em></p><p>answer should be C. Create a compute cluster.
&quot;To run a pipeline, you first have to set default compute target to run the pipeline on.&quot;
https://learn.microsoft.com/en-us/azure/machine-learning/samples-designer

Compute cluster is the compute target supported by Designer.</p></blockquote>

</details>

---

[<< Previous Question](question_424.md) | [Home](../index.md) | [Next Question >>](question_426.md)
