from queue import Queue
import graph_al as al
import graph_am as am



def breath_first_search(graph, start_node):
    visited_order = []
    visited = [False] * graph.num_vertices()
    path = [-1] * graph.num_vertices()

    q = Queue()
    q.put(start_node)
    visited[start_node] = True
    visited_order.append(start_node)

    while not q.empty():
        u = q.get()
        for adj_vertex in graph.vertices_reachable_from(u):
            if not visited[adj_vertex]:
                visited[adj_vertex] = True
                visited_order.append(adj_vertex)
                path[adj_vertex] = u
                q.put(adj_vertex)

    return path, visited_order


def depth_first_search(graph, start_node):
    visited_order = []
    visited = [False] * graph.num_vertices()
    path = [-1] * graph.num_vertices()

    stack = []  # A list can be used as a stack

    stack.append(start_node)

    while len(stack) > 0:
        u = stack.pop()

        if not visited[u]:
            visited[u] = True
            visited_order.append(u)

            for adj_vertex in graph.vertices_reachable_from(u):
                if not visited[adj_vertex]:
                    path[adj_vertex] = u
                    stack.append(adj_vertex)

    return path, visited_order


def main():
    graph = GraphAL(vertices=11, directed=True)
    # graph = GraphAM(vertices=11, directed=True)

    graph.insert_edge(0, 1)
    graph.insert_edge(0, 2)
    graph.insert_edge(0, 3)

    graph.insert_edge(1, 4)
    graph.insert_edge(2, 5)
    graph.insert_edge(3, 6)

    graph.insert_edge(4, 7)
    graph.insert_edge(5, 8)
    graph.insert_edge(6, 9)

    graph.insert_edge(7, 10)
    graph.insert_edge(8, 10)
    graph.insert_edge(9, 10)

    #   /--> 1 -> 4 -> 7 -\
    #  /                   \
    # 0 --> 2 -> 5 -> 8------> 10
    #  \                  /
    #  \--> 3 -> 6 -> 9--/

    graph.draw()

    path, visited_order = depth_first_search(graph, 0)
    print("DFS: ", visited_order)
    print("Path: ", path)
    print()
    path, visited_order = breath_first_search(graph, 0)
    print("BFS: ", visited_order)
    print("Path: ", path)


if __name__ == "__main__":
    main()
