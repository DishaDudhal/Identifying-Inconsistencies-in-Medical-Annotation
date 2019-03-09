
# coding: utf-8

# In[1]:


import os
import pprint
import re
from nltk import sent_tokenize
from datetime import datetime
import csv
import functools
import itertools
import sys
sys.path.append('..')
from full2018AB.QuickUMLS.quickumls import QuickUMLS


pp = pprint.PrettyPrinter(indent = 2)
Qmatcher = QuickUMLS('/home/dhanashree/Genjitsu/QuickUMLS/install')


# In[2]:


def MWEmatch(word, annotation):
    pattern = {}
    pattern.update({word : annotation})
    return pattern


# In[3]:


def ignore_annotation (ignore, word, annotation):
    try:
        annotation.pop(word.index(ignore))
        word.remove(ignore)
        return word, annotation
    except ValueError:
        ignore_list = ignore.split()
        for ignore in ignore_list:
            try:
                annotation.pop(word.index(ignore))
                word.remove(ignore)
            except ValueError:
                continue
        else:
            return word, annotation


# In[4]:


def inconsistency(file_name):
    with open (file_name + '.tsv') as tsvfile:

        reader = csv.reader(tsvfile, delimiter = "\t")
        Coun=0
        for row in reader:
            id = row[0]
            print(id)
            if row[2: ] != ['']:
                text = list(map(lambda ele: ele.split("$"), row[2:]))
                for i in text:
                    words = i[0: :2]
                    annotations = list(map(lambda x: x.upper(), i[1: :2]))
                    MWE = ' '.join(words)
                    out = Qmatcher.match(MWE, best_match = True, ignore_syntax = False)
                    try:
                        concept = out.pop(0)
                        ngram = concept[0]['ngram']
                        ignore_list = list(map(lambda element: element.strip(), MWE.split(ngram)))
                        list(map(ignore_list.remove, ['']*ignore_list.count('')))
                        list(map(functools.partial(ignore_annotation, word = words, annotation = annotations), ignore_list))
                        annot = '#'.join(annotations)
                        if(concept[0]['cui'] in clusters and clustersLookup):
                            clusters[concept[0]['cui']].add(annot)
                            clustersLookup[concept[0]['cui']].append([list(map(functools.partial(MWEmatch), words, annotations)), id])
                        else:
                            clusters.update({concept[0]['cui'] : {annot}})
                            clustersLookup.update({concept[0]['cui'] : [[list(map(functools.partial(MWEmatch), words, annotations)), id]]})
                    except IndexError:
                        continue
            Coun+=1
            if(Coun>500):
                break;


# In[5]:


clusters = {}
clustersLookup = {}
start = datetime.now()
inconsistency("AnnotatedData")
inCUIs = []
for cui, l1 in clusters.items():
    if len(l1) > 1:
        inCUIs.append(cui)
print("\nTime: ", datetime.now() - start)


# In[6]:


for i in inCUIs:
    print(i + "\t")
    print("chintu")
    pp.pprint(clustersLookup[i])


# In[7]:


print(len(clusters))


# In[8]:


print(len(inCUIs))

