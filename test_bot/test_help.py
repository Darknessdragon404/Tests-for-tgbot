from pytest import mark
from telethon import TelegramClient
from telethon.tl.custom.message import Message

@mark.asyncio
async def test_help(client: TelegramClient):

    with client.conversation("@DSlayerBot", timeout=5) as conv:
        await conv.send_message("/help")
        resp: Message = await conv.get_response()
        assert "открывает раздел взаимодействия!" in resp.raw_text
        assert "/notes - открывает раздел с заметками." in resp.raw_text