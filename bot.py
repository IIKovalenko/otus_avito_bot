# coding: utf-8
import bot_helpers


if __name__ == '__main__':
    updater = bot_helpers.get_configured_updater()
    bot_helpers.add_restart_handler(
        updater,
        admin_username='@melevir',
    )
    bot_helpers.start_bot(updater)
