from pathlib import Path

import pytest

templates = Path("/workdir/templates")

from app import app as flask_app

@pytest.fixture()
def app():
	flask_app.config.update({
		"TESTING": True,
	})
	yield flask_app

@pytest.fixture()
def client(app):
	return app.test_client()

def test_get(client):
	response = client.get("/")
	assert response.status_code == 200

def test_post(client):
	response = client.post("/", data={
		"tags": "sample-filename",
		"content": "sample-content",
	})
	assert response.status_code == 200

