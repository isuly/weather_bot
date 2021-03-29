# weather_bot
Weather telegram bot


# Инструкция для локального запуска в dev-режиме

## Подготовка окружения 

#### Версия Python
python3.9.1

#### Установка виртуального окружения
`python3 -m venv venv`

#### Применение виртуального окружения
`source venv/bin/activate`

#### Установка зависимостей
`pip install -r requirements.txt`

## Развертывание локальной инфраструктры
### Поднять все контейнеры

`cd deployment/dev && docker-compose up -d`

## Локальный запуск проекта

## Миграции
миграции нужно запускать из папки entertainy/app/db

#### Добавить миграцию
`alembic revision --autogenerate -m "name of migration"`

#### Запустить миграции
`alembic upgrade head`

#### Откатить миграцию 
`alembic downgrade -1`

## Запускаемый файл
`src/telegram_bot.py`