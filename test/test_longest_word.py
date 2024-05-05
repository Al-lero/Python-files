from longest_word import longest

def test_longest_word(): 
	assert longest('longest','maximum','consideration') == 'consideration 13'
	assert longest('welcome','out','breakfast') == 'breakfast 9' 
	assert longest('opposite','weather','mobile') == 'opposite 8' 
