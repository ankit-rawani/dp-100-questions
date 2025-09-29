# Question 48

You are developing deep learning models to analyze semi-structured, unstructured, and structured data types.

You have the following data available for model building:

✑ Video recordings of sporting events

✑ Transcripts of radio commentary about events

✑ Logs from related social media feeds captured during sporting events

You need to select an environment for creating the model.

Which environment should you use?

- A.Azure Cognitive Services
- B.Azure Data Lake Analytics
- C.Azure HDInsight with Spark MLib
- D.Azure Machine Learning Studio

<details>
  <summary>Show Suggested Answer</summary>

<strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Herr</strong> <code>(Sun 16 Aug 2020 09:11)</code> - <em>Upvotes: 35</em></p><p>The answer should be &quot;C&quot;, the question talks about an environment for model building. Cognitive services is primarily for those with little or no DS skills (Azure Cognitive Services are APIs, SDKs, and services available to help developers build intelligent applications without having direct AI or data science skills or knowledge)</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Mon 12 Dec 2022 17:42)</code> - <em>Upvotes: 1</em></p><p>Agree - C</p></blockquote>
<blockquote><p><strong>treadst0ne</strong> <code>(Tue 23 Feb 2021 17:07)</code> - <em>Upvotes: 4</em></p><p>I agree.</p></blockquote>
<blockquote><p><strong>levm39</strong> <code>(Mon 14 Jun 2021 09:53)</code> - <em>Upvotes: 11</em></p><p>Answer is A:
explanation is here: https://docs.microsoft.com/en-us/azure/cognitive-services/big-data/cognitive-services-for-big-data</p></blockquote>
<blockquote><p><strong>sar77</strong> <code>(Tue 15 Jul 2025 19:38)</code> - <em>Upvotes: 1</em></p><p>Azure Machine Learning Studio
Supports custom deep learning models.
Can handle structured, semi-structured, and unstructured data.
Integrates with PyTorch, TensorFlow, Keras, and supports GPU compute. ✅ Best choice for building and training deep learning models on diverse data types.</p></blockquote>
<blockquote><p><strong>f82411e</strong> <code>(Thu 15 May 2025 00:44)</code> - <em>Upvotes: 1</em></p><p>Azure Cognitive Services
Usa modelos ya entrenados. Útil para tareas simples, pero no sirve para entrenar modelos personalizados complejos.
B. Azure Data Lake Analytics
Es una solución para consultas y análisis de datos a gran escala, no para entrenar modelos.
Azure HDInsight con Spark MLlib
Bueno para ML tradicional en grandes volúmenes de datos, pero limitado para deep learning y datos no estructurados como video. La respuesta es la D</p></blockquote>
<blockquote><p><strong>jl420</strong> <code>(Tue 12 Nov 2024 17:13)</code> - <em>Upvotes: 2</em></p><p>While Azure Cognitive Services is a powerful suite of APIs and services for adding AI capabilities to applications, it is more focused on providing pre-built models for specific tasks such as vision, speech, language, and decision-making. These services are excellent for integrating AI features into applications quickly and easily, but they may not offer the same level of flexibility and control needed for developing custom deep learning models from scratch.

On the other hand, Azure Machine Learning Studio provides a comprehensive environment for developing, training, and deploying custom machine learning models, including deep learning models. It supports various data types and offers tools for data preparation, model training, and deployment, making it a more suitable choice for your needs.</p></blockquote>

<blockquote><p><strong>jefimija</strong> <code>(Mon 28 Oct 2024 08:20)</code> - <em>Upvotes: 1</em></p><p>Azure Cognitive Services is for using prebuilt models, not for training</p></blockquote>
<blockquote><p><strong>sl_mslconsulting</strong> <code>(Fri 07 Jun 2024 22:19)</code> - <em>Upvotes: 2</em></p><p>I would pick D and ChapGPT 4 agreed with me. I wrote AI-102 (the updated one) a while back. AI cognitive service is not what you think it is as people discussed here.</p></blockquote>
<blockquote><p><strong>Shariq</strong> <code>(Mon 27 May 2024 13:35)</code> - <em>Upvotes: 1</em></p><p>Should not it be Azure AI Service?</p></blockquote>
<blockquote><p><strong>prabhjot</strong> <code>(Mon 29 Jan 2024 13:02)</code> - <em>Upvotes: 1</em></p><p>ANS D - Azure Machine Learning Studio: Azure Machine Learning Studio provides a comprehensive environment for building, training, and deploying machine learning models, including deep learning models. It supports various data types, and you can use popular deep learning frameworks like TensorFlow and PyTorch. This option allows for a more integrated and customizable approach to deep learning model development.</p></blockquote>
<blockquote><p><strong>Ran2025</strong> <code>(Sat 30 Sep 2023 14:33)</code> - <em>Upvotes: 1</em></p><p>A is correct!</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Thu 20 Jul 2023 07:58)</code> - <em>Upvotes: 2</em></p><p>ChatGPT says A.</p></blockquote>
<blockquote><p><strong>PopeyeDS</strong> <code>(Sat 15 Jul 2023 06:57)</code> - <em>Upvotes: 1</em></p><p>question talks about the training hence we should go with A</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Mon 10 Jul 2023 10:30)</code> - <em>Upvotes: 2</em></p><p>It seems this isnt DP 100 question, but AI 102.</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Mon 10 Jul 2023 10:04)</code> - <em>Upvotes: 1</em></p><p>Can we build models with Cognitive services?</p></blockquote>
<blockquote><p><strong>SoftAI</strong> <code>(Wed 12 Apr 2023 17:14)</code> - <em>Upvotes: 2</em></p><p>i vote for cognitive services, simply because spark is not a better alternative in my opinion. real time processing is not mentioned anywhere</p></blockquote>
<blockquote><p><strong>sahithi2004</strong> <code>(Mon 20 Mar 2023 10:34)</code> - <em>Upvotes: 3</em></p><p>Azure HDInsight with Spark MLib, you can easily build and deploy machine learning models for analysing semi-structured, unstructured, and structured data types. It provides a scalable computing environment that can handle large amounts of data, and you can use various programming languages such as Python, R, and Scala to develop your models.
Azure Cognitive Services is a cloud-based platform that provides various APIs and pre-built models for developing applications with natural language processing, computer vision, and speech recognition capabilities. While it can be used to analyse unstructured data such as text and images, it may not be the most suitable choice for analysing semi-structured and structured data such as video recordings and social media logs.</p></blockquote>
<blockquote><p><strong>chiappo</strong> <code>(Thu 23 Feb 2023 11:16)</code> - <em>Upvotes: 1</em></p><p>The question references an environment for model building. Cognitive services is primarily for those with little or no DS skills (Azure Cognitive Services are APIs, SDKs, and services available to help developers build intelligent applications without having direct AI or data science skills or knowledge).</p></blockquote>

</details>

---

[<< Previous Question](question_47.md) | [Home](../index.md) | [Next Question >>](question_49.md)
