FROM python:3
WORKDIR /app
ENV FLASK_APP=bahadirServer
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip3 install flask \
    beautifulsoup4 \
    mysql-connector-python \
    requests
COPY . .
EXPOSE 80
CMD ["python3", "./bahadirServer.py"]
