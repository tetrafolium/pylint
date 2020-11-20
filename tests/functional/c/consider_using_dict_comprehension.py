# pylint: disable=missing-docstring, invalid-name

numbers = [1, 2, 3, 4, 5, 6]

dict()

dict([])

# [consider-using-dict-comprehension]
dict([(number, number * 2) for number in numbers])

# Cannot emit as this cannot be written as a comprehension
dict([value.split("=") for value in ["a=b", "c=d"]])
