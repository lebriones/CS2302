from scipy.interpolate import interp1d


class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight


class GraphAL:
    # Constructor
    def __init__(self, vertices, weighted=False, directed=False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.al)

    def insert_vertex(self):
        self.al.append([])

        return len(self.al) - 1  # Return id of new vertex

    def insert_edge(self, source, dest, weight=1):
        if not self.is_valid_vertex(source) or not self.is_valid_vertex(dest):
            print('Error, vertex number out of range')
        elif weight != 1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest, weight))
            if not self.directed:
                self.al[dest].append(Edge(source, weight))

    def delete_edge(self, source, dest):
        if source >= len(self.al) or dest >= len(self.al) or source < 0 or dest < 0:
            print('Error, vertex number out of range')
        else:
            deleted = self._delete_edge(source, dest)
            if not self.directed:
                deleted = self._delete_edge(dest, source)
            if not deleted:
                print('Error, edge to delete not found')

    def _delete_edge(self, source, dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i += 1
        return False

    def num_vertices(self):
        return len(self.al)

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for edge in self.al[src]:
            reachable_vertices.add(edge.dest)

        return reachable_vertices

    def display(self):
        print('[', end='')
        for i in range(len(self.al)):
            print('[', end='')
            for edge in self.al[i]:
                print('(' + str(edge.dest) + ',' + str(edge.weight) + ')', end='')
            print(']', end=' ')
        print(']')

    def draw(self):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.al)):
            for edge in self.al[i]:
                d, w = edge.dest, edge.weight
                if self.directed or d > i:
                    x = np.linspace(i * scale, d * scale)
                    x0 = np.linspace(i * scale, d * scale, num=5)
                    diff = np.abs(d - i)
                    if diff == 1:
                        y0 = [0, 0, 0, 0, 0]
                    else:
                        y0 = [0, -6 * diff, -8 * diff, -6 * diff, 0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i - d)
                    ax.plot(x, s * y, linewidth=1, color='k')
                    if self.directed:
                        xd = [x0[2] + 2 * s, x0[2], x0[2] + 2 * s]
                        yd = [y0[2] - 1, y0[2], y0[2] + 1]
                        yd = [y * s for y in yd]
                        ax.plot(xd, yd, linewidth=1, color='k')
                    if self.weighted:
                        xd = [x0[2] + 2 * s, x0[2], x0[2] + 2 * s]
                        yd = [y0[2] - 1, y0[2], y0[2] + 1]
                        yd = [y * s for y in yd]
                        ax.text(xd[2] - s * 2, yd[2] + 3 * s, str(w), size=12, ha="center", va="center")
            ax.plot([i * scale, i * scale], [0, 0], linewidth=1, color='k')
            ax.text(i * scale, 0, str(i), size=20, ha="center", va="center",
                    bbox=dict(facecolor='w', boxstyle="circle"))
        ax.axis('off')
        ax.set_aspect(1.0)
        plt.show()


import matplotlib.pyplot as plt
import numpy as np

# import graph_AM as graph # Replace line 3 by this one to demonstrate adjacy maxtrix implementation
# import graph_EL as graph # Replace line 3 by this one to demonstrate edge list implementation

if __name__ == "__main__":
    plt.close("all")
    g = GraphAL(6)
    g.insert_edge(0, 1)
    g.insert_edge(0, 2)
    g.insert_edge(1, 2)
    g.insert_edge(2, 3)
    g.insert_edge(3, 4)
    g.insert_edge(4, 1)
    g.display()
    g.draw()
    g.delete_edge(1, 2)
    g.display()
    g.draw()

    g = GraphAL(6, directed=True)
    g.insert_edge(0, 1)
    g.insert_edge(0, 2)
    g.insert_edge(1, 2)
    g.insert_edge(2, 3)
    g.insert_edge(3, 4)
    g.insert_edge(4, 1)
    g.display()
    g.draw()
    g.delete_edge(1, 2)
    g.display()
    g.draw()

    g = GraphAL(6, weighted=True)
    g.insert_edge(0, 1, 4)
    g.insert_edge(0, 2, 3)
    g.insert_edge(1, 2, 2)
    g.insert_edge(2, 3, 1)
    g.insert_edge(3, 4, 5)
    g.insert_edge(4, 1, 4)
    g.display()
    g.draw()
    g.delete_edge(1, 2)
    g.display()
    g.draw()

    g = GraphAL(6, weighted=True, directed=True)
    g.insert_edge(0, 1, 4)
    g.insert_edge(0, 2, 3)
    g.insert_edge(1, 2, 2)
    g.insert_edge(2, 3, 1)
    g.insert_edge(3, 4, 5)
    g.insert_edge(4, 1, 4)
    g.display()
    g.draw()
    g.delete_edge(1, 2)
    g.display()
    g.draw()
