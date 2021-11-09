from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import BOT_TOKEN, ADMIN_ID, GUEST_ID
import for_select as fs
import json as js
import for_func as ff

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


def auth(func):
    """Декоратор фильтр на чьи сообщения отвечать"""
    async def wrapper(messages):
        if not str(messages['from']['id']) in [ADMIN_ID, GUEST_ID]:
            return await messages.reply("Access denied...", reply=False)
        return await func(messages)
    return wrapper


@dp.message_handler(commands=['start', 'help'])
@auth
async def send_welcome(message: types.Message):
    await message.answer(f'Вот что я умею\n'
                         f'"120 сыр" - пример как записать РАСХОД\n'
                         f'"@1000 нал" - пример как записать ДОХОД\n'
                         f'"-3" - показать 3(или сколько надо) крайние записей из РАСХОДА\n'
                         f'"+3" - показать 3(или сколько надо) крайние записей из ДОХОДА\n'
                         f'"&-3" - показать 3(или сколько надо) с подробным описанием крайние записей из РАСХОДА\n'
                         f'"&+3" - показать 3(или сколько надо) с подробным описанием крайние записей из ДОХОДА\n'
                         )


user_choice = []


@dp.callback_query_handler(Text(startswith="ct_"))
async def callbacks_costs(call: types.CallbackQuery):
    """ Колбек РАСХОДОВ """
    pars = ff.orig_mess[0]
    arg = ''.join(pars['text'].split()[1])
    action = call.data.split("_")[1]
    if action == "products":
        await ff.update_text(call.message, 'Продукты')
        user_choice.append('Продукты')
    elif action == "housing":
        await ff.update_text(call.message, 'Жильё')
        user_choice.append('Жильё')
    elif action == "telephone":
        await ff.update_text(call.message, 'Телефон_Интернет')
        user_choice.append('Телефон_Интернет')
    elif action == "housGoods":
        await ff.update_text(call.message, 'Товары_для_дома')
        user_choice.append('Товары_для_дома')
    elif action == "education":
        await ff.update_text(call.message, 'Книги_Курсы')
        user_choice.append('Книги_Курсы')
    elif action == "Entertainment":
        await ff.update_text(call.message, 'Интертеймент')
        user_choice.append('Интертеймент')
    elif action == "junkFood":
        await ff.update_text(call.message, 'ДжанкФуд')
        user_choice.append('ДжанкФуд')
    elif action == "other":
        await ff.update_text(call.message, 'Прочие')
        user_choice.append('Прочие')
    elif action == "pharmacy":
        await ff.update_text(call.message, 'Аптека')
        user_choice.append('Аптека')
    elif action == "transit":
        await ff.update_text(call.message, 'Проезд_Транспорт')
        user_choice.append('Проезд_Транспорт')
    elif action == "cancel":
        await call.message.delete_reply_markup()
        await call.message.edit_text(f'ОТМЕНА')
        ff.orig_mess.clear()
        user_choice.clear()
    elif action == "finish":
        fs.update_category(arg,
                           user_choice[-1])  # Добавляем новый алиас в категории
        ff.message_again(ff.orig_mess[0])
        fs.sel_after_upd()
        await call.message.edit_text(
            f'Добавил "{arg}" в категорию "{user_choice[-1]}"\n'
            f'Крайняя запись в расход\n'
            f'# {fs.sel_after_upd()[0]} # {fs.sel_after_upd()[1]} '
            f'# {fs.sel_after_upd()[2]} #')
        user_choice.clear()
    await call.answer()


@dp.callback_query_handler(Text(startswith="in_"))
async def callbacks_income(call: types.CallbackQuery):
    """ Колбек ДОХОДОВ """
    pars = ff.orig_mess[0]
    arg = ''.join(pars['text'].split()[1])
    action = call.data.split("_")[1]
    if action == "cash":
        await ff.update_text_income(call.message, 'Наличка')
        user_choice.append('Наличка')
    elif action == "work":
        await ff.update_text_income(call.message, 'Безнал')
        user_choice.append('Безнал')
    elif action == "otherIn":
        await ff.update_text_income(call.message, 'Прочий_Доход')
        user_choice.append('Прочий_Доход')
    elif action == "cancel":
        await call.message.delete_reply_markup()
        await call.message.edit_text(f'ОТМЕНА')
        ff.orig_mess.clear()
        user_choice.clear()
    elif action == "finish":
        fs.update_category(arg,
                           user_choice[-1])  # Добавляем новый алиас в категории
        ff.message_again_income(ff.orig_mess[0])
        fs.sel_after_upd_income()
        await call.message.edit_text(
            f'Добавил "{arg}" в категорию "{user_choice[-1]}"\n'
            f'Крайняя запись в доход\n'
            f'# {fs.sel_after_upd_income()[0]} # {fs.sel_after_upd_income()[1]} # '
            f'{fs.sel_after_upd_income()[2]} #')
        user_choice.clear()
    await call.answer()


