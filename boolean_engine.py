def _are_bits_equal(x, y):
	return [[x, -y], [-x, y]]


def _are_bits_inequal(x, y):
	return [[x, y], [-x, -y]]

def _is_first_bit_least(x, y):
	return [[-x], [y]]



def _get_nand(x, y):
	return [[-x, -y]]

def _get_and(x, y):
	return [[x], [y]]


def _get_three_bits_xor_equals_false(x, y, z):
	return [[-x, -y, -z], [x, y, -z], [x, -y, z], [-x, y, z]]

def _get_three_bits_xor_equals_true(x, y, z):
	return [[x, y, z], [-x, -y, z], [-x, y, -z], [x, -y, -z]]


def _get_at_most_one_bit_equals_true(x, y, z):
	return [[-x, -y], [-x, -z], [-y, -z]]

def _get_at_least_two_bits_equal_true(x, y, z):
	return [[x, y], [x, z], [y, z]]






