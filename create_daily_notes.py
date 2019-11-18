#!/usr/bin/env python3
from datetime import datetime, timedelta
import sys
import time
import re
import bear

DATE_FORMAT = "%B %d, %Y"


def get_indent(line):
    return len(line) - len(line.strip())


def get_largest_indent(markdown):
    indent_levels = [get_indent(line)
                     for line in markdown.split('\n')]
    return max(indent_levels)


def is_complete(line):
    return len(line.strip()) > 0 and line.strip()[0] == '+'


def is_incomplete(line):
    return len(line.strip()) > 0 and line.strip()[0] == '-'


def has_children(line, cur_indent, markdown, cur_idx, largest_indent):
    if cur_idx + 1 >= len(markdown):
        return False
    return get_indent(markdown[cur_idx + 1]) == cur_indent + 1


def strip_complete(markdown, largest_indent):
    new_markdown_lines = markdown.split('\n')
    for cur_indent in reversed(range(largest_indent+1)):
        new_markdown_lines = [line for idx, line in enumerate(new_markdown_lines)
                              if get_indent(line) != cur_indent
                              or has_children(line, cur_indent, new_markdown_lines, idx, largest_indent)
                              or is_incomplete(line)]
    return '\n'.join(new_markdown_lines)


def strip_incomplete(markdown, largest_indent):
    new_markdown_lines = markdown.split('\n')
    for cur_indent in reversed(range(largest_indent+1)):
        new_markdown_lines = [line for idx, line in enumerate(new_markdown_lines)
                              if get_indent(line) != cur_indent
                              or has_children(line, cur_indent, new_markdown_lines, idx, largest_indent)
                              or is_complete(line)]
    return '\n'.join(new_markdown_lines)


def get_new_title(date_string):
    return datetime.today().strftime(DATE_FORMAT)


def create_new_note(note_markdown):
    [_, today, _, later, notes] = re.split(
        r"\n#* [A-Za-z]*\n", note_markdown)
    today_largest_indent = get_largest_indent(today)
    new_today = f'## Today\n{strip_complete(today[:], today_largest_indent)}\n'
    new_yesterday = f'## Yesterday\n{strip_incomplete(today[:], today_largest_indent)}\n'
    new_later = f'## Later\n{later}'
    new_notes = f'## Notes\n{notes}'
    new_title = get_new_title
    new_markdown = '\n'.join(
        [new_today, new_yesterday, new_later, new_notes])
    bear.create_note(new_title, new_markdown)


def get_last_daily_note_title():
    today = datetime.today()
    while True:
        today -= timedelta(days=1)
        today_title = today.strftime(DATE_FORMAT)
        if bear.does_note_exist(today_title):
            return today_title


def validate_todays_note_does_not_exist():
    today = datetime.today()
    if bear.does_note_exist(today.strftime(DATE_FORMAT)):
        print("Error: Today's note already exists")
        sys.exit(1)
    return


if __name__ == "__main__":
    validate_todays_note_does_not_exist()
    last_daily_note = get_last_daily_note_title()
    note_markdown = bear.open_note(last_daily_note)
    create_new_note(note_markdown)
    print(f"Created note for {last_daily_note}")
