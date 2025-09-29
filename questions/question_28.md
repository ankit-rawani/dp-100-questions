# Question 28

You have been tasked with ascertaining if two sets of data differ considerably. You will make use of Azure Machine Learning Studio to complete your task.

You plan to perform a paired t-test.

Which of the following are conditions that must apply to use a paired t-test? (Choose all that apply.)

* A.All scores are independent from each other.
* B.You have a matched pairs of scores.
* C.The sampling distribution of d is normal.
* D.The sampling distribution of x1- x2 is normal.

<details>
  <summary>Show Suggested Answer</summary>

  <strong>BC</strong><br>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>lookaaaa</strong> <code>(Thu 23 Nov 2023 20:59)</code> - <em>Upvotes: 9</em></p><p>A is for single sample t-test, D is for unpaired t-test, BC are for paired t-test</p></blockquote>
<blockquote><p><strong>jdada</strong> <code>(Sun 10 Nov 2024 16:00)</code> - <em>Upvotes: 6</em></p><p>B. You have a matched pairs of scores.
C. The sampling distribution of d is normal.
D. The sampling distribution of x1- x2 is normal.</p></blockquote>
<blockquote><p><strong>amittal09</strong> <code>(Fri 16 May 2025 06:19)</code> - <em>Upvotes: 1</em></p><p>https://learn.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/test-hypothesis-using-t-test#bkmk_HowToChoose</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Sun 07 Jul 2024 20:07)</code> - <em>Upvotes: 1</em></p><p>C and D refer to the same thing</p></blockquote>
<blockquote><p><strong>Ram19830916</strong> <code>(Thu 30 May 2024 13:28)</code> - <em>Upvotes: 1</em></p><p>A&lt;B&lt;C 

Choose a paired t-test when these conditions apply:

You have a matched pairs of scores. For example, you might have two different measures per person, or matched pairs of individuals (such as a husband and wife).

Each pair of scores is independent of every other pair.

The sampling distribution of d is normal.</p></blockquote>
<blockquote><p><strong>MarinaMijailovic</strong> <code>(Wed 21 Feb 2024 13:16)</code> - <em>Upvotes: 3</em></p><p>Can someone explain what is d and what is x1-x2</p></blockquote>
<blockquote><p><strong>WinnieS</strong> <code>(Thu 01 Feb 2024 10:51)</code> - <em>Upvotes: 2</em></p><p>B and C are correct.

A should change to EACH PAIR of scores is independent of other pairs, not ALL scores.
D should change to C</p></blockquote>
<blockquote><p><strong>meysa</strong> <code>(Wed 10 Jan 2024 23:48)</code> - <em>Upvotes: 2</em></p><p>B and D are correct.</p></blockquote>
<blockquote><p><strong>KIshor1212</strong> <code>(Wed 29 Nov 2023 14:23)</code> - <em>Upvotes: 4</em></p><p>Choose a paired t-test when these conditions apply:

***---You have a matched pairs of scores. For example, you might have two different measures per person, or matched pairs of individuals (such as a husband and wife).
Each pair of scores is independent of every other pair.
*** --The sampling distribution of d is normal.</p></blockquote>
<blockquote><p><strong>slcheng</strong> <code>(Fri 27 Oct 2023 06:52)</code> - <em>Upvotes: 1</em></p><p>Choose a paired t-test when these conditions apply:
You have a matched pairs of scores. For example, you might have two different measures per person, or matched pairs of individuals (such as a husband and wife).
Each pair of scores is independent of every other pair.
The sampling distribution of d is normal.</p></blockquote>
<blockquote><p><strong>JTWang</strong> <code>(Wed 11 Oct 2023 06:09)</code> - <em>Upvotes: 2</em></p><p>BC is the correct answer.</p></blockquote>
<blockquote><p><strong>Vuuma</strong> <code>(Sun 10 Sep 2023 05:33)</code> - <em>Upvotes: 2</em></p><p>Choose a paired t-test when these conditions apply:
1. You have a matched pairs of scores. For example, you might have two different measures per person, or matched pairs of individuals (such as a husband and wife).
2. Each pair of scores is independent of every other pair.
3.The sampling distribution of d is normal.</p></blockquote>
<blockquote><p><strong>Vuuma</strong> <code>(Sun 10 Sep 2023 05:32)</code> - <em>Upvotes: 1</em></p><p>Correct answer is BC</p></blockquote>
<blockquote><p><strong>Chimman</strong> <code>(Fri 03 Mar 2023 16:33)</code> - <em>Upvotes: 4</em></p><p>Clearly mentioned that it should be ABC as per the documentation.
https://docs.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/test-hypothesis-using-t-test</p></blockquote>
<blockquote><p><strong>TheCyanideLancer</strong> <code>(Thu 26 Jan 2023 05:33)</code> - <em>Upvotes: 4</em></p><p>As per MS documentation ans is ABC

https://docs.microsoft.com/en-us/previous-versions/azure/machine-learning/studio-module-reference/test-hypothesis-using-t-test</p></blockquote>
<blockquote><p><strong>Tsardoz</strong> <code>(Mon 16 Jan 2023 10:23)</code> - <em>Upvotes: 2</em></p><p>Answer should be ABD not sure why it just chose AB</p></blockquote>
<blockquote><p><strong>Tsardoz</strong> <code>(Mon 16 Jan 2023 10:22)</code> - <em>Upvotes: 1</em></p><p>Leaving out c because &#x27;d&#x27; is not defined.
https://www.jmp.com/en_au/statistics-knowledge-portal/t-test/paired-t-test.html#:~:text=Paired%20t%2Dtest%20assumptions&amp;text=Subjects%20must%20be%20independent.,obtained%20from%20the%20same%20subject.&amp;text=The%20measured%20differences%20are%20normally%20distributed.</p></blockquote>

</details>

---

[<< Previous Question](question_27.md) | [Home](/index.md) | [Next Question >>](question_29.md)
