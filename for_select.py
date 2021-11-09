import sqlite3

from config import NAME_DB

conn = sqlite3.connect(NAME_DB, check_same_thread=False)
cur = conn.cursor()


def select_amount_row_costs(table, amount):
    """ Выборка из РАСХОД с указанием кол-ва записей """
    data_str = []
    data_str_1 = []
    cur.execute(f"SELECT sum_of_money_co, descrip_co, cost_id "
                f"FROM {table} "
                f"ORDER BY created "
                f"DESC LIMIT {amount}")
    result = cur.fetchall()
    if result:
        for i in result:
            data_str.append(i)
        for num, el in enumerate(data_str, 1):
            data_str_1.append(f'{num}. "{el[0]}" *{el[1]}* - удалить /del_c{el[2]}')
        return "\n".join(map(str, data_str_1))
    return


def select_amount_row_income(table, amount):
    """ Выборка из ДОХОД с указанием кол-ва записей """
    data_str = []
    data_str_1 = []
    cur.execute(f"SELECT sum_of_money_in, descrip_in, income_id "
                f"FROM {table} "
                f"ORDER BY created "
                f"DESC LIMIT {amount}")
    result = cur.fetchall()
    if result:
        for i in result:
            data_str.append(i)
        for num, el in enumerate(data_str, 1):
            data_str_1.append(f'{num}. "{el[0]}" *{el[1]}* - удалить /del_i{el[2]}')
        return "\n".join(map(str, data_str_1))
    return


def select_amount_row_costs_data(table, amount):
    """ Выборка из РАСХОД с полной инф. """
    data_str = []
    data_str_1 = []
    cur.execute(f"SELECT sum_of_money_co, descrip_co, category, view_date "
                f"FROM {table} "
                f"ORDER BY created "
                f"DESC LIMIT {amount}")
    result = cur.fetchall()
    if result:
        for i in result:
            data_str.append(i)
        for num, el in enumerate(data_str, 1):
            data_str_1.append(f'{num}. "{el[0]}" *{el[1]}* *{el[2]}*  *{el[3]}*')
        return "\n".join(map(str, data_str_1))
    return


def select_amount_row_income_data(table, amount):
    """ Выборка из ДОХОД с полной инф. """
    data_str = []
    data_str_1 = []
    cur.execute(f"SELECT sum_of_money_in, descrip_in, category, view_date "
                f"FROM {table} "
                f"ORDER BY created "
                f"DESC LIMIT {amount}")
    result = cur.fetchall()
    if result:
        for i in result:
            data_str.append(i)
        for num, el in enumerate(data_str, 1):
            data_str_1.append(f'{num}. "{el[0]}" *{el[1]}* *{el[2]}*  *{el[3]}*')
        return "\n".join(map(str, data_str_1))
    return


def delete_by_row_id_costs(table, row):
    """ Удалить запись в РАСХОДАХ таблице по id"""
    cur.execute(f"DELETE "
                f"FROM {table} "
                f"WHERE cost_id = {row}")
    conn.commit()


def delete_by_row_id_income(table, row):
    """ Удалить запись в ДОХОДАХ таблице по id"""
    cur.execute(f"DELETE "
                f"FROM {table} "
                f"WHERE income_id = {row}")
    conn.commit()


def delete_row_costs(table):
    """ Удалить крайнею запись в РАСХОДЕ """
    cur.execute(f"DELETE "
                f"FROM {table} "
                f"WHERE cost_id = (SELECT MAX(cost_id) FROM {table})")
    conn.commit()


def delete_row_income(table):
    """ Удалить крайнею запись в ДОХОДЕ """
    cur.execute(f"DELETE "
                f"FROM {table} "
                f"WHERE income_id = (SELECT MAX(income_id) FROM {table})")
    conn.commit()


def sel_after_upd():
    cur.execute("SELECT sum_of_money_co, descrip_co, category "
                "FROM costs "
                "WHERE cost_id = (SELECT MAX(cost_id) FROM costs)")
    result = cur.fetchone()
    return result


def sel_after_upd_income():
    cur.execute("SELECT sum_of_money_in, descrip_in, category "
                "FROM income "
                "WHERE income_id = (SELECT MAX(income_id) FROM income)")
    result = cur.fetchone()
    return result


def update_category(alias, codname):
    cur.execute(f'UPDATE categories '
                f'SET included = included || " " || "{alias}"'
                f'WHERE name = "{codname}"')
    conn.commit()


def insert_costs(sum_of_money, for_what, categ_code, date_view, user_id, user_name, date):
    cur.execute(
        "INSERT INTO `costs`(sum_of_money_co, descrip_co, category, view_date, who_posted_co_id, who_posted_co_nick, "
        "created) "
        "VALUES (?,?,?,?,?,?,?)",
        (sum_of_money, for_what, categ_code, date_view, user_id, user_name, date))
    conn.commit()


