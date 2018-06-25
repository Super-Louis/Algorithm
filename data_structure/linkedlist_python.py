import json
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

class linkedList():

    def __init__(self):
        self.head = None

    def __repr__(self):

        data = list()
        current = self.head
        data.append(current.getData())
        while current.getNext():
            current = current.getNext()
            data.append(current.getData())

        return json.dumps(data)

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        current = Node(item)
        current.setNext(self.head)
        self.head = current

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
            if current.getData() == item:
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
            previous.setNext(node)
        node.setNext(current)

    def pop(self, pos=None):

        if pos == None:
            previous = None
            current = self.head

            while current.getNext():
                previous = current
                current = current.getNext()

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

    def reverse(self):

        middle = self.head
        next = middle.getNext()
        middle = next
        next.setNext(middle)
        while middle:
            next = middle.getNext()
            next.setNext(middle)
            middle = middle.getNext()





if __name__ == '__main__':
    myLinkedlist = linkedList()
    print(myLinkedlist.isEmpty())
    myLinkedlist.add(6)
    myLinkedlist.add(7)
    myLinkedlist.add(8)
    myLinkedlist.add('a')
    myLinkedlist.add('b')
    print(myLinkedlist)
    myLinkedlist.reverse()
    print(myLinkedlist)
    # myLinkedlist.remove('b')
    # print(myLinkedlist.isEmpty())
    # print(myLinkedlist.size())
    # print(myLinkedlist.search(3))
    # print(myLinkedlist.search(7))
    # myLinkedlist.remove(8)
    # print(myLinkedlist.search(8))
    # print(myLinkedlist.size())
    # print(myLinkedlist.search(6))
    # myLinkedlist.remove(6)
    # print(myLinkedlist.search(6))
    # print(myLinkedlist.size())
    # myLinkedlist.append('a')
    # myLinkedlist.append('b')
    # print(myLinkedlist.size())
    # print(myLinkedlist.search('a'))
    # print(myLinkedlist.index('b'))
    # # print(myLinkedlist.remove(8))
    # print(myLinkedlist.pop())
    # print(myLinkedlist.pop())
    # myLinkedlist.append('d')
    # print(myLinkedlist.pop())











