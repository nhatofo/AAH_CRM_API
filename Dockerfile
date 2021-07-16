FROM python:stretch

COPY . /app

WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

CMD ["python", "crm_api_server.py"]