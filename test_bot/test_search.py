from pytest import mark
from telethon import TelegramClient
from telethon.tl.custom.message import Message

@mark.asyncio
async def test_search(client: TelegramClient):

    with client.conversation("@DSlayerBot", timeout=5) as conv:
        await conv.send_message("/search")
        resp: Message = await conv.get_response()
        assert "Введите имя и фамилию" in resp.raw_text
        await conv.send_message("фффывй")
        assert "Это явно не писатель" in resp.raw_text
        await conv.send_message("фффывй фйй")
        assert "По вашему запросу ничего не найдено" in resp.raw_text
