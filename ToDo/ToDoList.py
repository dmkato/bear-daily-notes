from ToDo.ToDoLine import ToDoLine
from ToDo.ToDoNode import ToDoNode
from typing import List


class ToDoList:
    def __init__(self, to_do_list_markdown: str):
        self.to_do_items: ToDoNode = self.parse_to_do_items(
            to_do_list_markdown)

    def __str__(self):
        return "Empty To Do List"

    def get_to_do_lines(self, to_do_list_markdown: str) -> List[ToDoLine]:
        to_do_markdown_lines: List[str] = to_do_list_markdown.split(
            "\n")
        return [ToDoLine(line)
                for line in to_do_markdown_lines
                if line.strip() != ""]

    def parse_to_do_items(self, to_do_list_markdown: str) -> ToDoNode:
        to_do_lines: List[ToDoLine] = self.get_to_do_lines(to_do_list_markdown)
        to_do_root = ToDoNode()
        max_indent = max(to_do_lines, key=lambda line: line.indent).indent
        parent = to_do_root

        # for each indent level, add each child to the parent closest before it
        for cur_indent in range(max_indent):
            for line in to_do_lines:
                if line.indent == cur_indent - 1 and parent != None:
                    parent = [node for node
                              in parent.parent.children
                              if node.line == line][0]
                if line.indent == cur_indent and parent != None:
                    parent.children.append(ToDoNode.from_line(line))
            print(to_do_root)
        return to_do_root
