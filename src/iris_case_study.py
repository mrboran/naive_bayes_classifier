# step 6 - iris_case_study.py

from csv import reader
from random import seed
from random import randrange

import class_probabilities
import summarize_data_by_class

def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup

def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for _ in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

def accuracy_matric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

def evaluate_algorithm(dataset, algorithm, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = algorithm(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_matric(actual, predicted)
		scores.append(accuracy)
	return scores

def predict(summaries, row):
	probabilities = class_probabilities.calculate_class_probabilities(summaries, row)
	# best_pro = -1
	# for c, p in probabilities.items():
	# 	if p > best_pro:
	# 		best_pro = p
	# print(best_pro)
	best_label, best_prob = None, -1
	for class_value, probability in probabilities.items():
		if best_label is None or probability > best_prob:
			best_prob = probability
			best_label = class_value
	return best_label

def naive_bayes(train, test):
	summarize = summarize_data_by_class.summarize_by_class(train)
	predictions = list()
	for row in test:
		output = predict(summarize, row)
		predictions.append(output)
	return predictions


def test(dataset):
	# test
	seed(1)
	for i in range(len(dataset[0]) - 1):
		str_column_to_float(dataset, i)

	str_column_to_int(dataset, len(dataset[0])-1)

	n_folds = 5

	scores = evaluate_algorithm(dataset, naive_bayes, n_folds)
	print('Score: %s' % scores)
	print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

def run(dataset):
	for i in range(len(dataset[0]) - 1):
		str_column_to_float(dataset, i)
	str_column_to_int(dataset, len(dataset[0])-1)
	
	model = summarize_data_by_class.summarize_by_class(dataset)
	
	row = [5.7, 2.9, 4.2, 1.3]
	
	label = predict(model, row)
	
	print('Data=%s, Predicted: %s' % (row, label))

if __name__ == '__main__':
	filename = '../data/iris.csv'
	dataset = load_csv(filename)
	# test(dataset)
	run(dataset)
