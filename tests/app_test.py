import os

def test_form_data(filename: str, content: str) -> str:
	return f"{filename}{content}"

def test_write():
	with open(filename, 'w') as f:
		f.write(filename)
		f.write(content)
	with open(filename, 'r') as f:
		result = f.read()
	return result

