from addfunction import add

def test_add_function():
	assert add(3, 4) == 7
	assert add(10, 5) == 15
	
def test_add_String():
	assert add("lambo", " alero") == "lambo alero"
	assert add("Shakira", " Hibatullahi") == "Shakira Hibatullahi"

def test_negative_values_with_add_function():
	assert add(-3, -4) == 7