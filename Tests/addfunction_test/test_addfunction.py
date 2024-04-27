from addfunction import add

def test_add_function():
	assert add(5,8) == 13

def test_add_strings():
	assert add("Alero", " Kemi") == "Alero Kemi"

def test_negative_values_with_add_function():
	assert add (-3 , -4) == 7