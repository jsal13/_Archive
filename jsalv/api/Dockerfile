FROM python:3.10.0b2-buster

WORKDIR /src
COPY . /src

RUN pip install -r requirement.txt
CMD ['uvicorn', 'api:api', '--reload']
