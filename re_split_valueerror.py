#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.split
# re.split(pattern, string, maxsplit=0, flags=0)

#


import re

print('\nHow to use re.split on empty pattern match:')
re_source = 'foo\n\nbar\n'

# ValueError: split() requires a non-empty pattern match.
re_pattern = r'^$'

re_obj = re.compile(re_pattern)

print('The String is as the following: \t"{}"'.format(re_source))
print('The pattern is as the following: \t"{}"'.format(re_pattern))
print('The string is split by the pattern as the following:')
lst_split = re.split(re_pattern, re_source, flags=re.M)
print('\t{}'.format(lst_split))
