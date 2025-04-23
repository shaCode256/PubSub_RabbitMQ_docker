import pika
import time

def wait_for_rabbitmq():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
            print("Connected to RabbitMQ!")
            return connection
        except pika.exceptions.AMQPConnectionError:
            print("Waiting for RabbitMQ to be ready...")
            time.sleep(2)