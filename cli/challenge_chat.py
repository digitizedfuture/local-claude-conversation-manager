#!/usr/bin/env python3
import json
import os

def review_conversation(conversation_key, mode="single"):
    base_path = f"../logs/{conversation_key}/messages"
    
    if mode == "single":
        files = sorted(os.listdir(base_path))
        if files:
            latest_file = files[-1]
            with open(f"{base_path}/{latest_file}", "r") as f:
                data = json.load(f)
                print(f"Prompt: {data['prompt']}")
                print(f"Response: {data['response']}")
    elif mode == "whole":
        for file in sorted(os.listdir(base_path)):
            if file.endswith(".json"):
                with open(f"{base_path}/{file}", "r") as f:
                    data = json.load(f)
                    print(f"File: {file}")
                    print(f"Prompt: {data['prompt']}")
                    print(f"Response: {data['response']}")
                    print("-" * 50)

if __name__ == "__main__":
    conversation_key = input("Enter conversation key: ")
    mode = input("Enter review mode (single/whole): ")
    review_conversation(conversation_key, mode)
