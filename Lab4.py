
#date
import datetime
from datetime import timedelta
today = datetime.datetime.now()
five_days_ago = today - timedelta(days=5)

print(today.strftime("%Y-%m-%d"))
print("Five days ago:", five_days_ago.strftime("%Y-%m-%d"))



import datetime 
from datetime import timedelta
date = datetime.datetime.now()
today = date
tomorrow = date-datetime.timedelta(days=1)
yesterday = date-datetime.timedelta(days=1)
print("today" ,date.strftime("%y - %m - %d"))
print("tomorrow", tomorrow.strftime("%y - %m - %d"))
print("yesterday", yesterday.strftime("%y - %m - %d"))



import datetime

date = datetime.datetime.now()
print ("microsecond is", date.strftime("%f"))


from datetime import datetime


date1 = datetime(2025, 6, 10, 14, 30, 0)
date2 = datetime(2025, 6, 13, 12, 15, 0)

difference = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference)


#generator
def generate_squares(N):
    for i in range(1, N + 1):
        yield i * i

# Example usage
for square in generate_squares(5):
    print(square)



def even_numbers(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

# Input from user
n = int(input("Enter a number: "))
evens = even_numbers(n)
print("Even numbers:", ",".join(str(x) for x in evens))


def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage
n = 50
for number in divisible_by_3_and_4(n):
    print(number)


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Example usage
for val in squares(3, 7):
    print(val)


def countdown(n):
    for i in range(n, -1, -1):
        yield i

# Example usage
for num in countdown(5):
    print(num)



#math
import math
def convertor():
    degree = int(input("what is the degree   :"))
    radian = degree*math.pi/180
    print (radian)
convertor()

#area of trapoized
#formula = Area= 1/2* (base1+base2)*height
height = 5
base1 = 5
base2 = 6

area = 0.5 * (base1 + base2) * height
print("Expected Output:", area)


#area of regular polygon
# formula = Area= n*s**2\4*tan(pi/n)
import math

n = 4 
s = 25  

area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(area, 2))

# area of parallelogram
#formula = Area=Base×Height
base = 5
height = 6

area = base * height
print("Expected Output:", float(area))

#iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

#python scope
def myfunc():
  x = 300
  print(x)

myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


def myfunc():
  global x
  x = 300

myfunc()

print(x)


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


#python modulus
def greeting(name):
  print("Hello, " + name)

import mymodule

mymodule.greeting("Jonathan")


#my_module.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import mymodule

a = mymodule.person1["age"]
print(a)

import mymodule as mx

a = mx.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)

import platform

x = dir(platform)
print(x)

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from mymodule import person1

print (person1["age"])

#python date

import datetime

x = datetime.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

#python date 

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)

import math

import math

x = math.sqrt(64)

print(x)

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

import math

x = math.pi

print(x)


#python json

import json
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

json.dumps(x, indent=4)
json.dumps(x, indent=4, separators=(". ", " = "))
json.dumps(x, indent=4, sort_keys=True)



