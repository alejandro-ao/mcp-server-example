# MCP Server Example

This repository contains an implementation of a Model Context Protocol (MCP) server for educational purposes. This code demonstrates how to build a functional MCP server that can integrate with various LLM clients.

To follow the complete tutorial, please refer to the [YouTube video tutorial](https://youtu.be/Ek8JHgZtmcI).

## What is MCP?

MCP (Model Context Protocol) is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications - it provides a standardized way to connect AI models to different data sources and tools.

![MCP Diagram](img/mcp-diagram-bg.png)

### Key Benefits

- A growing list of pre-built integrations that your LLM can directly plug into
- Flexibility to switch between LLM providers and vendors
- Best practices for securing your data within your infrastructure

## Architecture Overview

MCP follows a client-server architecture where a host application can connect to multiple servers:

- **MCP Hosts**: Programs like Claude Desktop, IDEs, or AI tools that want to access data through MCP
- **MCP Clients**: Protocol clients that maintain 1:1 connections with servers
- **MCP Servers**: Lightweight programs that expose specific capabilities through the standardized Model Context Protocol
- **Data Sources**: Both local (files, databases) and remote services (APIs) that MCP servers can access

## Core MCP Concepts

MCP servers can provide three main types of capabilities:

- **Resources**: File-like data that can be read by clients (like API responses or file contents)
- **Tools**: Functions that can be called by the LLM (with user approval)
- **Prompts**: Pre-written templates that help users accomplish specific tasks

## System Requirements

- Python 3.10 or higher
- MCP SDK 1.2.0 or higher
- `uv` package manager

## Getting Started

### Installing uv Package Manager

On MacOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Make sure to restart your terminal afterwards to ensure that the `uv` command gets picked up.

### Project Setup

1. Create and initialize the project:
```bash
# Create a new directory for our project
uv init mcp-server
cd mcp-server

# Create virtual environment and activate it
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
uv add "mcp[cli]" httpx
```

2. Create the server implementation file:
```bash
touch main.py
```

### Running the Server

1. Start the MCP server:
```bash
uv run main.py
```

2. The server will start and be ready to accept connections

## Connecting to Claude Desktop

1. Install Claude Desktop from the official website
2. Configure Claude Desktop to use your MCP server:

Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
    "mcpServers": {
        "mcp-server": {
            "command": "uv",  # It's better to use the absolute path to the uv command
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/YOUR/mcp-server",
                "run",
                "main.py"
            ]
        }
    }
}
```

3. Restart Claude Desktop

## Troubleshooting

If your server isn't being picked up by Claude Desktop:

1. Check the configuration file path and permissions
2. Verify the absolute path in the configuration is correct
3. Ensure uv is properly installed and accessible
4. Check Claude Desktop logs for any error messages

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
