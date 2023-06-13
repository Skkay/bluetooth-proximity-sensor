FROM python:3.9.2

RUN apt-get update && apt-get install -y \
    python3-dev

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "main.py"]
