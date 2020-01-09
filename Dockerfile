FROM python:3.7-alpine
RUN apk add --no-cache tzdata
RUN mkdir /app
WORKDIR /app
COPY ./source .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
EXPOSE 8080