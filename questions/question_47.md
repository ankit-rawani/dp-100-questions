# Question 47

You are developing a hands-on workshop to introduce Docker for Windows to attendees.

You need to ensure that workshop attendees can install Docker on their devices.

Which two prerequisite components should attendees install on the devices? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

* A.Microsoft Hardware-Assisted Virtualization Detection Tool
* B.Kitematic
* C.BIOS-enabled virtualization
* D.VirtualBox
* E.Windows 10 64-bit Professional

<details>
  <summary>Show Suggested Answer</summary>

  <strong>CE</strong><br>
<p>C: Make sure your Windows system supports Hardware Virtualization Technology and that virtualization is enabled.</p>
<p>Ensure that hardware virtualization support is turned on in the BIOS settings. For example:</p>
<img src="images/q47_ref_4_0005100001.jpg" alt="Reference Image"><br>
<p>E: To run Docker, your machine must have a 64-bit operating system running Windows 7 or higher.</p>
<p>Reference:</p>
<p>https://docs.docker.com/toolbox/toolbox_install_windows/</p>
<p>https://blogs.technet.microsoft.com/canitpro/2015/09/08/step-by-step-enabling-hyper-v-for-use-on-windows-10/</p>

</details>

<details>
  <summary>Show Discussions</summary>

