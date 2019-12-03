from queue import Queue
from graph_al import GraphAL
from graph_am import GraphAM
from disjoint_set_forest import DSF

#Topological sort implementation from Diego's resources
def compute_indegree_every_vertex(graph):
    all_in_degrees = [0] * len(graph.al)
    for row in graph.al:
        for elem in row:
            all_in_degrees[elem.dest] += 1
    return all_in_degrees

def topological_sort(graph):
    all_in_degrees = compute_indegree_every_vertex(graph)
    sort_result = []
    q = Queue()

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.put(i)
    
    while not q.empty():
        u = q.get()
        sort_result.append(u)

        for adj_vertex in graph.vertices_reachable_from(u):
            all_in_degrees[adj_vertex] -= 1

            if all_in_degrees[adj_vertex] == 0:
                q.put(adj_vertex)
    
    if len(sort_result) != graph.num_vertices():
        return None

    return sort_result

def kruskal(graph):
    # declare and initialize minimum spanning tree
    min_span_tree = set()
    edges = set()
    # add all edges from the given graph
    for j in range(len(graph.am)):
        for k in range(len(graph.am[j])):
            if graph.am[j][k] != 0 and (k, j) not in edges:
                edges.add((j, k))
    # sort the edges from smallest to largest weights
    sorted_edges = sorted(edges, key=lambda e:graph.am[e[0]][e[1]])
    dsf = DSF(graph.vertices)
    for e in sorted_edges:
        u, v = e
        # if u, v already connected, abort this edge
        if dsf.find_loop(u, v):
            continue
        # if not, connect them and add this edge to the minimum spanning tree
        dsf.union(u, v)
        min_span_tree.add(e)
    return min_span_tree

