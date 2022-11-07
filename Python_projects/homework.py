# exercise 1

def count_vowels(txt):
    return sum([1 for x in txt.lower() if x in 'aeuio'])


count_vowels('abcd')
count_vowels('abcdef')
count_vowels('bcd')
