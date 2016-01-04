#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.3. difflib — Helpers for computing deltas
# 6.3.1. SequenceMatcher Objects

# Source code: Lib/difflib.py
# for comparing sequences

# 2015-12-31 06:33 奇怪的是,必须在引用中使用了difflib.xxx, 这个引用才会变色有效
import difflib

# class difflib.SequenceMatcher(isjunk=None, a='', b='', autojunk=True)

# DATA Attribute
#   bjunk
#   bpopular
#   b2j

# METHODS
#     set_seqs(a, b)
#     set_seq1(a)
#     set_seq2(b)
#     find_longest_match(alo, ahi, blo, bhi)
#     get_matching_blocks()
#     get_opcodes()
# Return list of 5-tuples describing how to turn a into b
# Each tuple is of the form (tag, i1, i2, j1, j2)
# The first tuple has i1 == j1 == 0
# remaining tuples have i1 equal to the i2 from the preceding tuple,
# and, likewise, j1 equal to the previous j2.
'''
Value	Meaning
'replace'	a[i1:i2] should be replaced by b[j1:j2].
'delete'	a[i1:i2] should be deleted. Note that j1 == j2 in this case.
'insert'	b[j1:j2] should be inserted at a[i1:i1]. Note that i1 == i2 in this case.
'equal'	a[i1:i2] == b[j1:j2] (the sub-sequences are equal).
'''
a = 'qabxcd'
b = 'abycdf'
s = difflib.SequenceMatcher(None, a, b)
for tag, i1, i2, j1, j2 in s.get_opcodes():
    # 2015-12-31 07:20 注意 {!r}用法,与'{}'的区别
    print("{:>7} a[{}:{}] --> b[{}:{}] {!r:>8} --> '{}'".
          format(tag, i1, i2, j1, j2, a[i1:i2], b[j1:j2]))
'''
 delete a[0:1] --> b[0:0]      'q' --> ''
  equal a[1:3] --> b[0:2]     'ab' --> 'ab'
replace a[3:4] --> b[2:3]      'x' --> 'y'
  equal a[4:6] --> b[3:5]     'cd' --> 'cd'
 insert a[6:6] --> b[5:6]       '' --> 'f'
 '''

#     get_grouped_opcodes(n=3)

#     ratio()
#     quick_ratio()
#     real_quick_ratio()

# 2015-12-31 06:31 注释的快捷键在CODE/COMMENTS钟,commd+J, OPION+COMMD+J
# TODO 有点看不懂哈,可能还用不上

# 6.3.2. SequenceMatcher Examples
# 测试A,B的相似度,大于0.6,就是比较相似了,这个在比较分析中比较有用
# lambda用于设置需要忽略的字符
# This is expensive to compute if get_matching_blocks() or
# get_opcodes() hasn’t already been called, in which case you
# may want to try quick_ratio() or real_quick_ratio() first to
# get an upper bound.

s = difflib.SequenceMatcher(lambda x: x==' -\n\t',
                            "private Thread currentThread;",
                            "private volatile Thread currentThread;")

# Return an upper bound on ratio() very quickly.
print(round(s.real_quick_ratio(), 3))
# Return an upper bound on ratio() relatively quickly
print(round(s.quick_ratio(), 3))
# Return a measure of the sequences’ similarity as a float in the range [0, 1].
# 1.0 if the sequences are identical, and
# 0.0 if they have nothing in common.
print(round(s.ratio(), 3))
'''0.866'''

for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d element" % block)
'''
a[0] and b[0] match for 6 element
a[6] and b[15] match for 23 element
a[29] and b[38] match for 0 element
'''

# last tuple returned by get_matching_blocks() is always
# a dummy, (len(a), len(b), 0), and this is the only case
# in which the last tuple element (number of elements matched) is 0.

for opcode in s.get_opcodes():
    print("%6s a[%d:%d] b[%d:%d]" % opcode)

''' REUSLT
 equal a[0:6] b[0:6]
insert a[6:6] b[6:15]
 equal a[6:29] b[15:38]
 '''
