#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations
# » 6.2.5. Regular Expression Examples
#  6.2.5.9. Writing a Tokenizer


# A tokenizer or scanner analyzes a string to categorize groups of characters.
# This is a useful first step in writing a compiler or interpreter.
#
# The text categories are specified with regular expressions.
# The technique is to combine those into a single master regular expression
# and to loop over successive matches:

import collections
import re

Token = collections.namedtuple('Token', ['typ', 'value', 'line', 'column'])


def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',      r'\d+(\.\d*)?'),    # Integer or decimal number
        ('ASSIGN',      r':='),             # Assignment operator
        ('END',         r';'),              # Statement terminator
        ('ID',          r'[A-Za-z]+'),      # Identifiers
        ('OP',          r'[+\-*/]'),        # Arithmetic operators
        ('NEWLINE',     r'\n'),             # Line endings
        ('SKIP',        r'[ \t]+'),         # Skip over spaces and tabs
        ('MISMATCH',    r'.'),              # Any other character
    ]
    # format 格式的写法是如何的呢?
    # tok_regex = '|'.join('(?P<{}>{})'.format(pair for pair in token_specification))
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    line_num = 1
    line_start = 0

    for mo in re.finditer(tok_regex, code):
        # print(mo)
        kind = mo.lastgroup
        # print(kind)
        value = mo.group(kind)
        # print(value)
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError('%r unexpected on line %d' % (value, line_num))
        else:
            if kind == 'ID' and value in keywords:
                kind = value
            column = mo.start() - line_start
            yield Token(kind, value, line_num, column)

statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
'''

for token in tokenize(statements):
    print(token)
