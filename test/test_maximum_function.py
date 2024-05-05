from maximum_function import maximum

def test_maximum_function(): 
	assert maximum(2,3,4,5) == 5
	assert maximum(10,10,10,10) == 10
	assert maximum (4,19,600,80) == 4
	assert maximum(-1,-6,-5,0) == 0