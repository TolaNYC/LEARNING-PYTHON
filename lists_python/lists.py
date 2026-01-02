height = 1.73
tall = True

# we use python lists to store multiple items that makes 
# sense to group together

student_heights = [1.73, 1.68, 1.71, 1.89, 1.79]
print(student_heights)


# lists can also be of the diffferent types 
student_mixed = [1.73, "Artur", True]
print(student_mixed)
# checking the type of the list
print(type(student_mixed))

# we can also access the elements of the list by their index
print(student_heights[0])


# the lists can be made of lists

# slicing a list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

print(house)
print(house[4][1])


#changing the elements of a list
heights = [ "Liz" ,1.73, "emma" ,1.68, "mom", 1.71, "dad",1.89]
# we can use indexes on both directions 
heights[1] = 3.5 
heights[-2]= "sister"
print(heights)


#slicing a list using indexes 
#⚠️ when using indexing for sliceing
# the first index is include and the last index is not included


heights2 = [ "Liz" ,1.73, "emma" ,1.68, "mom", 1.71, "dad",1.89,
 "artur", 1.82 ]
print(heights2[2:5])

# extending a list 
heights3 = [ "Liz" ,1.73, "emma" ,1.68, "mom", 1.71, "dad",1.89]
alHeights = heights3 + ["jane",3.4]
print(alHeights)

del alHeights[2]
print(alHeights)

#behind the scenes, lists in python 
# if we have a list x

x = [1,2,3]
y = x

#when we assign y = x, we are not creating a new list
# we are just creating a new reference to the same list
# which it is why when we modify say
# they appear the same list

y[0] = 10
print(x)
print(y)

# to actually create a new list 

z = list(x)
# this will actually copy the value of the list 
z[0]= 12
print(z)
print(x) 

# another way to create a copy of x on g
g = x[:]










