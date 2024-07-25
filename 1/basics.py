a=9
print(a)
a='meeeeee'
#a+=5- cannot do this unlike js
#in python every object has an id, reference count and a type
print(a)
print(id(a))    #memory address
print(type(a))  #what kind of data type
import sys
print(sys.getrefcount(a))   #place where data gets deallocated
print('\N{GRINNING FACE}')  #\N is imp to print emojis

#prints the whole library 
# shortcut for comment is ctrl+ /
# import calendar
# def printcalender(year):
#     print(calendar.calendar(year))

# year = 2024
# printcalender(year)

# hello = '''who are you??
#     excuse me
#         what have u done to me?????'''
# print(hello)

# typecasting is different
