#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.
# re.split(pattern, repl, string, count=0, flags=0)

#


import re

print('\nHow to use re.split on empty pattern match:')
re_source = '[lol]你好, 帮我吧这些Markup清除掉,[smile]谢谢'

# ValueError: split() requires a non-empty pattern match.
re_pattern = r'\[\w+\][.]*'
re_repl = ''

re_obj = re.compile(re_pattern)

print('The String is as the following: \t"{}"'.format(re_source))
print('The pattern is as the following: \t"{}"'.format(re_pattern))
print('The string is sub by the pattern as the following:')
lst_sub = re.sub(re_pattern, re_repl, re_source)
print('\t{}'.format(lst_sub))