@dp.message_handler(lambda message: message.text[0].isdigit() and len(
    message.text.split()) != 1)
@auth
async def start_func(message: types.Message):
    """ РАСХОД """
    category = fs.alias_for_filter_handler(message.text.split()[1])
    if category == 'nothing':
        ff.orig_mess.append(js.loads(message.as_json()))
        await ff.write_down_categories(message)
    else:
        await ff.write_down_expenses(message)


@dp.message_handler(lambda message: message.text[0].isdigit())
@auth
async def start_func_false(message: types.Message):
    """ Ловим не корректный ввод РАСХОД """
    await message.answer(f'НЕВЕРНО!\n'
                         f'Введи число и описание!\n'
                         f'например " 120 сыр "')


@dp.message_handler(lambda message: message.text.startswith('@') and len(
    message.text.split()) != 1)
@auth
async def incom_write(message: types.Message):
    """ ДОХОД """
    category = fs.alias_for_filter_handler_incom(message.text.split()[1])
    if category == 'nothing':
        ff.orig_mess.append(js.loads(message.as_json()))
        await ff.write_down_categories_income(message)
    else:
        await ff.write_down_income(message)


@dp.message_handler(lambda message: message.text.startswith('@'))
@auth
async def incom_write_false(message: types.Message):
    """ Ловим не корректный ввод ДОХОД """
    await message.answer(f'НЕВЕРНО!\n'
                         f'Введи число и описание!\n'
                         f'например " @1000 нал "')


@dp.message_handler(commands=['delCosts'])
async def process_command_1(message: types.Message):
    """ Удалить крайнею запись из РАСХОД  """
    fs.delete_row_costs("costs")
    await message.answer(f'Удалил из РАСХОД\n'
                         f'Крайние 3 записи\n'
                         f'{fs.select_amount_row_costs("costs", 3)}')


@dp.message_handler(commands=['delIncome'])
async def process_command_1(message: types.Message):
    """ Удалить крайнею запись из ДОХОД  """
    fs.delete_row_income("income")
    await message.answer(f'Удалил из ДОХОД\n'
                         f'Крайние 3 записи\n'
                         f'{fs.select_amount_row_income("income", 3)}')


@dp.message_handler(
    lambda message: message.text.startswith('-') and len(message.text) >= 2)
@auth
async def selection_costs(message: types.Message):
    """Вывод крайних записей в из РАСХОД по указанному кол-ву"""
    await message.answer(
        f'{fs.select_amount_row_costs("costs", message.text.replace("-", ""))}')


@dp.message_handler(
    lambda message: message.text.startswith('+') and len(message.text) >= 2)
@auth
async def selection_income(message: types.Message):
    """Вывод крайних записей в из ДОХОД по указанному кол-ву"""
    await message.answer(
        f'{fs.select_amount_row_income("income", message.text.replace("-", ""))}')


@dp.message_handler(
    lambda message: message.text.startswith('&-') and len(message.text) >= 3)
@auth
async def select_with_data_costs(message: types.Message):
    """Выборка с подробным описанием РАСХОД"""
    row_count = int(message.text[2:])
    await message.answer(
        f'{fs.select_amount_row_costs_data("costs", row_count)}')


@dp.message_handler(
    lambda message: message.text.startswith('&+') and len(message.text) >= 3)
@auth
async def select_with_data_income(message: types.Message):
    """Выборка с подробным описанием ДОХОД"""
    row_count = int(message.text[2:])
    await message.answer(
        f'{fs.select_amount_row_income_data("income", row_count)}')


@dp.message_handler(lambda message: message.text.startswith('/del_c'))
@auth
async def del_costs(message: types.Message):
    """Удаляет одну запись о РАСХОДЕ по её идентификатору"""
    row_id = int(message.text[6:])
    fs.delete_by_row_id_costs('costs', row_id)
    await message.answer(f'Удалил из РАСХОД\n'
                         f'Крайние 3 записи\n'
                         f'{fs.select_amount_row_costs("costs", 3)}')


@dp.message_handler(lambda message: message.text.startswith('/del_i'))
@auth
async def del_income(message: types.Message):
    """Удаляет одну запись о ДОХОДЕ по её идентификатору"""
    row_id = int(message.text[6:])
    fs.delete_by_row_id_income('income', row_id)
    await message.answer(f'Удалил из ДОХОД\n'
                         f'Крайние 3 записи\n'
                         f'{fs.select_amount_row_income("income", 3)}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
