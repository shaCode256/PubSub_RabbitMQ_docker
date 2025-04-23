FROM python:3.10-slim
WORKDIR /app
COPY publisher /app
COPY shared /app/shared
COPY publisher/requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["python", "app.py"]