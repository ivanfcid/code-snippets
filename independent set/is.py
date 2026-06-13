import sys
import copy
import operator


def add_to_solution(key):
    solution.append(key)
    # print(adjacency_clone[115][315], len(adjacency_clone))
    for key2 in adjacency[key]:
        if (adjacency[key][key2] == 1):
            # print(key, key2)
            del adjacency_clone[key][key2]
            del adjacency_clone[key2][key]
    # print(adjacency_clone[115][315], len(adjacency_clone))


if (len(sys.argv) > 1):
    # Prepare graph as "kind of" adjacency matrix. #
    adjacency = dict()
    node_degree = dict()
    solution = list()
    n = 0
    with open(sys.argv[1], "r") as fin:
        for line in fin:
            edge = line.replace("\n", "").split(" ")
            if (int(edge[0]) not in adjacency):
                adjacency[int(edge[0])] = dict()
            if (int(edge[1]) not in adjacency):
                adjacency[int(edge[1])] = dict()
            if (int(edge[0]) > n):
                n = int(edge[0])
            if (int(edge[1]) > n):
                n = int(edge[1])
            adjacency[int(edge[0])][int(edge[1])] = 1
            adjacency[int(edge[1])][int(edge[0])] = 1
    n += 1
    adjacency_clone = copy.deepcopy(adjacency)
    for i in range(1, n):
        for j in range(1, n):
            if (i not in adjacency[j]):
                adjacency[j][i] = 0
            if (j not in adjacency[i]):
                adjacency[i][j] = 0
    # Greedy algorithm ongoing. #
    for i in range(1, n):
        for j in range(1, n):
            if (adjacency[i][j] == 1):
                if (j not in node_degree):
                    node_degree[j] = 1
                else:
                    node_degree[j] += 1
    node_sorted = sorted(node_degree.items(), key=operator.itemgetter(1)[0])
    # node_sorted = sorted(node_degree.items(), key=operator.itemgetter(1))
    print(node_sorted)
    k = True
    # while k is True:
        # add_to_solution(node_sorted[0][0])
        # k = False
    # print(solution)
