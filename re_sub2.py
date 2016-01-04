#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.sub
# re.sub(pattern, repl, string, count=0, flags=0)

# repl can be a string or a function; if it is a string, any backslash escapes in it are processed. That is, \n is converted to a single newline character, \r is converted to a carriage return, and so forth. Unknown escapes such as \& are left alone. Backreferences, such as \6, are replaced with the substring matched by group 6 in the pattern. For example:

import re

print('\nHow to use re.sub:')
re_source = 'def myfunc():'

# ValueError: split() requires a non-empty pattern match.
re_pattern = r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):'
re_repl = r'static PyObject*\npy_\1(void)\n{'

re_obj = re.compile(re_pattern)

print('The String is as the following: \t"{}"'.format(re_source))
print('The pattern is as the following: \t"{}"'.format(re_pattern))
print('The string is sub by the pattern as the following:')
lst_sub = re.sub(re_pattern, re_repl, re_source)
print('\n{}'.format(lst_sub))

# 2015-12-23 06:38 终于明白\number, group()的用法了,提取如此的方便,继续学习吧
