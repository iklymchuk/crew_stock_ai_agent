<p align="center">
  <img src="https://github.com/user-attachments/assets/fbf1f1a8-cb3c-4f73-8a8c-58da9a4e84b3" width="50%" />
</p>

# MyStockPicker

## Goal
crew_stock_ai_agent is an agent-based prototype that discovers and evaluates promising publicly traded companies by scanning current news, performing targeted financial research, generating concise reports, and delivering short notifications via Telegram. The end goal is to help a user quickly identify and justify one investable idea each run.

## Technology stack
- Python 3.11+ (or latest compatible)
- Crewai agent framework (project entrypoint: `crewai run`)
- Web Search with Serper Dev (Google Search API)
- Natural language processing / summarization: configurable LLM (openai/gpt-4o-mini)
- Notifications: Telegram Bot API (python-telegram-bot or equivalent)
- Configuration: dotenv (.env) for API keys and bot tokens
- CI/Dev tooling: project uses `uv sync` for dependency sync (adjust per environment)

## Features
- Trending company discovery
  - Searches the latest news for a specified sector or query
  - Returns 2–3 companies that are currently trending for deeper research
- Financial research and analysis
  - Aggregates news, public filings and key metrics for each candidate
  - Produces a structured research summary per company
- Stock selection & rationale
  - Compares research results and selects the best candidate for investment
  - Provides concise rationale and notes on companies not chosen
- Reporting & notifications
  - Generates a human-readable report (Markdown) and store into output/
  - Store company findings in json format into output/
  - Sends short notifications about the selected company via Telegram
- Configurable inputs
  - Sector, date range and other parameters can be adjusted in `main.py` run inputs
- Extensible and testable
  - Designed to be extended with alternate search providers, richer analysis, and unit tests

## Installation
To install or sync dependencies (project-specific tool):
```bash
uv sync
```
(Replace with your preferred environment setup commands if needed, e.g., pip/poetry/conda.)

## Usage
Run the agent:
```bash
crewai run
```
Adjust input parameters for sector, date or other options inside the `run` function in `main.py`.

## Configuration
Create a `.env` file (example entries):
```
OPENAI_API_KEY=your_llm_api_key_here
MODEL=your_llm_model_here
SERPER_API_KEY=your_serper_api_key_here
TG_BOT_TOKEN = your_telegram_bot_token_here
TG_CHANNEL_ID = your_telegram_channel_id_here
```
