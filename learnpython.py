# Print function and strings
'''
print('hi')
print("Hi how are you?")
print('Single Quotes', 'add with space')
print('Single Quotes'+'add without space')
print("double quotes")
print('Hi',5)
print(int ('8'),5)
'''

# single line comment
'''multiple
    line
    comment
'''

'''
# Math in python
print(1+3)
print(3-1)
print(4*4)
print(22/7)
print(4**4)         #4 to the power of 4.
'''
'''
# Variables in python
# example_var
# EXAMPLE_VAR
exampleVar = 55+32
print(exampleVar)

exampleVar = print('whoa')
exampleVar

x,y =(3,5)          #Unpacking of values to variables.
print(x)
print(y)
'''

'''
# while loop
condition =1
while condition <10:
    print(condition)
    condition+=1
'''
'''
while True:
    print("doing stuff infinely")
'''

'''
# for loop
exampleList = [1,5,6,1,6,7,8,9,345,53,5]
for eachNo in exampleList:
     print (eachNo)
     print ('continue program')

# indentation really matters here
exampleList = [1,5,6,1,6,7,8,9,345,53,5]
for eachNo in exampleList:
     print (eachNo)

print ('continue program')

# range() fn in python
for x in range(1,110):
    print(x)
'''

'''
# if statements
x=5
y=8
if x>y:
    print('x is greater than y')
else:
    print('y is greater than x')

x=5
y=8
z=4
if z < y > x :
    print('y is greater than z and x')

if z<=x:
    print("z")

z=5
if z==x:
    print("both are equal")

if z!=y:
    print('not equal')
    '''

'''
# else if (elif)
x=5
y=10
z=22
if x>y:
    print('xis greater than y')
elif x<z:
    print('x is less than z')
elif 5>2:
    print('5 is greater than 2')
else:
    print('if and elif never ran')
'''
'''
# functions
def example():
    print('basic function')
    z=3+9
    print(z)

example()
'''
'''
# function with parameters
def simple_addition(num1, num2):
    answer = num1 + num2
    print('num1 is : ', num1)
    print(answer)

simple_addition(3,5)
simple_addition(num2=3,num1=10)
'''
'''# Function parameter default


def simple(num1, num2):
    pass


def simple(num1, num2=5):
    print(num1, num2)


simple(9)


def basic_window(width, height, font='TNR',
                 bgc='w', scrollbar=True):
    print(width, height, font, bgc)


basic_window(3000, 5000, 'a')
basic_window(3000, 5000, bgc='a')'''

# Global and Local variables
'''x = 6  # not a global variable


def example():
    z = 5
    print('z')
    print('x')
   # x+=1           #error
    print('x')


example()
'''
# not a global variable
'''x = 6


def example():
    global x
    z = 5
    print(z)
    print(x)
    x += 1  # no error here.
    print(x)


example()

'''
'''# uisng without global variable
x = 6


def example():
    globx = x
    print(globx)
    globx += 1  # no error here.
    print(globx)
    print(x)
    return globx


x = example()
'''

'''# sudo apt-get install python-matplotlib

# probable errors

# Writing to a file
text = 'sajfa ascjasnc ascnasc \n andnfafh ajvasn!'

saveFile = open('example.txt', 'w')
saveFile.write(text)
saveFile.close()
'''
'''
# Appending files
append = '\n ajfscac ach'

appendFile = open('example.txt','a')
appendFile.write(append)
appendFile.close()'''


'''#Reading from files
readMe = open('example.txt','r').read()
print(readMe)

readMe = open('example.txt','r').readlines()
print(readMe)
'''

'''# classes- as a way of grouping things together


class calculator:
    def addition(x, y):
        added = x + y
        print(added)

    def substraction(x, y):
        sub = x-y
        print(sub)

    def multiplication(x, y):
        mult = x*y


    def division(x, y):
        div = x/y
        print(div)

calculator.addition(3,5)
calculator.substraction(3,5)
calculator.multiplication(3,5)
calculator.division(3,5)
'''


'''#!/usr/bin/python       notifies linux the
#                       path of python so that it can be run as executable

def epic():
    print('wow this is great!')


if __name__ == '__main__':        #if thihs is the main file that is runnung
    print('such a great module')

'''

'''
# Input

x = input('What is your name?  ')
print('Hello',x)
'''
'''
# STATISTICS
import statistics

exampleList = [2,4,8,5,9,7,1,5,6,5,2,1,7,8,3,2,5,9,4,2,8]
print (statistics.mean(exampleList))
print (statistics.median(exampleList))
print (statistics.stdev(exampleList))
print (statistics.variance(exampleList))
'''
'''
    # Module import syntax
    import statistics as s

    exampleList = [2,4,8,5,9,7,1,5,6,5,2,1,7,8,3,2,5,9,4,2,8]
    print (s.mean(exampleList))
    print (s.median(exampleList))
    print (s.stdev(exampleList))
    print (s.variance(exampleList))'''
'''
    from statistics import variance
    from statistics import mean
    from statistics import median
    from statistics import stdev

    exampleList = [2,4,8,5,9,7,1,5,6,5,2,1,7,8,3,2,5,9,4,2,8]
    print (mean(exampleList))
    print (median(exampleList))
    print (stdev(exampleList))
    print (variance(exampleList))'''

