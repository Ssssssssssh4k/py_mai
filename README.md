# Лабораторная работа

## Задание

1) Создаем новый проект в PyCharm
2) Сервер на FLASK
3) Написать роут /, который редиректнет на роут /users
4) роут /users Выведет всех юзеров из словаря users
- в виде clickable ссылок
- <url>/user/<username или id>
5) Роут /user/<username или id> проверит пользователя в словаре users, и если нет, то вернет 404

## Запуск программы

pip install -r requirements.txt
python ./main.py

## Пример выполнения программы

### Пользователь есть в базе

![Пользователь есть в базе](https://myoctocat.com/assets/images/base-octocat.svg)

### Пользователь не обнаружен

![Пользователь не обнаружен](https://myoctocat.com/assets/images/base-octocat.svg)