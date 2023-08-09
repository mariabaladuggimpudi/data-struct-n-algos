def max_sum(A) -> int:
    max_seen = max_end = 0

    for a in A:
        max_end = max(a, a+max_end)
        max_seen = max(max_end, max_seen)
    print(max_seen)
    return max_seen

max_sum([904,40,523,12,-335,-385,-124,481,-31])