import itertools
def repeatedString(s, n):
    count_a_in_s = s.count('a')
    full_repeats = n // len(s)
    total_a = full_repeats * count_a_in_s
    remainder = n % len(s)
    total_a += s[:remainder].count('a')
    
    return total_a


s = 'abac'
n = 10
print(repeatedString(s, n))