def insert_income(sum_of_money, for_what, categ_code, date_view, user_id, user_name, date):
    cur.execute(
        "INSERT INTO `income`(sum_of_money_in, descrip_in, category, view_date, who_posted_in_id, who_posted_in_nick, "
        "created) "
        "VALUES (?,?,?,?,?,?,?)",
        (sum_of_money, for_what, categ_code, date_view, user_id, user_name, date))
    conn.commit()


def alias_for_filter(world):
    """ РАСХОД """
    cod_name_list = ['products', 'housing', 'telephone', 'housGoods', 'education',
                     'Entertainment', 'junkFood', 'other', 'pharmacy', 'transit']
    end = []
    for i in cod_name_list:
        arg = (f'{i}',)
        cur.execute("SELECT included "
                    "FROM categories "
                    "WHERE codename = ?", arg)
        result = ' '.join(cur.fetchall()[0]).split()
        end.append(result)
    if world.lower() in end[0]:
        return 'products', 'Продукты'
    elif world.lower() in end[1]:
        return 'housing', 'Жильё'
    elif world.lower() in end[2]:
        return 'telephone', 'Телефон_Интернет'
    elif world.lower() in end[3]:
        return 'housGoods', 'Товары_для_дома'
    elif world.lower() in end[4]:
        return 'education', 'Книги_Курсы'
    elif world.lower() in end[5]:
        return 'Entertainment', 'Интертеймент'
    elif world.lower() in end[6]:
        return 'junkFood', 'ДжанкФуд'
    elif world.lower() in end[7]:
        return 'other', 'Прочие'
    elif world.lower() in end[8]:
        return 'pharmacy', 'Аптека'
    elif world.lower() in end[9]:
        return 'transit', 'Проезд_Транспорт'
    else:
        return 'other', 'Прочие'


def alias_for_filter_income(world):
    """ ДОХОД """
    cod_name_list = ['cash', 'work', 'otherIn']
    end = []
    for i in cod_name_list:
        arg = (f'{i}',)
        cur.execute("SELECT included "
                    "FROM categories "
                    "WHERE codename = ?", arg)
        result = ' '.join(cur.fetchall()[0]).split()
        end.append(result)
    if world.lower() in end[0]:
        return 'cash', 'Наличка'
    elif world.lower() in end[1]:
        return 'work', 'Безнал'
    elif world.lower() in end[2]:
        return 'otherIn', 'Прочий_Доход'
    else:
        return 'otherIn', 'Прочий_Доход'


def alias_for_filter_handler(world):
    """ Фильтр для 'message_handler' РАСХОД """
    cod_name_list = ['products', 'housing', 'telephone', 'housGoods', 'education',
                     'Entertainment', 'junkFood', 'other', 'pharmacy', 'transit']
    end = []
    for i in cod_name_list:
        arg = (f'{i}',)
        cur.execute("SELECT included "
                    "FROM categories "
                    "WHERE codename = ?", arg)
        result = ' '.join(cur.fetchall()[0]).split()
        end.append(result)
    if world.lower() in end[0]:
        return 'products', 'Продукты'
    elif world.lower() in end[1]:
        return 'housing', 'Жильё'
    elif world.lower() in end[2]:
        return 'telephone', 'Телефон_Интернет'
    elif world.lower() in end[3]:
        return 'housGoods', 'Товары_для_дома'
    elif world.lower() in end[4]:
        return 'education', 'Книги_Курсы'
    elif world.lower() in end[5]:
        return 'Entertainment', 'Интертеймент'
    elif world.lower() in end[6]:
        return 'junkFood', 'ДжанкФуд'
    elif world.lower() in end[7]:
        return 'other', 'Прочие'
    elif world.lower() in end[8]:
        return 'pharmacy', 'Аптека'
    elif world.lower() in end[9]:
        return 'transit', 'Проезд_Транспорт'
    else:
        return 'nothing'


def alias_for_filter_handler_incom(world):
    """ Фильтр для 'message_handler' ДОХОД """
    cod_name_list = ['cash', 'work', 'otherIn']
    end = []
    for i in cod_name_list:
        arg = (f'{i}',)
        cur.execute("SELECT included "
                    "FROM categories "
                    "WHERE codename = ?", arg)
        result = ' '.join(cur.fetchall()[0]).split()
        end.append(result)
    if world.lower() in end[0]:
        return 'cash', 'Наличка'
    elif world.lower() in end[1]:
        return 'work', 'Безнал'
    elif world.lower() in end[2]:
        return 'otherIn', 'Прочий_Доход'
    else:
        return 'nothing'


if __name__ == '__main__':
    pass
