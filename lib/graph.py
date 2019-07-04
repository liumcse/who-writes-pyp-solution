"""TODO(xming): DO NOT SUBMIT without one-line documentation for graph.

TODO(xming): DO NOT SUBMIT without a detailed description of graph.
"""


class Node:
    def __init__(self, identifier, first_choice, second_choice, third_choice):
        self.identifier = identifier,
        self.first_choice = first_choice,
        self.second_choice = second_choice,
        self.third_choice = third_choice,
        self.offset = 0


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
