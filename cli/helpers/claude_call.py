import anthropic
from .api_key_reader import read_api_key

def call_claude(robot_role, messages, max_tokens=1000):
    
    # Initialize the Anthropic client with the API key
    api_key = read_api_key()
    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=max_tokens,
        temperature=0,
        system=robot_role,
        messages=messages
    )
    print(message.content[0].text)

    return message.content[0].text
