#!/usr/bin/env python3
import re
from Bear.Bear import Bear
from ToDo.ToDoList import ToDoList

if __name__ == "__main__":
    bear = Bear()
    note_markdown: str = bear.open_note(title="ToDo")
    to_do_note = ToDoList(note_markdown)
