# Question 200

HOTSPOT -

You plan to preprocess text from CSV files. You load the Azure Machine Learning Studio default stop words list.

You need to configure the Preprocess Text module to meet the following requirements:

✑ Ensure that multiple related words from a single canonical form.

✑ Remove pipe characters from text.

Remove words to optimize information retrieval.

![Question Image](images/q200_q_0017600004.png)

Which three options should you select? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

Hot Area:

![Question Image](images/q200_q_0017800001.png)

<details>
  <summary>Show Suggested Answer</summary>

  <img src="images/q200_ans_0_0018000001.png" alt="Answer Image"><br>
<p>Box 1: Remove stop words -</p>
<p>Remove words to optimize information retrieval.</p>
<p>Remove stop words: Select this option if you want to apply a predefined stopword list to the text column. Stop word removal is performed before any other processes.</p>
<p>Box 2: Lemmatization -</p>
<p>Ensure that multiple related words from a single canonical form.</p>
<p>Lemmatization converts multiple related words to a single canonical form</p>
<p>Box 3: Remove special characters</p>
<p>Remove special characters: Use this option to replace any non-alphanumeric special characters with the pipe | character.</p>
<p>Reference:</p>
<p>https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/preprocess-text</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>hyz123</strong> <code>(Fri 24 Dec 2021 16:42)</code> - <em>Upvotes: 14</em></p><p>&quot;Remove special characters&quot; should not be correct, because the requirement include remove pipe from the data,  but this one will add pipe to the data.
it should be &quot;Split tokens on special characters&quot;, this one should remove the pipe.</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Mon 23 Jan 2023 10:22)</code> - <em>Upvotes: 5</em></p><p>Split tokens on special characters just break words and won&#x27;t remove the pipe(|). 
According the page https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/preprocess-text:
Remove special characters: Use this option to remove any non-alphanumeric special characters.
So given answer is correct.</p></blockquote>
<blockquote><p><strong>epgd</strong> <code>(Tue 28 Dec 2021 22:05)</code> - <em>Upvotes: 11</em></p><p>Remove special characters: Use this option to replace any non-alphanumeric special characters with the pipe | character.</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Sat 14 Jan 2023 23:53)</code> - <em>Upvotes: 8</em></p><p>I think this description changed:
Remove special characters: Use this option to remove any non-alphanumeric special characters.
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/preprocess-text</p></blockquote>
<blockquote><p><strong>ljljljlj</strong> <code>(Wed 11 Jan 2023 15:02)</code> - <em>Upvotes: 7</em></p><p>On exam 2021/7/10</p></blockquote>
<blockquote><p><strong>victorafb</strong> <code>(Mon 22 Apr 2024 15:11)</code> - <em>Upvotes: 6</em></p><p>Answer is corret, check on 
https://learn.microsoft.com/en-us/azure/machine-learning/component-reference/preprocess-text</p></blockquote>
<blockquote><p><strong>David_Tadeu</strong> <code>(Sat 30 Sep 2023 09:03)</code> - <em>Upvotes: 7</em></p><p>I see these definitions

5Jun2019 - *Remove special characters*: Use this option to replace any non-alphanumeric special characters with the pipe | character. (https://docs.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/preprocess-text)

11Apr2021 - *Remove special characters*: Use this option to remove any non-alphanumeric special characters. (https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/preprocess-text)

So for the second I&#x27;m going with *Remove Special Characters*, i.e. I think the answer is right as of March 2022.</p></blockquote>
<blockquote><p><strong>michaelmorar</strong> <code>(Sun 30 Jun 2024 12:21)</code> - <em>Upvotes: 1</em></p><p>Thank you for this explanation!</p></blockquote>
<blockquote><p><strong>Mrinals</strong> <code>(Mon 22 May 2023 23:17)</code> - <em>Upvotes: 1</em></p><p>Remove special characters: Use this option to replace any non-alphanumeric special characters with the pipe | character.
in link &quot;https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/preprocess-text&quot;</p></blockquote>
<blockquote><p><strong>trickerk</strong> <code>(Sat 07 Jan 2023 09:05)</code> - <em>Upvotes: 2</em></p><p>Split tokens on special characters just break words and won&#x27;t remove the pipe(|). 
According the page https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/preprocess-text:
Remove special characters: Use this option to remove any non-alphanumeric special characters.
So given answer is correct.</p></blockquote>
<blockquote><p><strong>azurecert2021</strong> <code>(Sun 25 Dec 2022 19:06)</code> - <em>Upvotes: 1</em></p><p>looks like question is for designers or misprint the requirement as Remove special characters can not be the choice for studio as already explained by others.</p></blockquote>
<blockquote><p><strong>YG59</strong> <code>(Fri 02 Dec 2022 01:20)</code> - <em>Upvotes: 5</em></p><p>It seems like that &#x27;Remove Special Characters&#x27; has different definition in designer and studio. 
1) Designer: Use this option to remove any non-alphanumeric special characters.
https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-module-reference/preprocess-text
2) Studio: Use this option to replace any non-alphanumeric special characters with the pipe | character.
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/preprocess-text</p></blockquote>
<blockquote><p><strong>lucazav</strong> <code>(Thu 14 Apr 2022 10:48)</code> - <em>Upvotes: 7</em></p><p>The suggested answer works if you are using Azure ML Studio Classic (infact the picture is related to the Preprocess Text module of the Classic one).
It doesn&#x27;t work on the new Azure ML Designer. In order to remove the pipe there, you have to:
  - enter the string &quot;(\|)&quot; into the &quot;Custom regular expression&quot; textbox
  - leave the &quot;Custom replacement string&quot; textbox empty</p></blockquote>
<blockquote><p><strong>Kamalraj</strong> <code>(Sat 05 Feb 2022 07:50)</code> - <em>Upvotes: 5</em></p><p>Remove special characters is correct,
https://docs.microsoft.com/en-us/azure/machine-learning/studio-module-reference/preprocess-text</p></blockquote>
<blockquote><p><strong>allanm</strong> <code>(Tue 15 Nov 2022 21:14)</code> - <em>Upvotes: 2</em></p><p>Incorrect, the requirement states to &quot;remove pipe characters from text&quot;. Remove special characters will introduce the pipe (|) charcater in your &quot;bag of words&quot; which is not what is asked.</p></blockquote>

</details>

---

[<< Previous Question](question_199.md) | [Home](/index.md) | [Next Question >>](question_201.md)
