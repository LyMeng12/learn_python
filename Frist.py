# Python List
from tkinter.font import names
          # 0        1         2         3        4       5        6
names = ["apple", "banana", "cherry", "Orange", "Kiwi", "melon", "mango"]
           #-7       -6        -5        -4       -3       -2        -1

# Access List Items
# print(names[4:6])
# print(names[-7:-2])

# Change List Items

# names [0:4]=["Ban10","KAKA"]
# print(names)
# ['Ban10', 'KAKA', 'kiwi', 'melon', 'mango']

# add back array
# names.append("jksdhf")
# add find index array
# names.insert(2,"sdsd")
# add back many array
# names.extend(["apple", "banana", "cherry"])
# print(names)

# Remove List Items
# choose name remove list if have 2 name it go to first .
# names.remove("apple")

# remove index array
# names.pop(2)
# remove late array value
# names.pop()

# delete all index value
# del names[0]
# delete list = names
# del names

# loop list
# this loop index used for.
# for i in range(len(names)):
#     print(names[i])
# this loop index used while.
# i=0
# while i < len(names):
#     print(names[i])
#     i+=1

# new loop in python
# [print(names[i]) for i in range(len(names))]

# long List Comprehension
# newname=[]
# oldnames=[]
# for i in range(len(names)):
#     if "a"in names[i]:
#         newname.append(names[i])
#     else:
#         oldnames.append(names[i])
# print(newname)
# print(oldnames)

# sort List Comprehension
# newname=[x for x in names if "a" in x]
# print(newname)

# Sort Lists
# small to big
# names.sort()
# big to small
# names.sort(reverse=True)
# if have big later word it show first
# names.sort()
# big to small not show big later first
# names.sort(key = str.lower)
# change valeu friat to late and late to frist
# names.reverse()
# print(names)

# smart sort list
# def myfunc(n):
#   return abs(n - 50)
#
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)