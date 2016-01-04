#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations

# Learn the re.VERBOSE

import re

print('\nHow to use re in Normal Mode:')
re_source = ['abc', '100.', '230.00', ' ']
re_pattern = r'\d+\.\d*'

re_obj = re.compile(re_pattern)

print('The pattern is as the following: \n\t{}\n'.format(re_pattern))
for re_str in re_source:
    re_result = re.search(re_obj, re_str)
    re_matched = 'YES' if re_result else 'NO'
    print('\tMatched "{}"?:\t{}'.
          format(re_str, re_matched))
