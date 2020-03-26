# step 3 - summarize_data_by_class.py

import separate_by_class
import summarize_dataset

def summarize_by_class(dataset):
	separated = separate_by_class.separate_by_class(dataset)
	summaries = dict()
	for class_value, rows in separated.items():
		summaries[class_value] = summarize_dataset.summarize_dataset(rows)
	return summaries

if __name__ == '__main__':
	dataset = [[3.393533211,2.331273381,0],
	[3.110073483,1.781539638,0],
	[1.343808831,3.368360954,0],
	[3.582294042,4.67917911,0],
	[2.280362439,2.866990263,0],
	[7.423436942,4.696522875,1],
	[5.745051997,3.533989803,1],
	[9.172168622,2.511101045,1],
	[7.792783481,3.424088941,1],
	[7.939820817,0.791637231,1]]
	summary = summarize_by_class(dataset)
	for label in summary:
		print(label)
		for row in summary[label]:
			print(row)
