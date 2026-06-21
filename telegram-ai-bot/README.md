# Telegram AI Bot

Telegram-бот с тремя функциями:
- **Чат** — обычное сообщение боту отправляется в OpenAI и возвращает ответ.
- **`/music <название>`** — ищет песню и присылает ссылки на YouTube Music (бот не скачивает и не пересылает аудиофайлы — только легальные ссылки на поиск).
- **`/image <описание>`** — генерирует картинку через OpenAI Images API.

## 1. Получить Telegram Bot Token

1. Открой Telegram, найди бота **@BotFather**.
2. Отправь `/newbot`, придумай имя и username для своего бота.
3. BotFather пришлёт токен вида `123456:ABC-DEF1234ghIkl...` — это `TELEGRAM_BOT_TOKEN`.

## 2. Получить OpenAI API key

1. Зайди на https://platform.openai.com/api-keys
2. Войди/зарегистрируйся, нажми "Create new secret key".
3. Скопируй ключ (он показывается один раз) — это `OPENAI_API_KEY`.
4. На аккаунте должен быть привязан способ оплаты — OpenAI API платный (есть небольшой бесплатный лимит для новых аккаунтов).

## 3. Настройка

```bash
cd telegram-ai-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Открой `.env` и вставь свои ключи:

```
TELEGRAM_BOT_TOKEN=твой_токен_от_botfather
OPENAI_API_KEY=твой_ключ_openai
```

## 4. Запуск

```bash
python3 bot.py
```

Бот запустится и будет отвечать в Telegram. Останови процесс `Ctrl+C`, когда не нужен.

## Важно

- **Никогда не публикуй и не коммить файл `.env`** — он в `.gitignore`, ключи должны оставаться только у тебя.
- Музыка ищется и присылается только в виде ссылок на YouTube Music — бот не скачивает и не распространяет аудиофайлы, это законный способ поиска музыки.
