import csv
from sty import bg, rs
string_search=input("Enter a word to search : ")
string_search_lower = string_search.lower()
with open ('AnnotatedData.tsv') as tsvfile:
	reader = csv.reader(tsvfile, delimiter = "\t")
	for row in reader:
		linestr1 = " ".join(row[1:2])
		linestr1_lower=linestr1.lower()
		linestr2 = " ".join(row[2:])
		linestr2_lower=linestr2.lower()
		if string_search_lower in linestr1_lower:
			new =linestr1.replace(string_search,bg.yellow+string_search+bg.rs)
			new =new.replace(string_search_lower,bg.yellow+string_search_lower+bg.rs)
			print(new)
		if string_search_lower in linestr2_lower:
			new2 =linestr2.replace(string_search,bg.yellow+string_search+bg.rs)
			new2 =new2.replace(string_search_lower,bg.yellow+string_search_lower+bg.rs)
			print(new2+"\n\n\n\n")

