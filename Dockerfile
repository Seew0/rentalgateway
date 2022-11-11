FROM alpine

ENV FLASK_ENV=development FLASK_APP=rental.py

COPY . .

RUN apk -U ugrade &\
apk add python3 sqlite py3-pip 

RUN export FLASK_ENV=production &\ 
export FLASK_APP=rental.py 

RUN pip install -r requirements.txt

EXPOSE 5000:5000

CMD ["flask","run" ]

