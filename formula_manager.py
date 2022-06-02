from itertools import product

def make_big_var(size, cur_var_number):
	var = [i for i in range(cur_var_number, cur_var_number + size)]
	cur_var_number += size
	return var, cur_var_number

def make_var(cur_var_number):
	var = cur_var_number
	cur_var_number += 1
	return var, cur_var_number

def clean_clauses(clauses: [[int]]):
	print(clauses)
	answer_clauses = []
	for i in range(len(clauses)):
		clause_1 = clauses[i]
		fl = False
		for j in range(len(clauses)):
			if i == j:
				continue
			clause_2 = clauses[j]
			if all(x in clause_1 for x in clause_2):
				fl = True
				break
		if fl == False:
			answer_clauses.append(clause_1)
	return answer_clauses

def add_clauses(destination: [[int]], source: [[int]]):
	# destination = destination[:-1] + '&' + source + ')'
	for clause in source:
		destination.append(clause)


def convert_to_cnf(list_of_cnfs: [[int]]):
	all_clauses = []
	straight_product = product(*list_of_cnfs)
	for big_item in straight_product:
		big_item = list(big_item)
		clause = []
		for low_item in big_item:
			if type(low_item) is int:
				low_item = [low_item]
			clause = clause + low_item
		clause = list(set(clause))
		end_clause = list(set(map(lambda x : abs(x), clause)))
		if len(end_clause) == len(clause):
			all_clauses.append(sorted(clause))
	
	answer_clauses = []
	for i in range(len(all_clauses)):
		clause_1 = all_clauses[i]
		fl = False
		for j in range(len(all_clauses)):
			if i == j:
				continue
			clause_2 = all_clauses[j]
			if all(x in clause_2 for x in clause_1):
				fl = True
				break
		if fl == False:
			answer_clauses.append(clause_1)
	return answer_clauses
	# print(all_clauses)
	return all_clauses
	# exit(0)
	# print(list(clauses))
	# exit(0)
	# for clause in clauses:
	# 	print(clause)
	# return clauses
	return all_clauses