from abc import ABCMeta, abstractmethod
class MyList(object):
  __metaclass__ = ABCMeta

  def len(self):
    pass

  def getitem (self,j):
    pass

  def setitem (self, val ,j):
    pass

  def insertItem(self, item ,j=0):
    pass

  def removeItem(self, j=0):
    pass

  def printMyList(self):
    pass