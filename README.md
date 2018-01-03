# Ближайшие бары

Данный проект создан с целью поиска бара рядом с пользователем, а также бара с наименьшим и наибольшим числом мест. 

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
При запуске скрипта ему необходимо передать текущие координаты пользователя, а также путь до json-файла с данными о барах Москвы.

Запуск на Linux:

```bash

$ python bars.py 37 50 bars.json 
#Пример вывода
Наименьший бар {'geometry': {'coordinates': [37.53750797872186, 55.837926047147974], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 4, 'RowId': None, 'Attributes': {'global_id': 637413793, 'Name': 'Сушистор', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Северный административный округ', 'District': 'район Коптево', 'Address': 'город Москва, Михалковская улица, дом 8', 'PublicPhone': [{'PublicPhone': '(495) 230-00-00'}], 'SeatsCount': 0, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
Наибольший бар {'geometry': {'coordinates': [37.638228500803905, 55.70111462924677], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 4, 'RowId': None, 'Attributes': {'global_id': 637548020, 'Name': 'Спорт бар «Красная машина»', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Южный административный округ', 'District': 'Даниловский район', 'Address': 'Автозаводская улица, дом 23, строение 1', 'PublicPhone': [{'PublicPhone': '(905) 795-15-84'}], 'SeatsCount': 450, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
Ближайший бар {'geometry': {'coordinates': [37.0, 55.2], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 4, 'RowId': None, 'Attributes': {'global_id': 637516719, 'Name': 'Корпорация Бар', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Троицкий административный округ', 'District': 'поселение Роговское', 'Address': 'город Москва, улица Сретенка, дом 4', 'PublicPhone': [{'PublicPhone': 'нет телефона'}], 'SeatsCount': 110, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
```
Запуск на Windows происходит аналогично.
Ссылка для скачивания на файл с информацией о барах:
https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
