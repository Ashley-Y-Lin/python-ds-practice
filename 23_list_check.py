def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    not_list = [item for item in lst if not isinstance(item, list)]

    if not_list:
        return False

    return True
