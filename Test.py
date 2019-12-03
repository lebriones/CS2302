from queue import Queue
from graph_al import GraphAL
from graph_am import GraphAM
from disjoint_set_forest import DSF
from topological_kruskal import topological_sort
from topological_kruskal import kruskal

def main():
    g = GraphAL(6, directed=True)
    g.insert_edge(0, 1)
    g.insert_edge(0, 4)
    g.insert_edge(1, 2)
    g.insert_edge(1, 4)
    g.insert_edge(2, 3)
    g.insert_edge(4, 5)
    g.insert_edge(5, 2)
    g.insert_edge(5, 3)

    g1 = GraphAM(6, weighted=True)
    g1.insert_edge(0, 1, 4)
    g1.insert_edge(0, 2, 3)
    g1.insert_edge(1, 2, 2)
    g1.insert_edge(2, 3, 1)
    g1.insert_edge(3, 4, 5)
    g1.insert_edge(4, 1, 4)

    ans = topological_sort(g)
    ans2 = kruskal(g1)
    print("Graph 1 Topologial Sort:", ans)
    print("Graph 2 Kruskal:", ans2)

if __name__ == "__main__":
    main()