from numpy import diagonal
from numpy import fliplr


def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30

    Make sure original list has not been mutated:

        >>> m1 == [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        True

        >>> m1[0] == [1,   2]
        True
    """

    diag1 = diagonal(matrix)
    flipped_matrix = fliplr(matrix)
    diag2 = diagonal(flipped_matrix)

    sum = 0

    for num in diag1 + diag2:
        sum += num

    return sum
