class LogMessage(object):
    def __init__(self, parent, message):
        self.message = message
        self.parent = parent

    def __message__(self):
        return self.message()

    def __parent__(self):
        return self.parent()

    def __str__(self):
        return str(self.parent), str(self.message)
