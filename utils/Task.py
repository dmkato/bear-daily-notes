class Task:
    def __init__(self, message='', complete='', subtasks=[], level=0):
        self.message = message
        self.complete = complete
        self.subtasks = subtasks
        self.level = level

    def __str__(self):
        tabs = '\t' * self.level
        checkbox = '+' if self.complete else '-'
        message_str = tabs + checkbox + self.message + '\n'
        child_tasks = self.subtasks and [str(line) for line in self.subtasks]
        return message_str + child_tasks
