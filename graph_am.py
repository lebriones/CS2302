from scipy.interpolate import interp1d


class GraphAM:

    def __init__(self, vertices, weighted=False, directed=False):
        self.am = []

        for i in range(vertices):  # Assumption / Design Decision: 0 represents non-existing edge
            self.am.append([0] * vertices)

        self.vertices = vertices
        self.directed = directed
        self.weighted = weighted
        self.representation = 'AM'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.am)

    def insert_vertex(self):
        for lst in self.am:
            lst.append(0)

        new_row = [0] * (len(self.am) + 1)  # Assumption / Design Decision: 0 represents non-existing edge
        self.am.append(new_row)

        return len(self.am) - 1  # Return new vertex id

    def insert_edge(self, src, dest, weight=1):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.am[src][dest] = weight

        if not self.directed:
            self.am[dest][src] = weight

    def delete_edge(self, src, dest):
        self.insert_edge(src, dest, 0)

    def num_vertices(self):
        return len(self.am)

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for i in range(len(self.am)):
            if self.am[src][i] != 0:
                reachable_vertices.add(i)

        return reachable_vertices

    def display(self):
        print('[', end='')
        for i in range(len(self.am)):
            print('[', end='')
            for j in range(len(self.am[i])):
                edge = self.am[i][j]
                if edge != 0:
                    print('(' + str(j) + ',' + str(edge) + ')', end='')
            print(']', end=' ')
        print(']')

    def draw(self):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.am)):
            for j in range(len(self.am[i])):
                edge = self.am[i][j]

                if edge != 0:
                    d, w = j, edge
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
    g = GraphAM(6)
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

    g = GraphAM(6, directed=True)
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

    g = GraphAM(6, weighted=True)
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

    g = GraphAM(6, weighted=True, directed=True)
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
