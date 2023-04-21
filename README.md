# praktikum_new_diplom
[![foodgram_project_workflow](https://github.com/MrKarlkarlsn/foodgram-project-react/actions/workflows/foodgram_project_workflow.yml/badge.svg)](https://github.com/MrKarlkarlsn/foodgram-project-react/actions/workflows/foodgram_project_workflow.yml)
# Описание проекта
Сайт Foodgram, «Продуктовый помощник». Это онлайн-сервис и API для него. На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
# Технологии

- [Python 3.8.8](https://www.python.org/downloads/release/python-388/)
- [Django 2.2.16](https://www.djangoproject.com/download/)
- [Django Rest Framework 3.13.1](https://www.django-rest-framework.org/)
- [PostgreSQL 13.0](https://www.postgresql.org/download/)
- [gunicorn 20.0.4](https://pypi.org/project/gunicorn/)
- [nginx 1.21.3](https://nginx.org/ru/download.html)

# Контейнер

- [Docker 20.10.14](https://www.docker.com/)
- [Docker Compose 2.4.1](https://docs.docker.com/compose/)

### Использование CI/CD (GitHub Actions):
В переменные окружения (Secrets) добавить секреты из файла .env, а также:
```sh
DOCKER_PASSWORD=<пароль от DockerHub>
DOCKER_USERNAME=<имя пользователя DockerHub>
DOCKER_REPO_NAME=<имя репозитория(например, foodgram)>

SSH_HOST=<IP сервера>
SSH_USERNAME=<username для подключения к серверу>
PASSPHRASE=<пароль для использования SSH-ключа>
SSH_KEY=<ваш приватный SSH-ключ>

TELEGRAM_TO=<ID чата для получения уведомления>
TELEGRAM_TOKEN=<токен Telegram-бота>
```
*Workflow при пуше в master-ветку проверит код на соответствие PEP8, пересоберет и опубликует на DockerHub образ для backend-части проекта, задеплоит проект на сервере, в случае успеха отправит сообщение в Telegram*


# Примеры запросов

**GET**: http://127.0.0.1:8000/api/users/ 
Пример ответа:
```json
{
 "count": 123,
 "next": "http://127.0.0.1:8000/api/users/?page=4",
 "previous": "http://127.0.0.1:8000/api/users/?page=2",
 "results": [
 {
 "email": "[email protected]",
 "id": 0,
 "username": "test.user",
 "first_name": "Test",
 "last_name": "User",
 "is_subscribed": false
 }
 ]
}
```

**POST**: http://127.0.0.1:8000/api/users/ 
Тело запроса:
```json
{
 "email": "[email protected]",
 "username": "test.user",
 "first_name": "Test",
 "last_name": "User",
 "password": "Qwerty123"
}
```
Пример ответа:
```json
{
"email": "[email protected]",
"id": 0,
"username": "test.user",
"first_name": "Test",
"last_name": "User"
}
```

**GET**: http://127.0.0.1:8000/api/recipes/ 
Пример ответа:
```json
{
 "count": 123,
 "next": "http://127.0.0.1:8000/api/recipes/?page=4",
 "previous": "http://127.0.0.1:8000/api/recipes/?page=2",
 "results": [
 {
 "id": 0,
 "tags": [
 {
 "id": 0,
 "name": "Завтрак",
 "color": "#E26C2D",
 "slug": "breakfast"
 }
 ],
 "author": {
 "email": "[email protected]",
 "id": 0,
 "username": "test.user",
 "first_name": "Test",
 "last_name": "User",
 "is_subscribed": false
 },
 "ingredients": [
 {
 "id": 0,
 "name": "Картофель отварной",
 "measurement_unit": "г",
 "amount": 1
 }
 ],
 "is_favorited": true,
 "is_in_shopping_cart": true,
 "name": "string",
 "image": "http://127.0.0.1:8000/media/recipes/images/image.jpeg",
 "text": "string",
 "cooking_time": 1
 }
 ]
}
```
Автор - Кузьмин Артём : https://github.com/MrKarlkarlsn

