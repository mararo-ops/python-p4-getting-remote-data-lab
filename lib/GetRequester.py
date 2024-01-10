import requests
import json
class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        try:
            return response.json()
        except ValueError as e:
            print(f"Error loading JSON: {e}")
            return None

# Example usage:
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)

# Get the response body
response_body = requester.get_response_body()
print(f"Response Body:\n{response_body}\n")

# Load JSON data
json_data = requester.load_json()
print(f"JSON Data:\n{json_data}")
