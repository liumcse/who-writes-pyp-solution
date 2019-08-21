"""Tests for course_list."""

from lib.course_list import CourseList
import unittest

data = [
    {
        "name": "Tom",
        "first_choice": "CX1003",
        "second_choice": "CX1007",
        "third_choice": "CZ3003",
    },
    {
        "name": "Bob",
        "first_choice": "CZ3003",
        "second_choice": "CX3001",
        "third_choice": "CX1003",
    },
    {
        "name": "Lian",
        "first_choice": "CE3007",
        "second_choice": "",
        "third_choice": "",
    },
]


class CourseListTest(unittest.TestCase):

    def test_will_output_result(self):
        goal = {
            "CX1003": ("Tom",),
            "CX1007": ("Tom",),
            "CZ3003": ("Bob",),
            "CX3001": ("Bob",),
            "CE3007": ("Lian",),
        }
        course_list = CourseList()
        for info in data:
            course_list.add_student(
                info["name"], info["first_choice"], info["second_choice"], info["third_choice"])
        self.assertDictEqual(course_list.execute(), goal)


if __name__ == '__main__':
    unittest.main()
