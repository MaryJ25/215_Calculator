FROM python:3.8-buster

WORKDIR /usr/src/app

RUN pip install git+https://github.com/MaryJ25/215_Calculator/

COPY ./docker/app.py ./

CMD ["python", "app.py"]