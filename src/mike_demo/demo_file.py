def combine_two_string(string_a: str, string_b: str, sep: str = "-") -> str:
    """Combine two strings.

    Parameters
    ----------
    string_a : str
        First string.
    string_b : str
        Second string.
    sep: str
        Separator (Default: -)

    Returns
    -------
    str
        Combined string.
    """
    return string_a + sep + string_b


def add_two_ints(int_a: int, int_b: int) -> int:
    """Add two integers.

    Parameters
    ----------
    int_a : int
        Integer a.
    int_b : int
        Integer b.

    Returns
    -------
    int
        Sum of both ints.
    """
    return int_a + int_b
