import json
import os
from datetime import datetime

def replay_conversation(conversation_key):
    base_path = f"../logs/{conversation_key}/messages"
    
    if not os.path.exists(base_path):
        print(f"No conversation found for key: {conversation_key}")
        return

    files = sorted(os.listdir(base_path))
    for file in files:
        if file.endswith(".json"):
            with open(f"{base_path}/{file}", "r") as f:
                data = json.load(f)
                # Extract timestamp from filename, assuming format: log_YYYYMMDD.json
                timestamp_str = file.split("_")[1].split(".")[0]
                timestamp = datetime.strptime(timestamp_str, "%Y%m%d")
                print(f"\n--- {timestamp.strftime('%Y-%m-%d')} ---")
                print(f"User: {data['prompt']}")
                print(f"AI: {data['response']}")
                input("Press Enter to continue...")

if __name__ == "__main__":
    conversation_key = input("Enter conversation key to replay: ")
    replay_conversation(conversation_key)