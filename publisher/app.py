from shared.model import MessageData
from shared.utils import wait_for_rabbitmq
from datetime import datetime
import time

def publisher():
    connection = wait_for_rabbitmq()
    channel = connection.channel()

    # Create a fanout exchange (broadcast to all queues)
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    index = 0
    while True:
        msg = MessageData(
            name="Publisher4",
            index=index,
            time=datetime.now().isoformat()
        )
        message = msg.to_json()
        channel.basic_publish(exchange='logs', routing_key='', body=message)
        print(f"Publisher sent: {message}")
        index += 1
        time.sleep(1)

if __name__ == "__main__":
    publisher()
