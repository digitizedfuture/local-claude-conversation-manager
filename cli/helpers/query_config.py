import os
import json

def query_config(base_path):
    # Import the chat.json file
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'configs', 'chat.json')
    with open(config_path, 'r') as json_file:
        default_config_settings = json.load(json_file)

    config_file = f"{base_path}/default_config.env"
    if not os.path.exists(config_file):
        # Create default config file if it doesn't exist
        with open(config_file, "w") as f:
            for key, value in default_config_settings.items():
                f.write(f"{key.upper()}={value}\n")
    
    with open(config_file, "r") as f:
        config_content = f.read()
    # Parse the config file content
    return {key.lower(): value.strip() for line in config_content.splitlines() 
            if '=' in line for key, value in [line.split('=', 1)]}