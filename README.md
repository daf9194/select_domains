# Подбор похожих доменов

## Описание
Для оперативного поиска фишинговых ресурсов может применяться следующая
логика:
- задается ключевое слово
- при помощи набора стратегий (например, одна из них — подстановка схожих по написанию символов) формируется расширенный набор ключевых слов 
- полученное на предыдущем шаге множество перемножается на некоторое множество доменных зон (ru, com, net, org, biz и т. п.)
- отправляются dns-запросы с целью получить IP-адрес по каждому из элементов списка
- домены, по которым удалось определить ip, попадают в отчет

### Стратегии
- Стратегии формирования набора ключевых слов описаны в следующей таблице:
![Пример](https://raw.githubusercontent.com/daf9194/select_domains/master/img/scr_3.png)

## Установка приложения
1. Клонировать текущий репозиторий.
2. Установка дополнительных библиотек не требуется. Приложение использует только встроенные библиотеки Python3.
3. Запуск скрипта  `python3 main.py` .
