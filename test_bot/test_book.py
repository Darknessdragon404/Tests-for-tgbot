from pytest import mark
from telethon import TelegramClient
from telethon.tl.custom.message import Message


@mark.asyncio
async def test_help(client: TelegramClient):

    with client.conversation("@DSlayerBot", timeout=5) as conv:
        await conv.send_message("/book")
        resp: Message = await conv.get_response()
        assert "Если хотите взаимодействовать" in resp.raw_text
        message = '1'
        await conv.send_message(message)
        resp = await conv.get_response()
        assert resp.button_count == 5
        await conv.send_message("/give_book")
        resp: Message = await conv.get_response()
        assert "У вас нет прочитанных книг" in resp.raw_text
        await conv.send_message("/edit_book")
        resp: Message = await conv.get_response()
        assert "Введите название книги"  in resp.raw_text
        await conv.send_message("message")
        resp: Message = await conv.get_response()
        assert "Такой книги у вас нет" in resp.raw_text
        await conv.send_message("/delete")
        assert "Какую книгу хотите удалить?" in resp.raw_text
        await conv.send_message("message")
        resp: Message = await conv.get_response()
        assert "Такой книги у вас нет" in resp.raw_text