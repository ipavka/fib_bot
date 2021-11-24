# Telegram bot по записи расходов
##### Записывает расходы и распределяет по категориям. Например, запись 300 мтс будет записана в категорию "Связь" Отправленные записи валидируются и по описанию определяется нужная категория и записывается, если такого описания нет в категориях, предлагает выбрать категорию для записи и запишет ее.

## requirements
- requirements.txt

## Task modules
```
# main.py - бизнес логика, запуск
# for_func.py - отдельная часть логики
# for_select.py - SQL запросы в БД
# make_data.py - работа с датами
# keyboards.py - кнопки Telegram
# create_tables.ddl -  структура таблиц БД
# insert_data.ddl - базовый алиасы бля расходов
# config.py - креды
```

##### - Запись расхода и дохода



##### - Крайние записи расхода и дохода



##### - Подробные крайние записи расхода и дохода



##### - Добавление нового алиаса в расход



##### - Добавление нового алиаса в доход



##### - Удаление записи расхода



##### - Удаление записи дохода