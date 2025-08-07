FROM python:3.6
USER root
EXPOSE 80
COPY . .
WORKDIR .
RUN apt-get update && apt-get install steghide -y
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
