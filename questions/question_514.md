# Question 514

HOTSPOT -

You need to configure the Edit Metadata module so that the structure of the datasets match.

Which configuration options should you select? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q514_q_0035100001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q514_ans_0_image621.png" alt="Answer Image"><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>Yong2020</strong> <code>(Sat 20 Nov 2021 11:09)</code> - <em>Upvotes: 18</em></p><p>MedianValue should be made uncategorical to be consistent as the original formats are in text and numeric.</p></blockquote>
<blockquote><p><strong>CharlesZ</strong> <code>(Sat 12 Feb 2022 01:22)</code> - <em>Upvotes: 9</em></p><p>I think the answer should be floating and make uncategorical, becuase it&#x27;s a regression model and MedianValue is the target column. Uncategorical would make sense.</p></blockquote>
<blockquote><p><strong>phdykd</strong> <code>(Sun 25 Aug 2024 23:34)</code> - <em>Upvotes: 1</em></p><p>For the configuration options in the Edit Metadata module, you should select:

Launch column selector:
Integer
Unchanged: This will ensure that the MedianValue column in both datasets is recognized as an integer type and is not modified.</p></blockquote>
<blockquote><p><strong>spaceykacey</strong> <code>(Fri 05 May 2023 06:24)</code> - <em>Upvotes: 3</em></p><p>Should it not be &#x27;Integer&#x27;? The value is in $1000s.</p></blockquote>
<blockquote><p><strong>Mckay_</strong> <code>(Sun 14 Apr 2024 22:40)</code> - <em>Upvotes: 1</em></p><p>good observation. I totally agree with you.</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Mon 28 Nov 2022 17:29)</code> - <em>Upvotes: 3</em></p><p>if your source dataset has numbers handled as text, you must change them to a numeric data type before using math operations.
The supported data types are String, Integer, Double, Boolean, and DateTime.
Floating point and time span is not an option

For example, you might have a column that contains the numbers 0, 1, and 2, but know that the numbers actually mean &quot;Smoker,&quot; &quot;Non-smoker,&quot; and &quot;Unknown.&quot; In that case, by flagging the column as categorical you ensure that the values are used only to group data and not in numeric calculations.

Since it is numeric the option should be either &quot;unchanged&quot; or &quot;make uncategorical&quot;. 

The original data is text so it should be made uncategorical</p></blockquote>
<blockquote><p><strong>brendal89</strong> <code>(Fri 07 Oct 2022 10:19)</code> - <em>Upvotes: 2</em></p><p>if you google &quot;make uncategorical&quot; + edit metadata, you only get references to this particular exam question... I&#x27;m not convinced that &quot;make uncategorical&quot; even exists.</p></blockquote>
<blockquote><p><strong>Dasist</strong> <code>(Tue 27 Sep 2022 17:24)</code> - <em>Upvotes: 3</em></p><p>Integer and uncategorical as the MedianValue is written in 1000 (no decimal point) and it&#x27;s a regression model so must be numeric.</p></blockquote>
<blockquote><p><strong>Neuron</strong> <code>(Wed 03 Aug 2022 10:47)</code> - <em>Upvotes: 3</em></p><p>The table that shows types indicate MedianValue is in the $1000s. It&#x27;s an integer. Where did Floating Point come from? Also, the Paris data must be noncategorical, too, like the London data.</p></blockquote>
<blockquote><p><strong>RyuHayabusa</strong> <code>(Mon 15 Aug 2022 15:28)</code> - <em>Upvotes: 1</em></p><p>Read the text. One MedianValue is text and the other is numerical.</p></blockquote>
<blockquote><p><strong>YipingRuan</strong> <code>(Fri 13 Jan 2023 08:31)</code> - <em>Upvotes: 3</em></p><p>in 1000 means you can have value 4.5 in the column ($4500)</p></blockquote>
<blockquote><p><strong>Abhinav_nasaiitkgp</strong> <code>(Thu 21 Jul 2022 13:19)</code> - <em>Upvotes: 4</em></p><p>I don&#x27;t think it is necessary to make it uncategorical as text data is not categorical in this case which we have to make uncategorical. Answer is correct.</p></blockquote>
<blockquote><p><strong>allanm</strong> <code>(Thu 17 Nov 2022 00:53)</code> - <em>Upvotes: 1</em></p><p>What text data? The case study states that The MedianValue and AvgRoomsInHouse columns both hold data in numeric format.</p></blockquote>
<blockquote><p><strong>122120</strong> <code>(Sun 10 Jul 2022 06:11)</code> - <em>Upvotes: 7</em></p><p>there is no floating point.

