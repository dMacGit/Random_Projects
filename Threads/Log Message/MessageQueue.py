from queue import Queue

class MessageQueue(Queue):
    def __init__(self):
        super(MessageQueue, self).__init__()

    def __putMessage__(self,object):
        self.put(object)
        print("Adding ",object,"to queue")

    def __getMessage__(self):
        temp = self.get()
        print("Grabbing message ", temp, "from queue")
        return temp