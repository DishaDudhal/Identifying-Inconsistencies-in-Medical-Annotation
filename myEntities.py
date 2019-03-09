from cosine_similarity import cosine
from medical import Abbreviation
from StopWords_list import StopList
from myUMLS import remove_stopwords

def check_Abb(Term):
    key=Term[0].upper()
    Abb=""
    if(key.isalpha()==False):
        return False
    for i in Abbreviation[key]:
        j=list(i.keys())[0]
        term2=i[j].lower()
        if(cosine(Term,term2)==1.0 and cosine(remove_stopwords(term2),Term)==1.0):
            return True
    return False

def break_terms(A):
    res=[]
    and_flag=False
    anti_flag=False
    temp=[]
    nextTemp=[]
    for i in range(len(A)):
        if(A[i][0].lower()=='and'):
            res.append(temp)
            temp=[]
        else:
            if(A[i][0].lower() in StopList):
                temp.insert(0,'!')
            temp.append(A[i])
    if(temp!=[]):
        res.append(temp)
        temp=[]
    And_List=[]
    RES=[]
    i=0
    while(i<len(res)-1):
        if(res[i][0]!='!'):
            if(res[i+1][0]!='!'):
                And_List.append([res[i],res[i+1]])
            else:
                RES.append(res[i])
        else:
            RES.append(res[i])
        i+=1
    if(res[i][0]=='!'):
        RES.append(res[i])
    else:
        if(i==0):
            RES.append(res[i])
        else:
            if(res[i-1][0]=='!'):
                RES.append(res[i])
    Final=[]
    for i in range(len(And_List)):
        term=""
        temp=[]
        for j in range(len(And_List[i])):
            for k in range(len(And_List[i][j])):
                term+=And_List[i][j][k][0]+" "
        term=term[:-1]
        if(check_Abb(term.lower())):
            temp.extend(And_List[i][0])
            temp.append(['and','#'])
            temp.extend(And_List[i][1])
            Final.append(temp)
        else:
            Final.append(And_List[i][0])
            Final.append(And_List[i][1])
    for i in range(len(RES)):
        if(RES[i][0]=='!'):
            RES[i].pop(0)
        Final.append(RES[i])
    return(Final)
