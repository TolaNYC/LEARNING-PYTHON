
# Functions are pieces of reusable code
# say we have a list of students and their heights and you
#  want to find the max height of the students

students_heights = [1.73, 1.68, 1.71, 1.89, 1.79]
print(max(students_heights))

print(type(students_heights))

# round to the closest integer

print(round(12.36,1))
# round to the 1 decimal place
print(round(12.34, 2))

# for most of the commont tasks python has built-in function
# sorted is one of them

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full =first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full,reverse=True)

# Print out full_sorted
print(full_sorted)




# METHODS are functions that are associated with an object
# A common methd used on lists is index to find the index of first 
# occurrence of an element

fam = ['LIZ',1.73,'emma',1.68,'mom',1.71,'dad',1.89,'LIZ',1.73]
print(fam.index('LIZ'))
print(fam.count('LIZ'))
print(fam.count(1.73))

sister = "lisa"
print(sister.capitalize())
print(sister.replace("is","oret"))

# append method 
fam.append("maria,12")
print(fam)



# PACKAGES are modules that are available for import
# There are thousands of packages available for import 
# each module has it own set of functions and methods
# Some popular packages are:
# Numpy -> to work efficiently with arrays
# Matplotlib -> to create visualizations
# Pandas -> to work with data 
# Scikit-learn -> to work with machine learning
# to use the packages we need to install them first


import numpy as np

# this clarifies that we are using numpy to create an array
np.array([1,2,3])

# importing a specific function from a package
from numpy import array
from math import pi




