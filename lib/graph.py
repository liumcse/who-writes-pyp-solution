import math

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


class DuplicateStudentException(Exception):
    def __init__(self, student_name):
        super().__init__("Duplicate student `" + student_name + "`!")


class StudentNode:
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


class DirectedEdge:
    def __init__(self, target, weight):
        self.target = target
        self.weight = weight

    def get_student_node(self):
        return self.target

    def get_weight(self):
        return self.weight


class Graph:
    def __init__(self):
        self.course_list = []
        self.edges = {}

    def _add_course(self, student_node, course_code, weight):
        if course_code not in self.course_list:
            self.course_list.append(course_code)
            self.edges[course_code] = []
        self.edges[course_code].append(DirectedEdge(student_node, weight))

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
        """Warning: using this function will change Graph state. Call it once only!
        """
        result = {}
        for course_code in self.course_list:
            min_weight = math.inf
            selected = None
            # Update each edge and find the edge with smallest weight
            for edge in self.edges[course_code]:
                student_node = edge.get_student_node()
                edge_weight = edge.get_weight() + student_node.get_offset()
                if edge_weight < min_weight:
                    min_weight = edge_weight
                    selected = student_node
            # Add into result
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

        import json
        print(json.dumps(result, indent=2))
