import sys
import operator


def initialize(filename, adjacency, n):
    edges = list()
    node_degree = dict()
    with open(filename, "r") as fin:
        for line in fin:
            edge = line.replace("\n", "").split(" ")
            edges.append(edge)
            if int(edge[0]) > n:
                n = int(edge[0])
            if int(edge[1]) > n:
                n = int(edge[1])
    node_degree_list = [0]*(n+1)
    for i in range(1, n+1):
        adjacency[i] = dict()
        for j in range(1, n+1):
            adjacency[i][j] = 0
    for edge in edges:
        node_degree_list[int(edge[0])] += 1
        node_degree_list[int(edge[1])] += 1
        adjacency[int(edge[0])][int(edge[1])] = 1
        adjacency[int(edge[1])][int(edge[0])] = 1
    for i in range(1, len(node_degree_list)):
        node_degree[i] = node_degree_list[i]
    return [list(item) for item in sorted(node_degree.items(), key=operator.itemgetter(1), reverse=True)]


def add_to_solution(key, adjacency, node_sorted, solution):
    adjacent_nodes = list()
    solution.append(key)
    for key2 in adjacency[key]:
        if adjacency[key][key2] == 1:
            adjacent_nodes.append(key2)
            find_and_delete(key2, node_sorted)
    for nkey in adjacent_nodes:
        for key2 in adjacency[nkey]:
            if adjacency[nkey][key2] == 1:
                find_and_update(key2, node_sorted)
    find_and_delete(key, node_sorted)


def find_and_update(key, node_sorted):
    for node in node_sorted:
        if key == node[0]:
            node[1] -= 1


def find_and_delete(key, node_sorted):
    i = -1
    for j in range(0, len(node_sorted)):
        if node_sorted[j][0] == key:
            i = j
    if i != -1:
        del node_sorted[i]


def find_and_return(key, node_sorted):
    for node in node_sorted:
        if key == node[0]:
            return node[1]
    return 0


def greedy(filename):
    n = 0
    adjacency = dict()
    solution = list()
    node_sorted = initialize(filename, adjacency, n)
    while len(node_sorted) > 0:
        add_to_solution(node_sorted[0][0], adjacency, node_sorted, solution)
    print(solution, len(solution))


def __main__(filename):
    greedy(filename)


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        __main__(sys.argv[1])
