from cosine_similarity import cosine
import os
from medical import Abbreviation
from StopWords_list import StopList
import sys
sys.path.append('..')
from full2018AB.QuickUMLS.quickumls import QuickUMLS

priority={'problem':1,'finding':2,'procedure':3,'anatomical_structure':4,'body_function':5,'lab_data':6,'laboratory_data':6,'body_measurement':7,'measurement_value':8,'medical_device':9,'medicine':10,'modifier':11}

matcher = QuickUMLS('/home/dhanashree/Genjitsu/QuickUMLS/install')

def remove_stopwords(t):
    t=list(t.split())
    text=""
    for i in t:
        if(i not in StopList):
            text+=i+" "
    text=text[:-1]
    return text


def the_CUI(Term,Annot):
    Term=Term[0].upper()+Term[1:]
    #print(Term)
    out = matcher.match(Term, best_match = True, ignore_syntax = False)
    #print(out)
    if(len(out)):
        CUI=""
        max_sim=0
        terms=[]
        for i in range(len(out)):
            for j in range(len(out[i])):
                Term_from_umls=out[i][j]['term'].lower()
                #print(Term_from_umls)
                sim=cosine(Term.lower(),Term_from_umls)
                if(sim==1.0):
                    return [out[i][j]['cui'],out[i][j]['term']]
                else:
                    if(sim>max_sim):
                        CUI=out[i][j]['cui']
                        myTerm=out[i][j]['term']
                        #print("chintu",CUI,myTerm)
                        max_sim=sim
                        terms=[]
                        #terms.append([Term_from_umls,CUI])
                        for k in Annot:
                            if(Term_from_umls.lower()==k[0].lower()):
                                terms.append(priority[k[1].lower()])
                                break;
                        #print(terms)

                    elif(sim==max_sim):
                        for k in Annot:
                            mod=0
                            if(Term_from_umls.lower()==k[0].lower()):
                                mod=priority[k[1].lower()]
                                if(terms!=[]):
                                    if(mod<terms[0]):
                                        terms[0]=mod
                                        myTerm=Term_from_umls
                                        CUI=out[i][j]['cui']
                                        #print(CUI,myTerm)
                                break;
                            #terms.insert(mod-20,[Term_from_umls,out[i][j]['cui']])
                        #myTerm=terms[0][0]
                        #CUI=terms[0][1]
        if(CUI==""):
            CUI=out[0][0]['cui']
            myTerm=out[0][0]['term']
        return [CUI,myTerm]
    else:
        return ["No_CUIs",Term]

def get_CUI(Term,Annot):
    if(len(Term.split())>1):
        Term1=remove_stopwords(Term)
        key=Term1[0].upper()
        Abb=""
        if(key.isalpha()):
            for i in Abbreviation[key]:
                j=list(i.keys())[0]
                term2=i[j].lower()
                if(cosine(Term1,term2)==1.0 and cosine(remove_stopwords(term2),Term1)==1.0):
                    Abb=j.lower()
                    break;
            if(Abb!=""):
                CUI,myTerm=the_CUI(Abb,Annot)
                if(CUI=="No_CUIs"):
                    CUI,myTerm=the_CUI(term2,Annot)
            else:
                CUI,myTerm=the_CUI(Term,Annot)
        else:
            CUI,myTerm=the_CUI(Term,Annot)
    else:
        key=Term[0].upper()
        Abb=""
        term=""
        if(key.isalpha()):
            for i in Abbreviation[key]:
                j=list(i.keys())[0]
                if(Term==j.lower()):
                    Abb=j.lower()
                    term=i[j].lower()
                    break;
            if(Abb!=""):
                CUI,myTerm=the_CUI(Abb,Annot)
                if(CUI=="No_CUIs"):
                    CUI,myTerm=the_CUI(term,Annot)
            else:
                CUI,myTerm=the_CUI(Term,Annot)
        else:
            CUI,myTerm=the_CUI(Term,Annot)
    return [CUI,myTerm]
            
