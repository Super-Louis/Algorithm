graph = dict()
# 有向图
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy', 'bob']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = [] # 没有邻居，为[]
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

from collections import deque
def search(name):
    q = deque()
    q += graph[name]
    searched = list()
    while q:
        si = q.popleft()
        if not si in searched:
            if si[-1] == 'm':
                searched.append(si)
                print("{} is a mongo seller!".format(si))
                print("search path:{}".format(searched))
                return True
            else:
                searched.append(si)
                q += graph[si]
    return False
if __name__ == '__main__':
    search('you')
