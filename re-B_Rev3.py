#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations


import re

# RE Template Revision 3 - More Simple, Remove the duplicated
print('\nre template Revision 3 for \\B:')
re_source = ['python', 'py3', 'py2',
             'py', 'py.', 'py!']
re_pattern = r'py\B'
re_obj = re.compile(re_pattern)

for re_str in re_source:
    re_result = re.search(re_obj, re_str)
    re_matched = 'YES' if re_result else 'NO'
    print('\t{} is matched in "{}"?:\t{}'.
          format(re_pattern, re_str, re_matched))

# 不要修改代码,迭代代码, 保持原来的版本,方便学习, 2015-12-17 04:40
# 不断的发现问题,隔离变化 - 变量之美
