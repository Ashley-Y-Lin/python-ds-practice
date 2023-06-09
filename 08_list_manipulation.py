def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    #TODO: replace != with not
    """plug in loc and command vals at the end of if, function will return None
    if it doesn't return anything else """
    """ could also retstructure if to deal w locations and commands"""

    if location != 'beginning' and location != 'end':
        return None

    if command != 'remove' and command != 'add':
        return None

    if location == 'end' and command == 'remove':
        return lst.pop()
    elif location == 'end' and command == 'add':
        lst.append(value)
        return lst
    elif location == 'beginning' and command == 'remove':
        return lst.pop(0)
    else:
        lst.insert(0, value)
        return lst



