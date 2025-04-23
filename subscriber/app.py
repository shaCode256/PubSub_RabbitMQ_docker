import pika
from shared.model import MessageData
from shared.utils import wait_for_rabbitmq


def subscriber():
    connection = wait_for_rabbitmq()
    channel = connection.channel()

    # Create a fanout exchange and a new random queue
    channel.exchange_declare(exchange='pubSub4', exchange_type='fanout')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='pubSub4', queue=queue_name)

    def callback(ch, method, properties, body):
        try:
            message = body.decode()
            msg_obj = MessageData.from_json(message)
            print("Subscriber received:")
            print(f"Name: {msg_obj.name}")
            print(f"Index: {msg_obj.index}")
            print(f"Time: {msg_obj.time}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print("Start consuming")
    channel.start_consuming()


if __name__ == "__main__":
    subscriber()
