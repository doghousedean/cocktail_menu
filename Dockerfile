FROM python:3.8-buster

EXPOSE 80:5000/tcp

WORKDIR /app

COPY src/ .

RUN mv config.json oldconfig.json

RUN pip install -r requirements.txt

RUN ls -l 

ENTRYPOINT ["python"]
CMD ["main.py"]
