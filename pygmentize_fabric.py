#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygments import highlight
from fabric_lexer import FabLexer
from pygments.formatters import HtmlFormatter
from jinja2 import Template

def main():
    with open("input.txt") as fab_f:
        with open("out.jinja") as jinja_f:
            with open('out.html', 'w') as out_f:
                source = highlight(fab_f.read(),
                        FabLexer(),
                        HtmlFormatter(style="friendly"))
                out = Template(jinja_f.read()).render(source=source)
                out_f.write(out.encode('utf-8'))

if __name__ == '__main__':
    main()
