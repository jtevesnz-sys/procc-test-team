"""Bounded offline HTML checks; no browser execution or network access."""
from html.parser import HTMLParser
from pathlib import Path
import sys


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.in_title = False
        self.main = False
        self.h1 = False
        self.missing_alt = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'title':
            self.in_title = True
        elif tag == 'main' or attrs.get('role') == 'main':
            self.main = True
        if tag == 'h1':
            self.h1 = True
        if tag == 'img' and 'alt' not in attrs:
            self.missing_alt += 1

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def check(html):
    page = Page()
    page.feed(html)
    return {
        'Page title': bool(page.title.strip()),
        'Main landmark': page.main,
        'H1 element': page.h1,
        'Image alt attributes': page.missing_alt == 0,
    }


def main(args):
    if len(args) != 1:
        print('Usage: python website_check.py local-file.html', file=sys.stderr)
        return 2
    try:
        html = Path(args[0]).read_text(encoding='utf-8')
    except (OSError, UnicodeError) as exc:
        print('Cannot read file:', exc, file=sys.stderr)
        return 2
    result = check(html)
    for name, passed in result.items():
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    print('NOT_RUN: Browser interactions, responsive layout and live availability')
    return 0 if all(result.values()) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
