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
        self.head = None # head初始化
        self.size = 0

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
        """在首部添加"""
        current = Node(item)
        current.setNext(self.head)
        self.head = current
        self.size += 1

    def size(self):

        # count = 0
        # current = self.head
        # while current:
        #     count += 1
        #     current = current.getNext()
        return self.size

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
        """
        删除元素
        1. 寻找对应的item
        2. 如果未找到则直接报错
        3. 有对应的item, 则将该item的previous的next设置为该item的next
        :param item:
        :return:
        """
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
        """在尾部添加"""
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
        """返回item的索引"""
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
        """
        在中间插入，过程与删除类似
        :param pos:
        :param item:
        :return:
        """
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
        """
        弹出
        如果没有pos，则弹出尾部元素
        如果有，则跟insert类似
        :param pos:
        :return:
        """
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
        a = linkedList()
        current = self.head
        a.add(current.getData())
        while current.getNext():
            current = current.getNext()
            a.add(current.getData())
        return a

if __name__ == '__main__':
    myLinkedlist = linkedList()
    print(myLinkedlist.isEmpty())
    myLinkedlist.add(6)
    myLinkedlist.add(7)
    myLinkedlist.add(8)
    myLinkedlist.add('a')
    myLinkedlist.add('b')
    print(myLinkedlist)
    reverse_linkedlist = myLinkedlist.reverse()
    print(reverse_linkedlist)
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











