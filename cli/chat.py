#!/usr/bin/env python3
import json
import os
from datetime import datetime
from helpers.claude_call import call_claude
from helpers.query_config import query_config

def dict_to_env(settings):
    return "\n".join(f"{key.upper()}={value}" for key, value in settings.items())


def create_chat_log(prompt, conversation_key):
    base_path = f"../logs/{conversation_key}"
    os.makedirs(f"{base_path}/messages", exist_ok=True)
    os.makedirs(f"{base_path}/contexts", exist_ok=True)

    # Create initial prompt file if it doesn't exist
    initial_prompt_file = f"{base_path}/messages/initial_prompt.txt"
    if not os.path.exists(initial_prompt_file):
        with open(initial_prompt_file, "w") as f:
            f.write(prompt)

    # Get all existing log files
    log_files = sorted([f for f in os.listdir(f"{base_path}/messages") if f.startswith("log_")])

    # Initialize conversation history
    conversation_history = []
    
    # Read and parse existing log files
    for log_file in log_files:
        with open(f"{base_path}/messages/{log_file}", "r") as f:
            log_data = json.load(f)
            conversation_history.extend(log_data.get("history", []))
            conversation_history.append({"role": "user", "content": log_data["prompt"]})
            conversation_history.append({"role": "assistant", "content": log_data["response"]})

    # Add the new prompt to the conversation history
    conversation_history.append({"role": "user", "content": prompt})
    # Create new log file
    log_file = f"{base_path}/messages/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(log_file, "w") as f:
        config_settings = query_config(base_path)
        robot_role = config_settings.get("robot_role", "You are Claude.")

        # Prepare the message structure
        message_structure = {
            "prompt": prompt,
            "history": conversation_history[:-1],  # Exclude the current prompt
            "context": None  # TBD, set to null for now
        }

        # Call Claude with the structured message
        message = call_claude(robot_role, conversation_history)

        # Update the message_structure with Claude's response
        message_structure["response"] = message
        
        # Write the full message structure as JSON
        json.dump(message_structure, f, indent=2)

    # Create default context if it doesn't exist
    context_file = f"{base_path}/contexts/default.json"
    if not os.path.exists(context_file):
        with open(context_file, "w") as f:
            json.dump({"context": "No context"}, f, indent=2)

    print(f"Chat log created: {log_file}")

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    conversation_key = input("Enter conversation key: ")
    create_chat_log(prompt, conversation_key)
