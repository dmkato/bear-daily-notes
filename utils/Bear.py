from vendor.python_xcall.xcall import xcall

SCHEME = "bear"


class Bear:
    def __init__(self):
        return None

    def open_note(self, title=None):
        command = 'open-note'
        payload = {'title': title}
        res = xcall(SCHEME, command, payload)
        return res['note']

    def create_note(self, title=None, text=""):
        command = 'create'
        payload = {'title': title, 'text': text}
        res = xcall(SCHEME, command, payload)
        return res
