from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv
from myUMLS import get_CUI
from sty import bg,rs
import re
import xlsxwriter
import xlrd, csv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import matplotlib

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

def dict_sort(d):
	Sum=0
	for i in d.values():
		Sum+=len(i)
	return Sum

def csv_from_excel(filename):
	wb = xlrd.open_workbook(filename)
	sh = wb.sheet_by_name('Sheet1')
	your_csv_file = open('CalmDownItsJustGenjutsu_RG1_Evaluation_2.tsv', 'w')
	wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL, delimiter="\t")
	for rownum in range(sh.nrows):
		wr.writerow(sh.row_values(rownum))
	your_csv_file.close()
	
sentences=[]
annotations=[]
clusters={}
sorting=[]


def home(request):
	return render(request, 'home.html', {})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['dataset']:
        myfile = request.FILES['dataset']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'home.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'home.html')

def upload_csv(request):
	
	Total_Annotations=0
	Inconsistent_Annotations=0
	single=0
	MWE=0
	single_incons=0
	MWE_incons=0
	csv_file = request.FILES["csv_file"]
	file_data = csv_file.read().decode("utf-8")
	lines=file_data.split('\n')
	count=0
	for t in lines:
		row=t.split('\t')
		if(len(row)<2):
			continue
		sentences.append([row[0],row[1]])
		annotations.append([count])
		for j in row[2:]:
			if(j==''):
				break;
			else:
				Total_Annotations+=1
				annotations[-1].append([])
				A=j.split('$')
				if(len(A)<=2):
					single+=1
				else:
					MWE+=1
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
				annot=annot[:-1]
				key=key[:-1].lower()
				cui,term=get_CUI(key,a)
				term=term.lower()
				completeFlag=True
				myTag=''
				for alpha in a:
					if(stringSearch(alpha[0],term)):
						myTag=alpha[1]
						annot="["+term+"]"+myTag
						break;

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
						Inconsistent_Annotations+=1
						if(len(a)==1):
							single_incons+=1
						else:
							MWE_incons+=1
				except:
					try:
						clusters[cui][term]=[[annot,[count]]]
					except:
						clusters[cui]={}
						clusters[cui][term]=[[annot,[count]]]
		count+=1
		if(count>9500):
			break;
	clusters.pop('No_CUIs')

	x=sorted(clusters, key =lambda k: dict_sort(clusters[k]), reverse=True)
	workbook = xlsxwriter.Workbook('File13.xlsx')
	worksheet = workbook.add_worksheet()
	dictionary = clusters
	row = 0
	col = 0
	worksheet.write(row,col,"Group Name")
	for cui,clusterr in dictionary.items():
		row += 1
		col = 0
		worksheet.write(row, col, next(iter(clusterr)))
		for cluster_name,instances in clusterr.items():
			for instance in instances:
				s = instance[0]+"_SentList_["
				s += ','.join(map(str,instance[1]))
				s += "]"
				col += 1
				worksheet.write(row, col, s)
	workbook.close()
	csv_from_excel("File13.xlsx")
	#print('nilu',x)
	sorting.append(x)
	#print("gilu",sorting[0])
	#print(clusters)
	Measures=[Inconsistent_Annotations,Total_Annotations-Inconsistent_Annotations]
	Labels=['Inconsistency','Consistency']
	Colors=['gold','lightskyblue']
	explode=(0.1,0)
	plt.pie(Measures, explode=explode, labels=Labels, colors=Colors,
	autopct='%1.2f%%', shadow=True, startangle=140)
	plt.title('Inconsistency vs Consistency')
	plt.axis('equal')
	plt.savefig('index/static/Images/pie1.png')
	plt.close()
	Inconsistency=(Inconsistent_Annotations/Total_Annotations)*100
	Inconsistency=round(Inconsistency,2)
	Measures=[single_incons,single-single_incons]
	Labels=['Inconsistency','Consistency']
	Colors=['orange','lawngreen']
	explode=(0.1,0)
	plt.pie(Measures, explode=explode, labels=Labels, colors=Colors,
	autopct='%1.2f%%', shadow=True, startangle=140)
	plt.title('Inconsistency in Single Word Entities')
	plt.axis('equal')
	plt.savefig('index/static/Images/pie2.png')
	plt.close()
	Measures=[MWE_incons,MWE-MWE_incons]
	Labels=['Inconsistency','Consistency']
	Colors=['yellow','tomato']
	explode=(0.1,0)
	plt.pie(Measures, explode=explode, labels=Labels, colors=Colors,
	autopct='%1.2f%%', shadow=True, startangle=140)
	plt.title('Inconsistency in Multi-Word Entities')
	plt.axis('equal')
	plt.savefig('index/static/Images/pie3.png')
	plt.close()
	single_INCON=(single_incons/single)*100
	single_INCON=round(single_INCON,2)
	MWE_INCON=(MWE_incons/MWE)*100
	MWE_INCON=round(MWE_INCON,2)
	single_contrib=(single_incons/Inconsistent_Annotations)*100
	single_contrib=round(single_contrib,2)
	MWE_contrib=(MWE_incons/Inconsistent_Annotations)*100
	MWE_contrib=round(MWE_contrib,2)
	'''
	Measures=[]
	Labels=[]
	for i in range(5):
		Labels.append(list(clusters[sorting[i]].keys())[0])
		Sum=0
		for i in list(clusters[sorting[i]].values()):
			Sum+=len(i)
		print(Sum)
		Measures.append(Sum-1)
	Labels.append("Others")
	print(Inconsistent_Annotations)
	others=Inconsistent_Annotations-sum(Measures)
	print(others)
	Measures.append(others)
	Colors=['gold','lightskyblue','orange','lawngreen','yellow','tomato']
	explode=(0.1,0,0,0,0,0)
	plt.pie(Measures, explode=explode, colors=Colors,
	autopct='%1.2f%%', shadow=True, startangle=140)
	plt.title('Top 5 Inconsistent Clusters').set_ha("left")
	plt.gca().axis('equal')
	plt.legend(Labels,bbox_to_anchor=(1,0.5),bbox_transform=plt.gcf().transFigure, loc="best")
	plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
	plt.tight_layout()
	plt.savefig('index/static/Images/pie4.png', bbox_inches="tight")
	plt.close()'''
	Vals=[Inconsistency,single_contrib,MWE_contrib,single_contrib,single_INCON,MWE_INCON]
	return render(request, "select.html", {'clusters':clusters,'sorting':sorting[0],'sentences':sentences,'Vals':Vals})
	
