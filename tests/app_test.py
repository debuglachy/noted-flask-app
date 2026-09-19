import os

def test_withopen_write():
#	 Arrange
	content = 'a'

#	Act
	result = 	with open(content, content) as f:
				f.write(content)
			return

#	ASSERT
	assert cat result == 'a'
