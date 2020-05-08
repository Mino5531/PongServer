class QueueManager:
    instance = None

    def __init__(self):
        QueueManager.instance = self
