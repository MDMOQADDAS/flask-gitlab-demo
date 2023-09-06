FROM python:latest

WORKDIR /myapp

COPY * /myapp/

RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["python3", "app.py"]