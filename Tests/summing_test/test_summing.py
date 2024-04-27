
from summing import summing

def test_summing_function():
	assert(1,2,3,4,5) == 15	
	assert summing(4,5) == 9
	assert summing(5,7,9) == 21
	assert summing(2,3,6,7,7,8,10,40,25) == 128