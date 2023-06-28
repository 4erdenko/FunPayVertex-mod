# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

# Копируем проект в рабочую директорию
COPY . .
#ENV GOLDEN_KEY=er27lp95bskbsgksa9md44xyb5cl53v4
#ENV USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'
#ENV ENABLED=1
#ENV TOKEN='6063587774:AAEHtAn-TQPqkOPa62j3_EnLB5OXt238BMY'
#ENV SECRET_KEY='o3jEz&fk6^FXEC@MaN*8ZNxFgkpG4G'
# Создаем папку и файл конфигурации
RUN mkdir /app/configs
RUN echo "[FunPay]" >> /app/configs/_main.cfg \
    && echo "golden_key : ${GOLDEN_KEY}" >> /app/configs/_main.cfg \
    && echo "user_agent : ${USER_AGENT}" >> /app/configs/_main.cfg \
    && echo "autoRaise : 1" >> /app/configs/_main.cfg \
    && echo "autoResponse : 1" >> /app/configs/_main.cfg \
    && echo "autoDelivery : 1" >> /app/configs/_main.cfg \
    && echo "multiDelivery : 0" >> /app/configs/_main.cfg \
    && echo "autoRestore : 0" >> /app/configs/_main.cfg \
    && echo "autoDisable : 1" >> /app/configs/_main.cfg \
    && echo "oldMsgGetMode : 0" >> /app/configs/_main.cfg \
    && echo "" >> /app/configs/_main.cfg \
    && echo "[Telegram]" >> /app/configs/_main.cfg \
    && echo "enabled : ${ENABLED}" >> /app/configs/_main.cfg \
    && echo "token : ${TOKEN}" >> /app/configs/_main.cfg \
    && echo "secretKey : ${SECRET_KEY}" >> /app/configs/_main.cfg \
    && echo "" >> /app/configs/_main.cfg \
    && echo "[BlockList]" >> /app/configs/_main.cfg \
    && echo "blockDelivery : 0" >> /app/configs/_main.cfg \
    && echo "blockResponse : 0" >> /app/configs/_main.cfg \
    && echo "blockNewMessageNotification : 0" >> /app/configs/_main.cfg \
    && echo "blockNewOrderNotification : 0" >> /app/configs/_main.cfg \
    && echo "blockCommandNotification : 0" >> /app/configs/_main.cfg \
    && echo "" >> /app/configs/_main.cfg \
    && echo "[NewMessageView]" >> /app/configs/_main.cfg \
    && echo "includeMyMessages : 1" >> /app/configs/_main.cfg \
    && echo "includeFPMessages : 1" >> /app/configs/_main.cfg \
    && echo "includeBotMessages : 0" >> /app/configs/_main.cfg \
    && echo "notifyOnlyMyMessages : 0" >> /app/configs/_main.cfg \
    && echo "notifyOnlyFPMessages : 0" >> /app/configs/_main.cfg \
    && echo "notifyOnlyBotMessages : 0" >> /app/configs/_main.cfg \
    && echo "" >> /app/configs/_main.cfg \
    && echo "[Greetings]" >> /app/configs/_main.cfg \
    && echo "cacheInitChats : 1" >> /app/configs/_main.cfg \
    && echo "ignoreSystemMessages : 1" >> /app/configs/_main.cfg \
    && echo "sendGreetings : 1" >> /app/configs/_main.cfg \
    && echo "greetingsText : Здравствуйте \$username✌️" >> /app/configs/_main.cfg \
    && echo "" >> /app/configs/_main.cfg \
    && echo "[OrderConfirm]" >> /app/configs/_main.cfg \
    && echo "sendReply : 1" >> /app/configs/_main.cfg \
    && echo "replyText : \$username, спасибо за подтверждение заказа \$order_id!" >> /app/configs/_main.cfg \
    && echo " " >> /app/configs/_main.cfg \
    && echo "[ReviewReply]" >> /app/configs/_main.cfg \
    && echo "star1Reply : 0" >> /app/configs/_main.cfg \
    && echo "star2Reply : 0" >> /app/configs/_main.cfg \
    && echo "star3Reply : 0" >> /app/configs/_main.cfg \
    && echo "star4Reply : 0" >> /app/configs/_main.cfg \
    && echo "star5Reply : 1" >> /app/configs/_main.cfg \
    && echo "star1ReplyText : " >> /app/configs/_main.cfg \
    && echo "star2ReplyText : " >> /app/configs/_main.cfg \
    && echo "star3ReplyText : " >> /app/configs/_main.cfg \
    && echo "star4ReplyText : " >> /app/configs/_main.cfg \
    && echo "star5ReplyText : \$username, желаю побед 🔥" >> /app/configs/_main.cfg \
    && echo "" >> /app/configs/_main.cfg \
    && echo "[Proxy]" >> /app/configs/_main.cfg \
    && echo "enable : 0" >> /app/configs/_main.cfg \
    && echo "ip : " >> /app/configs/_main.cfg \
    && echo "port : " >> /app/configs/_main.cfg \
    && echo "login : " >> /app/configs/_main.cfg \
    && echo "password : " >> /app/configs/_main.cfg \
    && echo "check : 0" >> /app/configs/_main.cfg \
    && echo "" >> /app/configs/_main.cfg \
    && echo "[Other]" >> /app/configs/_main.cfg \
    && echo "watermark : " >> /app/configs/_main.cfg \
    && echo "requestsDelay : 4" >> /app/configs/_main.cfg \
    && echo "language : ru" >> /app/configs/_main.cfg

# Команда для запуска бота
CMD ["python", "main.py"]
