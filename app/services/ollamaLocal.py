import requests
import json

class OllamaAPI:
    def __init__(self, base_url, model):
        self.base_url = base_url
        self.model = model

    def call_api(self, prompt):
        url = f"{self.base_url}/api/generate"
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_data = response.json()
            if "response" in response_data:
                return response_data["response"]
            else:
                return "Key 'response' not found in the response data."
        else:
            return f"Request failed with status code: {response.status_code}"
    