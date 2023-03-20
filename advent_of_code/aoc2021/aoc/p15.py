""" 
Code for https://adventofcode.com/2021/day/15
"""

import numpy as np

# Note https://github.com/python/mypy/issues/5485 makes doing dataclasses
# frustrating with mypy, so we'll stick with standard classes for Node.


class Node:
    """Represents a single node in the graph."""

    def __init__(self, row: int, col: int, value: int):
        self.row = row
        self.col = col
        self.value = value


class Graph:
    """Represents a graph of nodes.  Neighbors are determined by proximity in row/column values."""

    def __init__(self, nodes: list[list[Node]]) -> None:
        self.nodes = nodes

    @property
    def size(self) -> int:
        return len(self.nodes)

    def __getitem__(self, pos: tuple[int, int]) -> Node:
        """Returns a node at pos = [row, col]."""
        return self.nodes[pos[0]][pos[1]]

    def get_neighbors(self, node: Node) -> list[Node]:
        neighbors = []
        row, col = node.row, node.col

        if row > 0:
            neighbors.append(self[row - 1, col])
        if col > 0:
            neighbors.append(self[row, col - 1])
        if row < self.size - 1:
            neighbors.append(self[row + 1, col])
        if col < self.size - 1:
            neighbors.append(self[row, col + 1])

        return neighbors

    def dijkstra(
        self, start_node: tuple[int, int] = (0, 0), end_node: tuple = (-1, -1)
    ) -> int:
        """Runs Dijkstra's algorithm to calculate minimum path from `start_node` to `end_node` on the graph.

        Parameters
        ----------
        start_node : tuple[int, int], optional
            Node index to start at, by default (0, 0)
        end_node : tuple, optional
            Node index to end at, by default (-1, -1)

        Returns
        -------
        int
            Total cost of the shortest path.
        """

        cost_matrix = np.infty * np.ones(shape=(self.size, self.size))
        cost_matrix[0, 0] = 0

        # We use a queue here to pop out already visited and marked nodes.
        queue = [self[start_node[0], start_node[1]]]
        while queue:
            current_node = queue.pop(0)
            for neighbor in self.get_neighbors(current_node):

                # Take the current cost for the neighbor and compare it
                # to the current node's total cost plus the neighbor's cost.

                neighbor_cost = cost_matrix[neighbor.row, neighbor.col]
                go_to_neighbor_cost = (
                    cost_matrix[current_node.row, current_node.col] + neighbor.value
                )

                # If it's less than the current neighbor cost, assign the neighbor the
                # cost of going from the current node to that neighbor.  Put the neighbor in the queue,
                # so we can search from that node now.
                if neighbor_cost > go_to_neighbor_cost:
                    cost_matrix[neighbor.row, neighbor.col] = go_to_neighbor_cost
                    queue.append(neighbor)

        return int(cost_matrix[end_node[0], end_node[1]])

    @classmethod
    def parse_input(cls, raw_input: str) -> "Graph":
        """Parses data (rows + cols of digits) from raw input into usable form."""
        input_split = [list(map(int, val)) for val in raw_input.splitlines()]
        size = len(input_split)  # Square
        nodes = np.array(
            [
                Node(row, col, input_split[row][col])
                for row in range(size)
                for col in range(size)
            ]
        )
        nodes = np.reshape(nodes, (size, size))
        return cls(nodes.tolist())


if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a15.csv", "r") as f:
        data = f.read()

    g = Graph.parse_input(data)
    solution_a = g.dijkstra()

    # -- PART 2 --
    # TODO: This could most likely be done in a significantly nicer way.
    def make_5x5_tiling_with_increments(input_data: str) -> list[list[Node]]:
        """Creates a 5x5 tiling of the input data graph, where the value is incremented by 1 for each item as it is tiled right and down.  9 -> 1, wrapping around.  The return value is a list of lists of Nodes."""

        # Get all values from the nodes in the standard-size Tile.
        vget_value_from_node = np.vectorize(lambda n: n.value)
        g = Graph.parse_input(data)
        data_tile = vget_value_from_node(g.nodes)

        # For-loops over each tile to make a row, then for-loops each finished row
        # to make the full tiles.
        data_tile_row = [data_tile.copy()]
        for _ in range(1, 5):
            tmp_data_tile = (data_tile_row[-1] + 1) % 10
            tmp_data_tile[tmp_data_tile == 0] += 1
            data_tile_row.append(tmp_data_tile)

        data_row = np.concatenate(data_tile_row, axis=1)
        data_tile = [data_row]

        for _ in range(1, 5):
            tmp_data_row = (data_tile[-1] + 1) % 10
            tmp_data_row[tmp_data_row == 0] += 1
            data_tile.append(tmp_data_row)

        value_data = np.concatenate(data_tile, axis=0)
        size = len(value_data)
        nodes_tiled = np.array(
            [
                Node(row, col, value_data[row, col])
                for row in range(size)
                for col in range(size)
            ]
        )
        nodes_tiled = np.reshape(nodes_tiled, (size, size))

        return nodes_tiled.tolist()

    nodes_tiled = make_5x5_tiling_with_increments(data)
    solution_b = Graph(nodes_tiled).dijkstra()

    print(f"AOC15a: {solution_a}\nAOC15b: {solution_b}")
