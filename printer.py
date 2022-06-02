def show_literal(x):
	if x > 0:
		return 'a' + str(x)
	return '!a' + str(-x)

def show_cnf_clause(clause):
	return '(' + '|'.join(list(map(lambda literal : show_literal(literal), clause))) + ')'

def show_cnf(clauses: [[int]]):
	return '(' + '&'.join(map(lambda clause : show_cnf_clause(clause), clauses)) + ')'

def and_link(main_formula, addition_formula):
	symbol = ''
	if main_formula != '()':
		symbol = '&'
	return main_formula[:-1] + symbol + addition_formula + ')'

def or_link(main_formula, addition_formula):
	symbol = ''
	if main_formula != '()':
		symbol = '|'
	return main_formula[:-1] + symbol + addition_formula + ')'

# clauses = [[1, 2], [-1, 2], [2, 3], [2, 3, 3], [2], [-4]]
# print(show_cnf(clauses))
