#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.subn
# re.subn(pattern, repl, string, count=0, flags=0)

# Perform the same operation as sub(), but return a tuple (new_string, number_of_subs_made).

import re

# define the repl function


def dashrepl(matchobj):
    if matchobj.group(0) == '-':
        return ' '
    else:
        return '-'


print('\nHow to use re.subn with repl function:')
re_source = 'pro----gram-files'

# ValueError: split() requires a non-empty pattern match.
re_pattern = '-{1,2}'
# TypeError: dashrepl() missing 1 required positional argument: 'matchobj'
# re_repl = dashrepl()
re_repl = dashrepl

re_obj = re.compile(re_pattern)

print('The String is as the following: \t"{}"'.format(re_source))
print('The pattern is as the following: \t"{}"'.format(re_pattern))
print('The string is subn by the pattern as the following:')
lst_sub = re.subn(re_obj, re_repl, re_source)
print('\n{}'.format(lst_sub))

# 2015-12-25 05:25 ('pro--gram files', 3)
