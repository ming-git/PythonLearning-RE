#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.2. re — Regular expression operations
# » 6.2.3 Regular Expression Objects

# Compiled regular expression objects support the following methods
# and attributes:

# 2015-12-25 08:02 开始尝试实战分析, 很有意思,以后的联系要和实际的结合
# 对于复杂的解析,还是需要独立的单元,方便分解

import re

# String Definition
re_in = '''Boliviana B733 at Sucre on Dec 22nd 2015, runway excursion

A Boliviana de Aviacion Boeing 737-300, registration CP-2552 performing flight OB-580 from Santa Cruz to Sucre (Bolivia) with 129 passengers and 6 crew, landed on Sucre's runway 05 at about 10:15L (13:15Z) and slowed, however, went off the right...'''

# 如何将子模式链接到上一级组合呢,这样就比较强大了
# 也方便后期修改

re_airnline = r"(?P<airline_abbr>.+)"

# Regular Expression Definition
# 2015-12-26 08:07 一大堆提取代码,最大的问题就是无法判读哪里出错了
# TODO: 继续学习,后期补齐

# re_p1 = r"(?P<airline_abbr>.+)"
# re_p2 = re_p1+r"(?P<type_abbr>\w\d\d\d)
re_pattern = r"(?P<airline_abbr>.+) (?P<type_abbr>\w\d\d\d) at (?P<trouble_airport>.+) on (?P<date_r>\w+ \w+ \d\d\d\d), (?P<trouble_name>.+)\n\n[A|AN] (?P<airline_fullname>.+) (?P<type>\w+ \d\d\d-\d\d\d), registration (?P<regno>\w+[0-9-]+) performing flight (?P<flightno>\w+[0-9-]+) from (?P<airportfrom>.+) to (?P<airportto>.+?) \w+"

# Complied regular expression object definition
regex = re.compile(re_pattern)

# regex.search(string, pos, endpos)
match = re.match(regex, re_in)
if match:
    print("{}".format(match.groups()))
    print("{}".format(match.groupdict()))
    # ValueError: too many values to unpack (expected 2)
    # 2015-12-26 08:46 solved, k, v in dict.items(), not
    for k, v in match.groupdict().items():
        print("{}:\t{}".format(k, v))

else:
    print('Something wrong')

'''Boliviana B733 at Sucre on Dec 22nd 2015, runway excursion

A Boliviana de Aviacion Boeing 737-300, registration CP-2552 performing flight OB-580 from Santa Cruz to Sucre (Bolivia) with 129 passengers and 6 crew, landed on Sucre's runway 05 at about 10:15L (13:15Z) and slowed, however, went off the right...'''

'''Canada A321 at Los Angeles on Dec 20th 2015, rejected takeoff as result of push back

An Air Canada Airbus A321-200, registration C-GJWN performing flight AC-788 from Los Angeles,CA (USA) to Toronto,ON (Canada), was accelerating for takeoff from runway 24L when the crew rejected takeoff at high speed (about 100 knots over ground).... '''


# 2015-12-25 05:25 ('pro--gram files', 3)
'''
>>> pattern = re.compile("d")
>>> pattern.search("dog")
<_sre.SRE_Match object; span=(0, 1), match='d'>
>>> pattern.search("dog", 1)
>>> pattern.search("dog", 0)
<_sre.SRE_Match object; span=(0, 1), match='d'>
'''

