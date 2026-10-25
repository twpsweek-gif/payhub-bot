# Используем легкий образ Python
FROM python:3.10-slim

# Создаем рабочую папку
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем библиотеки (обновляем pip для совместимости)
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь остальной код
COPY . .

# Команда запуска бота
CMD ["python", "bot.py"]