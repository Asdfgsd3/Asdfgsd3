lst = [10,20,"30"] #You can use both number and string in list
# lst is just a variable and the [] is the list function
score = [70,75,80,85,90]
# Similar to the example on top
# There are built in functions such as sum(), max(), min(), etc.
# Inside () should be the variable infront of the list

#range(start,end,cd)
#range(n): 0 to  n-1 with the common difference 1 
#range(m,n): m to n-1 with the common difference 1
#range(m,n,x): m to n-1 with the common difference x

list(range(10))
# [1,2,3,4,5,6,7,8,9]
list(range(0,10))
# [1,2,3,4,5,6,7,8,9]
list(range(0,10,2))
# [0,2,4,6,8]
list(range(0,10,1))
# [0,1,2,3,4,5,6,7,8,9]
#--------------------------------------------------------------------

# List indexing: the order of items in list 
# for example: 
score[0] 
# 70
score[1]
# 75
score[-3]
# 80
score[-1]
# 90

# List splicing: spliting items in terms of order 
# for example:

score[1:2]
# 75
score[:3]
# 70, 75, 80

# Adding list: set of number union with another set of number
# Multiplying list: set of number repeating x times 

score.append[100,100]
score.extend[95,100]

del score[4] # Deleting anything in list
del score[2:4]

nums = list(range(10))
nums1 = nums # Same thing as nums(if nums change this also change)
nums2 = nums [:] #duplicate of nums (does not change if nums change)

tp1 = (0,1,2,3,4,5,6,7,8,9) # Tuple is similar to list but it is immutable
# Tuple uses () bracket

set1 = (0,1,2,3,4,5,6,7,8,9) # In set there should be no more than one of each things 
# + = union
# & = intersection
# - = difference 
# ^ = symmetric difference

#-------------------------------------------------------------------------------------------

#dictionary: {"Key":"Value"}
information = {"Name":"Jiho Lee", "Age":"15", "Height":175}

