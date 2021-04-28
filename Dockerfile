FROM python:3.8
LABEL maintainer StarkLin "myemail@gmail.com"

RUN mkdir /app; exit 0
WORKDIR /app
ADD . /app

RUN pip3 --disable-pip-version-check install -r requirements.txt

CMD ["python3", "main.py"]