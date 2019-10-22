Inconsistency in Medical Annotations
===

Project Source Code can be downloaded from the github repository ykaran86/SIH19_ezDI
---

Author
---

1) Yogesh Karan
email:-ykaran86@gmail.com
2) Disha Dudhal
email:- dishadudhal@gmail.com
3) Devasish Mahato
email:-t7.devasishmahato@gmail.com
4) Dhanashree Revagade:-
email:-dhanashree.revagade@gmail.com
5) Shivam Dev Singh
6) Aravind Unnikrishnan

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
Front Page of the Web App
---
![img1](img1.png)

On Uploading a .tsv file
---
Uploading will take time as in this step preprocessing and clustering is done!

![img2](img2.png)

Home Page of the Web App
---
![img3](img3.png)

Search Page
---
![img4](img4.png)

On searching a word
---
Here, sentences containing blood are displayed

![img5](img5.png)

On searching a tag
---
Here, sentences with problematic temrs are displayed

![img6](img6.png)

On searching a part of a word
---
Even on searching a part of a word, sentences are displayed

![img7](img7.png)

The Clusters with Unique Annotation Patterns
---
![img8](img8.png)

On clicking a pattern sentences containing that annotation pattern are displayed
---
![img9](img9.png)

Inconsistency vs Consistency
---
![img10](img10.png)

Inconsistency in Single Word Entities vs Multi Word Entities
---
![img11](img11.png)

Few Words to Visitors
---

This Application is in its development phase and its obvious to get erroneous cluster patterns in some cases. A lot of improvement is needed.
Pull requests for any such changes are accepted. Feel free to fork this project and make your own changes too.

Thank you for Visiting!
