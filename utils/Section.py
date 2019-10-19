from utils.Task import Task


class Section:
    def __init__(self, init_str=""):
        if init_str == "":
            return
        (title, tasks) = self.parse_init_str(init_str)
        self.title = title
        self.tasks = tasks

    def parse_task(self, task):
        checkbox = task.strip()[0]
        [tabs, message] = task.split(f'{checkbox} ', 1)
        level = len(tabs)
        complete = checkbox == '+'
        return (message, complete, level)

    def get_level(self, task):
        (_, _, level) = self.parse_task(task)
        return level

    def get_children(self, tasks, idx, level):
        children = []
        for task in tasks[idx+1:]:
            if self.get_level(task) == level:
                return children
            children += [task]
        return children

    def parse_tasks(self, task_lines, base_level=0):
        if task_lines == []:
            return []
        tasks = []
        for (idx, task) in enumerate(task_lines):
            (message, complete, level) = self.parse_task(task)
            if level > base_level:
                continue
            subtasks = self.get_children(task_lines, idx, level)
            tasks += [Task(message, complete,
                           self.parse_tasks(subtasks, base_level + 1), level)]
        return tasks

    def parse_init_str(self, init_str):
        lines = init_str.split("\n")
        raw_title = lines[0]
        raw_tasks = lines[1:]
        title = raw_title.split("## ")[1]
        tasks = self.parse_tasks(raw_tasks)
        return (title, tasks)

    def __str__(self):
        title = f'## {self.title}\n'
        task_strs = str(self.tasks)
        return title + task_strs
