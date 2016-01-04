#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.findall(pattern, string, flags=0)
# Return all non-overlapping matches of pattern in string,
# as a list of strings.

# If one or more groups are present in the pattern,
# return a list of groups; this will be a list of tuples
# if the pattern has more than one group

# Empty matches are included in the result
# unless they touch the beginning of another match.


import re

print('\nHow to use re.findall:')
re_source = 'Words, words, words.'
re_pattern = r'\w+'

re_obj = re.compile(re_pattern)

print('The String is as the following: \t"{}"'.format(re_source))
print('The pattern is as the following: \t"{}"'.format(re_pattern))
print('The string is re.findall() by the pattern as the following:')
# cannot process flags argument with a compiled pattern")
# ValueError: cannot process flags argument with a compiled pattern
# lst_findall = re.findall(re_obj, re_in, re.I)
lst_findall = re.findall(re_obj, re_source)
print(lst_findall)
for item in lst_findall:
    print(item)

# <_sre.SRE_Match object; span=(5, 7), match=', '>
# <_sre.SRE_Match object; span=(12, 14), match=', '>
# <_sre.SRE_Match object; span=(19, 20), match='.'>
