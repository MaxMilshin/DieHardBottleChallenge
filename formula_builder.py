from formula_manager import make_big_var, add_clauses
from arithmetic_api import is_number_equal_to_given_constant, are_numbers_equal, is_first_number_least, is_number_equal_to_given_numbers_sum
from printer import and_link, or_link

def remain_the_same(bottles_indicies, main_vars, step):
	if len(bottles_indicies) == 0:
		return ''
	formula = '()'
	for ind in bottles_indicies:
		formula = and_link(formula, are_numbers_equal(main_vars[ind][step + 1], main_vars[ind][step])) 
	return formula

def build_formula(steps_count, big_var_size, bottles_size, desired_number):
	bottles_count = len(bottles_size)

	main_vars = [[] for i in range(bottles_count)]
	cur_var_number = 1

	for i in range(steps_count):
		for j in range(bottles_count):
			big_var, cur_var_number = make_big_var(big_var_size, cur_var_number)
			main_vars[j].append(big_var)

	overall_formula = '()'
	for i in range(bottles_count):
		overall_formula = and_link(overall_formula, is_number_equal_to_given_constant(main_vars[i][0], 0))
	
	end_state_condition_formula = '()'
	for i in range(bottles_count):
		end_state_condition_formula = or_link(end_state_condition_formula, is_number_equal_to_given_constant(main_vars[i][steps_count - 1], desired_number))
	overall_formula = and_link(overall_formula, end_state_condition_formula)

	for step in range(steps_count - 1):
		step_formula = '()'

		# fill one particalar bottle, rest of bottles remains the same
		for i in range(bottles_count):
			local_formula = '()'
			local_formula = and_link(local_formula, is_number_equal_to_given_constant(main_vars[i][step + 1], bottles_size[i]))
			remaining_bottles = list(range(i)) + list(range(i + 1, bottles_count))
			local_formula = and_link(local_formula, remain_the_same(remaining_bottles, main_vars, step))
			step_formula = or_link(step_formula, local_formula)

		# pour out water from one particalar bottle, rest of bottles remains the same
		for i in range(bottles_count):
			local_formula = '()'
			local_formula = and_link(local_formula, is_number_equal_to_given_constant(main_vars[i][step + 1], 0))
			remaining_bottles = list(range(i)) + list(range(i + 1, bottles_count))
			local_formula = and_link(local_formula, remain_the_same(remaining_bottles, main_vars, step))
			step_formula = or_link(step_formula, local_formula)

		# make one bottle empty, pouring water into another bottle
		for i in range(bottles_count):
			for j in range(bottles_count):
				if i == j:
					continue
				local_formula = '()'
				remaining_bottles = list(range(min(i, j))) + list(range(min(i, j) + 1, max(i, j))) + list(range(max(i, j) + 1, bottles_count))
				local_formula = and_link(local_formula, remain_the_same(remaining_bottles, main_vars, step))
				local_formula = and_link(local_formula, is_number_equal_to_given_constant(main_vars[i][step + 1], 0))
				z, cur_var_number = make_big_var(big_var_size, cur_var_number)
				addition_formula, cur_var_number = is_number_equal_to_given_numbers_sum(z, main_vars[i][step], main_vars[j][step], cur_var_number) 
				local_formula = and_link(local_formula, addition_formula)
				local_formula = and_link(local_formula, are_numbers_equal(z, main_vars[j][step + 1]))
				w, cur_var_number = make_big_var(big_var_size, cur_var_number)
				local_formula = and_link(local_formula, is_number_equal_to_given_constant(w, bottles_size[j]))
				local_formula = and_link(local_formula, is_first_number_least(z, w))
				step_formula = or_link(step_formula, local_formula)

		# make one bottle complete, pouring water from another bottle
		for i in range(bottles_count):
			for j in range(bottles_count):
				if i == j:
					continue
				local_formula = '()'
				remaining_bottles = list(range(min(i, j))) + list(range(min(i, j) + 1, max(i, j))) + list(range(max(i, j) + 1, bottles_count))
				local_formula = and_link(local_formula, remain_the_same(remaining_bottles, main_vars, step))
				local_formula = and_link(local_formula, is_number_equal_to_given_constant(main_vars[j][step + 1], bottles_size[j]))
				w, cur_var_number = make_big_var(big_var_size, cur_var_number)
				addition_formula, cur_var_number = is_number_equal_to_given_numbers_sum(w, main_vars[i][step + 1], main_vars[j][step + 1], cur_var_number) 
				local_formula = and_link(local_formula, addition_formula)
				addition_formula, cur_var_number = is_number_equal_to_given_numbers_sum(w, main_vars[i][step], main_vars[j][step], cur_var_number) 
				local_formula = and_link(local_formula, addition_formula)
				local_formula = and_link(local_formula, is_first_number_least(main_vars[j][step + 1], w))
				step_formula = or_link(step_formula, local_formula)

		# do not do something
		step_formula = or_link(step_formula, remain_the_same(list(range(bottles_count)), main_vars, step))
		
		overall_formula = and_link(overall_formula, step_formula)

	return overall_formula, cur_var_number
