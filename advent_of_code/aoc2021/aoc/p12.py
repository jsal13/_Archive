""" 
Code for https://adventofcode.com/2021/day/12
"""

from collections import defaultdict


class CaveSystem:
    def __init__(self, nodes: list[str], neighbors: dict[str, list[str]]):
        """
        Series of nodes, including start and end, for the cave system.
        """
        self.nodes = nodes
        self.neighbors = neighbors
        self.paths = [["end"]]  # initialize path list.

        self.completed_paths: list[list[str]] = []
        self.no_more_paths = False

    def step_until_complete(self, can_revisit_one_small_cave: bool = False) -> None:
        """Steps through paths until all paths are completed."""
        while True:
            self._step_path(can_revisit_one_small_cave)
            if self.no_more_paths:
                break

    def _step_path(self, can_revisit_one_small_cave: bool = False) -> None:
        def _is_small_cave(c: str) -> bool:
            return c.lower() == c

        # Start at "end" and work back to "start".
        new_paths = []
        for path in self.paths:
            if path[-1] == "start":
                self.completed_paths.append(path)
                continue

            for neighbor in self.neighbors[path[-1]]:

                # Do not revisit "end".
                if neighbor == "end" and "end" in path:
                    continue

                # Add a small cave, depending on parameter for multiple visits.
                elif _is_small_cave(neighbor):
                    visited_small_cave_twice = any(
                        [path.count(p) >= 2 for p in path if p == p.lower()]
                    )
                    visited_this_small_cave = path.count(neighbor) >= 1

                    if visited_this_small_cave and (
                        visited_small_cave_twice or not can_revisit_one_small_cave
                    ):
                        continue

                new_paths.append(path.copy() + [neighbor])

        if not new_paths:
            self.no_more_paths = True
        else:
            self.paths = new_paths

    @classmethod
    def parse_data(cls, data_str: str) -> "CaveSystem":
        lines = data_str.split("\n")
        _edges = [line.split("-") for line in lines]
        nodes = []
        neighbors = defaultdict(list)
        for edge in _edges:
            nodes += [edge[0], edge[1]]  # Dupes filtered below.
            neighbors[edge[0]].append(edge[1])
            neighbors[edge[1]].append(edge[0])
        return cls(nodes=list(set(nodes)), neighbors=neighbors)


if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a12.csv", "r") as f:
        data = f.read()

    def compute_num_paths(data: str, can_revisit_one_small_cave: bool = False) -> int:
        """Computes the total number of paths given the restrictions in the problem."""
        cs = CaveSystem.parse_data(data)
        cs.step_until_complete(can_revisit_one_small_cave)
        return len(cs.completed_paths)

    solution_a = compute_num_paths(data)
    solution_b = compute_num_paths(data, True)

    print(f"AOC12a: {solution_a}\nAOC12b: {solution_b}")
