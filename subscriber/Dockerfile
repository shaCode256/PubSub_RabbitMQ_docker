FROM python:3.10-slim
WORKDIR /app
COPY subscriber /app
COPY shared /app/shared
COPY subscriber/requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["python", "app.py"]