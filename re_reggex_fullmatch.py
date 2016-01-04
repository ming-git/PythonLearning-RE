#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations
# » 6.2.3 Regular Expression Objects

# Compiled regular expression objects support the following methods
# and attributes:
# If you want to locate a fullmatch anywhere in string,
# use search() instead (see also search() vs. fullmatch()).

import re

re_string = 'dog'

re_pattern = 'o[gh]'
re_gex = re.compile(re_pattern)

# regex.fullmatch(string[, pos[, endpos]])
# regex.fullmatch(string)
regex_fullmatch = re_gex.fullmatch(re_string)
print("{}".format(regex_fullmatch))

# regex.fullmatch(string, pos)
regex_fullmatch = re_gex.fullmatch(re_string, pos=1)
print("{}".format(regex_fullmatch))
