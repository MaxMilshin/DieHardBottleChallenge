from re import search

from formula_manager import calculate_big_var_size

def parse_number(solution, cur_var_number, big_var_size):
	number = 0
	for i in range(cur_var_number + big_var_size - 1, cur_var_number - 1, -1):
		if solution[i] == 1:
			number += 2 ** (cur_var_number + big_var_size - 1 - i)
	return number

def recover_answer(output, var_count, steps_count, bottle_sizes):
	solution = [0] * var_count
	for i in range(1, var_count):
		value = int(search('a' + str(i) + r' = \d', output.decode('utf-8'))[0][-1])
		solution[i] = value
	
	bottles_count = len(bottle_sizes)
	bottle_in = [[0] * steps_count for _ in range(bottles_count)]
	
	big_var_size = calculate_big_var_size(bottle_sizes)
	cur_var_number = 1
	for i in range(steps_count):
		for k in range(bottles_count):
			bottle_in[k][i] = parse_number(solution, cur_var_number, big_var_size)
			cur_var_number += big_var_size

	return bottle_in