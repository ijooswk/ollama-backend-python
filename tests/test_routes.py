from flask import Flask, jsonify
import pytest
import asyncio
from app.routes import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.mark.asyncio
async def test_get_page_description(client):
    url = "https://example.com"
    response = await client.post('/api/description', json={'url': url})
    data = json.loads(response.data)

    assert response.status_code == 200
    assert 'description' in data
    assert 'summary' in data
    assert data['url'] == url

@pytest.mark.asyncio
async def test_invalid_url(client):
    url = "invalid-url"
    response = await client.post('/api/description', json={'url': url})
    
    assert response.status_code == 400
    assert 'error' in json.loads(response.data)