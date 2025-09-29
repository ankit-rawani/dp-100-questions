# Question 271

You are building a machine learning model for translating English language textual content into French language textual content.

You need to build and train the machine learning model to learn the sequence of the textual content.

Which type of neural network should you use?

* A.Multilayer Perceptions (MLPs)
* B.Convolutional Neural Networks (CNNs)
* C.Recurrent Neural Networks (RNNs)
* D.Generative Adversarial Networks (GANs)

<details>
  <summary>Show Suggested Answer</summary>

  <strong>C</strong><br>
<p>To translate a corpus of English text to French, we need to build a recurrent neural network (RNN).</p>
<p>Note: RNNs are designed to take sequences of text as inputs or return sequences of text as outputs, or both. They&#x27;re called recurrent because the network&#x27;s hidden layers have a loop in which the output and cell state from each time step become inputs at the next time step. This recurrence serves as a form of memory.</p>
<p>It allows contextual information to flow through the network so that relevant outputs from previous time steps can be applied to network operations at the current time step.</p>
<p>Reference:</p>
<p>https://towardsdatascience.com/language-translation-with-rnns-d84d43b40571</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>RSMCT2011</strong> <code>(Fri 01 Jan 2021 11:19)</code> - <em>Upvotes: 11</em></p><p>Answer: C
https://chunml.github.io/ChunML.github.io/project/Creating-Text-Generator-Using-Recurrent-Neural-Network/</p></blockquote>
<blockquote><p><strong>james2033</strong> <code>(Sun 20 Oct 2024 02:51)</code> - <em>Upvotes: 1</em></p><p>NLP --&gt; sequence --&gt; RNN. Choose C.

CNN for image training. Remove B.

&#x27;Multi-layer perceptions&#x27; for neural network theory. Remove A.</p></blockquote>
<blockquote><p><strong>azurelearner666</strong> <code>(Fri 14 Apr 2023 08:05)</code> - <em>Upvotes: 1</em></p><p>C, RNN is the answer.</p></blockquote>
<blockquote><p><strong>adamwar</strong> <code>(Thu 03 Nov 2022 13:55)</code> - <em>Upvotes: 1</em></p><p>RNNs are not used much anymore in favour of LSTMS or similar, also CNNs can be used for seq2seq models</p></blockquote>
<blockquote><p><strong>spaceykacey</strong> <code>(Fri 11 Nov 2022 17:08)</code> - <em>Upvotes: 5</em></p><p>LSTMs are a type of RNN.</p></blockquote>
<blockquote><p><strong>ranjsi01</strong> <code>(Thu 19 Jan 2023 16:02)</code> - <em>Upvotes: 1</em></p><p>lstms = long short term memory</p></blockquote>
<blockquote><p><strong>dushmantha</strong> <code>(Tue 30 Aug 2022 04:38)</code> - <em>Upvotes: 3</em></p><p>Answer is correct</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Mon 11 Jul 2022 14:14)</code> - <em>Upvotes: 4</em></p><p>On exam 2021/7/10</p></blockquote>

</details>

---

[<< Previous Question](question_270.md) | [Home](/index.md) | [Next Question >>](question_272.md)
