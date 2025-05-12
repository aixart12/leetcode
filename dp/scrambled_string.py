

def is_scramble_recursive(s1: str, s2: str) -> bool:
    """
    Pure recursive check (no memoization) for Scrambled String.
    WARNING: exponential time for longer strings.
    """
    # base cases
    if s1 == s2:                # identical strings
        return True
    if len(s1) != len(s2):      # different lengths → impossible
        return False
    if sorted(s1) != sorted(s2):  # different multiset of chars
        return False
    n = len(s1)

    # try every split position 1 … n‑1
    for k in range(1, n):
        # no‑swap scenario
        if (is_scramble_recursive(s1[:k], s2[:k]) and
            is_scramble_recursive(s1[k:],  s2[k:])):
            return True
        # swap scenario
        if (is_scramble_recursive(s1[:k], s2[-k:]) and
            is_scramble_recursive(s1[k:],  s2[:-k])):
            return True
    return False

def is_scramble_recursive_memo(s1: str, s2: str , memo) -> bool :
    



# ─── quick demo ───
if __name__ == "__main__":
    n = len('great')
    memo = {}
    print(is_scramble_recursive("great", "rgeat"))   # True
    print(is_scramble_recursive_memo("great", "rgeat"))   # True

    print(is_scramble_recursive("abcde", "caebd"))   # False