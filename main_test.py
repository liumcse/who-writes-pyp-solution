"""Tests for main."""

import main
import unittest

data_src = [
    ["Tom", "cx1003", "CX1007", "cx1006"],
    ["Bob", "CZ3003", "Cx3001", ""],
    ["Lian", "cE3007", "", ""],
]


class MainTest(unittest.TestCase):

    def test_extract_from_data(self):
        goal = [
            {
                "name": "Tom",
                "first_choice": "CX1003",
                "second_choice": "CX1007",
                "third_choice": "CX1006",
            },
            {
                "name": "Bob",
                "first_choice": "CZ3003",
                "second_choice": "CX3001",
                "third_choice": "",
            },
            {
                "name": "Lian",
                "first_choice": "CE3007",
                "second_choice": "",
                "third_choice": "",
            },
        ]
        self.assertListEqual(main.extract_from_data(
            data_src, 0, 1, 2, 3), goal)


if __name__ == '__main__':
    unittest.main()
