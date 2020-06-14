import os
import sys
import time
import random
from telethon.tl import functions
from utils import create_client, confirmation

try:
    client = create_client()
    client.start()

    dialog_list = {}
    for dialog in client.get_dialogs():
        if not dialog.is_user and not dialog.is_group: continue

        dialog_list.update({str(dialog.id): dialog})
        print("{:>14}: {}".format(dialog.id, dialog.name))

    selected_dialog = input("Select target dialog: ")
    if selected_dialog not in dialog_list:
        print("Incorrect chat id. Exit.")
        sys.exit(1)

    target_chat = dialog_list[selected_dialog]

    confirmation("REALLY delete all YOUR messages? ")
    confirmation("From chat \"{}\"? ".format(target_chat.name))

    m_list = []
    for m in client.iter_messages(
        target_chat, from_user='me'
    ): m_list.append(m.id)

    confirmation("We have {} messages. Delete them? ".format(len(m_list)))

    client.delete_messages(target_chat, m_list, revoke=True)
    print("Finished.")
finally:
    client.disconnect()
