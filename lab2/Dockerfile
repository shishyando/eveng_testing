FROM python:3

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y iputils-ping


COPY . .
ENTRYPOINT [ "python3", "main.py" ]
CMD [ "google.com" ]