# Question 38

You are in the process of constructing a deep convolutional neural network (CNN). The CNN will be used for image classification.

You notice that the CNN model you constructed displays hints of overfitting.

You want to make sure that overfitting is minimized, and that the model is converged to an optimal fit.

Which of the following is TRUE with regards to achieving your goal?

* A.You have to add an additional dense layer with 512 input units, and reduce the amount of training data.
* B.You have to add L1/L2 regularization, and reduce the amount of training data.
* C.You have to reduce the amount of training data and make use of training data augmentation.
* D.You have to add L1/L2 regularization, and make use of training data augmentation.
* E.You have to add an additional dense layer with 512 input units, and add L1/L2 regularization.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>exam_monkey1234</strong> <code>(Tue 05 Jul 2022 11:00)</code> - <em>Upvotes: 50</em></p><p>I would say answer D</p></blockquote>
<blockquote><p><strong>Moshekwa</strong> <code>(Sun 31 Jul 2022 12:34)</code> - <em>Upvotes: 14</em></p><p>&quot;data augmentation simply means increasing size of the data that is increasing the number of images present in the dataset..  using data augmentation a lot of similar images can be generated. This helps in increasing the dataset size and thus reduce overfitting.&quot;

https://www.kdnuggets.com/2019/12/5-techniques-prevent-overfitting-neural-networks.html</p></blockquote>
<blockquote><p><strong>Nghia1</strong> <code>(Thu 30 May 2024 23:29)</code> - <em>Upvotes: 1</em></p><p>agree, option B reduce amount of training data will lead to overfitting.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Thu 01 Feb 2024 21:27)</code> - <em>Upvotes: 9</em></p><p>Moderator, you should correct the answers, not me!
D. You have to add L1/L2 regularization and make use of training data augmentation.
Overfitting occurs when a model is too complex for data it is being trained on and memorizes the training data instead of generalizing to new data. To reduce overfitting, you can use regularization techniques such as L1 or L2 regularization, which add a penalty term to the loss function to discourage the model from learning overly complex representations. Additionally, increasing the amount of training data can also help reduce overfitting by giving the model more information to learn from. One common way to increase the amount of training data is to use data augmentation, which involves transforming the existing data in ways that preserve the labels to generate additional training examples.</p></blockquote>
<blockquote><p><strong>dporwal04</strong> <code>(Thu 05 Dec 2024 09:01)</code> - <em>Upvotes: 2</em></p><p>D is the correct ans</p></blockquote>
<blockquote><p><strong>rakeshmk</strong> <code>(Fri 27 Sep 2024 09:26)</code> - <em>Upvotes: 1</em></p><p>The answer is D. Data augmentation really helps to reduce overfitting and L1L2 are most used regularization in Neural networks..
Dear moderator , please provide the correct answers. Many of them given here is misleading which can make chaos while attending exam</p></blockquote>
<blockquote><p><strong>endeesa</strong> <code>(Sat 08 Jun 2024 21:46)</code> - <em>Upvotes: 1</em></p><p>The only option that makes sense to me is D. Adding regularisation will reduce overfitting, similarly adding more data adds more diversity to the training set allowing it to generalise better. So answer is D</p></blockquote>
<blockquote><p><strong>bvkr</strong> <code>(Thu 28 Mar 2024 17:34)</code> - <em>Upvotes: 2</em></p><p>ChatGPT answer: Option D: You have to add L1/L2 regularization, and make use of training data augmentation.

When a deep CNN model displays hints of overfitting, it means that the model is too complex and has learned to fit the training data too closely. One way to minimize overfitting is to add regularization to the model, which adds a penalty term to the loss function, encouraging the model to choose simpler solutions.

L1/L2 regularization adds a penalty term to the loss function that discourages the model from using large weights in the network. This has the effect of reducing the complexity of the model and can help prevent overfitting.

Data augmentation is another effective technique to minimize overfitting. It involves applying random transformations to the training data, such as random rotations or translations, to create new training examples that are similar to the original ones. This helps the model to generalize better to unseen data.</p></blockquote>
<blockquote><p><strong>Yoshizn</strong> <code>(Wed 07 Feb 2024 16:01)</code> - <em>Upvotes: 1</em></p><p>Answer is D</p></blockquote>
<blockquote><p><strong>MansoorDataScientist</strong> <code>(Thu 25 Jan 2024 17:34)</code> - <em>Upvotes: 2</em></p><p>Steps for reducing overfitting:

Add more data.
Use data augmentation.
Use architectures that generalize well.
Add regularization (mostly dropout, L1/L2 regularization are also possible)
Reduce architecture complexity.</p></blockquote>
<blockquote><p><strong>Peeking</strong> <code>(Tue 16 Jan 2024 04:59)</code> - <em>Upvotes: 1</em></p><p>D is definitely the answer.</p></blockquote>
<blockquote><p><strong>Edriv</strong> <code>(Mon 11 Dec 2023 13:22)</code> - <em>Upvotes: 1</em></p><p>Why don&#x27;t C?</p></blockquote>
<blockquote><p><strong>lookaaaa</strong> <code>(Thu 23 Nov 2023 22:33)</code> - <em>Upvotes: 2</em></p><p>increse amount of data, simplify the model (decrese layers or NN unit, etc)</p></blockquote>
<blockquote><p><strong>zweic</strong> <code>(Thu 05 Oct 2023 15:03)</code> - <em>Upvotes: 2</em></p><p>I would say D</p></blockquote>
<blockquote><p><strong>jlopezfelizzola</strong> <code>(Mon 11 Sep 2023 04:52)</code> - <em>Upvotes: 2</em></p><p>My vote is for D. A &amp; E discarded because that is increasing the complexity of the architecture. B, C are suggesting reducing the amount of data. D will generate more data for the CNN to be able to generalize more.</p></blockquote>
<blockquote><p><strong>jlopezfelizzola</strong> <code>(Mon 11 Sep 2023 09:09)</code> - <em>Upvotes: 1</em></p><p>Source
https://towardsdatascience.com/deep-learning-3-more-on-cnns-handling-overfitting-2bd5d99abe5d</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sat 11 Mar 2023 11:14)</code> - <em>Upvotes: 1</em></p><p>Definitely D</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Fri 09 Dec 2022 12:08)</code> - <em>Upvotes: 1</em></p><p>I vote for D</p></blockquote>
<blockquote><p><strong>jed_elhak</strong> <code>(Mon 19 Sep 2022 00:46)</code> - <em>Upvotes: 4</em></p><p>Answer is D :)</p></blockquote>
<blockquote><p><strong>Maryam89</strong> <code>(Sat 13 Aug 2022 10:08)</code> - <em>Upvotes: 4</em></p><p>Answer is D</p></blockquote>

</details>

---

[<< Previous Question](question_37.md) | [Home](/index.md) | [Next Question >>](question_39.md)
