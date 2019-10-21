from ToDo.ToDoLine import ToDoLine
from typing import List


class ToDoNode:
    def __init__(self):
        self.children: List = []
        self.parent = None
        self.line: ToDoLine = None

    def __str__(self):
        return f'Line: {{ {self.line} }}, children: {[f"{{ {child} }}" for child in self.children]}'

    @classmethod
    def from_line(cls, to_do_line: ToDoLine):
        to_do_node = cls()
        to_do_node.line = to_do_line
        return to_do_node
