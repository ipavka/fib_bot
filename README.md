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

<img src="https://user-images.githubusercontent.com/72130001/143205783-37165825-3f7e-4343-9510-ea2c18f7c8fe.gif" width="300" height="500"/>

##### - Крайние записи расхода и дохода

<img src="https://user-images.githubusercontent.com/72130001/143206011-c0776b6e-fd17-4f14-b7cb-f672ee1ef3f9.gif" width="300" height="500"/>

##### - Подробные крайние записи расхода и дохода

<img src="https://user-images.githubusercontent.com/72130001/143206029-8480500f-4436-4304-9626-0702dd484154.gif" width="300" height="500"/>

##### - Добавление нового алиаса в расход

<img src="https://user-images.githubusercontent.com/72130001/143206051-dca6ae32-7227-4dd7-93d3-82b259be1b64.gif" width="300" height="500"/>

##### - Добавление нового алиаса в доход

<img src="https://user-images.githubusercontent.com/72130001/143206105-e8162eed-8886-4112-a283-5611db5e3ddf.gif" width="300" height="500"/>

##### - Удаление записи расхода

<img src="https://user-images.githubusercontent.com/72130001/143206132-be868820-7fa9-416b-badc-85ed87524bfd.gif" width="300" height="500"/>

##### - Удаление записи дохода

<img src="https://user-images.githubusercontent.com/72130001/143206149-ea7514d5-6aa0-4c34-827f-04ec3c3da041.gif" width="300" height="500"/>
