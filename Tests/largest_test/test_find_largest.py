from largest import find_largest

def test_find_largest():
	assert find_largest(3,4,6) == 8

def test_to_find_largest():
	assert find_largest(-2, -3, -4) == -2

def test_find_number():
	assert find_largest(54,3,21) == 54