FROM python:3.6-alpine
WORKDIR /srv/bot
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./bot.py" ]