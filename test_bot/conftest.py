import pytest
import os
from telethon import TelegramClient
from telethon.sessions import StringSession


api_id = int(os.environ["23421683"])
api_hash = os.environ["c7db1ff433f4d083f69f808e11a98bbd"]
session_str = os.environ["6278975621:AAGOEe_-MoGxGZgvE26ywIFOReSTxD1Q8K8/test"]


@pytest.fixture(scope="session")
async def client() -> TelegramClient:
    client = TelegramClient(
        StringSession(session_str), api_id, api_hash,
        sequential_updates=True
    )
    await client.connect()
    await client.get_me()
    await client.get_dialogs()

    yield client

    await client.disconnect()
    await client.disconnected