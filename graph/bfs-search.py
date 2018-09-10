# 广度优先搜索
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
def bfs_search(name):
    q = deque()
    q += graph[name]
    searched = list() # 可能有重复的元素
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

visited = []
def dfs_search(name):
    if name[-1] == 'm':
        print("found, {} is a mongo seller!".format(name), end = ' ')
        return True
    nodes = graph[name]
    for n in nodes:
        if n not in visited:
            print("search {}".format(n), end = ' ')
            visited.append(n)
            found = dfs_search(n)
            if found:
                return True
    return False

if __name__ == '__main__':
    bfs_search('you')
    dfs_search('you')