'''
from statistics import variance as v
exampleList = [2,4,8,5,9,7,1,5,6,5,2,1,7,8,3,2,5,9,4,2,8]
print (v(exampleList))'''

'''from statistics import variance , mean
exampleList = [2,4,8,5,9,7,1,5,6,5,2,1,7,8,3,2,5,9,4,2,8]
print (variance(exampleList))
print (mean(exampleList))
'''
'''
from statistics import variance as v, mean as m
exampleList = [2,4,8,5,9,7,1,5,6,5,2,1,7,8,3,2,5,9,4,2,8]
print (v(exampleList))
print (m(exampleList))
'''
'''
# for importing everything
from statistics import *
exampleList = [2,4,8,5,9,7,1,5,6,5,2,1,7,8,3,2,5,9,4,2,8]
print (variance(exampleList))
print (median(exampleList))
'''
'''
# Making a module and using it!
import examplemodule

examplemodule.ex('Arpit Shrivastava.')
'''
'''
# Tuples vs Lists (both are lists)
# tuple cannot be changed
# lists can be modified, values can be added, deleted, sorted, etc.

# tuple
c = 5, 6, 2, 6
c = (5, 6, 2, 6)
# lists
c = [5, 6, 2, 6]  # square bracket means lists

# example of tuples
def exampleFunc():
    return 5, 10
x, y = exampleFunc()
print(x, '   ', y)

# lists
c = [5, 6, 2, 6]
print(c[0])
print(c[3])
print(c[2], c[3])
'''
'''
# List Manipulating
x = [4, 5, 9, 6, 5, 4, 1, 2, 5]

x.append(7)
x.insert (2,99)
x.insert (0,101)
print(x)
x.remove(4)
print(x)
x.remove(x[0])
print(x)
print(x[5:])
print(x[5:7])
print(x[-1])
print(x)
print(x.index(1))
print(x.count(5))
print(x)
x.sort()
print(x)

y=['Jnaet', 'Jelly', 'kailey', 'Alice', 'Joe', 'Bob']
y.sort()
print(y)
'''
'''
# Multi Dimensional List

x=[[5,6],[7,8],[3,1],[9,0],[3,7]]

print(x[1])
print(x[1][1])


x=[
    [[5,6],[7,8]],
    [[3,1],[9,0]],
    [[3,7],[5,7]]
]
print(x)
print(x[1][0][0])
'''
'''
# reading CSV spreadsheet (Comma Seperated Variables)
import csv
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # print(readCSV)
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0], row[1])
'''
'''
import csv
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # print(readCSV)
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    whatColor = input('What color you want to know date of? ')
    # So that code runs even if user gives any case letter input
    coldex = colors.index(whatColor.lower)
    theDate = dates[coldex]
    print('The date of ', whatColor, 'is : ', theDate)
'''
'''
# Error Exeption Handling (Try and Error)
import csv
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # print(readCSV)
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    try:
        whatColor = input('What color you want to know date of? ')
        if whatColor in colors:
            # So that code runs even if user gives any case letter input
            coldex = colors.index(whatColor.lower())
            theDate = dates[coldex]
            print('The date of ', whatColor, 'is : ', theDate)
        else:
            print('Color not found!')

    # except Exception ,e    #for python2
    except Exception as e:
        print(e)

    print('continuing ')
'''
'''
# Dictionaries      (not working here)

exDict = {'Jack': '15', 'Bob': '20', 'Alice': '21', 'Kevin': '17'}
print(exDict)

print(exDict['Jack']

exDict['Tim']=14  

# # add into dictionary

# print(exDict)

# exDict['Tim']=15  # Updating values in dictionary

# print(exDict)

# del exDict['Tim']

# print(exDict)
'''

'''
#Built In Functions 

exNum1=5
exNum2=-5
print('exNum1: ', (exNum1))
print('exNum2: ', abs(exNum2))

if (abs(exNum2)==(exNum1)):
    print('Both are exactly same!!')
else:
    print('Not Same!!!..')
'''

'''#Other Built-In functions: 
exList = [5,6,2,1,4,8,5,2,4]
print(max(exList))
print(min(exList))
x=5.998
print(round(x))'''

'''import math     #Using math functions
x=5.7
print(math.floor(x))
print(math.ceil(x))


intMe='55'          #Using Type-casting functions
print(int(intMe))
print(float(intMe))
strMe=77
print(str(strMe))'''
'''
# #OS Modules     (Using OS Modules)
import os

curDir = os.getcwd()
print(curDir)
os.mkdir('newDir')

import time
time.sleep(2)

os.rename('newDir', 'newDir2')
time.sleep(2)

os.rmdir('newDir2')

#help(os)  - for help about the Module'''


#System Modules:

# argv most important functionality
import sys

sys.stderr.write('Testasdgasujd\n')
sys.stderr.flush()
sys.stdout.write('this is stdout text\n')

print(sys.argv )    #prints all the arguments passed 

if len(sys.argv)>1:
    print(sys.argv[1])









