#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations
# » 6.2.3 Regular Expression Objects

# Compiled regular expression objects support the following methods
# and attributes:

import re

re_string = 'dog'

re_pattern = 'd'
re_gex = re.compile(re_pattern)

# regex.search(string[, pos[, endpos]])
# regex.search(string)
regex_search = re_gex.search(re_string)
print("{}".format(regex_search))

# regex.search(string, pos)
regex_search = re_gex.search(re_string,pos=1)
print("{}".format(regex_search))
