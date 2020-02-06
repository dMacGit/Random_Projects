class LineNumberTooBig(Exception):
    """Thrown if the Number is higher then max bound"""
    pass

class LineNumberTooSmall(Exception):
    """Thrown if the Number is below the min bound"""
    pass

class LineNumberValueError(Exception):
    """Thrown if the Number is not Valid [General Error]"""
    pass

class SizeNumberTooSmall(Exception):
    """Thrown if the Size Value is below min bound"""
    pass

class SizeNumberTooBig(Exception):
    """Thrown if the Size Value is higher then max bound"""
    pass

class SizeNumberValueError(Exception):
    """Thrown if the Size Value is not valid [General Error]"""
    pass