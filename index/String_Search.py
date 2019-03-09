def stringSearch(Main_S,My_S):
	L=len(My_S)
	flag=True
	j=0
	bj=0
	for i in Main_S:
	    if(j>=L):
	        flag=True
	        break;
	    if(i==My_S[j]):
	        if(i==" "):
	            j+=1
	            bj=j
	        else:
	            j+=1
	    else:
	        j=bj
	if(j<L):
	    flag=False
	if(flag):
	    return True
	else:
	    return False
