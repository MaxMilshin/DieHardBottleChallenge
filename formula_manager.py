def make_big_var(size, cur_var_number):
	var = [i for i in range(cur_var_number, cur_var_number + size)]
	cur_var_number += size
	return var, cur_var_number

def make_var(cur_var_number):
	var = cur_var_number
	cur_var_number += 1
	return var, cur_var_number

def add_clauses(destination: [[int]], source: [[int]]):
	for clause in source:
		destination.append(clause)

def calculate_big_var_size(bottle_sizes: [int]):
	big_var_size = 1
	while 2 ** big_var_size <= max(bottle_sizes):
		big_var_size += 1
	return big_var_size + 1
