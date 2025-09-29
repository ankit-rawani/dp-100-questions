# Question 477

You are a data scientist building a deep convolutional neural network (CNN) for image classification.

The CNN model you build shows signs of overfitting.

You need to reduce overfitting and converge the model to an optimal fit.

Which two actions should you perform? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

* A.Add an additional dense layer with 512 input units.
* B.Add L1/L2 regularization.
* C.Use training data augmentation.
* D.Reduce the amount of training data.
* E.Add an additional dense layer with 64 input units.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>BC</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>jsnels86</strong> <code>(Tue 26 May 2020 15:50)</code> - <em>Upvotes: 25</em></p><p>I agree, B and C should be the correct answers</p></blockquote>
<blockquote><p><strong>Yilu</strong> <code>(Tue 12 May 2020 05:47)</code> - <em>Upvotes: 16</em></p><p>adding more training records should decrease the overfitting.</p></blockquote>
<blockquote><p><strong>Yilu</strong> <code>(Sat 16 May 2020 04:49)</code> - <em>Upvotes: 47</em></p><p>Answer should be B and C</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Thu 25 Mar 2021 15:26)</code> - <em>Upvotes: 1</em></p><p>I agree</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 11:47)</code> - <em>Upvotes: 1</em></p><p>Explanation:
B. L1/L2 regularization helps prevent overfitting by adding a penalty term to the loss function, discouraging the model from relying too heavily on any particular feature.
C. Data augmentation increases the diversity of your training set by applying random (but realistic) transformations to the existing images, which helps the model generalize better and reduce overfitting.
These two techniques are commonly used to address overfitting in deep learning models, especially CNNs for image classification.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 18 May 2024 06:33)</code> - <em>Upvotes: 1</em></p><p>B. Add L1/L2 regularization.

C. Use training data augmentation.

These methods directly address the problem of overfitting by either penalizing overly complex models or by making the training data more diverse and challenging for the model.</p></blockquote>
<blockquote><p><strong>Matt2000</strong> <code>(Tue 06 Feb 2024 12:09)</code> - <em>Upvotes: 1</em></p><p>This reference might be useful: https://towardsdatascience.com/8-simple-techniques-to-prevent-overfitting-4d443da2ef7d</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 24 Feb 2023 04:39)</code> - <em>Upvotes: 2</em></p><p>The two actions that can help reduce overfitting and converge the model to an optimal fit are:

B. Add L1/L2 regularization: Regularization techniques can help to reduce overfitting in a neural network. L1/L2 regularization adds a penalty term to the loss function, which encourages the model to learn simpler and smoother weight values. This, in turn, helps to prevent overfitting.

C. Use training data augmentation: Data augmentation is a technique that can be used to artificially increase the size of the training dataset by creating new examples from existing data. This can help the model to generalize better and reduce overfitting. Common data augmentation techniques for image data include random rotations, flips, and translations.

Options A and E suggest adding additional dense layers, which can increase the complexity of the model and potentially exacerbate overfitting. Option D suggests reducing the amount of training data, which can lead to underfitting and poor generalization performance. Therefore, options B and C are the best choices for reducing overfitting and improving model performance.</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Mon 13 Jun 2022 13:09)</code> - <em>Upvotes: 2</em></p><p>Regulation
Increase data through data argumentation</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Wed 08 Dec 2021 18:26)</code> - <em>Upvotes: 5</em></p><p>I agree with B and C</p></blockquote>
<blockquote><p><strong>saurabhk1</strong> <code>(Fri 05 Mar 2021 09:59)</code> - <em>Upvotes: 7</em></p><p>Answer should be B and C</p></blockquote>
<blockquote><p><strong>Neuron</strong> <code>(Tue 02 Feb 2021 22:21)</code> - <em>Upvotes: 4</em></p><p>Regularisation and data augmentation are correct. Dropouts and early termination are also correct but not in the options.</p></blockquote>
<blockquote><p><strong>aziti</strong> <code>(Tue 29 Dec 2020 20:11)</code> - <em>Upvotes: 4</em></p><p>During dropout, we are not actually reducing the training data but rather dropping the neurons to help them memorize less and not overfit.
https://www.kdnuggets.com/2019/12/5-techniques-prevent-overfitting-neural-networks.html
so the answer is B and C</p></blockquote>
<blockquote><p><strong>Sud3962</strong> <code>(Sat 19 Dec 2020 20:52)</code> - <em>Upvotes: 2</em></p><p>Answer should be B,C</p></blockquote>
<blockquote><p><strong>Pucha</strong> <code>(Thu 12 Nov 2020 05:41)</code> - <em>Upvotes: 3</em></p><p>Yes BC should be correct, image data augmentation - generating more training data artificially to expand the learning of algo</p></blockquote>
<blockquote><p><strong>BICube</strong> <code>(Sun 20 Sep 2020 17:39)</code> - <em>Upvotes: 5</em></p><p>and to support the argument for C:
&quot;Image data augmentation is a technique that can be used to artificially expand the size of a training dataset by creating modified versions of images in the dataset.

Training deep learning neural network models on more data can result in more skillful models, and the augmentation techniques can create variations of the images that can improve the ability of the fit models to generalize what they have learned to new images.&quot;
Ref: https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/</p></blockquote>
<blockquote><p><strong>hima618</strong> <code>(Sun 20 Sep 2020 06:13)</code> - <em>Upvotes: 2</em></p><p>Yes, BC are correct.</p></blockquote>
<blockquote><p><strong>rr200</strong> <code>(Thu 30 Jul 2020 14:36)</code> - <em>Upvotes: 4</em></p><p>BC are right answers.  To reduce overfitting in DL model, you either increase training data volume or reduce complexity of the model</p></blockquote>
<blockquote><p><strong>Timeless_Faceless</strong> <code>(Wed 15 Jul 2020 10:34)</code> - <em>Upvotes: 4</em></p><p>The answer is definitely B and C</p></blockquote>

</details>

---

[<< Previous Question](question_476.md) | [Home](/index.md) | [Next Question >>](question_478.md)
