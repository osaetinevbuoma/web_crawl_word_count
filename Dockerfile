FROM python:3.11.0a5-alpine3.15
WORKDIR /app
ENV FLASK_APP=crawler
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --update --no-cache gcc musl-dev linux-headers libxml2 libxslt libxml2-dev libxslt-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
