#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.split
# re.split(pattern, string, maxsplit=0, flags=0)
# if capturing parentheses are used in pattern,
# then the text of all groups in the pattern are also returned
# as part of the resulting list.


import re

print('\nHow to use re.split:')
re_source = 'Words, words, words.'

# the () in pattern
re_pattern = r'(\W+)'

re_obj = re.compile(re_pattern)

print('The String is as the following: \t"{}"'.format(re_source))
print('The pattern is as the following: \t"{}"'.format(re_pattern))
print('The string is split by the pattern as the following:')
lst_split = re.split(re_obj, re_source)
print('\t{}'.format(lst_split))
