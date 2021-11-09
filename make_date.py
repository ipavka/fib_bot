import datetime as dt
import time


def ru_date_unix(uts):
    """ Принимает в "UTS" формате дату и делает название месяца на русском """
    month_list = ('Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
                  'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря')
    time_str = dt.datetime.fromtimestamp(uts)
    month = (int(time_str.strftime('%m'))-1)
    date = time_str.strftime(f"%d_{month_list[month]}_%Y")
    return date


def make_date(ust):
    """ Делает дату в формате 'datetime' """
    named_tuple = time.localtime(ust)
    date = time.strftime("%Y-%m-%d %H:%M:%S", named_tuple)
    return date


if __name__ == '__main__':
    pass
