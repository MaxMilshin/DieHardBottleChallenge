import sys
import subprocess

from math import prod
from re import search
from functools import reduce

from formula_builder import build_formula
from answer_recovery import recover_answer

def run_satsolver(steps_count, big_var_size, bottles_size, desired_number):
	overall_formula, var_count = build_formula(steps_count, big_var_size, bottles_size, desired_number)
	input_file = open('input.txt', 'w')
	input_file.write(overall_formula)
	input_file.close()
	output = subprocess.check_output(['./limboole', '-s', 'input.txt'])
	return output, var_count

def main():

	bottles_size = list(map(int, input().split()))
	desired_number = int(input())

	big_var_size = 1
	while 2 ** big_var_size <= max(bottles_size):
		big_var_size += 1
	big_var_size += 1

	max_steps_count = reduce(lambda res, item: res * (item + 1), bottles_size, 1)
	
	left_bound, right_bound = 0, max_steps_count 
	while right_bound - left_bound > 1:
		steps_count = (left_bound + right_bound) // 2
		output, _ = run_satsolver(steps_count, big_var_size, bottles_size, desired_number)
		if search('UNSATISFIABLE formula', output.decode('utf-8')):
			left_bound = steps_count
		else:
			right_bound = steps_count

	steps_count = right_bound
	output, var_count = run_satsolver(steps_count, big_var_size, bottles_size, desired_number)
	if search('UNSATISFIABLE formula', output.decode('utf-8')):
		print('Impossible')
		exit(0)

	first_bottle_in, second_bottle_in = recover_answer(output, var_count, big_var_size, steps_count)
	print(first_bottle_in)
	print(second_bottle_in)

if __name__ == "__main__":
	main()

