""" 
Code for https://adventofcode.com/2021/day/18
"""

import copy
import string
import math
from itertools import permutations


class Node:
    """Class representing individual element in the summand."""

    def __init__(self, value: int, depth: int) -> None:
        """Represents individual element in the summand.

        Parameters
        ----------
        value : int
            Numeric value of the element.
        depth : int
            Depth of the element, in terms of how far it is nested.
        """
        self.value = value
        self.depth = depth

    def __repr__(self) -> str:
        return f"Node(value={self.value}, depth={self.depth})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return self.value == other.value and self.depth == other.depth
        return False


class Nodes:
    """Class representing a collection of Node objects."""

    def __init__(self, nodes: list[Node]):
        self.nodes = nodes

    def __repr__(self) -> str:
        return ", ".join(str(n) for n in self.nodes)

    def explode(self) -> None:
        """
        To explode a pair, the pair's left value is added to the first regular number to the left of the exploding pair (if any), and the pair's right value is added to the first regular number to the right of the exploding pair (if any). Exploding pairs will always consist of two regular numbers. Then, the entire exploding pair is replaced with the regular number 0.
        """

        new_nodes = copy.deepcopy(self.nodes)
        for n, node in enumerate(new_nodes):
            if n == len(new_nodes) - 1:
                break
            # If the depth is more than 5, explode.
            # The for-loop will always get the left-most node first,
            # check that the node to the right is at the same level.
            if node.depth >= 5 and new_nodes[n + 1].depth == node.depth:
                if n != 0:  # if not the leftmost...
                    new_nodes[n - 1].value += node.value
                if n != len(new_nodes) - 2:  # if right node is not right-most...
                    new_nodes[n + 2].value += new_nodes[n + 1].value

                # Add in new 0 node, remove the exploded nodes.
                new_nodes = (
                    new_nodes[:n] + [Node(0, node.depth - 1)] + new_nodes[n + 2 :]
                )
                break

        self.nodes = new_nodes

    def split_node(self) -> None:
        """To split a regular number, replace it with a pair; the left element of the pair should be the regular number divided by two and rounded down, while the right element of the pair should be the regular number divided by two and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes [6,6], and so on."""
        result_nodes = []

        already_split = False
        for n, node in enumerate(self.nodes):

            if node.value < 10 or already_split:
                result_nodes.append(node)

            else:
                result_nodes.append(Node(math.floor(node.value / 2), node.depth + 1))
                result_nodes.append(Node(math.ceil(node.value / 2), node.depth + 1))
                already_split = True

        self.nodes = result_nodes

    def reduce_nodes(self) -> None:
        while True:
            new_nodes: list[Node] = copy.deepcopy(self.nodes)
            self.explode()
            if new_nodes != self.nodes:
                # If an explosion has occurred, go back to the top.
                continue
            self.split_node()
            if new_nodes == self.nodes:
                break

    def add_new_nodes(self, right_node: "Nodes") -> None:
        """Add a node (on the right) to our existing nodes."""
        self.nodes = self.nodes + right_node.nodes
        for node in self.nodes:
            node.depth += 1

        self.reduce_nodes()

    def get_magnitude(self) -> int:
        _nodes = copy.deepcopy(self.nodes)
        while len(_nodes) > 1:

            if len(_nodes) == 2:
                _nodes = [
                    Node(value=3 * _nodes[0].value + 2 * _nodes[1].value, depth=0)
                ]
                break

            new_nodes = []
            for idx in range(len(_nodes) - 1):
                if _nodes[idx].depth == _nodes[idx + 1].depth:
                    new_node_val = 3 * _nodes[idx].value + 2 * _nodes[idx + 1].value

                    new_nodes = (
                        _nodes[:idx]
                        + [Node(new_node_val, depth=_nodes[idx].depth - 1)]
                        + _nodes[idx + 2 :]
                    )
                    _nodes = new_nodes
                    break

        return _nodes[0].value

    @classmethod
    def parse_data(cls, data: str) -> "Nodes":
        """Pretty gnarly way to do this.  I'll look back and see if there's something nicer with some kind of AST algs.  Right now,
        it just sort of goes over the symbols and for each one makes some alteration to depth (depth in the list), position (left or right),
        and the current digit we're considering.  Not a good parser."""

        nodes = []
        current_depth = 0
        current_digit = ""
        for symbol in data:
            if symbol == "[":
                current_depth += 1
            elif symbol in string.digits:
                current_digit += symbol
            elif symbol == ",":
                if current_digit:
                    nodes.append(Node(int(current_digit), current_depth))
                    current_digit = ""
            elif symbol == "]":
                if current_digit:
                    nodes.append(Node(int(current_digit), current_depth))
                    current_digit = ""
                current_depth -= 1
            else:
                print(f"Don't know what to do with {symbol} .")

        return Nodes(nodes)


# -- Helper Functions --


def get_sum_and_magnitude_for_input(data: list[str]) -> int:
    """Takes input data, sums all values, returns the magnitude."""
    n = Nodes.parse_data(data[0])
    for _n in data[1:]:
        n.add_new_nodes(Nodes.parse_data(_n))
    n.reduce_nodes()
    return n.get_magnitude()


def all_magnitudes_of_two_summands(data: list[str]) -> int:
    """Brute force, sums all pairs together (non-commutative!) and returns a list of magnitudes."""

    nodes = [Nodes.parse_data(data[i]) for i in range(len(data))]
    magnitudes = []
    for idxs in list(permutations(range(len(nodes)), 2)):
        nn = copy.deepcopy(nodes[idxs[0]])
        nn1 = copy.deepcopy(nodes[idxs[1]])
        nn.add_new_nodes(nn1)

        magnitudes.append(nn.get_magnitude())

    return max(magnitudes)


