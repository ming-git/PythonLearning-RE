#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations
# » 6.2.3 Regular Expression Objects

# Compiled regular expression objects support the following methods
# and attributes:
# If you want to locate a match anywhere in string,
# use search() instead (see also search() vs. match()).

import re

re_string = 'dog'

re_pattern = 'o'
re_gex = re.compile(re_pattern)

# regex.match(string[, pos[, endpos]])
# regex.match(string)
regex_match = re_gex.match(re_string)
print("{}".format(regex_match))

# regex.match(string, pos)
regex_match = re_gex.match(re_string,pos=1)
print("{}".format(regex_match))