def back(request):
	return render(request, "select.html", {'clusters':clusters,'sorting':sorting[0],'sentences':sentences,'lines':[],'count':0} )

def view_clusters(request):
	#print("pintu",sorting)
	#print("lintu",clusters)
	return render(request, "Inconsistencies.html", {'clusters':clusters,'sorting':sorting[0],'sentences':sentences})

def Search(request):
	return render(request, "search.html", {'clusters':clusters,'sorting':sorting[0],'sentences':sentences,'lines':[],'count':0} )

def search_by_word(request):
	lines=[]
	if request.method=='POST':
		string_search=request.POST['search']
		with open ('AnnotatedData.tsv') as tsvfile:
			reader = csv.reader(tsvfile, delimiter = "\t")
			count=0
			for row in reader:
				linestr1 = " ".join(row[1:2])
				obj = re.search(string_search, linestr1, re.IGNORECASE)	
				if (obj):
					new = re.compile(re.escape(string_search), re.IGNORECASE)
					k=new.sub("<mark>"+obj.group()+"</mark>", linestr1)
					print(k)
					count+=1
					lines.append(k)
	return render(request, "search.html", {'clusters':clusters,'sorting':sorting[0],'sentences':sentences,'lines':lines,'count':count} )

def search_by_annot(request):
	lines=[]
	if request.method=='POST':
		search_term=request.POST['search']
		cate = search_term.lower()
		with open ('AnnotatedData.tsv') as tsvfile:
			reader = csv.reader(tsvfile, delimiter = "\t")
			count =0
			for row in reader:
				linestr2 = "$".join(row[2:])
				new_list = linestr2.split("$")
				for i in range(len(new_list)):
					if ((new_list[i]).lower() == cate):
						print(new_list[i-1],end="\t")
						print(row[1])
						lines.append("<mark>"+new_list[i-1]+"</mark>"+"<br>"+row[1])
						print("\n\n")
						count += 1
			print("count : ",count	)
	return render(request, "search.html", {'clusters':clusters,'sorting':sorting[0],'sentences':sentences,'lines':lines,'count':count})
