FROM python:latest

ENV INSTALL_PATH /let-there-be-light
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
COPY src src/
COPY scripts scripts/
RUN chmod -R +x scripts
