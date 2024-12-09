# Pydantic AI Dice Game

A simple interactive dice game built with Pydantic AI and Google's Gemini model. The game features a friendly AI that manages the game state, rolls dice, and interacts with players by name.

## Quick Start

1. Setup environment:
```bash
uv sync
source .venv/bin/activate

# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies using uv
uv pip install -e .
```

2. Create `.env` file:
```bash
GEMINI_API_KEY=your_api_key_here
```

3. Run the game:
```bash
python main.py
```

## Project Structure

```
pydantic-ai-test/
├── .env                  # Environment variables
├── main.py              # Main game logic
├── pyproject.toml       # Project dependencies and metadata
└── README.md            # This file
```

## Features

- 🎲 Simulated six-sided die roll
- 👤 Personalized player interaction
- 📅 Real-time date display
- 🤖 AI-powered responses using Gemini 1.5 Flash

## Key Components

### Agent Configuration

The game uses a Pydantic AI agent configured with Gemini 1.5 Flash:

```python
agent = Agent(
    "gemini-1.5-flash",
    deps_type=str,
    system_prompt=(
        "You're a dice game..."
    )
)
```

### Tools

1. **roll_die()**: Simulates rolling a six-sided die
2. **get_player_name()**: Retrieves the current player's name
3. **System prompts**: Add personalization and date information

## Dependencies

- asyncio>=3.4.3
- pydantic-ai[logfire]>=0.0.11
- python-dotenv>=1.0.1
- ruff>=0.8.2

## Development

### Adding New Features

To add new game features:

1. Define new tools using `@agent.tool` or `@agent.tool_plain` decorators
2. Add system prompts using `@agent.system_prompt`
3. Update the main game loop in `main()`

### Logging

The project uses logfire for logging. Configure logging parameters in your code:

```python
logfire.configure()
```

## Common Issues & Solutions

1. **API Key Issues**
   - Ensure `.env` file exists
   - Verify API key is valid
   - Check environment variable loading

2. **Dependency Issues**
   - Run `uv pip install -e .`
   - Ensure Python version >= 3.9
   - If uv is not installed, install it via: `curl -LsSf https://astral.sh/uv/install.sh | sh`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project uses Pydantic AI and requires appropriate licensing for the Gemini API. Ensure you comply with Google's terms of service when using the Gemini API.
