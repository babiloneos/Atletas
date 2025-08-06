FROM python:3.6
USER root
COPY Atletas/app /app
WORKDIR /app
RUN apt-get update && apt-get install steghide -y
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
