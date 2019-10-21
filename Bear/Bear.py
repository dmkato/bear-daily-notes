from vendor.python_xcall.xcall import xcall


class Bear:
    SCHEME = "bear"

    def open_note(self, title=None):
        command = 'open-note'
        payload = {'title': title}
        res = xcall(self.SCHEME, command, payload)
        return res['note']

    def create_note(self, title=None, text=""):
        command = 'create'
        payload = {'title': title, 'text': text}
        res = xcall(self.SCHEME, command, payload)
        return res
