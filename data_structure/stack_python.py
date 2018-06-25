class Stack():

    def __init__(self):
        self.items = []

    def __repr__(self):
        return repr(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    # def reverse(self):

def reverse(string):
    s = Stack()
    for i in string:
        s.push(i)
    rs = ''
    while s.size():
        r = s.pop()
        rs += r
    print(rs)

def checkParenthesis(str):
    s = Stack()
    for p in str:
        if p in '({[':
            s.push(p)
        else:
            if not s.size():
                return False
            else:
                i = s.pop()
                if not match(p, i):
                    return False
    if not s.size():
        return True
    else:
        return False

def divideBybase(num, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while num:
        d = num % base
        s.push(d)
        num = num // base
    output = ''
    while s.size():
        output += digits[s.pop()]
    return output

def match(a, b):
    match_dict = {'}':'{', ']':'[', ')':'('}
    return match_dict[a] == b

def postfix():
    """
    (a+b)*c-(a-b)*d
    :return:
    """

if __name__ == '__main__':
    # s = Stack()
    # print(type(s))
    # s.push(1)
    # print(s)
    # print(list(s))
    reverse('cabada')
    print(checkParenthesis('(([]{(())}))'))
    print(divideBy2(666,16))
# a = s.pop()
# print(a)
# list(s)
# Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

