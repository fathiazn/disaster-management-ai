class AgentMessage:

    def __init__(
        self,
        sender,
        receiver,
        task,
        content
    ):
        self.sender = sender
        self.receiver = receiver
        self.task = task
        self.content = content


    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "task": self.task,
            "content": self.content
        }