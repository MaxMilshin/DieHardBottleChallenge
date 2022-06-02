def parse_number(solution, cur_var_number, big_var_size):
	number = 0
	for i in range(cur_var_number + big_var_size - 1, cur_var_number - 1, -1):
		if solution[i] == 1:
			number += 2 ** (cur_var_number + big_var_size - 1 - i)
	return number

def recover_answer(solution, big_var_size, steps_count):
	first_bottle_in = [0] * steps_count
	second_bottle_in = [0] * steps_count

	cur_var_number = 1
	for i in range(steps_count):
		first_bottle_in[i] = parse_number(solution, cur_var_number, big_var_size)
		cur_var_number += big_var_size
		second_bottle_in[i] = parse_number(solution, cur_var_number, big_var_size)	
		cur_var_number += big_var_size

	return first_bottle_in, second_bottle_in