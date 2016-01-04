#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.finditer(pattern, string, flags=0)


import re

print('\nHow to use re.split:')
re_source = 'Words, words, words.'
re_pattern = r'\W+'

re_obj = re.compile(re_pattern)

print('The String is as the following: \t"{}"'.format(re_source))
print('The pattern is as the following: \t"{}"'.format(re_pattern))
print('The string is split by the pattern as the following:')
itr_split = re.finditer(re_obj, re_source)
for item in itr_split:
    print(item)

# <_sre.SRE_Match object; span=(5, 7), match=', '>
# <_sre.SRE_Match object; span=(12, 14), match=', '>
# <_sre.SRE_Match object; span=(19, 20), match='.'>
