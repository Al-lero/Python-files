from minimum_function import minimum

def test_minimum_function(): 
	assert minimum(2,3,4,5) == 2
	assert minimum(10,10,10,10) == 10
	assert minimum (4,19,600,80) == 600
	assert minimum(-1,-6,-5,0) == -6