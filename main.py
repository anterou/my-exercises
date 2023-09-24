import numpy
import numpy as np

num_element = int(input("Print a number of elements:"))
check = int(num_element**0.5)
if(check**2==num_element):
    print(numpy.arange(num_element).reshape(check, check))
else:
    try:
        rows = check
        columns = rows + 1
        print(numpy.arange(num_element).reshape(rows, columns))
    except ValueError:
        print("It is not possible to create such a matrix")



