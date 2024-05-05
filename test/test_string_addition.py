from string_addition import string_addition

def test_string_addition():
	assert string_addition("addly") == "addlying"
	assert string_addition("to") == "to"
	assert string_addition("likely") == "likelying"