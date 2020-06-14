import os, sys
from const import API_ID, API_HASH
from telethon import TelegramClient, sync

def confirmation(message) -> None:
    while True:
        ans = input(message).lower()
        if ans not in ("y", "n"): print("y/n only")
        elif ans == "n": sys.exit(1)
        elif ans == "y": break


def select_session_name() -> str:
    SESS_DIR = "./sessions/"
    SESS_DIR_new = input(
        "Directory with sessions "
        "(press ENTER to leave default): ")
    if len(SESS_DIR_new): SESS_DIR = SESS_DIR_new

    print("\nAvailable session files:")
    sess_list = os.listdir(SESS_DIR)
    sess_list.sort()
    for i in range(len(sess_list)):
        print("{:>2} \"{}\"".format(
            "#" + str(i), sess_list[i].replace(".session", "")))
    return SESS_DIR + sess_list[int(input("Select session: "))]

def create_client() -> TelegramClient:
    selected_sess = select_session_name()
    return TelegramClient(selected_sess, API_ID, API_HASH)
