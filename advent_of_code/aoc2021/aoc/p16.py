""" 
Code for https://adventofcode.com/2021/day/16
"""

import math
from typing import Any

# Hex string to binary (0-padded 4-digit) string.
HEX_TO_BIN_STR = {f"{i:0X}": f"{i:04b}" for i in range(16)}


class Packet:
    """Class representation of Packet object."""

    def __init__(self, decoded_packet: str) -> None:
        self.packet = decoded_packet
        self.packet_values: list[Any] = []
        self.cursor = 0
        self.version_sum = 0  # For use in the problem.

    def parse(self) -> None:
        while "1" in self.packet[self.cursor :]:  # Not end-padded zeros.
            self.packet_values.append(self._next_packet())

    def _next_packet(self) -> Any:
        version, type_id = self._read_version_and_type_id()
        if type_id == 4:
            return self._parse_literal_value()
        else:
            length_type_bit = int(self._read_n_digits_and_update_cursor(1))
            if length_type_bit == 0:
                return self._parse_length_type_0_operator(type_id)
            else:
                return self._parse_length_type_1_operator(type_id)

    def _read_version_and_type_id(self) -> tuple[int, int]:
        """Reads the version, increments the cursor, and adds to the version sum.  Returns dict with "version" and "type_id" as keys."""

        version = int(self._read_n_digits_and_update_cursor(3), 2)
        type_id = int(self._read_n_digits_and_update_cursor(3), 2)
        self.version_sum += version

        return (version, type_id)

    def _read_n_digits_and_update_cursor(self, n: int) -> str:
        """Reads and returns a string of n-digits at the current cursor position."""
        digits = self.packet[self.cursor : self.cursor + n]
        self.cursor += n
        return digits

    def _parse_literal_value(self) -> int:
        """Gets literal value of type_id == 4 packet."""

        contents = ""
        packet_complete = False
        while not packet_complete:
            if self.packet[self.cursor] == "0":
                packet_complete = True
            contents += self._read_n_digits_and_update_cursor(n=5)[1:]
        return int(contents, 2)

    def _parse_length_type_0_operator(self, type_id: int) -> int:
        """Parse Lenght_Type 0 Operators."""
        subpacket_len = int(self._read_n_digits_and_update_cursor(15), 2)
        current_cursor_pos = self.cursor
        values = []
        while self.cursor < current_cursor_pos + subpacket_len:
            values.append(self._next_packet())
        return self._parse_values_for_operator_type_id(type_id, values)

    def _parse_length_type_1_operator(self, type_id: int) -> int:
        """Parse Lenght_Type 1 Operators."""
        subpacket_num = int(self._read_n_digits_and_update_cursor(11), 2)
        values = [self._next_packet() for _ in range(subpacket_num)]
        return self._parse_values_for_operator_type_id(type_id, values)

    def _parse_values_for_operator_type_id(
        self, type_id: int, values: list[int]
    ) -> int:
        """Given a list of values, produce the correct output for operator the corresponding type_id."""
        if type_id == 0:
            return sum(values)
        elif type_id == 1:
            return math.prod(values)
        elif type_id == 2:
            return min(values)
        elif type_id == 3:
            return max(values)
        elif type_id == 5:
            return int(values[0] > values[1])
        elif type_id == 6:
            return int(values[0] < values[1])
        elif type_id == 7:
            return int(values[0] == values[1])
        else:
            return -1

    @classmethod
    def decode_packet(cls, encoded_packet: str) -> "Packet":
        decoded_packet = "".join([HEX_TO_BIN_STR[s] for s in encoded_packet])
        return cls(decoded_packet)


# -- Testing --
# Note: the initial tests break at the second part, as we add functionality to make the operators work.  To get around this,
# you can have the `._parse_values_for_operator_type_id` method always return the list itself.
def test_literal_packet() -> None:
    test_encoded_packet = "D2FE28"
    test_packet = Packet.decode_packet(test_encoded_packet)
    test_packet.parse()

    expected_value = [2021]
    assert (
        test_packet.packet_values == expected_value
    ), f"Expected {expected_value}, got {test_packet.packet_values}"


def test_operator_0_packet() -> None:
    test_encoded_packet = "38006F45291200"
    test_packet = Packet.decode_packet(test_encoded_packet)
    test_packet.parse()

    expected_value = [[10, 20]]
    assert (
        test_packet.packet_values == expected_value
    ), f"Expected {expected_value}, got {test_packet.packet_values}"


def test_operator_1_packet() -> None:
    test_encoded_packet = "EE00D40C823060"
    test_packet = Packet.decode_packet(test_encoded_packet)
    test_packet.parse()

    expected_value = [[1, 2, 3]]
    assert (
        test_packet.packet_values == expected_value
    ), f"Expected {expected_value}, got {test_packet.packet_values}"


def test_version_sum() -> None:
    tests = [
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    ]
    for test in tests:
        test_packet = Packet.decode_packet(test[0])
        test_packet.parse()
        assert (
            test_packet.version_sum == test[1]
        ), f"Expected {test[1]}, got {test_packet.version_sum}"


def test_operator_specifics() -> None:
    tests = [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    ]

    for test in tests:
        test_packet = Packet.decode_packet(test[0])
        test_packet.parse()
        assert (
            test_packet.packet_values[0] == test[1]
        ), f"Expected {test[1]}, got {test_packet.packet_values[0]}"


# test_literal_packet()
# test_operator_0_packet()
# test_operator_1_packet()
# test_version_sum()
test_operator_specifics()

if __name__ == "__main__":

    # Initialize Data.
    with open("./aoc/data/a16.csv", "r") as f:
        data = f.read()

    packet = Packet.decode_packet(data)
    packet.parse()
    solution_a = packet.version_sum
    solution_b = packet.packet_values[0]

    print(f"AOC16a: {solution_a}\nAOC16b: {solution_b}")
