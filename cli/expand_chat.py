#!/usr/bin/env python3
import json
import os

def expand_information(conversation_key):
    base_path = f"../logs/{conversation_key}/messages"
    compressed_file = f"{base_path}/compressed_{conversation_key}.json"
    
    if not os.path.exists(compressed_file):
        print("Compressed file not found.")
        return
    
    with open(compressed_file, "r") as f:
        compressed_data = json.load(f)
    
    expanded_file = f"{base_path}/expanded_{conversation_key}.json"
    with open(expanded_file, "w") as f:
        json.dump(compressed_data, f, indent=2)
    
    print(f"Expanded information saved to: {expanded_file}")

if __name__ == "__main__":
    conversation_key = input("Enter conversation key: ")
    expand_information(conversation_key)