<blockquote><p><strong>fredgu</strong> <code>(Mon 05 Jun 2023 08:17)</code> - <em>Upvotes: 13</em></p><p>Just took the DP-100 test today, Dec 5, 2020, and found that none of the questions or knowledge points from page 1 to page 26 have been tested or mentioned. Nearly 95% of the questions tested in the exam were about Azure Data Science Service. And you are suggested to type codes to get familiar with the new coding style instead of wasting time on researching ML Studio (Classic) here.</p></blockquote>
<blockquote><p><strong>Winny</strong> <code>(Sat 02 Dec 2023 11:53)</code> - <em>Upvotes: 6</em></p><p>I totally disagree with @fredgu. I took the test on the last week of May 2021 and most but not all questions were in the exam. I Used this as revision and I did well in the exam.</p></blockquote>
<blockquote><p><strong>woyaodp100</strong> <code>(Fri 20 Oct 2023 14:03)</code> - <em>Upvotes: 2</em></p><p>can you be more clear of what consists P1 to P26? Which questions are these?</p></blockquote>
<blockquote><p><strong>Wayne888</strong> <code>(Wed 29 May 2024 15:03)</code> - <em>Upvotes: 1</em></p><p>I did pass with excellent over 900 scores with help here. But expect questions outside here. I used this practice as style of the test. I should say questions some times similar but not exact.</p></blockquote>
<blockquote><p><strong>SamiMelke</strong> <code>(Thu 29 Jun 2023 05:54)</code> - <em>Upvotes: 4</em></p><p>Can you clarify? what do you mean by the new coding style or Azure Data Science Service.</p></blockquote>
<blockquote><p><strong>Edhotp</strong> <code>(Sun 16 Jul 2023 00:31)</code> - <em>Upvotes: 4</em></p><p>Same with @fredgu, mostly it use new azure learning studio (ml.azure.com)</p></blockquote>
<blockquote><p><strong>ning</strong> <code>(Mon 11 Nov 2024 12:18)</code> - <em>Upvotes: 2</em></p><p>Documentation mentioned two things: virtualization and 64 bits operation system; mapping to answers will be C / E</p></blockquote>
<blockquote><p><strong>austin06112000</strong> <code>(Thu 05 Sep 2024 01:24)</code> - <em>Upvotes: 2</em></p><p>Answer is right. by Mar 4,2022.</p></blockquote>
<blockquote><p><strong>leraS28</strong> <code>(Mon 22 Jul 2024 22:41)</code> - <em>Upvotes: 1</em></p><p>I think we need virtualization, because the Students use Windows Machine, and we need Linux for machine learning. In Docker you can only use the same operating system, that means that first we need to install a Linux VM and Docker on top. Otherwise we should not need virtualization</p></blockquote>
<blockquote><p><strong>leraS28</strong> <code>(Tue 23 Jul 2024 23:38)</code> - <em>Upvotes: 1</em></p><p>I found even better explanation here https://sloopstash.com/blog/can-docker-containers-run-on-any-operating-system.html</p></blockquote>
<blockquote><p><strong>Akki0120</strong> <code>(Thu 04 Jan 2024 17:06)</code> - <em>Upvotes: 1</em></p><p>If anyone wants all questions ping me 9403778084</p></blockquote>
<blockquote><p><strong>Sandhya_Soman</strong> <code>(Fri 21 Jun 2024 09:29)</code> - <em>Upvotes: 1</em></p><p>HI Akki, Please help me with the questions</p></blockquote>
<blockquote><p><strong>unonw</strong> <code>(Thu 07 Mar 2024 15:45)</code> - <em>Upvotes: 1</em></p><p>can you help me too?</p></blockquote>
<blockquote><p><strong>bikydrum</strong> <code>(Mon 19 Aug 2024 22:29)</code> - <em>Upvotes: 1</em></p><p>Need your help with questions.</p></blockquote>
<blockquote><p><strong>Akki0120</strong> <code>(Thu 04 Jan 2024 17:02)</code> - <em>Upvotes: 4</em></p><p>If anyone wants all questions ping me 9403778084</p></blockquote>
<blockquote><p><strong>shaimag</strong> <code>(Mon 12 Feb 2024 18:55)</code> - <em>Upvotes: 2</em></p><p>hi Akki , Can you help me with the Question Sets</p></blockquote>
<blockquote><p><strong>unonw</strong> <code>(Thu 07 Mar 2024 15:44)</code> - <em>Upvotes: 1</em></p><p>can you help me too?</p></blockquote>
<blockquote><p><strong>morojenie</strong> <code>(Thu 29 Feb 2024 09:58)</code> - <em>Upvotes: 1</em></p><p>can you help me too?</p></blockquote>
<blockquote><p><strong>abhijmk</strong> <code>(Mon 25 Dec 2023 05:35)</code> - <em>Upvotes: 2</em></p><p>C&amp;E are absolutely correct , for more details can refer here https://docs.docker.com/docker-for-windows/install-windows-home</p></blockquote>
<blockquote><p><strong>narendralv</strong> <code>(Sat 16 Dec 2023 18:04)</code> - <em>Upvotes: 4</em></p><p>C &amp; E are correct. Please follow the link for more information https://docs.docker.com/docker-for-windows/install/</p></blockquote>
<blockquote><p><strong>prashantjoge</strong> <code>(Mon 20 Nov 2023 19:07)</code> - <em>Upvotes: 1</em></p><p>azure databricks support clustering while azure data factory supports orchestration (https://docs.microsoft.com/en-us/azure/databricks/clusters/configure).  The orchestration here should be in the context of data processing (think SSIS, ETL, informatica etc.)  Answer should be B. Azure containers  instances provide some basic orchestration capabilities, but then again the context is different. https://docs.microsoft.com/en-us/azure/container-instances/container-instances-orchestrator-relationship</p></blockquote>
<blockquote><p><strong>dev2dev</strong> <code>(Sun 03 Sep 2023 05:17)</code> - <em>Upvotes: 2</em></p><p>I think its c and d. because the question is asking about the components. how OS is a component?</p></blockquote>
<blockquote><p><strong>levm39</strong> <code>(Sat 07 Oct 2023 11:22)</code> - <em>Upvotes: 1</em></p><p>VirtualBox is not required for Docker. C is correct, I would assume the OS is already installed, but anyway I think the answer is correct, just tricky</p></blockquote>
<blockquote><p><strong>foorx</strong> <code>(Wed 23 Nov 2022 13:58)</code> - <em>Upvotes: 4</em></p><p>Docker can now run on Win 10 Home with WSL2 now?</p></blockquote>
<blockquote><p><strong>Parzival</strong> <code>(Mon 13 Feb 2023 23:55)</code> - <em>Upvotes: 2</em></p><p>Yes,
https://docs.docker.com/docker-for-windows/install-windows-home/</p></blockquote>

</details>

---

[<< Previous Question](question_46.md) | [Home](/index.md) | [Next Question >>](question_48.md)
