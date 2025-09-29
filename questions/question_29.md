# Question 29

You want to train a classification model using data located in a comma-separated values (CSV) file.

The classification model will be trained via the Automated Machine Learning interface using the Classification task type.

You have been informed that only linear models need to be assessed by the Automated Machine Learning.

Which of the following actions should you take?

* A.You should disable deep learning.
* B.You should enable automatic featurization.
* C.You should disable automatic featurization.
* D.You should set the task type to Forecasting.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>A</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>gaint</strong> <code>(Wed 05 Jan 2022 07:18)</code> - <em>Upvotes: 22</em></p><p>Answer should be A</p></blockquote>
<blockquote><p><strong>lander_c</strong> <code>(Mon 04 Apr 2022 01:53)</code> - <em>Upvotes: 5</em></p><p>Disabling automatic featurization does not cause the models evaluated to be linear only. 
Automatic featurization has the following steps listed https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-auto-features#automatic-featurization

The only way to force linear algorithms to be evaluated is to use the blocked algorithms. list.</p></blockquote>
<blockquote><p><strong>phydev</strong> <code>(Sat 20 Jan 2024 13:44)</code> - <em>Upvotes: 20</em></p><p>This was on Exam today (20 July 2023). There was another option to Block all the other algorithms except the linear ones, which I chose as my answer.</p></blockquote>
<blockquote><p><strong>amittal09</strong> <code>(Fri 16 May 2025 06:23)</code> - <em>Upvotes: 2</em></p><p>The goal is to assess only linear models. Deep learning models are non-linear and complex. By disabling deep learning algorithms in the Automated Machine Learning settings, you ensure that only linear models (like Logistic Regression, Linear SVM, etc.) are considered during the model selection process.</p></blockquote>
<blockquote><p><strong>deyoz</strong> <code>(Mon 26 Aug 2024 23:47)</code> - <em>Upvotes: 1</em></p><p>I go for A</p></blockquote>
<blockquote><p><strong>NullVoider_0</strong> <code>(Tue 11 Jun 2024 10:18)</code> - <em>Upvotes: 1</em></p><p>AutoML tries different models and algorithms during the automation and tuning process. If you want to focus only on linear models, you need to limit the scope of algorithms that AutoML considers.</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Fri 12 Apr 2024 08:32)</code> - <em>Upvotes: 1</em></p><p>&#x27;Deep learning&#x27; for polynomial model, so &#x27;linear model&#x27; can disable.</p></blockquote>
<blockquote><p><strong>endeesa</strong> <code>(Fri 08 Dec 2023 22:11)</code> - <em>Upvotes: 1</em></p><p>Answer is A</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Wed 25 Oct 2023 10:21)</code> - <em>Upvotes: 5</em></p><p>The correct answer is A, as deep learning models are inherently non-linear.</p></blockquote>
<blockquote><p><strong>bvkr</strong> <code>(Thu 28 Sep 2023 15:59)</code> - <em>Upvotes: 2</em></p><p>ChatGPT answer is B:
option B is the most appropriate choice:

B. You should enable automatic featurization.

Enabling automatic featurization will allow the Automated Machine Learning interface to automatically preprocess the CSV data and extract relevant features that are compatible with linear models. Automatic featurization can also handle missing values, categorical variables, and feature scaling, which can be time-consuming and error-prone if done manually.

Disabling deep learning (option A) may be necessary if the dataset is small or if the use of deep learning is not feasible or desired, but it is not relevant to the given scenario. Setting the task type to Forecasting (option D) is also not relevant since the task type has already been specified as Classification. Disabling automatic featurization (option C) may be appropriate if the CSV data has already been preprocessed and feature engineering has been performed manually, but it is not necessary if the CSV data is in its raw form.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sun 27 Aug 2023 20:29)</code> - <em>Upvotes: 1</em></p><p>The correct answer is B. You should enable automatic featurization.

Automated Machine Learning (AutoML) is a process that automates various aspects of machine learning, such as data preprocessing, feature engineering, and model selection. It aims to make machine learning more accessible to individuals with limited expertise in data science.

In this scenario, the user has been informed that only linear models need to be assessed. Enabling automatic featurization is important because it will allow the AutoML interface to transform the data and generate additional features that may improve the performance of the linear models.

Disabling automatic featurization (option C) would prevent the AutoML interface from generating additional features, potentially limiting the performance of the linear models. Disabling deep learning (option A) is not necessary since the problem does not involve deep learning models. Setting the task type to Forecasting (option D) is also incorrect since the user has been informed that a classification model needs to be trained.</p></blockquote>
<blockquote><p><strong>mamau</strong> <code>(Sat 12 Aug 2023 06:56)</code> - <em>Upvotes: 2</em></p><p>C. You should disable automatic featurization. Automated Machine Learning (AutoML) provides the ability to automatically engineer features in order to simplify the process of building a machine learning model. However, in this case, the requirements specify that only linear models need to be assessed, so it would be best to disable automatic featurization to ensure that only linear models are considered. This would help ensure that the results are in line with the requirements.</p></blockquote>
<blockquote><p><strong>manuu97</strong> <code>(Fri 16 Jun 2023 13:33)</code> - <em>Upvotes: 1</em></p><p>By exclusion the right answer is A</p></blockquote>
<blockquote><p><strong>lookaaaa</strong> <code>(Tue 23 May 2023 20:14)</code> - <em>Upvotes: 3</em></p><p>featurization has no effect of linear models, so BC are wrong; 
As for D, you should choose classification not forecasting</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Tue 11 Apr 2023 06:19)</code> - <em>Upvotes: 2</em></p><p>The Answer is A.</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Mon 12 Sep 2022 10:01)</code> - <em>Upvotes: 3</em></p><p>Without blocking algorithm options, the answer is A.</p></blockquote>
<blockquote><p><strong>RyanTsai</strong> <code>(Sat 19 Mar 2022 10:09)</code> - <em>Upvotes: 2</em></p><p>ans: B. You should enable automatic featurization.</p></blockquote>
<blockquote><p><strong>Mirjalol</strong> <code>(Tue 01 Aug 2023 10:44)</code> - <em>Upvotes: 9</em></p><p>you should be blocked for misleading people</p></blockquote>
<blockquote><p><strong>BenAji</strong> <code>(Thu 10 Feb 2022 08:57)</code> - <em>Upvotes: 6</em></p><p>No right answer, as AML only support an option to &quot;Blocked Algorithm&quot;     https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-automated-ml-for-ml-models</p></blockquote>

</details>

---

[<< Previous Question](question_28.md) | [Home](/index.md) | [Next Question >>](question_30.md)
