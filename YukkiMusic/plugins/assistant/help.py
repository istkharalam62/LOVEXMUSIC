import logging

from pyrogram import Client, filters

from YukkiMusic import app

from .. import all


@all.on_message(filters.command(["help"]))
async def inline_help_menu(client: Client, message):
    try:
        bot_results = await client.get_inline_bot_results(
            f"@{app.username}", "help_menu"
        )
        await client.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=bot_results.query_id,
            result_id=bot_results.results[0].id,
        )
        try:
            await message.delete()
        except:
            pass
    except Exception as e:
        logging.exception(e)


@all.on_message(filters.command(["ping"]))
async def ping(c, m):
    await m.reply_text("I am alive")