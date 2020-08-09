FROM python:3.6-alpine
USER root
COPY app /app
WORKDIR /app
RUN apk update && apk add --no-cache steghide --repository http://dl-3.alpinelinux.org/alpine/edge/testing/
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
