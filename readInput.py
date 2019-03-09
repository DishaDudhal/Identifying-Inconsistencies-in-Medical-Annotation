from myUMLS import get_CUI
import pprint
pp=pprint.PrettyPrinter(indent = 2)
import csv
def dict_sort(d):
    Sum=0
    for i in d.values():
        Sum+=len(i)
    return Sum

sentences=[]
annotations=[]
clusters={}

with open ('AnnotatedData.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter = "\t")
    count=0
    for row in reader:
        sentences.append([row[0],row[1]])
        annotations.append([count])
        for j in row[2:]:
            if(j==''):
                break;
            else:
                annotations[-1].append([])
                A=j.split('$')
                z=0
                key=""
                annot=""
                a=[]
                while(z<len(A)):
                    if(A[z+1].lower()!="measurement_value"):
                        key+=A[z]+" "
                    annotations[-1][-1].append([A[z],A[z+1]])
                    annot+="["+A[z]+"]"+A[z+1]+" "
                    a.append([A[z],A[z+1]])
                    z+=2
                #pp.pprint(a)
                annot=annot[:-1]
                key=key[:-1].lower()
                cui,term=get_CUI(key,a)
                term=term.lower()
                try:
                	myFlag=True
                	for x in range(len(clusters[cui][term])):
                		if(clusters[cui][term][x][0].lower() == annot.lower()):
                			if(count not in clusters[cui][term][x][1]):
                				clusters[cui][term][x][1].append(count)
                			myFlag=False
                			break;
                	if(myFlag):
                		clusters[cui][term].append([annot,[count]])
                except:
                	try:
                		clusters[cui][term]=[[annot,[count]]]
                	except:
                		clusters[cui]={}
                		clusters[cui][term]=[[annot,[count]]]              
        count+=1
        if(count>1000):
            break
clusters.pop('No_CUIs')
sorting = sorted(clusters, key =lambda k: dict_sort(clusters[k]), reverse=True)
pp.pprint(clusters)

