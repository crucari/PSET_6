#3 functions in this file: algorithms for lines, sentences, and substrings

# Implement lines in such a way that, given two strings, a and b, it returns a list of the lines that are, identically, in both a and b.
# The list should not contain any duplicates. Assume that lines in a and b will be be separated by \n,
# but the strings in the returned list should not end in \n. If both a and b contain
# one or more blank lines (i.e., a \n immediately preceded by no other characters), the returned list should include an empty string (i.e., "").

from nltk.tokenize import sent_tokenize

def lines(a, b):
    """Return lines in both a and b"""

    return list(set(a.split('\n')).intersection(b.split('\n')))

def sentences(a, b):
    """Return sentences in both a and b"""

    return list(set(sent_tokenize(a)).intersection(sent_tokenize(b)))

def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    return set(list_sub(a, n)).intersection(list_sub(n, n))

def list_sub(a,n):

    return [a[i: i + n] for i in range(len(a) - (n - 1))]