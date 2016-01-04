#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.sub
# re.sub(pattern, repl, string, count=0, flags=0)

# If repl is a function, it is called for every non-overlapping
# occurrence of pattern. The function takes a single match object
# argument, and returns the replacement string. For example:

import re

# define the repl function


def dashrepl(matchobj):
    # TODO: AttributeError: 'str' object has no attribute 'group'
    # 2015-12-23 07:14 命令行完全正确啊?
    if matchobj.group(0) == '-':
        return ' '
    else:
        return '-'


print('\nHow to use re.sub with repl function:')
re_source = 'pro----gram-files'

# ValueError: split() requires a non-empty pattern match.
re_pattern = '-{1,2}'
# TypeError: dashrepl() missing 1 required positional argument: 'matchobj'
# re_repl = dashrepl()
re_repl = dashrepl

re_obj = re.compile(re_pattern)

print('The String is as the following: \t"{}"'.format(re_source))
print('The pattern is as the following: \t"{}"'.format(re_pattern))
print('The string is sub by the pattern as the following:')
lst_sub = re.sub(re_obj, re_repl, re_source)
print('\n{}'.format(lst_sub))

# 2015-12-23 07:01 没有如期发生? 可能是re_pattern的字符输入包括了汉字''
# 2015-12-23 07:22 完全正常了
