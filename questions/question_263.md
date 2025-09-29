# Question 263

HOTSPOT -

You are hired as a data scientist at a winery. The previous data scientist used Azure Machine Learning.

You need to review the models and explain how each model makes decisions.

Which explainer modules should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](../images/q263_q_0028200001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q263_ans_0_0028300001.png" alt="Answer Image"><br>

<p>Meta explainers automatically select a suitable direct explainer and generate the best explanation info based on the given model and data sets. The meta explainers leverage all the libraries (SHAP, LIME, Mimic, etc.) that we have integrated or developed. The following are the meta explainers available in the SDK:</p>
<p>Tabular Explainer: Used with tabular datasets.</p>
<p>Text Explainer: Used with text datasets.</p>
<p>Image Explainer: Used with image datasets.</p>
<p>Box 1: Tabular -</p>
<p>Box 2: Text -</p>
<p>Box 3: Image -</p>
<p>Incorrect Answers:</p>
<p>Hierarchical Attention Network (HAN)</p>
<p>HAN was proposed by Yang et al. in 2016. Key features of HAN that differentiates itself from existing approaches to document classification are (1) it exploits the hierarchical nature of text data and (2) attention mechanism is adapted for document classification.</p>
<p>Reference:</p>
<p>https://medium.com/microsoftazure/automated-and-interpretable-machine-learning-d07975741298</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Colourseun</strong> <code>(Tue 20 Aug 2024 18:40)</code> - <em>Upvotes: 13</em></p><p>Tabular, Text, Image is the right answer</p></blockquote>

</details>

---

[<< Previous Question](question_262.md) | [Home](/index.md) | [Next Question >>](question_264.md)
