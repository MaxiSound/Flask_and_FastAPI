# Задание №3.
# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.
# Задание №4.
# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными
# пользователей и обновлять их в базе данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Реализуйте валидацию данных запроса и ответа.
# Задание №5.
# Создать API для удаления информации о пользователе из базы данных.
# Приложение должно иметь возможность принимать DELETE запросы и
# удалять информацию о пользователе из базы данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Реализуйте проверку наличия пользователя в списке и удаление его из
# списка.
# Задание №6.
# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.

import logging
from fastapi import Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import logging
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI()
templates = Jinja2Templates(directory="templates")
user_list = []


class User(BaseModel):
    user_id: int
    name: str
    email: Optional[str] = None
    password: str


@app.get("/")
async def start():
    logger.info('Мы на стартовой странице')
    return {"Начинаем увлекательное приклеючение по миру FastAPI": True}


@app.post("/user/")
async def create_user(user: User):
    logger.info('Отработал POST запрос.')
    user_list.append(user)
    logger.info(user_list)
    return user


@app.put("/user/{user_id}")
async def update_item(user_id: int, new_user: User):
    logger.info(f'Отработал PUT запрос для user_id = {user_id}.')
    for i in user_list:
        if i.user_id == user_id:
            i.name = new_user.name
            i.email = new_user.email
            i.password = new_user.password
    logger.info(user_list)
    return {"user_id": user_id, "user": new_user}


@app.delete("/user/{user_id}")
async def delete_item(user_id: int):
    for i in user_list:
        if i.user_id == user_id:
            user_list.remove(i)
    logger.info(user_list)
    return {"user_id": user_id}


@app.get("/userlist", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("user.html", {"request": request, "user": user_list})
