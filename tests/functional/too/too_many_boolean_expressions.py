"""Checks for if statements containing too many boolean expressions"""

# pylint: disable=invalid-name, comparison-with-itself, chained-comparison, condition-evals-to-constant

x = y = z = 5
# [too-many-boolean-expressions]
if x > -5 and x < 5 and y > -5 and y < 5 and z > -5 and z < 5:
    pass
elif True and False and 1 and 2 and 3:
    pass
# [too-many-boolean-expressions]
elif True and False and 1 and 2 and 3 and 4 and 5:
    pass
# [too-many-boolean-expressions]
elif True and (True and True) and (x == 5 or True or True):
    pass
# [too-many-boolean-expressions]
elif True and (True or (x > -5 and x < 5 and (z > -5 or z < 5))):
    pass
elif True == True == True == True == True == True:
    pass

if True and False and 1 and 2 and 3:
    pass
