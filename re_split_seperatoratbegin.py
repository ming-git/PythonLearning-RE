#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.split
# re.split(pattern, string, maxsplit=0, flags=0)
# 注意分隔符出现在string头部,尾部的情况

# If there are capturing groups in the separator and
# it matches at the start of the string, the result
# will start with an empty string.
# The same holds for the end of the string:


import re

print('\nHow to use re.split:')
re_source = '...words, words...'

# the () in pattern
re_pattern = r'\W+'

re_obj = re.compile(re_pattern)

print('The String is as the following: \t"{}"'.format(re_source))
print('The pattern is as the following: \t"{}"'.format(re_pattern))
print('The string is split by the pattern as the following:')
lst_split = re.split(re_pattern, re_source)
print('\t{}'.format(lst_split))

# Becareful
# Result: 	['', 'words', 'words', '']
# NOT 	['words', 'words']

"""
How to use re.split:
The String is as the following: 	"...words, words..."
The pattern is as the following: 	"\W+"
The string is split by the pattern as the following:
	['', 'words', 'words', '']

Process finished with exit code 0
"""

