class Node:

    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class Orderedlist():

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        previous = None
        current = self.head

        while current:
            if current.getData() > item:
                break
            else:
                previous = current
                current = current.getNext()
        if not previous: # add to head
            self.head = temp
            temp.setNext(current)
        else:
            previous.setNext(temp)
            temp.setNext(current)

    def size(self):

        count = 0
        current = self.head
        while current:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):

        found = False
        current = self.head
        while not found and current:
            if current.getData() > item:
                return False
            elif current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):

        current = self.head
        previous = None
        found = False
        while not found and current:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                raise ValueError(f"{item} is not in list")
            else:
                previous = current
                current = current.getNext()

        if not found:
            raise ValueError(f"{item} is not in list")

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):

        previous = None
        current = self.head
        last = Node(item)
        while current:
            previous = current
            current = current.getNext()
        if not previous:
            self.head = last
        elif previous.getData() > item:
            raise ValueError(f"{item} is not valid")
        else:
            previous.setNext(last)
        last.setNext(None)

    def index(self, item):

        found = False
        current = self.head
        index = 0
        while not found and current:
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                raise ValueError(f"{item} is not in list")
            else:
                current = current.getNext()
                index += 1
        if found:
            return index
        else:
            raise ValueError(f"{item} is not in list")

    def insert(self, pos, item):

        node = Node(item)
        ps = 0
        previous = None
        current = self.head

        while ps != pos:
            previous = current
            current = current.getNext()
            ps +=1

        if not previous:
            self.head = node
        else:
            if previous.getData() <= item <= current.getData():
                previous.setNext(node)
            else:
                raise ValueError(f"{item} is not valid")
        node.setNext(current)

    def pop(self, pos=None):

        if pos == None:
            previous = None
            current = self.head

            while current.getNext():
                previous = current
                current = current.getNext()
            if not previous:
                self.head = None
            else:
                previous.setNext(None)
        else:
            ps = 0
            previous = None
            current = self.head
            while ps != pos:
                previous = current
                current = current.getNext()
                ps += 1

            if not previous:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())


        return current.getData()




if __name__ == '__main__':
    orderedlist = Orderedlist()
    print(orderedlist.isEmpty())
    orderedlist.add(6)
    orderedlist.add(7)
    orderedlist.add(8)
    # myLinkedlist.remove('b')
    # print(orderedlist.isEmpty())
    # print(orderedlist.size())
    print(orderedlist.search(3))
    print(orderedlist.search(7))
    # orderedlist.remove(8)
    # print(orderedlist.search(8))
    print(orderedlist.size())
    # print(orderedlist.search(6))
    # orderedlist.remove(6)
    # print(orderedlist.search(6))
    # print(orderedlist.size())
    # orderedlist.append(5)
    orderedlist.append(9)
    print(orderedlist.size())
    # print(orderedlist.search(3))
    print(orderedlist.index(9))
    # print(myLinkedlist.remove(8))
    print(orderedlist.pop(0))
    print(orderedlist.pop())
    # orderedlist.append('d')
    print(orderedlist.pop())
    # print(orderedlist.pop())











