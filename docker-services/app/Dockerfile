FROM python:3.8

EXPOSE 4311

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app
COPY . /app

RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT ["python", "main.py"]
