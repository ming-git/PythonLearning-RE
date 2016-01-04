#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.split
# re.split(pattern, string, maxsplit=0, flags=0)

import re

print('\nHow to use re.split with IGNORECASE:')
re_source = '0a3B9'
re_pattern = r'[a-f]+'

re_obj = re.compile(re_pattern)

print('The String is as the following: \t"{}"'.format(re_source))
print('The pattern is as the following: \t"{}"'.format(re_pattern))
print('The string is split by the pattern as the following:')

# 典型问题:注意 2015-12-19 08:29
# Can not process flags argument with a complied pattern
# lst_split = re.split(re_obj, re_in, flags=re.IGNORECASE)

lst_split = re.split(re_pattern, re_source, flags=re.IGNORECASE)
print('\t{}'.format(lst_split))
