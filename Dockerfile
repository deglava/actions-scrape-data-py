WORKDIR /src

#to COPY the remote file at working directory in container
COPY src /src

RUN pip install yfinance

ENTRYPOINT [ "python", "main.py"]
