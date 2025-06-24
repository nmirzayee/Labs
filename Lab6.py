f = open("demofile.txt")

f = open("demofile.txt")
print(f.read())

f = open("D:\\myfiles\welcome.txt")
print(f.read())

with open("demofile.txt") as f:
  print(f.read())

  f = open("demofile.txt")
print(f.readline())
f.close()

with open("demofile.txt") as f:
  print(f.read(5))

  with open("demofile.txt") as f:
  print(f.readline())

with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

  with open("demofile.txt") as f:
  for x in f:
    print(x)

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())

  ith open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())

  import os
os.remove("demofile.txt")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder")


from functools import reduce
import time
import math

# multiply list 
def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# count
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# palindrome
def is_palindrome(s):
    return s == s[::-1]

# sqrt
def delayed_sqrt(n, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(n)

# all true
def all_true(t):
    return all(t)

import os
import string
import shutil

# 1
def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)
    return directories, files, all_items

# 2
def check_access(path):
    return {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }

# 3
def path_info(path):
    if os.path.exists(path):
        return os.path.basename(path), os.path.dirname(path)
    return None, None

# 4
def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

# 5
def write_list_to_file(lst, filename):
    with open(filename, 'w') as f:
        for item in lst:
            f.write(f"{item}\n")

# 6
def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as f:
            pass

# 7
def copy_file(src, dst):
    shutil.copyfile(src, dst)

# 8
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
