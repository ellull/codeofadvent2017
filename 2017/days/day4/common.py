from itertools import permutations

def is_valid(passphrase):
    words = passphrase.split(' ')
    return len(words) == len(set(words))

def is_valid_v2(passphrase):
    anagrams = [''.join(sorted(word)) for word in passphrase.split(' ')]
    return len(anagrams) == len(set(anagrams))
