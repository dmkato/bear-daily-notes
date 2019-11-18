from vendor.python_xcall.xcall import xcall

SCHEME = "bear"


def open_note_with_meta(title=None):
    command = 'open-note'
    payload = {'title': title}
    res = xcall(SCHEME, command, payload)
    return res


def open_note(title=None):
    return open_note_with_meta(title)['note']


def create_note(title=None, text=""):
    command = 'create'
    payload = {'title': title, 'text': text}
    res = xcall(SCHEME, command, payload)
    return res


def does_note_exist(title=None):
    try:
        note = open_note_with_meta(title)
        return note['is_trashed'] == 'no'
    except:
        return False
