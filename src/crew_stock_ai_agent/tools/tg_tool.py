import os
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests


class TgMessageInput(BaseModel):
    """A message to be sent to the TG channel"""
    message: str = Field(..., description="A message to be sent to the TG channel")

class TgMessageTool(BaseTool):
    name: str = "Send a message to the TG channel"
    description: str = (
        "This tool is used to send a message to the user."
    )
    args_schema: Type[BaseModel] = TgMessageInput

    def _run(self, message: str) -> str:

        tg_bot_token = os.getenv("TG_BOT_TOKEN")
        tg_channel_id = os.getenv("TG_CHANNEL_ID")

        url = f"https://api.telegram.org/bot{tg_bot_token}/sendMessage"

        payload = {
            "chat_id": tg_channel_id,
            "text": message
        }

        response = requests.post(url, data=payload)
