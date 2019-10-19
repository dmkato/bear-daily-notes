#!/usr/bin/env python3
import re
from utils.Bear import Bear


def tokenize_note(note):
    return [("##" if idx != 0 else "") + section for (idx, section) in enumerate(note.split("##"))]


def remove_completed(section):
    lines = section.split("\n")
    completed = get_completed_tasks(lines)
    # completed = [line for line in lines if re.match(r'\s*\+', line)]
    incomplete = [line for line in lines if line not in completed]
    return ("\n".join(incomplete), "\n".join(completed))


if __name__ == "__main__":
    bear = Bear()
    note = bear.open_note(title="ToDo")

    (title, today, tomorrow, this_week,
        this_month, yesterday) = tokenize_note(note)
    (new_today, completed) = remove_completed(today)
    (yesterday_title, _) = remove_completed(yesterday)
    new_yesterday = yesterday_title + completed
    new_note = title + new_today + tomorrow + \
        this_week + this_month + new_yesterday

    print(f'Note: \n{note}')
    print(f'New Note: \n{new_note}')
