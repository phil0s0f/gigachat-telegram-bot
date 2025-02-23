# GigaChat Телеграм бот

## 📌 Описание

Этот проект представляет собой Telegram-бота, который использует языковую модель GigaChat для ответов на вопросы
пользователей через API.

## 🛠️ Установка и запуск

### 1. Установка зависимостей

Для работы бота необходимо установить следующие зависимости:

```sh
pip install gigachat pyTelegramBotAPI
```

### 2. Настройка переменных окружения

Перед запуском необходимо задать переменные окружения:

- `TELEGRAM_TOKEN` — токен Telegram-бота.
- `GIGA_KEY` — API-ключ для GigaChat.

### 3. Запуск бота

```sh
python bot.py
```

## 📂 Структура проекта

```
/telegram-giga-chatbot
│── bot.py                 # Основной файл бота
│── gigachat_client.py     # Модуль для работы с GigaChat API
│── history_manager.py     # Управление историей пользователей
│── config.py              # Конфигурация бота
│── README.md              # Описание проекта
```

## 🔧 Конфигурация

Все основные настройки хранятся в `config.py`:

```python
SYSTEM_ROLE_CONTENT = "Ты Юрий Гагарин. Любишь отвечать метафорами про космос"
TEMPERATURE = 0.7
MAX_TOKENS = 100
```

Можно изменить `SYSTEM_ROLE_CONTENT`, чтобы бот отвечал в другом стиле.


