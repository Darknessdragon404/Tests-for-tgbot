from pytest import mark
from telethon import TelegramClient
from telethon.tl.custom.message import Message

@mark.asyncio
async def test_help(client: TelegramClient):

    with client.conversation("@DSlayerBot", timeout=5) as conv:
        await conv.send_message("/notes")
        resp: Message = await conv.get_response()
        assert "Выберите желаемую операцию" in resp.raw_text
        assert resp.button_count == 5
        await conv.send_message("/give_notes")
        resp: Message = await conv.get_response()
        assert "У вас нет заметок" in resp.raw_text
        await conv.send_message("/edit_notes")
        resp: Message = await conv.get_response()
        assert "Введите название заметки"  in resp.raw_text
        await conv.send_message("message")
        resp: Message = await conv.get_response()
        assert "Такой заметки у вас нет" in resp.raw_text
        await conv.send_message("/delete_notes")
        assert "Введите" in resp.raw_text
        await conv.send_message("message")
        resp: Message = await conv.get_response()
        assert "Такой заметки у вас нет" in resp.raw_text