def simple_hash(key: str, table_size=17, hash_base=31) -> int:
    """ Simple hash function. 
        Returns the ASCII code of the first character
        modulo table size.
    """

    return ord(key[0]) % table_size

def better_hash(key: str, table_size=17, hash_base=31) -> int:
    """ Universal Hash function.
        Takes into account all characters. 
        Uses varying coefficients for all characters.
    """

    value = 0
    a = 31415
    for char in key:
        value = (ord(char) + a * value) % table_size
        a = a * hash_base % (table_size - 1)
    return value