import math
import random
import json

OFFSET = {
    "first_choice": 10,
    "second_choice": 10,
    "third_choice": 10
}

WEIGHT = {
    "first_choice": 10,
    "second_choice": 20,
    "third_choice": 30
}


class StudentNode:
    """Represents a student and their choices.

    Attributes:
        identifier -- A string represents the name of the student.
        first_choice -- A string represents the first choice of course.
        second_choice -- A string represents the second choice of course.
        third_choice -- A string represents the third choice of course.
    """

    def __init__(self, identifier, first_choice, second_choice, third_choice):
        self.identifier = identifier,
        self.first_choice = first_choice,
        self.second_choice = second_choice,
        self.third_choice = third_choice,
        self.offset = 0

    def get_name(self):
        return self.identifier

    def get_first_choice(self):
        return self.first_choice

    def get_second_choice(self):
        return self.second_choice

    def get_third_choice(self):
        return self.third_choice

    def get_offset(self):
        return self.offset

    def update_offset(self, new_offset):
        self.offset += new_offset


class Branch:
    """Weighted branch that points to a student.

    Attributes:
        target -- A StudentNode represents the student it points to.
        weight -- An integer represents the weight of the branch.
    """

    def __init__(self, target, weight):
        self.target = target
        self.weight = weight

    def get_student_node(self):
        return self.target

    def get_weight(self):
        return self.weight


class CourseList:
    """List of courses with weighted branches pointing to students.

    Raises:
        Exception: When execute() is called more than once.
    """

    def __init__(self):
        self.course_list = []
        self.branches = {}
        self.dirty = False

    def _add_course(self, student_node, course_code, weight):
        if course_code not in self.course_list:
            self.course_list.append(course_code)
            self.branches[course_code] = []
        self.branches[course_code].append(Branch(student_node, weight))

    def add_student(self, identifier, first_choice, second_choice, third_choice):
        student_node = StudentNode(
            identifier, first_choice, second_choice, third_choice)
        if first_choice:
            self._add_course(student_node, first_choice,
                             WEIGHT["first_choice"])
        if second_choice:
            self._add_course(student_node, second_choice,
                             WEIGHT["second_choice"])
        if third_choice:
            self._add_course(student_node, third_choice,
                             WEIGHT["third_choice"])

    def execute(self):
        """Calling this method will result in state change.
        """
        if self.dirty:
            raise Exception("Execute should only be called once!")
        self.dirty = True
        result = {}
        for course_code in self.course_list:
            min_weight = math.inf
            selected = None
            # Update each branch and find the one with smallest weight
            # Use random selection to break tie
            mapping = {}
            for branch in self.branches[course_code]:
                student_node = branch.get_student_node()
                branch_weight = branch.get_weight() + student_node.get_offset()
                if branch_weight < min_weight:
                    min_weight = branch_weight
                if branch_weight not in mapping:
                    mapping[branch_weight] = []
                mapping[branch_weight].append(student_node)
            selected = random.choice(mapping[min_weight])
            result[course_code] = selected.get_name()
            # Update student offset
            if course_code == selected.get_first_choice():
                selected.update_offset(
                    selected.get_offset + OFFSET["first_choice"])
            elif course_code == selected.get_second_choice():
                selected.update_offset(
                    selected.get_offset + OFFSET["second_choice"])
            elif course_code == selected.get_third_choice():
                selected.update_offset(
                    selected.get_offset + OFFSET["third_choice"])

        print(json.dumps(result, indent=2))
        return result