Select the Data type option if you need to assign a different data type to the selected columns. You might need to change the data type for certain operations. For example, if your source dataset has numbers handled as text, you must change them to a numeric data type before using math operations.

The supported data types are String, Integer, Double, Boolean, and DateTime.

If you select multiple columns, you must apply the metadata changes to all selected columns. For example, let&#x27;s say you choose two or three numeric columns. You can change them all to a string data type and rename them in one operation. However, you can&#x27;t change one column to a string data type and another column from a float to an integer.

If you don&#x27;t specify a new data type, the column metadata is unchanged.

The column type and values will change after you perform the Edit Metadata operation. You can recover the original data type at any time by using Edit Metadata to reset the column data type.</p></blockquote>
<blockquote><p><strong>aziti</strong> <code>(Thu 30 Jun 2022 13:51)</code> - <em>Upvotes: 2</em></p><p>I dont think there is such a thing as make uncategorical. Since the string version of the MedianValue we had is already not categorical we do not need to switch the MedianValue, thus leaving it unchanged would leave us with a non categorical Median integer value..maybe</p></blockquote>
<blockquote><p><strong>Rickii</strong> <code>(Mon 17 Jan 2022 12:04)</code> - <em>Upvotes: 2</em></p><p>The answer is Floating point, Make Categorical</p></blockquote>
<blockquote><p><strong>Indranee</strong> <code>(Wed 20 Jul 2022 07:43)</code> - <em>Upvotes: 1</em></p><p>To make &#x27;MedianValues&#x27; categorical, do you mean turning values into bins of &#x27;MedianValues&#x27;?</p></blockquote>
<blockquote><p><strong>Alexandra</strong> <code>(Wed 05 Jan 2022 11:52)</code> - <em>Upvotes: 3</em></p><p>as the Paris dataset needs to match London dataset types and London has numerical data types in MoedianValues columns, shouldn&#x27;t the answer be &#x27;Integer&#x27; and &#x27;Make Uncategorical&#x27;?</p></blockquote>
<blockquote><p><strong>pepmir</strong> <code>(Sat 25 Dec 2021 22:06)</code> - <em>Upvotes: 5</em></p><p>&quot;You must ensure that the datatype of the MedianValue column of the Paris dataset matches the structure of the London dataset.&quot;
If we run Summary on the data, it might end up as Categorical due to the nature of data.
That said &quot;Unchanged&quot; might do it here.</p></blockquote>
<blockquote><p><strong>ajithvajrala</strong> <code>(Tue 23 Nov 2021 12:53)</code> - <em>Upvotes: 1</em></p><p>yes, I too agree with Yong2020.</p></blockquote>
<blockquote><p><strong>ceni99</strong> <code>(Thu 18 Nov 2021 23:44)</code> - <em>Upvotes: 1</em></p><p>Correct me if I&#x27;m wrong, but I believe the answer should be &quot;Make Categorical&quot; if you don&#x27;t want the MedianValue column to be numerical calculated.</p></blockquote>
<blockquote><p><strong>kty</strong> <code>(Sun 25 Sep 2022 18:48)</code> - <em>Upvotes: 3</em></p><p>An initial investigation shows that the datasets are identical in structure apart from the MedianValue column. The smaller Paris dataset contains the MedianValue in text format, whereas the larger London dataset contains the MedianValue in numerical format
so the answer is :

floating and uncategorical</p></blockquote>

</details>

---

[<< Previous Question](question_513.md) | [Home](/index.md) | [Next Question >>](question_515.md)
