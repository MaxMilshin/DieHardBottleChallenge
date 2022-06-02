from boolean_engine import _are_bits_equal, _are_bits_inequal, _is_first_bit_least, _get_nand, _get_and, _get_three_bits_xor_equals_false, _get_three_bits_xor_equals_true, _get_at_most_one_bit_equals_true, _get_at_least_two_bits_equal_true 
from formula_manager import add_clauses, make_var
from printer import show_cnf, and_link, or_link


def are_numbers_equal(x: [int], y: [int]):
	clauses = []
	for xx, yy in list(zip(x, y)):
		add_clauses(clauses, _are_bits_equal(xx, yy))
	return show_cnf(clauses)

def is_first_number_least(x: [int], y: [int]):
	n = len(x)
	formula = '()'
	for i in range(n + 1):
		local_clauses = []
		if i != n:
			add_clauses(local_clauses, _is_first_bit_least(x[i], y[i]))
		for j in range(i):
			add_clauses(local_clauses, _are_bits_equal(x[j], y[j]))
		formula = or_link(formula, show_cnf(local_clauses))
	return formula

def is_number_equal_to_given_constant(x: [int], c: int):
	i = len(x) - 1
	clauses = []
	while c > 0:
		if c % 2 == 1:
			clauses.append([x[i]])
		else:
			clauses.append([-x[i]])
		c //= 2
		i -= 1
	while i >= 0:
		clauses.append([-x[i]])
		i -= 1
	return show_cnf(clauses)

def is_number_equal_to_given_numbers_sum(z: [int], x: [int], y: [int], cur_var_number):
	result_formula = '()'
	last_carry = None
	for i in range(len(x) - 1, -1, -1):
		local_formula = '()'
		local_formula_for_carry = '()'
		if i == len(x) - 1:
			# z[i] = 0,	(x[i] + y[i]) mod 2 = 0
			
			clauses_1 = [[-z[i]]]
			add_clauses(clauses_1, _are_bits_equal(x[i], y[i]))

			# z[i] = 0,	(x[i] + y[i]) mod 2 = 0
			clauses_2 = [[z[i]]]
			add_clauses(clauses_2, _are_bits_inequal(x[i], y[i]))

			# convert to CNF "clauses_1 or clauses_2"
			local_formula = or_link(local_formula, show_cnf(clauses_1))
			local_formula = or_link(local_formula, show_cnf(clauses_2))

			# add_clauses(all_clauses, convert_to_cnf([clauses_1, clauses_2]))

			last_carry, cur_var_number = make_var(cur_var_number)

			# last_carry = 0, carry(x + y) = 0 
			carry_clauses_1 = [[-last_carry]]
			add_clauses(carry_clauses_1, _get_nand(x[i], y[i]))

			# last_carry = 1, carry(x + y) = 1 
			carry_clauses_2 = [[last_carry]]
			add_clauses(carry_clauses_2, _get_and(x[i], y[i]))

			# convert co cnf "carry_clauses_1 or carry_clauses_2"
			# add_clauses(all_clauses, convert_to_cnf([carry_clauses_1, carry_clauses_2]))
			local_formula_for_carry = or_link(local_formula_for_carry, show_cnf(carry_clauses_1))
			local_formula_for_carry = or_link(local_formula_for_carry, show_cnf(carry_clauses_2))
		
		else:
			# z[i] = 0, (x[i] + y[i] + last_carry) mod 2 = 0
			clauses_1 = [[-z[i]]]
			add_clauses(clauses_1, _get_three_bits_xor_equals_false(x[i], y[i], last_carry))

			# z[i] = 1, (x[i] + y[i] + last_carry) mod 2 = 1
			clauses_2 = [[z[i]]]
			add_clauses(clauses_2, _get_three_bits_xor_equals_true(x[i], y[i], last_carry))

			# convert to CNF "clauses_1 or clauses_2"
			# add_clauses(all_clauses, convert_to_cnf([clauses_1, clauses_2]))
			local_formula = or_link(local_formula, show_cnf(clauses_1))
			local_formula = or_link(local_formula, show_cnf(clauses_2))



			new_carry, cur_var_number = make_var(cur_var_number)

			# new_carry = 0, carry(x + y + last_curry) = 0 
			carry_clauses_1 = [[-new_carry]]
			add_clauses(carry_clauses_1, _get_at_most_one_bit_equals_true(x[i], y[i], last_carry))

			# new_carry = 1, carry(x + y + last_curry) = 1 
			carry_clauses_2 = [[new_carry]]
			add_clauses(carry_clauses_2, _get_at_least_two_bits_equal_true(x[i], y[i], last_carry))

			last_carry = new_carry

			# convert co cnf "carry_clauses_1 or carry_clauses_2"
			# add_clauses(all_clauses, convert_to_cnf([carry_clauses_1, carry_clauses_2]))
			local_formula_for_carry = or_link(local_formula_for_carry, show_cnf(carry_clauses_1))
			local_formula_for_carry = or_link(local_formula_for_carry, show_cnf(carry_clauses_2))
		
		result_formula = and_link(result_formula, local_formula)
		result_formula = and_link(result_formula, local_formula_for_carry)


	return result_formula, cur_var_number