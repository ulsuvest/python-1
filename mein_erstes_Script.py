import numpy as np
import pandas as pd
from math import sqrt
from statistics import mean
from statistics import stdev

with open ("test.csv", "r") as my_file:
    my_file_content = my_file.readlines()

print(my_file_content[1])

my_first_Array = [1,2,4,6]

mittelwert = (mean(my_first_Array))
standardabweichung = (stdev(my_first_Array))

print(mittelwert*standardabweichung)