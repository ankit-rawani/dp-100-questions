# Question 467

You are performing feature engineering on a dataset.

You must add a feature named CityName and populate the column value with the text London.

You need to add the new feature to the dataset.

Which Azure Machine Learning Studio module should you use?

- A.Extract N-Gram Features from Text
- B.Edit Metadata
- C.Preprocess Text
- D.Apply SQL Transformation

<details>
  <summary>Show Suggested Answer</summary>

<strong>D</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>VickyM</strong> <code>(Mon 11 May 2020 20:11)</code> - <em>Upvotes: 50</em></p><p>Since a new column\feature is being added, I believe the answer Apply SQL Transform</p></blockquote>
<blockquote><p><strong>jmonk</strong> <code>(Thu 28 May 2020 09:01)</code> - <em>Upvotes: 20</em></p><p>The correct answer is D. Apply SQL Transfer
Editing the metadata allows you to rename or change the data type of existing columns. It does not allow you to add a column and set it&#x27;s value to &quot;London&quot;.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sun 23 Jun 2024 11:43)</code> - <em>Upvotes: 1</em></p><p>To add a new feature with a constant value like &quot;London&quot; for all rows, the most efficient way is to use SQL. The &quot;Apply SQL Transformation&quot; module allows you to execute SQL queries on your dataset, which can easily add a new column with a constant value.</p></blockquote>
<blockquote><p><strong>evangelist</strong> <code>(Sat 18 May 2024 06:12)</code> - <em>Upvotes: 1</em></p><p>Apply SQL Transformation: This module allows you to use SQL queries to manipulate and transform your dataset. You can easily add a new column and populate it with the desired value using an SQL statement.</p></blockquote>
<blockquote><p><strong>BR_CS</strong> <code>(Mon 21 Aug 2023 13:43)</code> - <em>Upvotes: 1</em></p><p>This question appears at least twice and is wrong both times. i checked. Edit Metadata cannot add a new column and assign a value. There is, however, a distinct &quot;Add column&quot; component.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Wed 09 Aug 2023 11:41)</code> - <em>Upvotes: 1</em></p><p>d is answer</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Fri 24 Feb 2023 03:19)</code> - <em>Upvotes: 1</em></p><p>B is answer</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Wed 14 Dec 2022 21:08)</code> - <em>Upvotes: 1</em></p><p>Answer is D. The new column is Data not Metadata.</p></blockquote>
<blockquote><p><strong>taer</strong> <code>(Wed 23 Nov 2022 10:17)</code> - <em>Upvotes: 3</em></p><p>should be D</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Sun 12 Jun 2022 13:45)</code> - <em>Upvotes: 1</em></p><p>Select *, &#x27;London&#x27; as City from t1</p></blockquote>
<blockquote><p><strong>pancman</strong> <code>(Tue 12 Apr 2022 21:35)</code> - <em>Upvotes: 2</em></p><p>Correct answer is D. I have checked this on Azure Designer Studio to make sure. Edit metadata allows you to alter existing columns. However, it doesn&#x27;t allow you to add a new column or set the value of it. However, you can add a new column and change its value using Apply SQL Transformation.</p></blockquote>
<blockquote><p><strong>silva_831</strong> <code>(Thu 17 Nov 2022 07:40)</code> - <em>Upvotes: 1</em></p><p>Thank you guys for doing practice to verify the answer. Appreciate it.</p></blockquote>
<blockquote><p><strong>Thornehead</strong> <code>(Thu 24 Mar 2022 23:19)</code> - <em>Upvotes: 1</em></p><p>D is the sure shot.</p></blockquote>
<blockquote><p><strong>synapse</strong> <code>(Sat 12 Mar 2022 11:24)</code> - <em>Upvotes: 1</em></p><p>D is the correct answer</p></blockquote>
<blockquote><p><strong>dija123</strong> <code>(Tue 14 Dec 2021 19:11)</code> - <em>Upvotes: 2</em></p><p>I think B is correct, Marking columns as features is what the Edit metadata module can do,
Creating new column is not mentioned in the question, It is populate!</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Wed 13 Apr 2022 08:44)</code> - <em>Upvotes: 1</em></p><p>&quot;You must add a feature named CityName ...&quot; = You must create a new column named CItyName</p></blockquote>
<blockquote><p><strong>dushmantha</strong> <code>(Mon 30 Aug 2021 08:41)</code> - <em>Upvotes: 3</em></p><p>The answer should be &quot;Apply SQL Transformation&quot;. I have checked it. The metadata does not allow to add new columns</p></blockquote>

</details>

---

[<< Previous Question](question_466.md) | [Home](../index.md) | [Next Question >>](question_468.md)
