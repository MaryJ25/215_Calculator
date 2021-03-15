FROM python:3.8-buster

COPY . /calculator

WORKDIR /calculator

RUN pip install git+https://github.com/MaryJ25/Calculator/

CMD python ./example.py
