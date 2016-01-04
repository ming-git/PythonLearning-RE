#  Python 3.5.1
# » Documentation » The Python Standard Library
# » 6. Text Processing Services
# » 6.3. difflib — Helpers for computing deltas

# Source code: Lib/difflib.py
# for comparing sequences

# for comparing sequences
# can produce difference information in various formats,
# including HTML and context and unified diffs.
# For comparing directories and files, see also, the filecmp module

#  -----------------------class difflib.SequenceMatcher
#   for comparing pairs of sequences of any type,
#   so long as the sequence elements are hashable

#   to find the longest contiguous matching subsequence
#   that contains no “junk” elements
#   these “junk” elements are ones that are uninteresting in some sense,
#   such as blank lines or whitespace.

#   Timing: quadratic time for the worst case; best case time is linear.
#   Automatic junk heuristic:
#   New in version 3.2: The autojunk parameter.

# ------------------------class difflib.Differ
#   for comparing sequences of lines of text,
#   and producing human-readable differences or deltas.

#   Differ uses SequenceMatcher both to compare sequences of lines,
#   and to compare sequences of characters within similar
#   (near-matching) lines.

# Each line of a Differ delta begins with a two-letter code:
#   Code	Meaning
#   '- '	line unique to sequence 1
#   '+ '	line unique to sequence 2
#   '  '	line common to both sequences
#   '? '	line not present in either input sequence

# ------------------------class difflib.HtmlDiff
# NA

# difflib.context_diff(a, b, fromfile='', tofile='', fromfiledate='',
# tofiledate='', n=3, lineterm='\n')

# Compare a and b (lists of strings); return a delta (a generator generating the delta lines) in context diff format.

# 2015-12-30 06:49 无法解析的包?
# 在context_diff前加入difflib后解决

import difflib
import sys
import keyword

s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']

# fromfile= is ok, fromfile =  is not suggested
for line in difflib.context_diff(s1, s2,
                                 fromfile='before.py',
                                 tofile='after.py',
                                 fromfiledate='Aug 2nd 2014',
                                 tofiledate='Aug 3rd 2014',
                                 n=3):
    sys.stdout.write(line)

'''Result
*** before.py	Aug 2nd 2014
--- after.py	Aug 3rd 2014
***************
*** 1,4 ****
! bacon
! eggs
! ham
  guido
--- 1,4 ----
! python
! eggy
! hamster
  guido
'''

# difflib.get_close_matches(word, possibilities, n=3, cutoff=0.6)

# Return a list of the best “good enough” matches.
# word is a sequence for which close matches are desired
# (typically a string), and possibilities is a list of sequences
# against which to match word (typically a list of strings).

# Optional argument n (default 3) is the maximum number of
# close matches to return; n must be greater than 0.

# Optional argument cutoff (default 0.6) is a float in the range [0, 1].
#  Possibilities that don’t score at least that similar to word are ignored.

# The best (no more than n) matches among the possibilities are
# returned in a list, sorted by similarity score, most similar first.

words = 'appel'
possibilities = ['ape', 'apple', 'peach', 'puppy']
list_match = difflib.get_close_matches(words, possibilities)
print(list_match)

match_wheel = difflib.get_close_matches('wheel', keyword.kwlist)
print(match_wheel)

match_apple = difflib.get_close_matches('apple', keyword.kwlist)
print(match_apple)

match_accept = difflib.get_close_matches('accept', keyword.kwlist)
print(match_accept)

'''Result
['apple', 'ape']
['while']
['False']
['except']
'''

# difflib.ndiff(a, b, linejunk=None, charjunk=IS_CHARACTER_JUNK)
# Compare a and b (lists of strings); return a Differ-style delta
# (a generator generating the delta lines).

diff = difflib.ndiff('one\ntwo\nthree\n'.splitlines(keepends=True),
                     'ore\ntree\nemu\n'.splitlines(keepends=True))
print(diff)
print("".join(diff), end=" ")

'''Result
<generator object Differ.compare at 0x101191990>
- one
?  ^
+ ore
?  ^
- two
- three
?  -
+ tree
+ emu
'''

# difflib.restore(sequence, which)
# Return one of the two sequences that generated a delta.

# materialize the generated delta into a list
diff = list(diff)
# TODO 空串2015-12-31 06:21 没有达到预期的效果?
print(diff)
# restore seq1 form the difflib.ndiff
print(' '.join(difflib.restore(diff, 1)), end=' ')
# restore seq2 form the difflib.ndiff
print(' '.join(difflib.restore(diff, 2)), end=' ')
