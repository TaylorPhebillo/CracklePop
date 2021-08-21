def to_crackle_pop(inputVal):
    """Return the CracklePop transformation of an integer
    If the number is divisible by 3, return Crackle instead of the number.
    If it's divisible by 5, return Pop.
    If it's divisible by both 3 and 5, return CracklePop.
    Otherwise, return the string version of the number
    """
    # This problem feels like there's a clever solution,
    # but I can't find one that is clearer code than
    # the naive way. So, optimizing for clarity over
    # efficiency or configurability.
    if (inputVal % (3 * 5)) == 0:
        return "CracklePop"
    if (inputVal % 3) == 0:
        return "Crackle"
    if (inputVal % 5) == 0:
        return "Pop"
    return str(inputVal)


print("\n".join([to_crackle_pop(i) for i in range(1, 101)]))
