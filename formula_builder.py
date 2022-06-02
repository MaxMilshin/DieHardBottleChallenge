from formula_manager import make_big_var, add_clauses
from arithmetic_api import is_number_equal_to_given_constant, are_numbers_equal, is_first_number_least, is_number_equal_to_given_numbers_sum
from printer import and_link, or_link


def build_formula(steps_count, big_var_size, bottles_size, desired_number):
	bottles_count = len(bottles_size)

	# main_vars = [[] for i in range(bottles_count)]
	cur_var_number = 1

	# for i in range(steps_count):
	# 	for j in range(bottles_count):
	# 		big_var, cur_var_number = make_big_var(big_var_size, cur_var_number)
	# 		main_vars[j].append(big_var)

	x = []
	y = []

	for i in range(steps_count):				
		big_var, cur_var_number = make_big_var(big_var_size, cur_var_number)
		x.append(big_var)
		big_var, cur_var_number = make_big_var(big_var_size, cur_var_number)
		y.append(big_var)

	overall_formula = '()'
	overall_formula = and_link(overall_formula, is_number_equal_to_given_constant(x[0], bottles_size[0]))
	overall_formula = and_link(overall_formula, is_number_equal_to_given_constant(y[0], bottles_size[1]))
	
	for i in range(steps_count - 1):
		j = i + 1
		main_cnf = [[] for i in range(9)]
		step_formula = '()'

		# x, y -> n, y (fill the first bottle)
		local_formula = '()'
		local_formula = and_link(local_formula, is_number_equal_to_given_constant(x[j], bottles_size[0]))
		local_formula = and_link(local_formula, are_numbers_equal(y[j], y[i])) 
		step_formula = or_link(step_formula, local_formula)

	 	# x, y -> x, m (fill the second bottle)
		local_formula = '()'
		local_formula = and_link(local_formula, is_number_equal_to_given_constant(y[j], bottles_size[1]))
		local_formula = and_link(local_formula, are_numbers_equal(x[j], x[i]))
		step_formula = or_link(step_formula, local_formula)

		# x, y -> 0, y (pour out the water from first bottle)
		local_formula = '()'
		local_formula = and_link(local_formula, is_number_equal_to_given_constant(x[j], 0))
		local_formula = and_link(local_formula, are_numbers_equal(y[j], y[i])) 
		step_formula = or_link(step_formula, local_formula)

		# x, y -> x, 0 (pour out the water from second bottle)
		local_formula = '()'
		local_formula = and_link(local_formula, is_number_equal_to_given_constant(y[j], 0))
		local_formula = and_link(local_formula, are_numbers_equal(x[j], x[i]))
		step_formula = or_link(step_formula, local_formula)

		# x, y -> 0, x + y and x + y < m (make first bottle empty, pouring water into second bottle)
		local_formula = '()'
		local_formula = and_link(local_formula, is_number_equal_to_given_constant(x[j], 0))
		z, cur_var_number = make_big_var(big_var_size, cur_var_number)
		addition_formula, cur_var_number = is_number_equal_to_given_numbers_sum(z, x[i], y[i], cur_var_number) 
		local_formula = and_link(local_formula, addition_formula)
		local_formula = and_link(local_formula, are_numbers_equal(z, y[j]))
		w, cur_var_number = make_big_var(big_var_size, cur_var_number)
		local_formula = and_link(local_formula, is_number_equal_to_given_constant(w, bottles_size[1]))
		local_formula = and_link(local_formula, is_first_number_least(z, w))
		step_formula = or_link(step_formula, local_formula)

		# x, y -> x + y, 0 and x + y < n (make second bottle empty, pouring water into first bottle)
		local_formula = '()'
		local_formula = and_link(local_formula, is_number_equal_to_given_constant(y[j], 0))
		z, cur_var_number = make_big_var(big_var_size, cur_var_number)
		addition_formula, cur_var_number = is_number_equal_to_given_numbers_sum(z, x[i], y[i], cur_var_number) 
		local_formula = and_link(local_formula, addition_formula)
		local_formula = and_link(local_formula, are_numbers_equal(z, x[j]))
		w, cur_var_number = make_big_var(big_var_size, cur_var_number)
		local_formula = and_link(local_formula, is_number_equal_to_given_constant(w, bottles_size[0]))
		local_formula = and_link(local_formula, is_first_number_least(z, w))
		step_formula = or_link(step_formula, local_formula)

		# x, y -> x + y - m, m and x + y >= m (make second bottle complete, pouring water from first bottle)
		local_formula = '()'
		local_formula = and_link(local_formula, is_number_equal_to_given_constant(y[j], bottles_size[1]))
		w, cur_var_number = make_big_var(big_var_size, cur_var_number)
		addition_formula, cur_var_number = is_number_equal_to_given_numbers_sum(w, x[j], y[j], cur_var_number) 
		local_formula = and_link(local_formula, addition_formula)
		addition_formula, cur_var_number = is_number_equal_to_given_numbers_sum(w, x[i], y[i], cur_var_number) 
		local_formula = and_link(local_formula, addition_formula)
		local_formula = and_link(local_formula, is_first_number_least(y[j], w))
		step_formula = or_link(step_formula, local_formula)


		# x, y -> n, x + y - n and x + y >= n (make first bottle complete, pouring water from second bottle)
		local_formula = '()'
		local_formula = and_link(local_formula, is_number_equal_to_given_constant(x[j], bottles_size[0]))
		w, cur_var_number = make_big_var(big_var_size, cur_var_number)
		addition_formula, cur_var_number = is_number_equal_to_given_numbers_sum(w, y[j], x[j], cur_var_number) 
		local_formula = and_link(local_formula, addition_formula)
		addition_formula, cur_var_number = is_number_equal_to_given_numbers_sum(w, y[i], x[i], cur_var_number) 
		local_formula = and_link(local_formula, addition_formula)
		local_formula = and_link(local_formula, is_first_number_least(x[j], w))
		step_formula = or_link(step_formula, local_formula)

		# x, y -> x, y (nothing has changed)
		local_formula = '()'
		local_formula = and_link(local_formula, are_numbers_equal(x[j], x[i]))
		local_formula = and_link(local_formula, are_numbers_equal(y[j], y[i]))
		step_formula = or_link(step_formula, local_formula)

		
		overall_formula = and_link(overall_formula, step_formula)

	end_state_condition_formula = '()'
	end_state_condition_formula = or_link(end_state_condition_formula, is_number_equal_to_given_constant(x[steps_count - 1], desired_number))
	end_state_condition_formula = or_link(end_state_condition_formula, is_number_equal_to_given_constant(y[steps_count - 1], desired_number))
	
	overall_formula = and_link(overall_formula, end_state_condition_formula)
	# overall_formula = and_link(overall_formula, is_number_equal_to_given_constant(y[steps_count - 1], 2))

	return overall_formula, cur_var_number
