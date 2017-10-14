FROM python:3-alpine3.6

WORKDIR /usr/src/app

COPY crontab /var/spool/cron/crontabs/root

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py .

# CMD ["sh","-c","crond -l 2 -f"]
CMD ["python","main.py"]