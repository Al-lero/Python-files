from palindrome import is_palindrome

def test_for_palindrome_returns_true():
	assert is_palindrome("dad") == True
	assert is_palindrome("12121") == True
	assert is_palindrome("neveroddoreven")

def test_for_palindrome_returns_false():
	assert is_palindrome("ball") == False
	assert is_palindrome("10111") == False

def test_for_number_returns_false():
	assert is_palindrome(10) == False