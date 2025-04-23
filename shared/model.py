import json


class MessageData:
    """
    A data model for a message sent between a publisher and subscriber.
    Attributes:
    name (str): Identifier or name of the message sender.
    index (int): Sequential number or ID of the message.
    time (str): Timestamp of when the message was created, in ISO 8601 format.
    """
    def __init__(self, name, index, time):
        self.name = name
        self.index = index
        self.time = time

    def to_json(self):
        """
        :return: str: A JSON string representation of the MessageData instance.
        """
        return json.dumps({
            "Name": self.name,
            "Index": self.index,
            "Time": self.time
        })

    @classmethod
    def from_json(cls, json_str):
        """
        :param json_str: str: A JSON string containing MessageData keys.
        :return: MessageData: An instance of the class with data from json_str.
        """
        data = json.loads(json_str)
        return cls(
            name=data.get("Name"),
            index=data.get("Index"),
            time=data.get("Time")
        )
