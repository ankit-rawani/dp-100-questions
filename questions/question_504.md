# Question 504

DRAG DROP -

You need to define a modeling strategy for ad response.

Which three actions should you perform in sequence? To answer, move the appropriate actions from the list of actions to the answer area and arrange them in the correct order.

Select and Place:

![Question Image](../images/q504_q_0033000001.png)

<details>
  <summary>Show Suggested Answer</summary>

<img src="../images/q504_ans_0_0033000002.png" alt="Answer Image"><br>

<p>Step 1: Implement a K-Means Clustering model</p>
<p>Step 2: Use the cluster as a feature in a Decision jungle model.</p>
<p>Decision jungles are non-parametric models, which can represent non-linear decision boundaries.</p>
<p>Step 3: Use the raw score as a feature in a Score Matchbox Recommender model</p>
<p>The goal of creating a recommendation system is to recommend one or more &quot;items&quot; to &quot;users&quot; of the system. Examples of an item could be a movie, restaurant, book, or song. A user could be a person, group of persons, or other entity with item preferences.</p>
<p>Scenario:</p>
<p>Ad response rated declined.</p>
<p>Ad response models must be trained at the beginning of each event and applied during the sporting event.</p>
<p>Market segmentation models must optimize for similar ad response history.</p>
<p>Ad response models must support non-linear boundaries of features.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/multiclass-decision-jungle https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/score-matchbox-recommender</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>phdykd</strong> <code>(Sun 25 Aug 2024 06:37)</code> - <em>Upvotes: 2</em></p><p>The three actions to perform in sequence for defining a modeling strategy for ad response are as follows:

Implement a K-Means clustering model
Use the cluster as a feature in a decision jungle model
Use the raw score as a feature in a logistic regression model
Therefore, the correct order of actions is A, C, and D.</p></blockquote>

<blockquote><p><strong>ning</strong> <code>(Sun 17 Dec 2023 13:03)</code> - <em>Upvotes: 1</em></p><p>No idea, guess the answer is OK, thought process ...
K-means --&gt; we do not what will come, so clustering ...
Need a score as input for recommendation --&gt; Tree Forest Regression --&gt; Whatever score indicates what action we should take ????</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Mon 18 Dec 2023 14:35)</code> - <em>Upvotes: 1</em></p><p>On a second thought, it might not be the case, this is very confusing ...
Response rate is just response vs no response, no it is binary classification ...
Also, it mentioned the distribution of features for training and production data are different ...
So my bet is :
1. sweep clustering
2. Tree forest
3. Logistic regression</p></blockquote>
<blockquote><p><strong>jackreacher</strong> <code>(Mon 23 May 2022 04:11)</code> - <em>Upvotes: 1</em></p><p>Is there anybody who can explain this? Thanks</p></blockquote>
<blockquote><p><strong>Indranee</strong> <code>(Wed 20 Jul 2022 08:57)</code> - <em>Upvotes: 26</em></p><p>This question is challenging. The answer looks right.

1. The ad response model needs to support &#x27;non-linear decision boundaries&#x27;. This is supported by the decision jungle model. So now we have the decision jungle model as one of the three steps.
2. The decision jungle model uses K-means clusters as inputs, so K-Means comes before the decision jungle model. K-means clustering can be used to identify &#x27;market/customer segments&#x27;.
3. There remains a third step either before K-means or after decision jungle model. The ad response model needs to be &#x27;applied during the event&#x27;. It does seem that a recommender model is the more appropriate choice to apply onto the live dataset and serve recommendations during the event. And the recommender model would logically be at the last step.
4. So the overall flow seems to be identifying market/customer segments using KMeans -&gt; Non-linear decisions using Decision Jungle (frankly I still wonder how this model fits in the end-to-end flow) -&gt; serve recommendations using the recommender model.</p></blockquote>

</details>

---

[<< Previous Question](question_503.md) | [Home](../index.md) | [Next Question >>](question_505.md)
