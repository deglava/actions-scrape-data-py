FROM python:latest

WORKDIR /src

#to COPY the remote file at working directory in container
COPY src /src
COPY stockprice.csv stockprice.csv

RUN pip install yfinance

CMD [ "python", "main.py"]
