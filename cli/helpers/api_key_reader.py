import os

def read_api_key():
    api_key_path = os.path.join(os.path.dirname(__file__), '..', '..', 'api_key.txt')
    with open(api_key_path, 'r') as file:
        return file.read().strip()