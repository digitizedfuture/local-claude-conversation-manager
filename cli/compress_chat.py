#!/usr/bin/env python3
import json
import os
from helpers.claude_call import call_claude
from helpers.query_config import query_config

def compress_information(conversation_key):
    base_path = f"../logs/{conversation_key}/messages"
    compressed_dir = f"{base_path}/compressed"
    os.makedirs(compressed_dir, exist_ok=True)

    all_user_prompts = []
    all_assistant_responses = []
    
    for file in sorted(os.listdir(base_path)):
        if file.endswith(".json"):
            with open(f"{base_path}/{file}", "r") as f:
                data = json.load(f)
                all_user_prompts.append(data["prompt"])
                all_assistant_responses.append(data["response"])
    
    # Combine all prompts and responses
    combined_user_prompts = " ".join(all_user_prompts)
    combined_assistant_responses = " ".join(all_assistant_responses)
    
    # Prepare the message for Claude
    messages = [
        {"role": "user", "content": "Summarize the following conversation between a user and an AI assistant. Provide a concise summary for both the user's inputs and the assistant's responses. Format your response as 'User: <user summary> Assistant: <assistant summary>'"},
        {"role": "assistant", "content": "Certainly! I'll summarize the conversation in the format you requested. Please provide the user inputs and assistant responses."},
        {"role": "user", "content": f"User inputs: {combined_user_prompts}\n\nAssistant responses: {combined_assistant_responses}"}
    ]
    
    # Get Claude's summary
    config_settings = query_config(base_path)
    robot_role = config_settings.get("robot_role", "You are an AI assistant tasked with summarizing conversations.")
    summary = call_claude(robot_role, messages)
    
    # Parse the summary to extract user and assistant parts
    try:
        user_summary, assistant_summary = summary.split("Assistant:", 1)
        user_summary = user_summary.replace("User:", "").strip()
        assistant_summary = assistant_summary.strip()
    except ValueError:
        print("Warning: Could not split the summary as expected. Using the entire summary as user input.")
        user_summary = summary.strip()
        assistant_summary = "No separate assistant summary available."
    
    # Create the compressed data
    compressed_data = [
        {"role": "user", "content": user_summary},
        {"role": "assistant", "content": assistant_summary}
    ]
    
    # Save the compressed data
    compressed_file = f"{compressed_dir}/compressed_{conversation_key}.json"
    with open(compressed_file, "w") as f:
        json.dump(compressed_data, f, indent=2)
        
    print(f"Compressed information saved to: {compressed_file}")

if __name__ == "__main__":
    conversation_key = input("Enter conversation key: ")
    compress_information(conversation_key)