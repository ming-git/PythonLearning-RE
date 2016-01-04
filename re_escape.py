#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations


import re

# Learn the re.escape
# re.subn(pattern, repl, string, count=0, flags=0)
# Perform the same operation as sub(), but return a tuple (new_string, number_of_subs_made).
funcname = 're.escape'

print('\nHow to use {} example:'.format(funcname))
re_source = 'pro----gram-files'


print('The String is as the following: \t"{}"'.format(re_source))
print('The string is {} by the pattern as the following:'.format(funcname))
lst_esc = re.escape(re_source)
print('\n{}'.format(lst_esc))

# >>>
# pro\-\-\-\-gram\-files

# 2015-12-25 05:25 ('pro--gram files', 3)
# 2015-12-25 05:30 修改变量名时注意用refactor,避免遗漏
