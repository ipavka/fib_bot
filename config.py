import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
GUEST_ID = os.getenv('GUEST_ID')
NAME_DB = os.getenv('NAME_DB')


def user_n(user_id):
    """ Фильтр имени по id """
    if str(user_id) == ADMIN_ID:
        return 'admin'
    elif str(user_id) == GUEST_ID:
        return 'guest'
    else:
        return 'unknown'


if __name__ == '__main__':
    pass
