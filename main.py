import sys
import subprocess

from math import prod
from re import search

from formula_builder import build_formula
from answer_recovery import recover_answer

bottles_size = list(map(int, input().split()))

big_var_size = 1
while 2 ** big_var_size <= max(bottles_size):
	big_var_size += 1

steps_count = prod(bottles_size)

overall_formula, cur_var_number = build_formula(steps_count, big_var_size, bottles_size)
# print(overall_formula)

# run satsolver and answer recovering
input_file = open('input.txt', 'w')
input_file.write(overall_formula)
input_file.close()
output = subprocess.check_output(['./limboole', '-s', 'input.txt'])
if search(r'UNSATISFIABLE formula \d*', output.decode('utf-8')):
	print('Impossible')
	exit(0)
solution = [0] * cur_var_number
for i in range(1, cur_var_number):
	value = int(search('a' + str(i) + r' = \d', output.decode('utf-8'))[0][-1])
	solution[i] = value
print(solution[1:])
# print(solution)
# print(output)
# exit(0)


# solution = []
first_bottle_in, second_bottle_in = recover_answer(solution, big_var_size, steps_count)
print(first_bottle_in)
print(second_bottle_in)

