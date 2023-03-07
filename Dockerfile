FROM python:3.8-slim-buster

ENV FLASK_ENV=development FLASK_APP=rental.py

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=127.0.0.1"]
