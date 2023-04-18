def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # look at rithm solution

    freqs = {}

    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1
        # freqs[num] += 1

    highest_val = 0
    highest_num = 0

    for key in freqs:
        if freqs[key] > highest_val:
            highest_val = freqs[key]
            highest_num = key

    return highest_num
