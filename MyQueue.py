from abc import ABCMeta, abstractmethod
class MyQueue(object):
    __metaclass__ = ABCMeta

    def len(self):
        pass

    def first(self):
        pass

    def is_empty(self):
        pass

    def enqueue(self,item):
        pass

    def dequeue(self):
        pass

    def printMyQueue(self):
        pass