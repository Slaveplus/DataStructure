from MyList import MyList
class ArrayBasedList(MyList):
    def __init__ (self, size):
        self.item=size*[None]
        self.length=size

    def len(self):
        return self.length

    def getitem(self,j):
        if(self.length>j):
            return self.item[j]
        raise ValueError("value not in list")

    def setitem(self, val, j):
        if(self.length>j):
            self.item[j]=val
            return
        raise ValueError("Index out of range")

    def insertItem(self, item, j=0):
        if(j>self.length and j<0):
            raise ValueError ("Index out of range")
        else:
            self.length+=1
            for i in range(len(self.item)-2,j-1,-1): #한칸씩 밀기
                self.item[i+1]=self.item[i]
            self.item[j]=item

    def removeItem(self, j=0):
        if(self.length>j):
            self.length-=1
            del(self.item[j])
        else:
            raise ValueError("cannot remove item")

    def printMyList(self):
        if(self.length==0):
            raise ValueError("List is empty")
        else:
            print(self.item)

obj=ArrayBasedList(10)
obj.setitem(4,0)
obj.setitem(3,1)
obj.setitem(1,2)
obj.insertItem(2,1)
obj.printMyList()
obj.removeItem(3)
obj.removeItem(1)
obj.removeItem(0)
obj.printMyList()

