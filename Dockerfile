# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /fp_bot

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Timezone
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# Устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt /fp_bot
RUN pip install --no-cache-dir -r ./requirements.txt

# Копируем проект в рабочую директорию
COPY . /fp_bot

# Команда для запуска бота
CMD ["python", "main.py"]
