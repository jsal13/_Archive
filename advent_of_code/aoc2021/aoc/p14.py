""" 
Code for https://adventofcode.com/2021/day/14
"""

from collections import defaultdict
from typing import Dict


class PolymerTemplate:
    """Class representing the polymer template."""

    def __init__(self, polymer_template: str, insertion_rules: Dict[str, str]) -> None:
        self.polymer_template = polymer_template
        self.insertion_rules = insertion_rules

        # Initializes the count for the current pairs we have.
        self.current_pair_counts: Dict[str, int] = defaultdict(int)
        for idx in range(len(self.polymer_template) - 1):
            self.current_pair_counts[self.polymer_template[idx : idx + 2]] += 1

    def step(self) -> None:
        """Steps through inserting and updating current_pair_counts."""
        self.current_pair_counts_copy = self.current_pair_counts.copy()
        for poly, num_pairs in self.current_pair_counts.items():
            self.insert_from_rule(poly)
        self.current_pair_counts = self.current_pair_counts_copy

    def insert_from_rule(self, poly_pair: str) -> None:
        """Gets the rule and adds new polymer pairs to the current_pair_counts."""
        rule = self.insertion_rules[poly_pair]
        num_pairs = self.current_pair_counts[poly_pair]

        # Adds two new polymers to the count.
        self.current_pair_counts_copy[f"{poly_pair[0]}{rule}"] += num_pairs
        self.current_pair_counts_copy[f"{rule}{poly_pair[1]}"] += num_pairs

        # Removes the old, modified polymer.
        self.current_pair_counts_copy[poly_pair] -= num_pairs

    def count_polymers(self) -> dict[str, int]:
        """Counts the total number of polymer singletons in `current_pair_counts`."""
        total_polymer_count: dict[str, int] = defaultdict(int)

        # Take the first value in the original series,
        # then we'll look at the second value in each
        # pair so that we don't double-count.
        total_polymer_count[self.polymer_template[0]] += 1

        for pair, count in self.current_pair_counts.items():
            total_polymer_count[pair[1]] += count

        return total_polymer_count

    @classmethod
    def parse_data(cls, data: str) -> "PolymerTemplate":
        polymer_template, insertion_rules_raw = data.split("\n\n")

        # Note: Split this into two parts mainly due to
        # https://github.com/python/typeshed/issues/4450
        insertion_rules_tuples = [
            tuple(rule.split(" -> ")) for rule in insertion_rules_raw.splitlines()
        ]
        insertion_rules = {r[0]: r[1] for r in insertion_rules_tuples}

        return cls(polymer_template=polymer_template, insertion_rules=insertion_rules)


if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a14.csv", "r") as f:
        data = f.read()

    def count_polymers(data: str, steps: int = 10) -> int:
        """Counts polymers given the data after `steps` steps."""
        pt = PolymerTemplate.parse_data(data)
        for i in range(steps):
            pt.step()

        counts = sorted(
            [(k, v) for k, v in pt.count_polymers().items()], key=lambda x: x[1]
        )
        return counts[-1][1] - counts[0][1]

    solution_a = count_polymers(data, 10)
    solution_b = count_polymers(data, 40)

    print(f"AOC14a: {solution_a}\nAOC14b: {solution_b}")
