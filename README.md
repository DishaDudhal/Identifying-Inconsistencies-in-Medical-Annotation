Inconsistency in Medical Annotations
===

Project Source Code can be downloaded from the github repository ykaran86/SIH19_ezDI
---

Author
---

Yogesh Karan

email:-ykaran86@gmail.com

Supervisor
---
Yesoda Bhargava

https://yesodabhargava.com/

Contributors
---

Dhanashree Revagade

Shivam Dev Singh

Aravind Unnikrishnan

Devasish Mahato

Disha Dudhal

**created and tested on Ubuntu 18.04 with Python 3.6**

An Attempt(which finally led us to the victory) to provide a solution to the company **ezDI** in the complicated type problem statement **Identify Inconsistency in Medical Annotations** in the **Smart India Hackathon(Software Edition) 2019**. This is a Web App developed in Django which displays the clusters of semantically similar medical terms having inconsistencies in Annotations. This project is based on strict dictionary lookup based approach.
Technologies used in this project:
	
	1. Django (Web Framework)
	2. QuickUMLS python module for looking into the UMLS
	3. UMLS for providing medical insights
	    (https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html)
**Input to the application:-** .tsv file containing sentences and their annotations

**Output of the application:-** .tsv file containing medical groups with their annotation patterns (apart from the web App)

Features provided in the Web App:

	1. Clusters with unique annotation patterns are displayed 
      (in order such that clusters with maximum inconsistency are shown first)
	2. On Clicking a particular pattern of a cluster,  sentences containing that pattern are shown.
	3. Search operations are also enabled so that one can search for occurence of 
        a particular word in the provided dataset or a particular annotation tag
	4. Statistical Insights are also provided which displays the proportion of inconsistency 
        in the data or contribution of multi-word entities vs single word entities in the inconsistencies