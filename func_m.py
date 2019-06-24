import doctest
 
 
def func_m(a, b, c):
    """Вычисляет среднее арифметическое трех чисел.
 
    >>> func_m (20, 30, 70)
    40.0
 
    >>> func_m (1, 5, 8)
    4.667
 
    """
 
    return round((a + b + c) / 3, 3)
 
 
doctest.testmod()

