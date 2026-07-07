FROM python:3.11-alpine

WORKDIR /app

COPY app.py .
COPY templates/ templates/

RUN pip install flask psycopg2-binary

EXPOSE 80

CMD ["python", "app.py"]