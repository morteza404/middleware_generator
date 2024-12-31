FROM python:3.10-alpine

RUN mkdir /config /output

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "generate_middleware.py"]
