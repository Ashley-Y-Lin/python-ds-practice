def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency(551122, 221515)
    True

    >>> same_frequency(321142, 3212215)
    False

    >>> same_frequency(1212, 2211)
    True
    """
    num1_arr = [int(n) for n in str(num1)]
    num2_arr = [int(n) for n in str(num2)]

    for n in num1_arr:
        if n in num2_arr:
            num2_arr.remove(n)
        else:
            return False

    return True
