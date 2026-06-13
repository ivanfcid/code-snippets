import sys
import networkx as nx
import matplotlib.pyplot as plt

if (len(sys.argv) > 1):
    G = nx.read_edgelist(sys.argv[1])
    nx.draw_networkx(G, node_size=0.1, width=0.01, with_labels=False)
    plt.savefig(sys.argv[1].replace("mis", "png"))
