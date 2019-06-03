import re
import collections
 
list_of_paths = ['text1.txt', 'text2.txt']
 
for path in list_of_paths:
  with open(path) as f:
    f = f.read()
    reg = re.compile('[^a-zA-Z \\n]')
    l = reg.sub('', f).split()
  c = collections.Counter()
  for word in l:
    c[word] += 1
  print(dict(c))
 
print(list_of_paths)
