import re
 
listes_of_path = [r'D:/python/test1.txt']
reg = re.compile('[^а-яА-Яa-zA-Z \\n]')
for file in listes_of_path:
    with open(file,'r') as f_in:
        data = f_in.read()
        l = reg.sub(' ', data).split()
        c = {}
        for word in l:
            c[word] = c.get(word,0)+1
    for k,v in c.items():
        print(k,v)
