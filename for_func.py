from aiogram import types
from config import user_n
from for_select import insert_costs, alias_for_filter_income, alias_for_filter, insert_income
from make_date import make_date, ru_date_unix
import json as js
import keyboards as kb

orig_mess = []  # Словарь с исходным сообщением


async def write_down_categories(message: types.Message):
    await message.answer(f'В какую категорию добавить?', reply_markup=kb.menu_costs)


async def write_down_categories_income(message: types.Message):
    await message.answer(f'В какую категорию добавить?', reply_markup=kb.menu_income)


async def update_text(message: types.Message, name_cat):
    # Функция для обновления текста с отправкой той же клавиатуры
    await message.edit_text(f"Добавить в {name_cat}?", reply_markup=kb.menu_costs)


async def update_text_income(message: types.Message, name_cat):
    # Функция для обновления текста с отправкой той же клавиатуры
    await message.edit_text(f"Добавить в {name_cat}?", reply_markup=kb.menu_income)


def message_again(mes: dict):
    date = make_date(mes['date'])  # конвертируем дату
    date_view = ru_date_unix(mes['date'])
    # берм id и ник (точнее id, так как ник есть не у всех)
    user_id = mes['from']['id']
    user_name = user_n(user_id)  # user_n функция из config.py
    sum_of_money = mes['text'].split()[0]
    for_what = ' '.join(mes['text'].split()[1:])
    category = alias_for_filter(mes['text'].split()[1])
    categ_code = category[0]
    insert_costs(sum_of_money, for_what, categ_code, date_view, user_id, user_name, date)
    orig_mess.clear()


def message_again_income(mes: dict):
    date = make_date(mes['date'])  # конвертируем дату
    date_view = ru_date_unix(mes['date'])
    # берм id и ник (точнее id, так как ник есть не у всех)
    user_id = mes['from']['id']
    user_name = user_n(user_id)  # user_n функция из config.py
    sum_of_money = mes['text'].split()[0].replace('@', '')
    for_what = ' '.join(mes['text'].split()[1:])
    category = alias_for_filter_income(mes['text'].split()[1])
    categ_code = category[0]
    insert_income(sum_of_money, for_what, categ_code, date_view, user_id, user_name, date)
    orig_mess.clear()


async def write_down_expenses(message: types.Message):
    dict_json = js.loads(message.as_json())  # данные берем json формате
    date = make_date(dict_json['date'])  # конвертируем дату
    date_view = ru_date_unix(dict_json['date'])
    # берм id и ник (точнее id, так как ник есть не у всех)
    user_id = dict_json['from']['id']
    user_name = user_n(user_id)  # user_n функция из config.py
    sum_of_money = message.text.split()[0]
    for_what = ' '.join(message.text.split()[1:])
    category = alias_for_filter(message.text.split()[1])
    categ_code = category[0]
    categ_name = category[1]
    insert_costs(sum_of_money, for_what, categ_code, date_view, user_id, user_name, date)
    await message.answer(f'Это запись в РАСХОД\n'
                         f'{sum_of_money} << Сумма\n'
                         f'{for_what} << Что куплено\n'
                         f'Категория: {categ_name}')


async def write_down_income(message: types.Message):
    dict_json = js.loads(message.as_json())  # данные берем json формате
    date = make_date(dict_json['date'])  # конвертируем дату
    date_view = ru_date_unix(dict_json['date'])
    # берм id и ник (точнее id, так как ник есть не у всех)
    user_id = dict_json['from']['id']
    user_name = user_n(user_id)  # user_n функция из config.py
    sum_of_money = message.text.split()[0].replace('@', '')
    for_what = ' '.join(message.text.split()[1:])
    category = alias_for_filter_income(message.text.split()[1])
    categ_code = category[0]
    categ_name = category[1]
    insert_income(sum_of_money, for_what, categ_code, date_view, user_id, user_name, date)
    await message.answer(f'Это запись в ДОХОД\n'
                         f'{sum_of_money} << Сумма\n'
                         f'{for_what} << Источник\n'
                         f'Категория: {categ_name}')


if __name__ == '__main__':
    pass
