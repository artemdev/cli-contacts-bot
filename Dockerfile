FROM python:3.11.4-slim

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

COPY pyproject.toml $APP_HOME/pyproject.toml
COPY poetry.lock $APP_HOME/poetry.lock

RUN pip install poetry 
RUN poetry config virtualenvs.create false && poetry install --only main
# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 3000

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "helper_bot/main.py"]