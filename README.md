# Local Claude Conversation Manager Documentation

## Overview

The Chat Log System is a sophisticated git-like mini-system for managing local chat logs from Claude with advanced data manipulation features. It provides a robust framework for capturing, organizing, and analyzing chats with AI assistants.

## System Structure
```
local_claude_conversation_manager/
├── api_key.txt
├── cli/
│   ├── chat.py
│   ├── review_chat.py
│   ├── compress_chat.py
│   ├── expand_chat.py
│   └── replay_chat.py
├── logs/
│   └── [chat_key]/
│       ├── default_config.txt
│       ├── messages/
│       │   ├── initial_prompt.txt
│       │   ├── log_[date].json
│       │   └── compressed/
│       │       └── compressed_[chat_key].json
│       └── contexts/
│           └── default.json
└── configs/
    └── chat.json
```
## Key Components

### 1. CLI Scripts

#### chat.py
This script handles the main interaction with Claude, creating chat logs and managing chat history.

Key features:
- (TODO) Supports multiple input types (text, voice, images)
- Maintains chat history
- Integrates with the configuration system

#### review_chat.py
Allows users to review past conversations in single message or whole conversation mode.

#### compress_chat.py
Compresses chat data for efficient storage and analysis.

#### expand_chat.py
Expands compressed conversation data for detailed review.

#### replay_chat.py
Enables users to replay entire conversations chronologically.

### 2. Configuration System

The system uses a flexible configuration approach with a JSON file for easy customization.

### 3. Helpers

- claude_call.py: Manages the interaction with the Claude API
- api_key_reader.py: Securely reads the API key
- query_config.py: Handles configuration management

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation Steps

1. Clone the repository or download the source code.
   ```
   git clone https://github.com/digitizedfuture/local-claude-chat-manager

2. Navigate to the project directory:
   ```
   cd local-claude-chat-manager
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up your API key:
   - Create a file named `api_key.txt` in the root directory.
   - Add your Claude API key to this file.
   ```
   # example API key
   sk-ant-api03-xxx...xxx...
   ```


6. You're ready. Start by running the chat script:
   ```
   python cli/chat.py
   ```

## Usage

- To start a new chat: `python cli/chat.py`
- To review chats: `python cli/review_chat.py`
- To compress chats: `python cli/compress_chat.py`
- To expand chats: `python cli/expand_chat.py`

## Advanced Features

- Compression and Expansion of chat data
- chat Replay functionality
- Flexible Configuration system

## Security and Privacy

- Secure API key storage
- Compressed data stored separately
- .gitignore file to prevent accidental commits of sensitive data

## Future Developments

- TBD

For more information on each script, run it with the \`--help\` flag or refer to the inline documentation within each file.
