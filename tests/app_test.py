from pathlib import Path

import pytest

templates = Path("/workdir/templates")

from app import index

@pytest.fixture()
def appx():
	appx = index()
	yield appx

@pytest.fixture()
def client(appx):
	return appx.test_client()

def test_get(client):
	response = client.get("/")
	assert response.request.path == templates / "index"

def test_post(client):
	response = client.post("/", data={
		"tags": "sample-filename",
		"content": "sample-content",
	})
	assert response.request.status == 200

