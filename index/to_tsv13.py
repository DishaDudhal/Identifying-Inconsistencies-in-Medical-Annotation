import xlsxwriter
import xlrd, csv
#from clustering import clusters
from views import clusters
#from my_pro import sentences

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


def csv_from_excel(filename):
		wb = xlrd.open_workbook(filename)
		sh = wb.sheet_by_name('Sheet1')
		your_csv_file = open('CalmDownItsJustGenjutsu_RG1_Evaluation_2.tsv', 'w')
		wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL, delimiter="\t")

		for rownum in range(sh.nrows):
				wr.writerow(sh.row_values(rownum))

		your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel("File13.xlsx")
