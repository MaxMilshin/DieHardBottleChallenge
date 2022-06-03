import sys
import subprocess

from math import prod
from re import search
from functools import reduce
from optparse import OptionParser

from formula_builder import build_formula
from answer_recovery import recover_answer

def run_satsolver(steps_count, bottles_size, desired_number):
	overall_formula, var_count = build_formula(steps_count, bottles_size, desired_number)
	input_file = open('input.txt', 'w')
	input_file.write(overall_formula)
	input_file.close()
	output = subprocess.check_output(['./limboole', '-s', 'input.txt'])
	return output, var_count


def main():
	parser = OptionParser()

	parser.add_option('-o', '--optimal',           default=False,  help='find optimal solution',                      action='store_true'       ,  dest='is_optimal_needed')
	parser.add_option('-t', '--transfusionBound',  default=10000,  help='maximum number of transfusions',             action='store', type='int',  dest='transfusion_bound') 
	parser.add_option('-b', '--bottleCapacities',  default='',     help='comma-separated capacities of each bottle',  action='store', type='str',  dest='bottle_sizes')
	parser.add_option('-d', '--desiredNumber',     default=0,      help='desired number gallons',                     action='store', type='int',  dest='desired_number')

	(options, args) = parser.parse_args()

	
	bottle_sizes = list(map(int, options.bottle_sizes.split(',')))
	desired_number = options.desired_number
	max_steps_count = min(options.transfusion_bound, reduce(lambda res, item: res * (item + 1), bottle_sizes, 1))

	if options.is_optimal_needed == True:
		left_bound, right_bound = 0, max_steps_count 
		while right_bound - left_bound > 1:
			steps_count = (left_bound + right_bound) // 2
			output, _ = run_satsolver(steps_count, bottle_sizes, desired_number)
			if search('UNSATISFIABLE formula', output.decode('utf-8')):
				left_bound = steps_count
			else:
				right_bound = steps_count
		steps_count = right_bound
	else:
		steps_count = max_steps_count

	output, var_count = run_satsolver(steps_count, bottle_sizes, desired_number)
	if search('UNSATISFIABLE formula', output.decode('utf-8')):
		print('Impossible')
		exit(0)

	bottle_in = recover_answer(output, var_count, steps_count, bottle_sizes)
	for bottle_trace in bottle_in:
		print(bottle_trace)
	
if __name__ == "__main__":
	main()

