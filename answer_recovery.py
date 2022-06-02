from re import search

def parse_number(solution, cur_var_number, big_var_size):
	number = 0
	for i in range(cur_var_number + big_var_size - 1, cur_var_number - 1, -1):
		if solution[i] == 1:
			number += 2 ** (cur_var_number + big_var_size - 1 - i)
	return number

def recover_answer(output, var_count, big_var_size, steps_count, bottles_count):
	solution = [0] * var_count
	for i in range(1, var_count):
		value = int(search('a' + str(i) + r' = \d', output.decode('utf-8'))[0][-1])
		solution[i] = value
	print(solution[1:])

	bottle_in = [[0] * steps_count for _ in range(bottles_count)]
	
	cur_var_number = 1
	for i in range(steps_count):
		for k in range(bottles_count):
			bottle_in[k][i] = parse_number(solution, cur_var_number, big_var_size)
			cur_var_number += big_var_size

	return bottle_in