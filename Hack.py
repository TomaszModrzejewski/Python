import hashlib
import re
import fileinput

n = input('Enter Filename: ');
f = open(n, 'r')

for line in f: 

  p = line.strip()

  if len(p) < 6:
    print(p + " not valid")
    continue

  h = hashlib.sha1(p).hexdigest()[6:]

  passwords = open('combo_not.txt', 'r')
  found = False

  for password in passwords:
    if re.search(h,password):
      print(p + " found")
      found = True
      break

  if not found:
      print(p + " *NOT* found")