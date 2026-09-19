import os

def test_withopen_write():
#	 Arrange
	file = 'a'

#	Act
	with open(file, 'w') as f:
		f.write('sample')
	with open(file, 'r') as f:
		result = f.read()

#	ASSERT
	assert result == 'sample'
