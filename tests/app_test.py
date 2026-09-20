import os

from flask import request

def test_data(result):
	assert result == "general-note-tag3\nToday I learned..."

def test_write(filename, content):
	with open(filename, 'w') as f:
		f.write(filename)
		f.write(content)
	with open(filename, 'r') as f:
		result = f.read()
	return test_data(result)

def test_get():
	filename = request.form.get('tags')
	content = request.form.get('content')
	return test_write(filename, content)

