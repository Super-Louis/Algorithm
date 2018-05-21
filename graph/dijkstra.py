# graph
graph = {}
graph['start'] = {}
graph['start']['A'] = 6
graph['start']['B'] = 2
graph['A'] = {}
graph['A']['end'] = 1
graph['B'] = {}
graph['B']['A'] = 3
graph['B']['end'] = 5
graph['end'] = {}

# cost
inf = float('Inf')
costs = {}
costs['A'] = 6
costs['B'] = 2
costs['end'] = inf

# parent
parents = {}
parents['A'] = 'start'
parents['B'] = 'start'
parents['end'] = None

# 已处理的数组
processed = []

def dijkstra():
    node = find_lowest_cost_node(costs)
    while node:
        node_cost = costs[node]
        for key in graph[node]:
            cost = graph[node][key]
            new_cost = node_cost + cost
            if new_cost < costs[key]: # 更新cost及parent map
                costs[key] = new_cost
                parents[key] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

def find_lowest_cost_node(costs): # 找到cost中最小且未处理的node
    lowest_cost = inf
    Node = None
    for key, value in costs.items():
        if (value < lowest_cost) and (key not in processed):
            Node = key
            lowest_cost = value
    return Node

if __name__ == '__main__':
    dijkstra()
    print(costs)
    print(parents)
    print(processed)