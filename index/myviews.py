from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import matplotlib
from clustering import clusters
from clustering import lines
from clustering import contents
from clustering import Total_Annotations, Inconsistent_Annotations
from clustering import single,MWE,single_incons,MWE_incons
from clustering import sorting

#register = template.Library()

# Create your views here.
def home(request):
	'''
        figures = {'a' :[1, 2], 'b' :[1, 3, 5], 'c' :[2, 4, 6, 7],'d':[8,9,10],'e':[20,30,40,50]}
	print(type(figures))
	labels = figures.keys()
	freq =[]
	for item in labels:
		freq.append(len(figures[item]))
	index = np.arange(len(labels))
	plt.bar(index, freq)
	plt.xlabel('Cluster', fontsize=10)
	plt.ylabel('Inconsistency', fontsize=10)
	plt.xticks(index, labels, fontsize=10, rotation=30)
	plt.title('Inconsistencies')
	plt.savefig('index/static/bar.png')
	plt.close()
	pie_chart(labels, freq, index)
	'''
	print(Total_Annotations, Inconsistent_Annotations)
	print(single,MWE,single_incons,MWE_incons)
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
	plt.close()
	Vals=[Inconsistency,single_contrib,MWE_contrib,single_contrib,single_INCON,MWE_INCON]
	return render(request, 'home.php', {'clusters': clusters,'sorting':sorting, 'lines': lines,'sentences': contents,'Vals':Vals})

def pie_chart(labels, freq, index):
	plt.pie(freq, labels=labels,
	autopct='%1.2f%%', shadow=True, startangle=140)
	plt.title('Inconsistencies')
	plt.axis('equal')
	plt.savefig('index/static/pie.png')
	plt.close()
	return
