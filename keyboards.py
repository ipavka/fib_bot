from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Кнопки для расхода
costs_1 = InlineKeyboardButton('Продукты', callback_data='ct_products')
costs_2 = InlineKeyboardButton('Жильё', callback_data='ct_housing')
costs_3 = InlineKeyboardButton('Телефон_Интернет', callback_data='ct_telephone')
costs_4 = InlineKeyboardButton('Товары_для_дома', callback_data='ct_housGoods')
costs_5 = InlineKeyboardButton('Книги_Курсы', callback_data='ct_education')
costs_6 = InlineKeyboardButton('Интертеймент', callback_data='ct_Entertainment')
costs_7 = InlineKeyboardButton('ДжанкФуд', callback_data='ct_junkFood')
costs_8 = InlineKeyboardButton('Прочие', callback_data='ct_other')
costs_9 = InlineKeyboardButton('Аптека', callback_data='ct_pharmacy')
costs_10 = InlineKeyboardButton('Проезд_Транспорт', callback_data='ct_transit')
costs_agree = InlineKeyboardButton('Подтвердить'u'\U00002705', callback_data='ct_finish')
costs_cancel = InlineKeyboardButton('Отменить'u'\U0000274C', callback_data='ct_cancel')
menu_costs = InlineKeyboardMarkup(row_width=2)
menu_costs.add(costs_1, costs_2, costs_3, costs_4, costs_5, costs_6, costs_7,
               costs_8, costs_9, costs_10)\
                .add(costs_agree).add(costs_cancel)


# Кнопки для дохода
income_1 = InlineKeyboardButton('work', callback_data='in_work')
income_2 = InlineKeyboardButton('Наличка', callback_data='in_cash')
income_3 = InlineKeyboardButton('Прочий_Доход', callback_data='in_otherIn')
income_agree = InlineKeyboardButton('Подтвердить'u'\U00002705', callback_data='in_finish')
income_cancel = InlineKeyboardButton('Отменить'u'\U0000274C', callback_data='in_cancel')
menu_income = InlineKeyboardMarkup(row_width=2)
menu_income.add(income_1, income_2, income_3).add(income_agree).add(income_cancel)