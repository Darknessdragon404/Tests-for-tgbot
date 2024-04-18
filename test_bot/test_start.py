from pytest import mark
from telethon import TelegramClient
from telethon.tl.custom.message import Message

@mark.asyncio
async def test_start(client: TelegramClient):

    with client.conversation("@DSlayerBot", timeout=5) as conv:
        await conv.send_message("/start")
        resp: Message = await conv.get_response()
        assert "Приветствую!" in resp.raw_text
        assert resp.button_count == 5