# -- Tests --


def test_explode_once() -> None:
    """Tests related to exploding once."""

    tests = [
        ("[[[[[9,8],1],2],3],4]", [0, 9, 2, 3, 4]),
        ("[7,[6,[5,[4,[3,2]]]]]", [7, 6, 5, 7, 0]),
        ("[[6,[5,[4,[3,2]]]],1]", [6, 5, 7, 0, 3]),
        ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", [3, 2, 8, 0, 9, 5, 4, 3, 2]),
        ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", [3, 2, 8, 0, 9, 5, 7, 0]),
    ]

    for test in tests:
        n = Nodes.parse_data(test[0])
        n.explode()
        assert [s.value for s in n.nodes] == test[1]


def test_split_once() -> None:
    """Tests related to splitting once."""

    tests = [
        ("[[10,1],[4,17]]", [5, 5, 1, 4, 17]),
    ]

    for test in tests:
        n = Nodes.parse_data(test[0])
        n.split_node()
        assert [s.value for s in n.nodes] == test[1]


def test_adding_nodes() -> None:
    """Tests related to adding and reducing new nodes."""

    tests = [
        (["[[[[4,3],4],4],[7,[[8,4],9]]]", "[1,1]"], [0, 7, 4, 7, 8, 6, 0, 8, 1]),
    ]

    for test in tests:
        n = Nodes.parse_data(test[0][0])
        n2 = Nodes.parse_data(test[0][1])
        n.add_new_nodes(n2)
        n.reduce_nodes()
        assert [s.value for s in n.nodes] == test[1]


def test_sum_multiple() -> None:
    """Tests relating to summing multiple nodes and reducing."""

    tests = [
        (["[1,1]", "[2,2]", "[3,3]", "[4,4]"], [1, 1, 2, 2, 3, 3, 4, 4]),
        (["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]"], [3, 0, 5, 3, 4, 4, 5, 5]),
        (
            ["[1,1]", "[2,2]", "[3,3]", "[4,4]", "[5,5]", "[6,6]"],
            [5, 0, 7, 4, 5, 5, 6, 6],
        ),
        (
            [
                "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
                "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
                "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
                "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
                "[7,[5,[[3,8],[1,4]]]]",
                "[[2,[2,2]],[8,[8,1]]]",
                "[2,9]",
                "[1,[[[9,3],9],[[9,0],[0,7]]]]",
                "[[[5,[7,4]],7],1]",
                "[[[[4,2],2],6],[8,7]]",
            ],
            [8, 7, 7, 7, 8, 6, 7, 7, 0, 7, 6, 6, 8, 7],
        ),
    ]

    for test in tests:
        n = Nodes.parse_data(test[0][0])
        for _n in test[0][1:]:
            n.add_new_nodes(Nodes.parse_data(_n))
        n.reduce_nodes()

        msg = f"Expected {test[1]}, got {[i.value for i in n.nodes]}."
        assert [i.value for i in n.nodes] == test[1], msg


def test_magnitude() -> None:
    """Tests related to calculating magnitude."""
    tests = [
        ("[[1,2],[[3,4],5]]", 143),
        ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
        ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
        ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
        ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
        ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
    ]

    for test in tests:
        n = Nodes.parse_data(test[0])
        n.reduce_nodes()

        assert (
            n.get_magnitude() == test[1]
        ), f"Expected {test[1]}, got { n.get_magnitude()}."


def test_misc_input() -> None:
    """Test for a larger input."""
    tests = [
        (
            [
                "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
                "[[[5,[2,8]],4],[5,[[9,9],0]]]",
                "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
                "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
                "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
                "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
                "[[[[5,4],[7,7]],8],[[8,3],8]]",
                "[[9,3],[[9,9],[6,[4,9]]]]",
                "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
                "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
            ],
            4140,
        )
    ]

    for test in tests:
        n = Nodes.parse_data(test[0][0])
        for _n in test[0][1:]:
            n.add_new_nodes(Nodes.parse_data(_n))
        n.reduce_nodes()

        assert (
            n.get_magnitude() == test[1]
        ), f"Expected {test[1]}, got { n.get_magnitude()}."


def test_magnitude_of_two_summands() -> None:
    """Tests the function which finds the greatest magnitude of any two summands of a list of Nodes."""
    tests = [
        (
            [
                "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
                "[[[5,[2,8]],4],[5,[[9,9],0]]]",
                "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
                "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
                "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
                "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
                "[[[[5,4],[7,7]],8],[[8,3],8]]",
                "[[9,3],[[9,9],[6,[4,9]]]]",
                "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
                "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
            ],
            3993,
        )
    ]

    for test in tests:
        value = all_magnitudes_of_two_summands(test[0])
        assert value == test[1], f"Expected {test[1]}, got { value }."


def run_tests() -> None:
    test_explode_once()
    test_split_once()
    test_adding_nodes()
    test_sum_multiple()
    test_magnitude()
    test_misc_input()
    test_magnitude_of_two_summands()


run_tests()

# ---

if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a18.csv", "r") as f:
        data = f.read().splitlines()

    solution_a = get_sum_and_magnitude_for_input(data)
    solution_b = all_magnitudes_of_two_summands(data)

    print(f"AOC18a: {solution_a}\nAOC18b: {solution_b}")
