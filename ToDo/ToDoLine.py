class ToDoLine:
    def __init__(self, markdown_line):
        stripped_line: str = markdown_line.strip()
        self.indent: str = len(markdown_line) - len(stripped_line)
        self.control_char: chr = stripped_line.split(" ")[0]
        self.text: str = " ".join(stripped_line.split(" ")[1:])

    def __eq__(self, other):
        return (self.text == other.text and
                self.control_char == other.control_char and
                self.indent == other.indent)

    def __str__(self) -> str:
        return (f'indent: {self.indent}, '
                f'control character: {self.control_char}, '
                f'text: {self.text}')
