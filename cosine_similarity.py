'''
import re, math
from collections import Counter
WORD = re.compile(r'\w+')

def get_cosine(v1, v2):
        intersection = set(v1.keys()) & set(v2.keys())
        dot_prod_numerator=0
        for x in intersection:
            dot_prod_numerator=dot_prod_numerator+(v1[x]* v2[x])
            
        norm1=0
        for x in v1.keys():
            norm1=norm1+(v1[x])*(v1[x])

        norm2=0
        for x in v2.keys():
            norm2=norm2+(v2[x])*(v2[x])
            
        numerator=dot_prod_numerator
        denominator=math.sqrt(norm1*norm2)
    
        if not denominator:
            return 0.0
        else:
            return float(numerator)/denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def cosine(text1,text2):
        vec1=text_to_vector(text1)
        vec2=text_to_vector(text2)
        return(get_cosine(vec1,vec2))
'''
def cosine(a,b):
    set1=set(a.split())
    set2=set(b.split())
    diff_LR=list(set1-set2)
    diff_RL=list(set2-set1)
    similar_score=(len(set1)-len(diff_LR))/len(set1)
    return(similar_score)



