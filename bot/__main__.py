import asyncio
import logging

from pyrogram import idle

from . import app, commands, download


async def main():
    logging.info("Registering commands...")
    commands.register(app)

    try:
        await app.start()

        logging.info("Starting download manager...")
        manager_task = asyncio.create_task(download.manager.run())

        me = await app.get_me()
        logging.info(f"Bot started! I'm @{me.username}")

        await idle()

    except KeyboardInterrupt:
        logging.info("KeyboardInterrupt: Stopping bot...")
        manager_task.cancel()
        await app.stop()
        logging.info("Bot stopped due to KeyboardInterrupt!")
        return 1

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        manager_task.cancel()
        await app.stop()
        logging.info("Bot stopped due to error!")
        return 1

    finally:
        logging.info("Stopping download manager...")
        manager_task.cancel()
        await manager_task

    logging.info("Bot stopped gracefully!")
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()
