from character_return import chracter_return

def test_character_return():
	assert character_return("o") == ""
	assert character_return("semicolon") == "seon"
	assert character_return("hello") == "helo"
	assert character_return("on") == "onon"	
	assert character_return("dinner") == "din" 