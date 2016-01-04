
#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations


import re

# m = re.search("(?<=abc)def", "abcdef")
# print(m.group(0))
re_pattern = "(?<=abc)def"
re_str = "abcdef"

re_obj = re.compile(re_pattern)
re_result = re.search(re_obj, re_str)

print(re_result)
print(re_result.group(0))

# m = re.search('(?<=-)\w+', 'spam-egg')
# print(m.group(0))
re_pattern = '(?<=-)\w+'
re_str = 'spam-egg'

re_obj = re.compile(re_pattern)
re_result = re.search(re_obj, re_str)

print(re_result)
print(re_result.group(0))

# re template Revison 1
print('RE template Revision 1')
re_pattern = '(.+) \1'
re_str = 'the the'

re_obj = re.compile(re_pattern)
re_result = re.search(re_obj, re_str)

print(re_result)
if re_result:
    print(re_result.group(0))
else:
    print('NoneType')

# re template Revison 2
print('\nre template Revision 2 for \\b:')
re_source = ['foo', 'foo.', '(foo)',
             'bar foo baz', 'foobar', 'foo3']
re_pattern = r'\bfoo\b'
re_obj = re.compile(re_pattern)

for re_str in re_source:
    re_result = re.search(re_obj, re_str)
    if re_result:
        print('\t{} is matched in "{}":?\tYES'.
              format(re_pattern, re_str))
    else:
        print('\t{} is matched in "{}"?:\tNO'.
              format(re_pattern, re_str))

# re template Revision 2 for \\B
print('\nre template Revision 2 for \\B:')
re_source = ['python', 'py3', 'py2', 'py', 'py.', 'py!']
re_pattern = r'py\B'
re_obj = re.compile(re_pattern)

for re_str in re_source:
    re_result = re.search(re_obj, re_str)
    if re_result:
        print('\t{} is matched in "{}"?:\tYES'.
              format(re_pattern, re_str))
    else:
        print('\t{} is matched in "{}"?:\tNO'.
              format(re_pattern, re_str))

